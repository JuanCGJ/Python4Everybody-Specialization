def computepay(h,r):
   if h<= b:
     p=h*r
     return p
   else :
     p=b*r
     add=(h-40)*r*a
     p=float(p+add)
     return p

hrs=input("Enter Hours:")
h=float(hrs)
hr=input("Enter Hours Rate: ")
r=float(hr)
b=float(40)
a=float(1.5)
p = computepay(h,r)
print("Pay",p)
