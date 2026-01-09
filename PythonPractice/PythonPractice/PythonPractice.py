def flag():
    for i in range(3):
        print("*****===============")
    for i in range(3):
        print("====================")

print("hello")
name = input("What is your name")
age = int(input("What is your age?"))
if age >= 18:
    print(name + ", You can vote")
    flag()
else:
    print(name + ", You cannot vote")


