
#lesson.4
#1
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20}

# Ascending
ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", ascending)

# Descending
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", descending)

#2
d = {0: 10, 1: 20}
d[2] = 30
print(d)  # {0: 10, 1: 20, 2: 30}

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)

#4
n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#5
squares = {x: x**2 for x in range(1, 16)}
print(squares)

#set exercises
#1
my_set = {1, 2, 3, 4}
print(my_set)

#2
for item in my_set:
    print(item)

#3
my_set.add(5)
my_set.update([6, 7])
print(my_set)

#4
my_set.remove(3)  # Error if 3 not in set
print(my_set)

#5
my_set.discard(10)  # no error if 10 not in set
print(my_set)
