"""Project - Expense report"""

expense_sheet = open("Expenses_2014.xls", 'r')

for line in expense_sheet:
	print line

expense_sheet.close()