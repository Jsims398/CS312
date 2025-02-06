# 1) 
# a) f= theta(g)
# b) f= O(g)
# c) f= Omega(g)
# d) f= theta(g)
# e) f= theta(g)
# f) f= theta(g)
# m) f= Omega(g)

# 2)


# 3) 
# a) 

def fabonacci(n): # O(n^3)
    if n == 0 or n == 1 or n == 2: # c
        return 1 # c
    return fabonacci(n-1) + fabonacci(n-2) * fabonacci(n-3) # O(n^3)

# b)
def linearFib(n): # O(n)
    # if n <= 2; return 1                   base case       c
    # 
    # f = array of size n+1                 array           c    
    # f[0] = 1; f[1] = 1; f[2] = 1          set values      c
    # 
    # for i = 3 to n                        loop            (n-2)
    #   f[i] = f[i-1] + f[i-2] * f[i-3]     calculation     c
    # return f[n]
    return