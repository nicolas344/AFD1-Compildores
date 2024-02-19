# Formal Languages and Compilers Homework-1
## Author
Nicolas Rico Montesino
## Assignment
1. A deterministic finite automaton (DFA) accepting the language
{x e {0, 1}* | x represents a multiple of three in binary}DFÑs implementation: Using some programming language, write down a program that read a string from the command-line and determines if it belongs to the language accepted by the above automaton.

[![Captura-de-pantalla-2024-02-17-181432.png](https://i.postimg.cc/Wb9S28sZ/Captura-de-pantalla-2024-02-17-181432.png)](https://postimg.cc/bst1gQDY)

2. Random test: Implement a code that generates a random string in {0, 1} * with parameters size n and multiple-of-3.1s. Test to determine if a string of 1000000 characters of 01s is a multiple of 3 in binary

## About
- The program was executed on Windows OS.
- The chosen language was Python.
- The libray used was [Automata](https://caleb531.github.io/automata/) and the class used is [DFA](https://caleb531.github.io/automata/api/fa/class-dfa/) .**The library requires Python 3.8 or newer.**
- The code editor used was Visual Studio Code.
## Installing Requirements
Follow these instructions to run the program:

1. Dowload the program.

You can use the next zip
[AFD1-Compildores-master (1).zip](https://github.com/nicolas344/AFD1-Compildores/files/14337610/AFD1-Compildores-master.1.zip)

3. Make sure you have Python 3.8 or newer.
  
    ```bash
    python --version

    ```
4. Install the Automaton library required using `pip`

    ```bash
    pip install automata-lib
    ```

## Run the program
1. Go to your editor and open de program and press in AFD_1 or AFD_2, then you can execute the program.
[![Captura-de-pantalla-2024-02-17-190943.png](https://i.postimg.cc/HxzHnRZH/Captura-de-pantalla-2024-02-17-190943.png)](https://postimg.cc/YGvTynBy)
## AFD_1
1. Enter your input, for example:

    ```bash
    Enter a string to check if it is accepted by the DFA: 1111 
    ```

2. Check the answer
    ```bash
    '1111' is accepted by the DFA
    ```
3. And it will give you a output message if the string is not acepted
    ```bash
    '101011' is not accepted by the DFA
    ```
## AFD_2
- It will automaty generate and string with 1000000 of characters
1. In case the binary string generated is a multiple of 3 in binary it will give you the next output
    ```bash
    The DFA accepts the string
    ```
2. If in the case that the generated string is not a multiple of 3 in binary will give you the next output
    ```bash
    The DFA rejects the string, so is not a multiple of three in binary
    ```
