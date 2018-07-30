'''
Name = String reversal
Author = Archana Raghu
'''



""" string reversal using list comprehension """
string = "Batman"

k= [i for i in reversed(string)]
print("".join(k))

""" string reversal using slicing """

string = "batman"

print(string[::-1]) #using string slicing

""" using functions """

def strrev (string, start, end) :
	while start < end:
		""" swapping """
		string[start], string[end] = string[end], string[start]
		start += 1
		end -= 1

	return string

string = "Batman"
""" converting the string to a list """
string = list(string)
print("The given string is")
print(string)
""" returns the string as output """
print("reversed string is")
print(strrev(string, 0, len(string) -1))

