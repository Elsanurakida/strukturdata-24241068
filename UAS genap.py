# meminta input data belanja customer dan tanggal belanja simpan dalam tuple 
nama_customer = input ("memasukkan nama customer")
tanggal_belanja = input ("memasukkan tanggal belanja customer")
data_customer = ( nama_customer , tanggal_belanja)

jumlah_belanja = int(input("Masukkan Jumlah barang : "))

# Dictionary untuk menyimpan data
jumlah_barang = {}

# Perulangan untuk input data setiap mahasiswa
aftar_belanja = []
for i in range(jumlah_belanja):
    print(f"\nBarang ke-{i+1}:")
    nama_barang = input("  Nama barang: ")
    harga_satuan = float(input("  Harga satuan: "))
    qty = int(input("  Jumlah (QTY): "))
  
    # Simpan dalam dictionary
    barang = {
        "nama": nama_barang,
        "harga": harga_satuan,
        "Qty": qty,
        "subtotal" : "harga_satuan * qty"
    }

#  Simpan dictionary barang dalam list
    jumlah_barang.append(barang)

    print("\n===== STRUK BELANJA =====")
print(f"Nama Customer : {data_customer[0]}")
print(f"Tanggal       : {data_customer[1]}")
print("\nDaftar Belanja:")
print("{:<20} {:>10} {:>10} {:>12}".format("Nama Barang", "Harga", "QTY", "total"))

total_bayar = 0
for barang in jumlah_barang:
    print("{:<20} {:>10,.2f} {:>10} {:>12,.2f}".format(
        barang["nama"], barang["harga"], barang["qty"], barang["subtotal"]))
    total_bayar += barang["subtotal"]

print("\nTotal Bayar: Rp{:,.2f}".format(total_bayar))
