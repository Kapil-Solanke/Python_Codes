# ls = ["roti", "kapda", "makan"]
# for i in ls:
#     print(i)
#     break
#
# else:
#     print("end")

# Note if there is no break in for then else is executed, but if there is break in for then  else is not executed

ls1 = ["roti", "kapda", "makan"]
for i in ls1:
    # print(i)
    if i == "kapda":
        break

else:
    print("Your item was not found")
