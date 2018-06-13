print("list with user defined input")
x=input("enter 1st no :")
y=input("enter 2nd no :")
z=input("enter 3rd no :")
l=[x,y,z]
print(l)
print("add new list to above list-")
ll=["google","apple","facebook","microdsoft","tesla"]
print(l.extend(ll))
print(l)
print("count the no. of times :")
l1=[1,2,3,1,2,1,1]
print(l1)
print(l1.count(1))
print("sorting of number-")
l1.sort()
print(l1)
print("create 2 array and then merge-")
l2=[4,2,5]
print(l2)
l2.sort()
print(l2)
l3=[3,1,8,3,5]
print(l3)
l3.sort()
print(l3)
l4=l2+l3
l4.sort()
print(l4)
print("implement stack and queue using list-")
l5=[]
l5.append(int(input("enter any no :")))
l5.append(int(input("enter any no :")))
l5.append(int(input("enter any no :")))
print(l5)
print("stack-")
l5.pop()
print(l5)
print("queue-")
del l5[0]
print(l5)
l5.append(int(input("enter any no :")))
l5.append(int(input("enter any no :")))
print(l5)
print("stack-")
l5.pop()
print(l5)
print("queue-")
del l5[0]
print(l5)

