jumlah_deret = int(input("Masukkan jumlah deret: "))

# Inisialisasi tiga nilai pertama
fibo = [1, 2]

# Generate sisa deret
for i in range(2, jumlah_deret):
    next_value = fibo[-1] + fibo[-2]
    fibo.append(next_value)

# Cetak hasil sebanyak jumlah deret
print("Output:")
print(' '.join(str(x) for x in fibo[:jumlah_deret]))