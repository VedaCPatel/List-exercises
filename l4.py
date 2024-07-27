list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
j=[]
for i in list2[::-1]:
    j.append(i)
for x in range(list1):
    print(f"{list1[x]} {j[x]}")
