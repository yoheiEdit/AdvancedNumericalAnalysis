s = input()
a = input()
b = input()

list_ = ''
for i in range(int(s)):
    if a[i] == b[i]:
        list_ += '0'
    else:
        list_ += '1'
    
print(list_)