def Fizz_Buzz(n):
    for i in range(1, n + 1):
     if i % 3 == 0:
        print(f"{i} - Fizz")
     if i % 5 == 0:
        print(f"{i} - Buzz")
     if i % 5 == 0 and i % 3 == 0:
        print(f"{i} - FizzBuzz")
     else:
        print(i)
n = int(input("введите число :"))  
Fizz_Buzz(n)         



