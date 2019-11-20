#Problem-3
N = int(input("Enter A Number : "))
sum = 0
for i in range(1, N+1):
    sum = sum + i * i
print("Sum of Squares of first N Natural Numbers  Is : ",sum)
SUM = 0
for i in range(1, N+1):
        SUM = SUM + i
        sq = SUM * SUM
print("Squares of Sum of The N Natural Numbers Is : ",sq)
Diff = sq - sum
print("Difference Is : ",Diff)