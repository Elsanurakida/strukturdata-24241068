# membuat function sederhana
def sapa():
    print("Halo, selamat datang!")

sapa()  # Memanggil fungsi 1
sapa()  # memanggil fungsi 2
sapa()  # memanggil fungsi 3 

# Function dengan parameter
# function dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

# Pemanggilan Function
sapa_nama("Adam")
sapa_nama("Elsa")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)

# function dengan return (nilai kembali)
def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume Persegi = {vol_persegi}")

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

# pemanggilan function, dengan 1 argumen
student("wallbert") # hanya firstname

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

# *args untuk argumen bervariasi
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Selamat Datang', 'Di', 'PTI UNDIKMA')