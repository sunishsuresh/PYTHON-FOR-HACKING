######################################methods                             #
name = "surya"
age = 20
gpa = 3.9

#print ("my name is " + name + " and i am age is " + age + " old ") # this statement is not gonna work you can't have diff type

print ("my name is " + name + " and i am age is " + str(age) + " old ")
print('\n') #new line
print("current age")
age += 1 #  '=+' its add number in variable
print (age)
age -= 1
print (age)
age /= 1  
print (age)

#######################################Relation and boolean operators                             #
greater_than = 8 > 5
less_than = 5 < 7
greater_then_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
print (greater_than,less_than,greater_then_equal_to,less_than_equal_to)
test_and = (7 > 6) and (8 < 6)
test_or = (5 >= 7) or (9 >=9)
print (test_and,test_or) 
print('\n')

###############################conditional statement##################
#soda with one parameter
def soda(money):
	if money >= 2:
		return print("YOU GOT YOUR SODA .ENJOY!!!!")
	else:
		return print("money is less no soda for you")

print('\n')
# beer program with two parameter
print(soda(3))
print(soda(1))
print(soda(10))	
def beer(age,money):
	if age >= 21 and money >= 5:
		return print("here is your beer enjoy!!!")
	elif age < 21 and money >= 5:
		return print("nice try kid")
	elif age >= 21 and money < 5:
		return print ("come back with more money")
	else:
		return print ("poor kid")
print(beer(19,100))
print(beer(22,50))
print(beer(21,4))
print(beer(28,23))
print(beer(19,1))
#####################################list##############################
print("list have brackets :")
movie =["go goa gone","your name","mob 100","aka one","lol is lol","full metal"]
print(movie[0])       #list should be in [] and start with 0
print(movie[0:4])     #[0:4] it take form (first item in the list)0 to 3 not(4)
print(movie[0:])      #[0:last item] take item form where you decide to end item
print(movie[:1])      #[first item:1] <-
print(movie[-1])      #last item from item
movie.append("pyscho") #'append' use to add item in list
print(len(movie)) #length of list
movie.pop(3) # .pop(index) it will remove that item. () <- this will remove last item
print(movie)
movie =["go goa gone","your name","mob 100","aka one","lol is lol","full metal"]
name = ["surya","harsh","harshitha","sunish","khan","faraaz"]
combine = zip(name,movie) #zipfunction <- it return zip object .its pair list item 
print(list(combine))
#####################################tuples############################

#tuples have parentheses and cannot change
grade =('A','B','C','D','F')
print(grade[0])

######################################loop###########################

#for loops -starts to finish of iterate
car =["maruti","BMW","coco","farari"]
for sykon in car:
	if sykon == "coco":
		break

#while loops execute as long as true
h=0
while h < 5:
	print(h)
	h+=1
