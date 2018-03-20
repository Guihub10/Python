for value in range(1,5):
	print(value)
	
numbers = list(range(1,16,2))#create list with function range, start with 1, end with 15 and step length is 2
print(numbers)

print(numbers.pop() ** 2)# ** stands for square

squares = [value**2 for value in range(1,6)] #initialize a list with for sentence
print(squares)

print(squares[0:3]) # a cut off of squares
print(squares[-2:])

for value in squares[2:-2]:
	print(value) 

newreference =  numbers;
newcopy =  numbers[:]
print(newreference,newcopy)
numbers.append(100)
print(newreference,newcopy)

dimensions = (0,100) #it is unchangeble

words = ['zealous' , 'clarify', 'vulgar', 'aspire','slavish','antiquated']
unhandled = 'antiquated'

if unhandled not in words:
	print("No unhandled word")
elif 'apple' in words:
	print('apple is not is list')
else:
	print("An unhandled word " + unhandled.title())




