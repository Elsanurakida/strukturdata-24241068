# cara membuat tuple singleton
satu = ('Isi',)
dua = "ini adalah tuple?",

# cek tipe datanya
print(type(satu))
print(type(dua))

# jika tidak pakai koma
satu = ('Isi')
dua = "ini adalah tuple?"

# cek tipe datanya
print(type(satu))
print(type(dua))

# membuat tuple
nama = ('Reni', 'Jlita')

# mengakses indeks ke 1 dari tuple
print(nama[1])

# Membuat Tuple
t = (1, 5, 10, 15)
t_list = list (t)
t_list[0]= 0
t = tuple (t_list)

print(t)