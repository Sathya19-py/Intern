#Problem-1
N = int(input("Enter A Number : "))
i = 0
for x in range(i,N):
    a = input("enter a email : ")
    if a == "username@domain.com":
        print("valid email")
        print(a)
    else:
        print("Invalid Email")
