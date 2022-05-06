import os
def decofun(fun):
    def subfun():
        print("subfun")
        fun()
    return subfun

@decofun
def fun():
    print("fun")


v="₹53,000"
s=v.split('₹')
c=s[1]
s2=c.split(',')
print(s2)
l=len(s2)
d=""
for x in range(0,l):
    d=d+s2[x]
i=int(d)
print("int: ",i)
assert i>59000, "I i greater than expected"
print("After assertion")