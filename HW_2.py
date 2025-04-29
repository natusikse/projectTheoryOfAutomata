fset = frozenset


class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.Q = states
        self.Sigma = alphabet
        self.delta = transitions
        self.q_0 = initial_state
        self.F = final_states

    def check(self, word):
        state = self.q_0
        while word:
            if (state, word[0]) not in self.delta:
                return False
            state = self.delta[(state, word[0])]
            word = word[1:]
        return state in self.F

    def language(self):
        words = {''}
        while True:
            for word in words:
                if self.check(word):
                    yield word
            words = [
                word + letter
                for word in words
                for letter in self.Sigma
            ]


# DFA that computes the language of binary words beginning with 1
M1 = DFA(
    {"start", "valid"},
    {'0', '1'},
    {("start", '1'): "valid",
     ("start", '0'): "start",
     ("valid", '0'): "valid",
     ("valid", '1'): "valid"},
    "start",
    {"valid"}
)

# DFA that recognizes only '101'
M2 = DFA(
    {"q0", "q1", "q2", "q3"},
    {'0', '1'},
    {("q0", '1'): "q1", ("q1", '0'): "q2", ("q2", '1'): "q3"},
    "q0",
    {"q3"}
)

# DFA that computes words over {'a', 'b'} that begin and end with the same letter
M3 = DFA(
    {"empty", "a_state", "b_state", "valid_a", "valid_b"},
    {'a', 'b'},
    {("empty", 'a'): "a_state", ("empty", 'b'): "b_state",
     ("a_state", 'a'): "valid_a", ("a_state", 'b'): "a_state",
     ("b_state", 'b'): "valid_b", ("b_state", 'a'): "b_state",
     ("valid_a", 'a'): "valid_a", ("valid_a", 'b'): "a_state",
     ("valid_b", 'b'): "valid_b", ("valid_b", 'a'): "b_state"},
    "empty",
    {"valid_a", "valid_b"}
)

# DFA that accepts words containing the same letter twice in a row
M4 = DFA(
    {"start", "aa", "bb", "valid"},
    {'a', 'b'},
    {("start", 'a'): "aa", ("start", 'b'): "bb",
     ("aa", 'a'): "valid", ("aa", 'b'): "start",
     ("bb", 'b'): "valid", ("bb", 'a'): "start",
     ("valid", 'a'): "valid", ("valid", 'b'): "valid"},
    "start",
    {"valid"}
)


class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.Q = states
        self.Sigma = alphabet
        self.delta = transitions
        self.q_0 = initial_state
        self.F = final_states

    def check(self, word):
        states = {self.q_0}
        while word:
            states = self.E(states)
            state_new = set()
            for q in states:
                state_new.update(self.delta.get((q, word[0]), set()))
            states = state_new
            word = word[1:]
        return bool(states.intersection(self.F))

    def E(self, states):
        states_e = set(states)
        while True:
            new_states = states_e.copy()
            for q in states_e:
                new_states.update(self.delta.get((q, ''), set()))
            if new_states == states_e:
                return new_states
            states_e = new_states

    def language(self):
        words = {''}
        while True:
            for word in words:
                if self.check(word):
                    yield word
            words = [
                word + letter
                for word in words
                for letter in self.Sigma
            ]

    def to_DFA(self):
        initial = fset(self.E({self.q_0}))
        dfa_states = {initial}
        dfa_delta = {}
        dfa_final = set()
        unprocessed = [initial]

        while unprocessed:
            current = unprocessed.pop()
            for symbol in self.Sigma:
                new_state = fset(
                    self.E({q for q in current if (q, symbol) in self.delta for q in self.delta[(q, symbol)]}))
                dfa_delta[(current, symbol)] = new_state
                if new_state not in dfa_states:
                    dfa_states.add(new_state)
                    unprocessed.append(new_state)
                if new_state & self.F:
                    dfa_final.add(new_state)

        return DFA(dfa_states, self.Sigma, dfa_delta, initial, dfa_final)


# Demonstrate DFA functionality
print("Testing M1 (words beginning with '1'):")
for w in ["1", "10", "110", "0", "011"]:
    print(f"{w}: {M1.check(w)}")

print("\nTesting M2 (only '101'):")
for w in ["101", "100", "1", "1010"]:
    print(f"{w}: {M2.check(w)}")

print("\nTesting M3 (begin and end with same letter):")
for w in ["a", "b", "aba", "bab", "ab"]:
    print(f"{w}: {M3.check(w)}")

print("\nTesting M4 (same letter twice in a row):")
for w in ["aa", "bb", "ab", "ba", "abba"]:
    print(f"{w}: {M4.check(w)}")

#printning code features

print("testing M1 (words beginning with '1'):")
for w in ["1", "10", "110", "0", "011"]:
    print(f"{w}: {M1.check(w)}")

print("\ntesting M2 (only '101'):")
for w in ["101", "100", "1", "1010"]:
    print(f"{w}: {M2.check(w)}")

print("\ntesting M3 (begin and end with same letter):")
for w in ["a", "b", "aba", "bab", "ab"]:
    print(f"{w}: {M3.check(w)}")

print("\ntesting M4 (same letter twice in a row):")
for w in ["aa", "bb", "ab", "ba", "abba"]:
    print(f"{w}: {M4.check(w)}")


#Example:
#   Below machine N is an NFA that computes the language of binary words ending in 1.
N = NFA(
    {"start", "end"},
    {'0', '1'},
    {("start", '0'): {"start"},
        ("start", '1'): {"start", "end"},
        ("end", '0'): set(),
        ("end", '1'): set(),
        # don't forget to define the epsilon arrows in NFA.
        ("start", ''): set(),
        ("end", ''): set()},
    "start",
    {"end"}
)
count = 0
for w in N.language():
    if count > 64:
        break
    print(w)
    count = count + 1
#   If problem 5 is implemented correctly, below printing will work as expected:
count = 0
for w in N.to_DFA().language():
    if count > 64:
        break
    print(w)
    count = count + 1
