a = input("Enter num1 \n")
b = input("Enter num2 \n")
try:
    print("The sumo thes numbers is", int(a) + b)
except  Exception as e:
    print(e)

print("These line will be printed even if above line thrwos error , thats why we use try and catch")
