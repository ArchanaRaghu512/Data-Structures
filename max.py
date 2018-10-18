string = 'abb'

max = 0
for i in string:
    if string.count(i) > max:
        max = string.count(i)
print (max)
