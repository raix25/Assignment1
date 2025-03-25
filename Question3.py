#string is the user input 
string = (input("Please enter the string:"))
substring= 'm' #substring to navigation and occurence
string = string.lower() #so that M and m are treated equally

m_count= string.count(substring) #for counting the occurence of m
before_count = sum(1 for char in string if 'a' <= char < 'm') # for counting letters before m
after_count = sum(1 for char in string if 'm' <= char <= 'z')#for counting letter after m 

print(f'Number of occurence of m:',m_count)
print(f'Number of letters before m:',before_count)
print(f'Number of letters after m:', after_count)
