
#excercise1 range

list = [1,2,3,56,78,4,54,67,99989,30]

#excercise2 even-  now im going to make an even number program. 

list = range(100)

for numbers in list:
    if numbers % 2 == 0:
        print(numbers)

#excercise3   Create a list of numbers, create a new list which contains every number in the given list which is positive.

list = [ -1,-3,-5,-7,-8,-9,-10,1,2,3,4,5,6,7,8,565,3434,23,23121,24,2424,-32]

for num in list: 
    if num >= 0:
        print(num, end = '')


#excercise4 Positive Numbers II
#Create a list of numbers, create a new list which contains every number in the given list which is positive.



list1 = [ -1,-3,-5,-7,-8,-9,-10,1,2,3,4,5,6,7,8,565,3434,23,23121,24,2424,-32]
list2 = []

for num in list1:
    if num >= 0:
        list2.append(num) 
print(list2)  


#Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the 
#numbers in the first list multiplied by the factor. Print this list.


list = [ 1,2,3,4,5,6,7,8,989,3434,4546,1212,435,5675]
for num in list:
    multiplied_list = [element * 2 for element in list]

print(multiplied_list)


#Given a string, print the string reversed.


stringname = 'catthis is a string,  im going to attempt to print this string in reverse.'
stringlength = len(stringname)
print(stringname[stringlength::-1])

git remote add origin https://github.com/Softjafar00/excercises1-8-.git
git push -u origin master









