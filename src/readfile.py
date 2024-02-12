from sekuens import Sequence
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Membaca line pertama
        buffer_size = int(lines[0])  

        # Membaca line kedua dan menjadikannya sebagai tupel (kolom,baris)
        matrix_size = tuple(map(int, lines[1].split())) 

        # Membaca dan menyimpan data matriks dari file
        matrix_data = [line.split() for line in lines[2:2+matrix_size[1]]] 

        # Membaca dan menyimpan jumlah sekuens
        total_sequence = int(lines[2+matrix_size[1]]) 
        
        sequences = []
        # Menyimpan sequence dalam sebuah list of Sequence
        for i in range(2+matrix_size[1]+1, len(lines), 2):
            sequence_tokens = lines[i].split()
            weight = int(lines[i+1])
            sequences.append(Sequence(sequence_tokens, weight))

    return buffer_size, matrix_size, matrix_data, total_sequence, sequences
