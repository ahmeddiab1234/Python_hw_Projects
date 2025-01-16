# hW - 1 - Operator - Logical Operator - Create Logic!

nb,ng,nt = map(int, input().split())

print(nb > 25)
print(ng <= 30)
print(nb>20 and nt>2 and ng>30 and nt>4)
print(nb<60 or ng <70)
print((not nb>=60) and (not ng>=70))
print(nb >= ng+10)
print((nb-ng > 10) or (nt>5))
print((nb >= ng+10) or (ng >= nb+15))
'''
nb=10, ng=15,Z=20
10 15 20
False
True 
False
True 
True 
False
True 
False
'''