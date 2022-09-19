import math

a = float(input('Inform the value of A: '))
b = float(input('Inform the value of B: '))
c = float(input('Inform the value of C: '))

delta = b * b - 4 * a * c

if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("For the equation {}x2 + {}x + {} = 0, we obtained the following values: x1 = {} and x2 = {}".format(a,b,c,x1,x2))
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2*a)
    print("For the equation {}x2 + {}x + {} = 0, we obtained the following value: x = {}".format(a,b,c,x))
else:
    print("For the equation {}x2 + {}x + {} = 0, there are no real values for x".format(a,b,c))