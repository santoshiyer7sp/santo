a=list()
n=int(input("enter the size of list:"))
for i in range(n):
    b=int(input("enter a element:"))
    a.append(b)

print("list with duplicates:",a)
c=tuple(set(a))
print("tuple without duplicates:",c)