import time
x=int(input("Enter the upper limit:"))
num = int(round(time.time() * 1000%int(x)))
print(num)
