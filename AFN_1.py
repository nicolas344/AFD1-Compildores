from automata.fa.dfa import DFA

while True:
    dfa = DFA(
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
    input_str = input("Enter a string to check if it is accepted by the DFA (or 'exit' to quit): ")

    if input_str.lower() == 'exit':
        print("Goodbye!")
        break

    if dfa.accepts_input(input_str):
        print(f"'{input_str}' is accepted by the DFA.")
    elif input_str == "e":
        print(f"The DFA accepts the string '{input_str}'")
    else:
        print(f"'{input_str}' is not accepted by the DFA.")

