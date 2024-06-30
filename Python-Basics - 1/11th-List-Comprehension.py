l1 = [30, 40, 50, 60, 70]
l2 = []

for i in l1:
    l2.append(i)

print(l2, l1, sep='\n')

# List Comprehension

l3 = [i for i in l1 if i > 40]
print(l3)
