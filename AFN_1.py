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
    input_str = input("Ingrese una cadena para verificar si es aceptada por el DFA (o 'salir' para terminar): ")

    if input_str.lower() == 'salir':
        print("¡Hasta luego!")
        break

    if dfa.accepts_input(input_str):
        print(f"'{input_str}' es aceptado por el DFA.")
    else:
        print(f"'{input_str}' no es aceptado por el DFA.")
