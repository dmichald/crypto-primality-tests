import random
   
def calculateJacobian(a, n):
 
    if (a == 0):
        return 0;# (0/n) = 0
 
    ans = 1
    if (a < 0):
         
        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):
         
            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans
 
    if (a == 1):
        return ans; # (1/n) = 1
 
    while (a):
        if (a < 0):
             
            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):
                 
                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans
 
        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans
 
        # swap
        a, n = n, a
 
        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n
 
        if (a > n // 2):
            a = a - n
 
    if (n == 1):
        return ans
 
    return 0;    
    
def exp_func(x, y):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        if(exp[i:i+1]=='1'):
            value = value*x
    return value

def fermat(n,t):
    if(n < 3):
        print('n musi byc >=3')
        return
    if(t<1):
        print('t musi byc >=1')

    for i in range(1,t):
        a = random.randint(2,n-2)
        r = exp_func(a, n-1) % n
        if(r != 1):
            print( str(n) + " : zlozona")
            return
    print(str(n) + ' : pierwsza')

def areCongruent(a,b,m):
    r1 = a % m
    r2 = b % m
    return r1 == r2

def sol_str(n,t):
    if( n < 3):
        print("n >= 3")
        return
    if (n % 2 == 0):
        print('n musi byc nieparzyste')
        return
    if(t < 1):
        print('t >=1')
        return
    for i in range(1,t):
        a = random.randint(2,n-2)
        pow = int((n-1)/2)
        r = exp_func(a,pow) % n
        if(r!=1) and (r!= n-1):
            print(str(n) + " : zlozona1")
            return
        s = calculateJacobian(a,n)
        if not(areCongruent(r,s,n)):
            print(str(n) + " : zlozona2")
            return
        
    print(str(n) + " : pierwsza")
    
def miller_rabin(n,t):
    if( n < 3):
        print("n >= 3")
        return
    if (n % 2 == 0):
        print('n musi byc nieparzyste')
        return
    if(t < 1):
        print('t >=1')
        return
    r = n - 1
    s = 0
    while (r % 2 == 0):
        r //= 2
        s = s +1
    for i in (range(1,t)):
        a = random.randint(2,n-2)
        y = exp_func(a,r) % n
        if( y != 1) and (y != n-1):
            j = 1
            while((j <= s) and (y != n-1)):
                y = (y * y) % n
                if(y == 1):
                    print(str(n) + ' : zlozona1')
                    return
                j = j + 1
            if (y != n -1):
                print(str(n) + ' : zlozona2')
                return
    print(str(n) + ' : pierwsza')
    return

               
fermat(561,1000)
sol_str(561,1000)   
miller_rabin(561,1000)
