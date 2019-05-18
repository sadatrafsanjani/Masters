def armstrong(n, length):

    sum = 0
    t = n
    while(t > 0):
      
        digit = t % 10
        sum += digit ** length
        print("Before: ", t)
        t //= 10
        print("After: ", t)

    if(n == sum):
      print(n,"is an Armstrong Number")
    else:
      print(n,"is not an Armstrong Number")



def prime(n):

    if(n > 1):
        for i in range(2, n):
            if ((n % i) == 0):
                print(n, "is not a Prime Number")
                break
            else:
                print(n, "is a Prime Number")
    else:
        print(n, "is not a prime number")




number = input("Enter a number:")
length = len(number)
n = int(number)

armstrong(n, length)
prime(n)