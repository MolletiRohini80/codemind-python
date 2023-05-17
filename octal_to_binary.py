def octtobin(o):
    return bin(int(o,8))
print(end="")
num=input()
b=octtobin(num)
print(b[2:])