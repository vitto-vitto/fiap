points = input('Insert client current points: ')
points = int(points) #turning points into int number

if points >= 1000:
    print('The client can receive more 3gb of bonus internet')
elif points >= 500:
    print('The client can receive more 1,5GB of bonus internet')
elif points >= 200:
    print('The client can receive more 500mb of bonus internet')
else:
    print("The client can't receive any bonus")