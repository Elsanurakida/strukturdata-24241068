# Input: jumlah deret
jumlah_deret = int(input("Masukkan jumlah deret: "))

# Menghitung bilangan genap
bilangan_genap = [i for i in range(2, jumlah_deret + 1) if i % 2 == 0]
print("Output:", ', '.join(map(str, bilangan_genap)))