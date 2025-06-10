class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Menambahkan node di akhir linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        """Menampilkan isi linked list"""
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def delete_awal(self):
        """Menghapus node awal"""
        if not self.head:
            print("Linked list kosong!")
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_akhir(self):
        """Menghapus node akhir"""
        if not self.head:
            print("Linked list kosong!")
            return
        curr = self.head
        if not curr.next:
            self.head = None
            return
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def delete_berdasarkan_nilai(self, target):
        """Menghapus node berdasarkan nilai data"""
        if not self.head:
            print("Linked list kosong!")
            return

        curr = self.head

        # Jika node yang akan dihapus adalah head
        if curr.data == target:
            self.delete_awal()
            return

        while curr:
            if curr.data == target:
                if curr.next:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                else:
                    # Node terakhir
                    curr.prev.next = None
                return
            curr = curr.next
        print(f"Data {target} tidak ditemukan dalam linked list.")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Linked list awal:")
dll.display()

print("\nHapus node awal:")
dll.delete_awal()
dll.display()

print("\nHapus node akhir:")
dll.delete_akhir()
dll.display()

print("\nHapus node dengan nilai 20:")
dll.delete_berdasarkan_nilai(20)
dll.display()

print("\nCoba hapus data yang tidak ada (50):")
dll.delete_berdasarkan_nilai(50)
