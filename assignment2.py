# -----------------Task 1 ------------------------

num = int(input("Enter a number : "))

if(num % 2 == 0):
    print(num, "is an even number")
else:
    print(num, "is an odd number")


# ---------------------Task 2 -----------------

for i in range(1,51):
    print(i)

total = sum(range(1,51))
print("The sum of numbers from 1 to 50 is : ",total)