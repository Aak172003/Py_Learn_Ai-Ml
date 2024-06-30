# 1st WAP to find sum of all even number up to 50

sum = 0
for i in range(1 , 51):
    if(i % 2 == 0):
        sum = sum + i
    # i = i + 1

print("sum -> " , sum)


# 2nd WAP to write first 20 number and their squared number

for i in range(1, 21):
    print("value - ", i, " it's squared - ", i ** 2)

# 3rd WAP to check if a number is divisible bby 8 , 12  up to 100 numbers .

for i in range(1 , 101):
    if(i % 8==0 and i%12==0):
        print(i)
