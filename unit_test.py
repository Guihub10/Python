import unittest
from test_in_0324 import get_formatted_name

#Test for function
class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name(first = 'shi', last = 'hao')
		self.assertEqual(formatted_name, 'shi hao')
	def test_first_last_name_2(self):
		formatted_name = get_formatted_name(first = 'shi', last = 'hao')
		self.assertEqual(formatted_name, 'Shi Hao')
#unittest.main();	
#Test for class


class AnoymousSurvey():
	def __init__(self, question):
		self.question = question
		self.responses = []
	def show_question(self):
		print(self.question)
	def store_response(self, new_response):
		self.responses.append(new_response)
	def show_results(self):
		print("Survey results: ")
		for response in self.responses:
			print('- ' + response)

question = "What language did you first learn as your second language?"
my_survey = AnoymousSurvey(question)

my_survey.show_question();
print("Enter 'q' at any time to quit. \n")
while True:
	response = input("language: ")
	if response == 'q':
		break;
	my_survey.store_response(response)

print("Thanks for everyone who participated in the survey! \n")
my_survey.show_results()
		
class TestAnoymousSurvey(unittest.TestCase):
	def setUp(self):
		question = "What language do you speak?"
		self.my_survey = AnoymousSurvey(question)
		self.responses = ['English', 'Chinese','Spanish']
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	def test_store_multi_response(self):
		self.my_survey.store_response(self.responses)
		self.assertIn(self.responses, self.my_survey.responses)
		
unittest.main()
