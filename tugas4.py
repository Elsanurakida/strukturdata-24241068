# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan mahasiswa 
def create():
    nama = input("Masukkan nama mahasiswa :")
    data_mahasiswa.append(nama)
    print ("data berhasil ditambahkan.\n")

# Fungsu untuk menampilkan semua data mahasiswa
def read():
    if not data_mahasiswa:
        print("belum ada data mahasiswa.\n")
    else:
        print("daftar mahasiswa:")
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}.{nama}")
            print()

# fungsi untuk mengubah nama mahasiswa berdasarkan indeks 
def update():
    read()
    try:
        index =int(input("Masukkan indeks mahasiswa yang ingin diubah :"))
        if 0 <= index < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru:")
            data_mahasiswa[index] = nama_baru 
            print ("data berhasil diperbaharui.\n")
        else:
            print("indeks tidak valid.\n")
    except ValueError :
        print("Masukkan angka yang valid.\n")

# Fungsi untuk menghapus data mahasiswa berdasarkan indeks
def delete():
    read()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= indeks < len(data_mahasiswa):
            del data_mahasiswa[indeks]
            print("Data berhasil dihapus.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Masukkan angka yang valid.\n")

# Fungsi utama
def main():
    while True:
        print("Menu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            create()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid.\n")

# Menjalankan program
main()