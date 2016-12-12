def function_builder(n):
	l=[]
	for i in range(n):
		print('creating something with', n)
		l.append(lambda x: x+i)
	print('end loop',i)
	return l


