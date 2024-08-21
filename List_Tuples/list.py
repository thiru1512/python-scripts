data_lis = ["mani","thiru",25,6.7,"george","peter","sam"]

num = [100,50,25]

data_tup = ( "mani", "tjiru",100,200,50,"kumar")

print(data_lis)

print(data_tup)

num.sort()

print(num)

type1 = type(data_lis)
type2 = type(data_tup)
print(type1,type2)

length = len(data_lis)
print(length)

length1= len(data_tup)
print(length1)

data_lis.append("new1")
print(data_lis)

data_lis.remove("new1")
print(data_lis)

new_list = data_lis + [1,2,3]
print(new_list)

list1 = ["babu","gopu"]

new_list1 = data_lis + list1

print(new_list1)

new_tup = ("babu","bob")
new_tup1 = data_tup + new_tup
print(new_tup1)


print(data_lis[0])

print(data_lis[0]+ " " + data_lis[1])

data_lis.append("new2")
print(data_lis)

print(len(data_lis))

subset = data_lis[1:5]

print(subset)

check = "mani" in data_lis
print(check)