import random
import string       # for imporing all ascii characters 

char_set= string.ascii_letters + string.digits + string.punctuation

password=""

n=8
for i in range(1,n+1):
    password+=random.choice(char_set)


print(f"You Suggested Password: {password}")