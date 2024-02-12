from token import Token
from matrix import Matriks

def check_token_validity(tokens,sequence):
    if len(sequence)>len(tokens):
        return False 
    else: 
        for i in range(len(tokens)-len(sequence)+1):
            if tokens[i] == sequence[0]:
                valid = True
                for j in range(1,len(sequence)):
                    if tokens[i+j] != sequence[j]:
                        valid = False
                        break

                if valid:
                    return True 
        return False

def check_move_validity(baris, kolom, stack):
    if stack != []:
        for token in stack:
            if (token.row, token.column) == (baris, kolom):
                return True 
    return False 

def sum_weight(sequences,tokens):
    reward = 0
    for seq in sequences:
        if check_token_validity([token.token for token in tokens],seq.tokens):
            reward += seq.weight 
    return reward

def find_optimal_reward(possible_sequence,sequences): 
    maks = sum_weight(sequences,possible_sequence[0])
    makspath = possible_sequence[0]
    for i in range(1,len(possible_sequence)):
        if sum_weight(sequences,possible_sequence[i]) > maks :
            maks = sum_weight(sequences,possible_sequence[i])
            makspath = possible_sequence[i]
    return maks,makspath


def find_path(matrix, stack, row, column, buffer_size, optimal_path, horizontal):
    if buffer_size != 1:
        if not horizontal:
            for i in range(matrix.baris):
                if not check_move_validity(i ,column,  stack):
                    stack.append(Token(matrix.data[i][column],column,i)) 
                    find_path(matrix, stack, i, column, buffer_size-1, optimal_path, True)
                    stack.pop()
        else : 
            for i in range(matrix.kolom):
                if not check_move_validity(row, i, stack):
                    stack.append(Token(matrix.data[row][i],i,row)) 
                    find_path(matrix, stack, row, i, buffer_size-1, optimal_path, False)
                    stack.pop()
    else : 
        optimal_path.append(list(stack))

def print_solution(opt_reward, opt_path):
    string_output = ""
    if opt_reward != 0:
        string_output += f"Bobot Hadiah Optimal : {opt_reward}\n"
        flag = True
        buffer_content = ""
        coordinate_content = ""
        for i in opt_path:
            buffer_content += i.token + " "
            coordinate_content += f"{i.column + 1}, {i.row + 1}\n"
        string_output += f"Isi dari Buffer Optimal : {buffer_content.strip()}\n"
        string_output += f"Koordinat dari Setiap Token :\n{coordinate_content.strip()}"
    else:
        string_output += "Tidak ada solusi yang memenuhi\n"

    print(string_output)
    return string_output

    





