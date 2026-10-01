limit=float(input())
n=int(input())
error=0

for i in range (n):
    znach = input()
    if znach == 'error':
        error+=1

print(n)
print(error)
