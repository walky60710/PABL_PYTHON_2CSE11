
# print the sum of the values from 1 to 5 as follows. there are more but gib sol to these for now
Q. 01-01
print(1+2+3+4+5)

# Q. 02-02
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

# Q. 03-01
print('*' * 22)
print('# ' * 11)

# Q. 04-01
name = "David Doe"
address = "1600 Wilshire Blvd #205, Los Angeles CA 90017"
print(name, address)

# Q. 05-01
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True
print(5 != 5)    # False

# Q. 06-01
a = int(input())
b = int(input())
if a < b:
    print(a, b)
else:
    print(b, a)

# Q. 07-01
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor):"))
married = int(input("Are you married? (1 if you are married, 0 if you are single):"))
if adult == 1 and married == 1:
    print("You are an adult who is married.")
elif adult == 1 and married == 0:
    print("You are an adult who is single.")
elif adult == 0 and married == 1:
    print("You are a minor who is married.")
else:
    print("You are a minor who is single.")

# Q. 08-01
for i in range(2, 13):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, ": Prime number")
    else:
        print(i, ": Composite number")

# Q. 09-01
armstrong = []
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        armstrong.append(i)
print("Three-digit Armstrong numbers:", *armstrong)

# Q. 10-01
l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']
for a in l1:
    for b in l2:
        print(a, b)

# Q. 11-01
person = {'Name' : 'David Doe', 'Age' : 26, 'Weight' : 82, 'Job' : 'Data scientist'}
person['Father'] = 'John Doe'
print(person)

# Q. 12-01
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)

#Q. 13-01

a = [[1, 2], [3, 4], [5, 6]]
flat = []
for sub in a:
    for num in sub:
        flat.append(num)
print(flat)

#Q. 14-01
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(sum(maria.values()) / len(maria))

# Q. 15-01
import copy
school = {'kim': {'age': 16, 'hei': 170, 'grade': 3}, 'lee': {'age': 15, 'hei': 168, 'grade': 2}, 'choi': {'age': 14, 'hei': 173, 'grade': 1}}
school2 = copy.deepcopy(school)
print(school is school2)

#Q. 16-01
scores = (('Hyun', 88, 95, 90), ('Kang', 85, 90, 95), ('Park', 70, 90, 80), ('Hong', 90, 90, 95))
names, eng, math, sci = zip(*scores)
print(sum(math) / len(math))



