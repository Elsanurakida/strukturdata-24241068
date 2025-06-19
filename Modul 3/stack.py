# Membuat Stack
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print ("Stack : ", stack)

# cek apakah stack kosong 
if not bool (stack) :
    print("stack kosong!")
else:
    print("stack tidak kosong! ", stack)

# cek puncak stack
if not bool (stack) :
    print ("stack kosong!")
else:
    print("top/peek : ", stack [-1])

# operasi pop (menghapus, prinsip LIPO)
if len (stack) != 0:
    print("pop , stack.pop()")























# pop 
if len(stack) != 0:
    print("Pop : ", stack.pop())
    print("Stack : ", stack)
else :
    print("Stack Kosong!")

# top/peek
if not bool(stack):
    print("Stack Kosong!")
else:
    print("stack : ", stack)
    print("Top/Peek : ", stack[-1])


# isEmpty
if not bool(stack):
    print("Stack Kosong ")
else :
    print("Stack tidak kosong! ", stack)


# size
print("Stack Size : ", len(stack))