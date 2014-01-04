"""Project - Expense report
Feature List:
1. Categorize spending:
	a. Groceries
	b. Eating Out
	c. Gas
	d. Online Shopping

2.  

Bugs:
1. Negative numbers are not deducted in the total
2. Amazon(Remote+Calendar) format not matched"""
import re

def main():
	
	expense_file = open('Data.txt','r')
	category_dict = {'Groceries': 0,
					'Eating Out': 0, 
					'Gas': 0, 
					'Online Shopping': 0,
					'Misc': 0} #Dictionary that keeps track of spenidng in each category {category->sum}
	total_spent = 0 #Total spent for the month
	grocery_keywords = ['valli', 'walmart', 'jewel', 'indian grocery', 'groc']
	eating_out_keywords = ['dinner', 'lunch', 'breakfast']


	text_data = expense_file.read()
	expense_file.close()
	match = re.findall(r'(\w+\+*\s*\w+)\s+\-*\$([0-9]+\.[0-9]+)', text_data) #Re for all the items
	#print match
	#print type(category_dict['Misc'])

	for description, cost in match:
		print description.lower(), float(cost)
		total_spent += float(cost)
		if description.lower() in grocery_keywords:
			print description
			category_dict['Groceries']+=float(cost)
		elif description.lower() == 'gas':
			category_dict['Gas'] += float(cost)
		else:
			category_dict['Misc']+=float(cost)
			


	print "Total spent this month: ",round(total_spent,2)
	print category_dict



if __name__ == '__main__':
  main()