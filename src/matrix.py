class Matriks:
    # Fungsi untuk menmbetuk sebuah matriks
    def __init__(self, baris, kolom):
        self.baris = baris
        self.kolom = kolom
        self.data = [[0 for _ in range(kolom)] for _ in range(baris)]

    # Fungsi untuk melakukan setting atau perubahan value dalam setiap kotak matriks
    def setVal(self, i, j, value):
        if 0 <= i < self.baris and 0 <= j < self.kolom:
            self.data[i][j] = value
        else:
            raise IndexError(f"Index out of range")
            
    
#Fungsi untuk mencetak matriks
def print_matrix(matrix):
    for row in matrix.data:
        print(" ".join(map(str, row)))




