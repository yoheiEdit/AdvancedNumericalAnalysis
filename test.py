s = int(input())

tmp = s
ans = 1
while(tmp != 1):
    ans = ans * tmp
    tmp = tmp - 1
    
print(ans)

import math
print(math.factorial(s))