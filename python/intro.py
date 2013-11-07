# Ben's intro to Python

# numbers!
age = 26

#why are these different output?
print(age/5)
print(age/5.0)
pi = 3.14159
avagadro = 6.02214E23

# strings!
s = 'Thomas Henry Huxley'
names = s.split()

#split is a string function, what does it return?
first_name = names[0]
middle_name = names[1]
last_name = names[2]
s2 = first_name + ' ' + middle_name + ' ' + last_name

# 'if' statement - indentation matters!
if (s == s2):
    print('yes!!!')
else:
    print('nooooooo')

# list (ordered sequence)
beatles = ['John', 'Paul', 'George', 'Pete', 'Stuart']
len(beatles)
beatles.pop()
beatles.pop()
beatles.append('Ringo')

led_zeppelin = ["Jimmy", "Robert", "John", "John"]

# 'for' loop - indentation matters!
for b in beatles:
    print('Hello ' + b)

# set (no order, no duplicates)
unique_zeppelin = set(led_zeppelin)
unique_beatles = set(beatles)

#which members are shared between the two?
shared = unique_zeppelin.intersection(unique_beatles)
print(shared)


# no guaranteed order when iterating over a set
for beatle in unique_beatles:
    print(beatle)

