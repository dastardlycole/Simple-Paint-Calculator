#Simple app Paint calculator

#how much paint is needed

print('Paint calculator')
print('Enter a wall size as width, height in feet or press enter to stop')
print('Example: 12, 8')

# Variables
walls=[] # list of wall measurements
gallons=1/350 # one gallon covers 350 square feet
total=0 #total gallons to buy

# Get user input
while True:
    s=input('Enter a wall size')# user input for wall size
    if len(s)==0: 
        break # this continues asking for wall size until user has no more and then breaks

 #Verify the input   
    sqft=s.split(',')
    if len(sqft)<2:
        print('Invalid format')
        break
    #   Convert string to ints
    w=int(sqft[0])#gets the width
    h=int(sqft[1])#gets the height
    item=(w,h)
    walls.append(item)
    print(f'Adding wall:{item}')

    #Calculate how much paint is needed
    print(f'you entered: {walls}')
    for m in walls:
        w=m[0]
        h=m[1]
        s=w*h
        v=s*gallons
        total+=v #or you could write total = total+v

print(f'You need to buy {round(total,2)} gallons of paint') #this is  just like fprintf %s to get it to 2 dp       