def new_func():
    x = int(input("Input number: "))
    binary_str = ""
    while x > 0:
        binary_str += str(x % 2)
        x = x // 2
    
    return binary_str

print(new_func())
