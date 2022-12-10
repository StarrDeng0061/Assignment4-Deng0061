import random

n = int(input("Enter list length n:"))
m = int(input("Enter (positive integer) m:"))

cpu_nbrs = []
for i in range(n):
    cpu_nbrs.append(random.randint(0,m))

while True:
    inp = input("Enter guess [0 "+str(m)+"]:")
    if int(inp) == cpu_nbrs[0]:
        print("You win!!")
        print("The cpu generated list:", cpu_nbrs)
        break
    cpu_nbrs.insert(0,cpu_nbrs.pop(n-1))