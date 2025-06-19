# Membuat program untuk menerima input dari pengguna untuk operasi push dan pop stack
# langkah 1 menyiapkan stack array
tumpukan = []

# langkah 2 push elemen ke stack
while True:
    isi_elemen = input("Masukkan isi elemen (ketik Selesai jika tidak): ")
    if isi_elemen.lower() == 'selesai':
        break
    stack = tumpukan.append(int(isi_elemen))
    print("tumpukan : ", tumpukan)

# langkah 3 pop elemen dari stack
for i in range(len(tumpukan)):
    if len(tumpukan) != 0:
        hapus = input('Apakah ingin menghapus elemen [ya/tidak] : ')
        if hapus.lower() == 'tidak' :
            break
        print("Pop : ", tumpukan.pop())
        print("tumpukan : ", tumpukan)
    else :
        print("Stack Kosong!")