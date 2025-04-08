# Perulangan (loop)

# for kondisi : JIKA KONDISI TERPENUHI 
#   aksi JALANKAN AKSI

angka_list = [0,2,4,8,10] # ini adalah list
print (angka_list)

angka = 0 
print (angka)
angka += 1 # angka = angka + 1
print (angka)
angka += 1 
print (angka)

# for-loop 
for i in angka_list :
    print (f"i sekarang -> {i}")

print ("loop berakhir \n")

# dengan range 
for i in range (5) :
    print (f"i sekarang -> {i}")

print (f"i sekarang -> {i}")

for i in range (1,10) :
    print (f"i sekarang -> {i}")

print ("loop berakhir \n")

# for loop 
for i in range (1,4) : 
    print ("*" * i)

print ("loop berakhir \n")
