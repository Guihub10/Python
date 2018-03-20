fruits = ['banana','pear','strawberry','apple']

print('For each fruit in fruits:')
for fruit in fruits:
	print(fruit.title()+ '\t')

print("\nOriginal fruits is:" )
print(fruits)

fruits.sort(reverse = True)
print("\nFruits after reverse sort is:" )
print(fruits)

print("\nSorted fruits is:" )
print(sorted(fruits))

fruits.reverse()
print("\nFruits after reverse is:" )
print(fruits)

fruits.insert(2,'orange');
print("\nFruits after insert orange at 2 and append grapes is:" )
print(fruits.append('grapes'))

del(fruits[0])
print("\nFruits after del by index 0 is:" )
print(fruits)

fruits.remove('banana')  #Only remove the first meeting one
print("\nFruits after remove value 'banana' is:" )
print(fruits)

fruits.pop()
print("\nFruits after pop is:" )
print(fruits)

