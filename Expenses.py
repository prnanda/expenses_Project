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
					'Online Shopping': 0} #Dictionary that keeps track of spenidng in each category {category->sum}
	total_spent = 0 #Total spent for the month


	text_data = expense_file.read()
	expense_file.close()
	match = re.findall(r'(\w+\+*\s*\w+)\s+\-*\$([0-9]+\.[0-9]+)', text_data) #Re for all the items
	#print match

	for description, cost in match:
		print description, float(cost)
		total_spent += float(cost)


	print total_spent



if __name__ == '__main__':
  main()