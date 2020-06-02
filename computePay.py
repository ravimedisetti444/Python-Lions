def computepay(h,r):
    if h>40:
    	p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = r*h
    return p

hrs = input("Enter Hours:")
rate= input("Enter Rate per hour:")
try:
    h=float(hrs)
    r=float(rate)
    print("Pay",computepay(h,r))
except:
    print("Please enter in digits!!!")
