import streamlit as st
import numpy as np
import pandas as pd
import math
from game import get_random_value, validate
st.set_page_config(page_title="My Streamlit App", page_icon=":tada:", layout="wide")

def main():
    menu=["Play", "Instructions", "About"]
    option = st.sidebar.selectbox("Menu",menu)

    if option == 'Play':
        st.subheader('Quantum Play Begins!')
        st.write("Computer --> |0>")
        st.write("User --> |1>")
        st.write("This is Play")
        psi = '|Ψ|>'
        if 'board' not in st.session_state:
            st.session_state.board = [[psi, psi, psi], [psi, psi, psi], [psi, psi, psi]]
            st.session_state.available_moves = [0,1,2,3,4,5,6,7,8,9]

        moves = st.selectbox("Make a move!", st.session_state.available_moves)
        if moves==1:
            if st.session_state.board[0,0] == psi:
                st.session_state.board[0,0] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==2:
            if st.session_state.board[0,1]==psi:
                st.session_state.board[0,1] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==3:
            if st.session_state.board[0,2]==psi:
                st.session_state.board[0,2] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==4:
            if st.session_state.board[1,0]==psi:
                st.session_state.board[1,0] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==5:
            if st.session_state.board[1,1]==psi:
                st.session_state.board[1,1] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==6:
            if st.session_state.board[1,2]==psi:
                st.session_state.board[1,2] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==7:
            if st.session_state.board[2,0]==psi:
                st.session_state.board[2,0] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        if moves==8:
            if st.session_state.board[2,1]==psi:
                st.session_state.board[2,1] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        if moves==9:
            if st.session_state.board[2,2]==psi:
                st.session_state.board[2,2] = get_random_value()
                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.dession_state.board)
                    st.session_state.available_moves = list()
                    return 0
                comp_square = np.random.randint(1,9)
                col = (comp_square -1)%3
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col] = comp_value

                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's value: ", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        
        #####################################
    elif option=="Instructions":
        st.subheader('Instructions')
        psi = '|Ψ>'
        board = np.array[[psi, psi, psi], [psi, psi, psi], [psi, psi, psi]]
        st.write("Board")
        st.dataframe(board)
    
    else:
        st.subheader('About')
        about = """
            created by: Vijay Wulfekuhle
            created using python, qiskit, streamlit,
            The Game is built to help beginners to understand quantum superposition in a fun way
            The Equation below displays the mathematical form of Quantum Superposition
            """
        st.write(about)
if __name__ == "__main__":
    condition = main()
    if condition == 0:
        st.subheader('Game Over!')