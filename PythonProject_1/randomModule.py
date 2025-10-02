import random           # Don't need to install


print(random.randint(1,6))     # between 1 and 6 (inclusisve)

print(random.uniform(50,60))    # decimal value between 50 and 60

print(random.random())          # probablity between 0 and 1


names= ("Awais","Faiz","Ahad","Ali")

print(random.choice(names))         # for sequence like list,tuple,string

print(random.choice([9,7,8]))           # for multiple choices

population=["Punjab","Sindh","KPK","Balochistan"]

print(random.choices(population,k=3))   # k randm ele may be same

print(random.sample(population,k=3))        #  k randm ele unique

random.shuffle(population)
print(population)