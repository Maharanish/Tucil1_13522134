import random
from sekuens import Sequence 

#Melakukan randomisasi komponen matriks
class FillMtx:
    def __init__(self, tokens):
        self.tokens = tokens

    def filling_matrix(self, baris, kolom):
        matrix = []
        for _ in range(baris):
            row = []
            for _ in range(kolom):
                random_token = random.choice(self.tokens)
                row.append(random_token)
            matrix.append(row)
        return matrix

#Melakukan randomisasi untuk pola sekuens beserta bobotnya
def random_sequence(tokens, max_sequence):
    sequence = random.sample(tokens, min(len(tokens), random.randint(2, max_sequence)))
    return sequence

def random_weight():
    # Asumsi : Bobot sekuens diberikan batas dari -100 sampai 100 karena di QNA dikatakan bisa saja bernilai negatif
    return random.randint(-100,100)

def random_sequences(tokens, total_sequence, max_sequence):
    sequences = []
    for _ in range(total_sequence):
        sequence = random_sequence(tokens, max_sequence)
        weight = random_weight()
        sequences.append(Sequence(sequence, weight))
    return sequences
