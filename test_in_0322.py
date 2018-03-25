def make_pizza(*toppings):
	print(toppings)

make_pizza('mushrooms', 'green peppers','extra chess')


def build_profile(first, last, **user_info):
	profile ={}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile =  build_profile('albert', 'einstein', location='princeton', field = 'physics')
print(user_profile)

#from  test_in_0321 import describe_pets as dp
#import test_in_0321 \\\\\test_in_0321.describe_pets(xxx)
#from  test_in_0321 import *
#dp('dog', 5,'coco')


class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __getxxx(self):
		print('\n a')
			
	def sit(self):
		print(self.name.title() + " is now sitting. ")
	
	def roll_over(self):
		print(self.name.title() + " rolled over!")
		self.__getxxx()
	



my_dog = Dog('willie', 5)

print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")

my_dog.sit()
my_dog.roll_over()

with open('test_file.txt') as file_object:
	contents =  file_object.read()
	print(contents)
	
