#Shabrina Maharani - 13522134

import os
import time
from matrix import Matriks, print_matrix
from sekuens import Sequence
from token import Token
from readfile import read_file
from randoming import FillMtx, random_sequences
from breachprotocol import find_optimal_reward, find_path, print_solution

print("\033[96m" + r"""
                                                                                                                                                 
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████       ██████ ██████  ██████  ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██      ██   ██ ██   ██ ██      
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██      ██████  ██████  ███████ 
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██      ██   ██ ██           ██ 
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████       ██████ ██████  ██      ███████ 
                                                                                                                                                                                                                                                                    

""")
print("\033[95m" + "                               Cyberpunk 2077 Breach Protocol Solver by Shabrina Maharani")
print(r"""_.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._. """)
print("\n")
print("\033[93m"+"Pilih Masukan")
print("1. Masukan dari keyboard")
print("2. Masukan dari file")
pilihan = input("Pilihan Anda: ")
if pilihan == "1":
    total_token = int(input("Masukkan jumlah token unik: "))
    while True:
        tokens = input("Masukkan token yang boleh digunakan untuk mengisi matrix (Contoh : BD 1C 7A): ").split()
        if len(tokens) != total_token:
            print(f"Jumlah token yang dimasukkan tidak sesuai dengan jumlah token unik")
        else:
            break
    buffer_size = int(input("Masukkan ukuran buffer: "))
    print("Masukkan ukuran matriks (Format : row column): ")
    baris, kolom = map(int, input().split())
    total_sequence = int(input("Masukkan jumlah sekuens: "))
    max_sequence = int(input("Masukkan ukuran maksimal sekuens: "))

    # Menghasilkan masukan secara acak
    # Menghasilkan matriks dengan isi yang random menggunakan input token dari pengguna
    random_matrix = FillMtx(tokens).filling_matrix(baris, kolom)

    # Mengeluarkan output hasil random matriks
    print("Matriks acak:")
    mtx = Matriks(baris, kolom)
    for i in range(baris):
        for j in range(kolom):
            mtx.setVal(i, j, random_matrix[i][j])
    print_matrix(mtx)

    # Menghasilkan pola sekuens yang random
    sequences = random_sequences(tokens, total_sequence, max_sequence)

    # Mengeluarkan output hasil random sequence dan bobotnya
    for i, seq in enumerate(sequences, 1):
        print(f"sequences {i}: {seq.tokens}, Reward: {seq.weight}")

elif pilihan == "2":
    # Membaca masukan dari berkas .txt
    nama_file = input("Masukkan nama file (Format : filename.txt): ")
    file_path = os.path.join("..", "test", nama_file)
    buffer_size, matrix_size, matrix, total_sequence, sequences= read_file(file_path)
    mtx = Matriks(matrix_size[1], matrix_size[0])
    #print("Buffer size:", buffer_size)
    #print("Matrix size:", matrix_size)
    for i in range(matrix_size[1]):
        for j in range(matrix_size[0]):
            mtx.setVal(i, j, matrix[i][j])
    #print("Buffer size:", buffer_size)
    #print("Matrix size:", matrix_size)
    #print("Matrix data:")
    #print_matrix(mtx)
    #print("Total sequences:", total_sequence)
    #print("Sequences and weight:")
    #for i, seq in enumerate(sequences, 1):
        #print(f"sequences {i}: {seq.tokens}, Reward: {seq.weight}")

else:
    print("Pilihan tidak valid.")

print("-------Please Wait! Your Solution is On The Way------")
# Mencari Solusi Optimal 
stack = [] 
optimal_path = []

startTimeexe = time.time()
find_path(mtx, stack, 0, 0, buffer_size+1, optimal_path, True)
opt_reward,opt_path = find_optimal_reward(optimal_path,sequences)
exe_time = (time.time() - startTimeexe) * 1000
print_solution(opt_reward,opt_path)
print("\n")
print(f"Waktu eksekusi program: {exe_time} ms")
print("\n")

# Menyimpan solusi dalam berkas.txt
save_file = input("Apakah Anda ingin menyimpan solusi(y/n): ")
if save_file == "y":
    folder_path = os.path.join("..", "test", "solution")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = input("Masukkan nama berkas untuk menyimpan solusi (Format : filename.txt) : ")
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as f:
        if opt_reward != 0:
            f.write("Bobot Hadiah Optimal : " + str(opt_reward) + "\n")
            f.write("Isi dari Buffer Optimal : " + " ".join([token.token for token in opt_path]) + "\n")
            f.write("Koordinat dari Setiap Token : \n")
            for token in opt_path:
                f.write(f"{token.column + 1}, {token.row + 1}\n") #Formatnya : kolom, baris
        else :
            f.write("Tidak ada solusi yang memenuhi")
        f.write("\n")
        f.write("\n")
        f.write("Waktu eksekusi program: " + str(exe_time)+" ms\n")
    print("\n")
    print("Solusi telah disimpan dalam berkas:", file_path)
else:
    print("\033[95m" + "")
    print(r"""_.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._. """)
    print("                                      Terima kasih sudah menjalankan program ini!")