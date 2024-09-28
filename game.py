from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import streamlit as st
def quantum_superposition():
    circuit = QuantumCircuit(1,1)

    circuit.h(0)

    circuit.measure(0,0)

    simulator = AerSimulator()

    result = simulator.run(circuit).result().get_counts()
    return result


def get_random_value():
    res = quantum_superposition()
    values = list(res.values())
    keys = list(res.keys())
    print(values)
    print(keys)
    random_value = '|' + str(keys[np.argmax(values)]) + '>'
    print(random_value)
    return random_value

def validate(arr):
    """
    The method checks if the game is finished!
    Parameters:
    arr (list of lists) : the list that serves as the board
    Returns:
    returns 0 if any of the winning conditions is satisfied by any of the players,
    else returns 1
    """
    flag = True
    zero_ket = '|0>'
    one_ket = '|1>'
    
    # Check principal diagonal condition for user
    if arr[0][0] == one_ket and arr[1][1] == one_ket and arr[2][2] == one_ket:
        st.success('User has won!')
        flag = False
    # Check principal diagonal condition for computer
    elif arr[0][0] == zero_ket and arr[1][1] == zero_ket and arr[2][2] == zero_ket:
        st.success('Computer wins!')
        flag = False
    # Check second diagonal condition for user
    elif arr[0][2] == one_ket and arr[1][1] == one_ket and arr[2][0] == one_ket:
        st.success('User has won!')
        flag = False
    # Check second diagonal condition for computer
    elif arr[0][2] == zero_ket and arr[1][1] == zero_ket and arr[2][0] == zero_ket:
        st.success('Computer wins!')
        flag = False

    if not flag:
        return 0

    # Check rows and columns
    for index in range(3):
        # Check rows for user
        if arr[index] == [one_ket, one_ket, one_ket]:
            st.success('User has won!')
            return 0
        # Check rows for computer
        if arr[index] == [zero_ket, zero_ket, zero_ket]:
            st.success('Computer wins!')
            return 0

        # Check columns for user
        if [arr[0][index], arr[1][index], arr[2][index]] == [one_ket, one_ket, one_ket]:
            st.success('User has won!')
            return 0
        # Check columns for computer
        if [arr[0][index], arr[1][index], arr[2][index]] == [zero_ket, zero_ket, zero_ket]:
            st.success('Computer wins!')
            return 0

    # Check for draw
    if all(cell != '|Ψ|' for row in arr for cell in row):
        st.write("It's a draw!")
        return 0

    return 1    