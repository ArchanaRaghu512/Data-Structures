'''
Name = Palindrome
Author = Archana Raghu
'''


def Palindrome():
    string1 = input('Enter a string: ')
    string2 = string1[::-1]
    if string1 == string2:
        return 'It is a palindrome'
    else:
        return 'It is not a palindrome'

print(Palindrome())



