Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello this is python programming"
>>> text.split()
['hello', 'this', 'is', 'python', 'programming']
>>> text = "hello    this  is    python           programming"
>>> text.split()
['hello', 'this', 'is', 'python', 'programming']
>>> t = text.split()
>>> t
['hello', 'this', 'is', 'python', 'programming']
>>> ' '.join(t)
'hello this is python programming'
>>> ratings = [5,6,7,8,8,8,9,7,6]
>>> d = {}
>>> for i in range(len(ratings)):
	d['user_{}'.format(i)] = ratings[i]

	
>>> d
{'user_0': 5, 'user_1': 6, 'user_2': 7, 'user_3': 8, 'user_4': 8, 'user_5': 8, 'user_6': 9, 'user_7': 7, 'user_8': 6}
>>> 
