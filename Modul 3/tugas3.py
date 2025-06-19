# =====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====

# Node stack disimpan sebagai dictionary: {"data": ..., "next": ...}
def create_node(data, next_node=None):
    return {"data": data, "next": next_node}

# Push elemen ke stack
def push(stack, data):
    if is_full(stack):
        print("Stack sudah penuh, tidak bisa menambahkan elemen.")
        return False
    new_node = create_node(data, stack["top"])
    stack["top"] = new_node
    stack["count"] += 1
    return True

# Pop elemen dari stack
def pop(stack):
    if is_empty(stack):
        print("Stack kosong, tidak bisa menghapus.")
        return None
    data = stack["top"]["data"]
    stack["top"] = stack["top"]["next"]
    stack["count"] -= 1
    return data

# Cek ukuran stack
def size(stack):
    return stack["count"]

# Cek elemen puncak
def peek(stack):
    if is_empty(stack):
        return None
    return stack["top"]["data"]

# Cek apakah stack kosong
def is_empty(stack):
    return stack["top"] is None

# Cek apakah stack penuh
def is_full(stack):
    return stack["count"] >= stack["capacity"]

# Menampilkan isi stack sebagai list
def get_stack_list(stack):
    current = stack["top"]
    elements = []
    while current:
        elements.insert(0, current["data"])
        current = current["next"]
    return elements

# ========== PROGRAM UTAMA ==========

print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
kapasitas = int(input("Tentukan berapa kapasitas stack : "))

# Inisialisasi stack
stack = {
    "top": None,
    "count": 0,
    "capacity": kapasitas
}

while True:
    print("\nPilih menu berikut ini : ")
    print("1. Menambah isi stack")
    print("2. Menghapus isi stack")
    print("3. Cek Ukuran Stack saat ini")
    print("4. Cek Puncak Stack")
    print("5. Cek Stack Full")
    print("6. Keluar")

    pilihan = input("\nMasukkan pilihan anda : ")

    if pilihan == "1":
        while True:
            data = input("Masukkan isi stack : ")
            if push(stack, data):
                print(f"Stack : {get_stack_list(stack)}")
            else:
                break

            lanjut = input("\nMenambah isi Stack Pilih [Ya/Tidak] : ").lower()
            if lanjut != "ya":
                break

    elif pilihan == "2":
        hasil = pop(stack)
        if hasil is not None:
            print(f"Data {hasil} telah dihapus.")
            print(f"Stack : {get_stack_list(stack)}")

    elif pilihan == "3":
        print(f"Ukuran stack saat ini adalah: {size(stack)}")

    elif pilihan == "4":
        puncak = peek(stack)
        if puncak is not None:
            print(f"Puncak stack adalah: {puncak}")
        else:
            print("Stack masih kosong.")

    elif pilihan == "5":
        print(f"Apakah stack penuh? {is_full(stack)}")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")