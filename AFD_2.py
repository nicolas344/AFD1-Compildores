import random
from automata.fa.dfa import DFA


def generate_binary(length=7):
    return ''.join(random.choice('01') for _ in range(length))


dfa1 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q0'}
)

binary_string = generate_binary()
if dfa1.accepts_input(binary_string):
    print(f"The DFA accepts the string '{binary_string}'")
else:
    print(f"The DFA rejects the string, so is not a multiple of three in binary '{binary_string}'")
