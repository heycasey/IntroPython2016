def safe_input():
		try:
			variable=input('Please enter something: ')
		except (EOFError, KeyboardInterrupt) as the_error:
			print('\nYou have cancelled out')
		else:
			print('You said: ',variable)

safe_input()