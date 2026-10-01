limit=float(input())
n=int(input())
error=0
prevish=0
peak=-10000000000.0
srznach=0.0
sum=0.0

for i in range (n):
    znach = input()
    if znach == 'error':
        error+=1
    else:
        znach=float(znach)
        if znach>limit:
            prevish+=1
        if znach>peak:
            peak=znach
        sum+=znach
srznach=sum/(n-error)
print(n)
print(error)
print(prevish)
print(f'{peak:.1f}')
print(f'{srznach:.1f}')
