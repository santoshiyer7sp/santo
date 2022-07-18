a=list()
n=int(input("enter the size of list:"))
for i in range(n):
    b=int(input("enter a element:"))
    a.append(b)
c=tuple(a)
print("elements before reversing a tuple:",c)
a.reverse()
print("elements after reversing a tuple:",tuple(a))
