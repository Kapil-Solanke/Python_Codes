# **************************************** LIST COMPREHENSIONS *******************************************
# for list comprehensions we use square brackets

# ls = []
# for i in range(100):
#     if i %3 == 0:
#         ls.append(i)

# ls = [i for i in range(100) if i % 3 == 0]
# Condition is optional
# print(ls)

# **************************************** DICTIONARY COMPREHENSIONS *******************************************
# for dictionary comprehensions we use curly brases with key value pairs

# dict1 = {1: "Item1", 2: "item2",...100:"item100"}

# dict1 = {i: f"item{i}" for i in range(100)}
# dict1 = {i: f"Item{i}" for i in range(5)}
# dict1 = {value: key for key, value in dict1.items()}
# print(type(dict1))
# print(dict1)

# **************************************** SET COMPREHENSIONS *******************************************
# for set comprehensions we use curly brases

# set1 = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
# print(set1)
# print(type(set1))

# **************************************** GENERATOR COMPREHENSIONS *******************************************
# generator set comprehensions we use paranthesis

evens = (i for i in range(100) if i % 2 == 0)
print(type(evens))
for i in evens:
    print(i)

# we can iterate generators only one time
# for i in evens:
#     print(i)


# **************************************** Practice Question *******************************************
i = int(input("How many items in list\n"))
list1 = []
for j in range(i):
    item = list1.append((input()))

# print(list1)

print("Which type of comprehension o you want\nEnter 1 for list comprehension\nEnter 2 for set comprehension\n"
      "Enter 3 for dict comprehension\n")
choice = int(input())

if choice == 1:
    list2 = [i for i in list1]
    print(list2)

elif choice == 2:
    list2 = {i for i in list1}
    print(list2)
elif choice == 3:
    list2 = {key: value for key, value in enumerate(list1)}
    print(list2)