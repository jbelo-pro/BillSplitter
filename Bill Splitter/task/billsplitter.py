import random
print('Enter the number of friends joining (including you):')
amount_party = int(input())
if amount_party <= 0:
	print('No one is joining for the party')
else:
	print('Enter the name of every friend (including you), each on a new line:')
	party = {}
	for n in range(amount_party):
		name = input()
		party[name] = 0
	print('Enter the total bill value:')
	bill = float(input())

	for k in party.keys():
		party[k] = round(bill/amount_party, 2)

	print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
	answer = input()
	if answer == 'Yes':
		r = random.randint(1, len(party))
		lucky = list(party.keys())[r]
		print(f'{lucky} is the lucky one!')

		new_amount = round(bill/(amount_party - 1), 2)
		for key, value in party.items():
			if key == lucky:
				party[key] = 0
			else:
				party[key] = new_amount
	else:
		print('No one is going to be lucky')
	print(party)