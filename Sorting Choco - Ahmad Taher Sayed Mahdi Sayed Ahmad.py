#To make this easier to implement, I will use two classes.
#One for chocolates to give them unique attributes.
#Another for studnets to give them chocolates.
#Lets start with defining the class chocolates first.
class Chocolate:
    #Here we give the chocolate its attributes
    def __init__ (self, ID, type, price, weight):
        self.__ID = ID
        self.__type = type
        self.__price = price
        self.__weight = weight

    #Here are the setter and getter functions for easy access
    def getID (self):
        return self.__ID
    def setID (self, ID):
        self.__ID = ID

    def getType (self):
        return self.__type
    def setType (self, type):
        self.__type = type

    def getPrice (self):
        return self.__price
    def setPrice (self, price):
        self.__price = price

    def getWeight (self):
        return self.__weight
    def setWeight (self, weight):
        self.__weight = weight

    #This is to display the chocolate
    def displayChocolate (self):
        return [self.__ID, self.__type, self.__price, self.__weight]


#Here we will define the class Studnet.
class Student:
    #Notice that we gave them a list for them to store their chocolate
    def __init__(self, studID, name):
        self.__studID = studID
        self.__name = name
        self.__givenChoco = []

    #Setter/getter functions
    def getStudID (self):
        return self.__studID
    def setStudID (self, studID):
        self.__studID = studID

    def getName (self):
        return self.__name
    def setName (self, name):
        self.__name = name

    #Here to give/remove chocolates
    def getGivenChoco (self):
        return self.__givenChoco
    def addChoco (self, chocolate):
        if chocolate not in self.__givenChoco:
            self.__givenChoco.append(chocolate)
    def removeChoco (self, chocolate):
        if chocolate in self.__givenChoco:
            self.__givenChoco.remove(chocolate)

    #This so we can display the student and their chocolates.
    def displayStudChoco (self):
        chocolates = []
        for choco in self.__givenChoco:
            chocolates.append(choco.displayChocolate())
        print (f"Student ID: {self.__studID}")
        print (f"Studnet name: {self.__name}")
        print (f"Student Chocolates: {chocolates}")


def choco_distrubution_iterative (chocolates, students):
    #This function goes through every chocolate in order.
    #Then gives them to the sudents.
    #Note: it pops the chocolate from the list when it is taken.
    #In other words, two students can't have the same chocolate.
    #This approch uses a for and a while loop to make it irreatitive.
    num_chocos = len(chocolates)
    num_studs = len(students)

    while chocolates and students:
        #This makes sure the code does not break when we have less students than chocolates and vice-versa.
        for i in range(min(num_chocos, num_studs)):
            temp = chocolates.pop(0)
            students[i].addChoco(temp)
            num_chocos -= 1  #Update the number of chocolates.
        num_studs = len(students)

def choco_distribution_recursive (chocolates, students):
    #The function first checks if the list is "empty" or not.
    #When it is empty it ends the recursive procces.
    #Then it pops the first chocolate and gives it to the first sutdent in the list.
    if not chocolates or not students:
        return
    temp = chocolates.pop(0)
    students[0].addChoco(temp)

    #Here the function excludes the first student from the process because they already have a chocolate.
    #A chocolate is alredy popped so we don't need to do the same.
    choco_distribution_recursive(chocolates, students[1:])

def choco_merge_sort (chocolates, attribute):
    #This function uses merge sort and asks for the attribute.
    #This helps it sort by either price or weight.
    if len (chocolates) == 1:
        return chocolates

    #Here we split the array.
    middle_idx = len(chocolates)//2
    left_array = chocolates[:middle_idx]
    right_array = chocolates[middle_idx:]

    #Here we recursively split the arrays until one element remains.
    left_array = choco_merge_sort(left_array, attribute)
    right_array = choco_merge_sort(right_array, attribute)

    #Here we merge the elements using another function.
    return choco_merge(left_array, right_array, attribute)

def choco_merge (left_array, right_array, attribute):
    #This is used to merge two arrays based on the given attribute.
    result = []
    left_index = 0
    right_index = 0

    #Here we check the attribute and merge accodringly:
    if attribute == "price":
        #In here we merge based on price.
        #If the item in left array has a lower price than the right, we added it to the result list.
        #Otherwise, we add the item in the right array.
        #These keeps going as long there are items left in both arrays.
        while left_index < len(left_array) and right_index < len(right_array):
            #Note we check the price but sort the chocolate itelf.
            if left_array[left_index].getPrice() < right_array[right_index].getPrice():
                result.append(left_array[left_index])
                left_index += 1
            else:
                result.append(right_array[right_index])
                right_index += 1

        #Here we add the remaning chocolate from the left array to the result.
        while left_index < len(left_array):
            result.append(left_array[left_index])
            left_index += 1

        #Here we add the remaning chocolate from the right array to the result.
        while right_index < len(right_array):
            result.append(right_array[right_index])
            right_index += 1

    #Here is the same but for merging the weight.
    elif attribute == "weight":
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index].getWeight() < right_array[right_index].getWeight():
                result.append(left_array[left_index])
                left_index += 1
            else:
                result.append(right_array[right_index])
                right_index += 1

        while left_index < len(left_array):
            result.append(left_array[left_index])
            left_index += 1

        while right_index < len(right_array):
            result.append(right_array[right_index])
            right_index += 1

    #In case the attribute does not exist.
    else:
        return "Attribute not available"

    return result


def search_choco (student_list, choco):
    #We go through every studen within a list.
    #If the student does have the chocolate within themselves
    #we return that student.
    for student in student_list:
        if choco in student.getGivenChoco():
            return student

#Here we create the chocolates and add them to the list.
choco1 = Chocolate ("001", "Hazelnut", 2.5, 6.0)
choco2 = Chocolate ("002", "Almond", 2.0, 5.0)
choco3 = Chocolate ("003", "Peanut butter", 4.0, 7.0)
chocolate_list = [choco2, choco3, choco1]
print (f"     Iterative process     ")
print (f"Chocolates before: {chocolate_list}")


#Here we create the studnets and add them to the list.
stud1 = Student ("202208928", "Ahmad Taher")
stud2 = Student ("202209842", "Stud 2")
stud3 = Student ("202201234", "Stud 3")
student_list = [stud1, stud2, stud3]
print ("Students before:")
for i in student_list:
    i.displayStudChoco()
print ("")

#Here we test that the distributive iterative function works.
#And show how everything looks after we distribute the chocolates.
#We can see that the function works as intended.
choco_distrubution_iterative (chocolate_list, student_list)
print (f"Chocolates after: {chocolate_list}")
print ("Students after:")
for i in student_list:
    i.displayStudChoco()
print("")


#Here we try the recursive method with new students and chocolates.
choco4 = Chocolate ("004", "Sour", 3.5, 10.0)
choco5 = Chocolate ("005", "Mint", 1.5, 3.0)
choco6 = Chocolate ("006", "Milk", 2.75, 7.0)
chocolate_list = [choco5, choco6, choco4]
print (f"     Recursive process     ")
print (f"Chocolates before: {chocolate_list}")

#Students are next.
stud4 = Student ("202253234", "Stud 4")
stud5 = Student ("202209968", "Stud 5")
stud6 = Student ("202200000", "Stud 6")
student_list = [stud4, stud5, stud6]
print ("Students before:")
for i in student_list:
    i.displayStudChoco()
print ("")

#Here we try the recursive function.
#We can see that it works as inteded due to students getting the chocolates.
choco_distribution_recursive (chocolate_list, student_list)
print (f"Chocolates after: {chocolate_list}")
print ("Students after:")
for i in student_list:
    i.displayStudChoco()
print("")


#Here we will test our merge sort using list of chocolates.
#We will sort one time by price and another by weight.
print ("    Merge Sort   ")
choco7 = Chocolate ("007", "Sour", 5.0, 9.0)
choco8 = Chocolate ("008", "Dark", 1.5, 3.5)
choco9 = Chocolate ("009", "Hazelnut", 2.75, 7.0)
choco10 = Chocolate ("010", "Milk", 3.5, 3.0)
choco11 = Chocolate ("011", "Almond", 2.0, 4.0)
chocolate_list = [choco7, choco8, choco9, choco10, choco11]


#We will print the list before sorting and after sorting.
#We will see that our function works as intended.
print ("Before sorting: ")
for i in chocolate_list:
    print (f"Chocolate {i.getID()}: [{i.getPrice()}, {i.getWeight()}gm]")

#Here we sort by price
print("")
print ("After sorting by price: ")
for i in choco_merge_sort(chocolate_list, "price"):
    print (f"Chocolate {i.getID()}: [{i.getPrice()}, {i.getWeight()}gm]")

#Here we sort by weight
print("")
print ("After sorting by weight: ")
for i in choco_merge_sort(chocolate_list, "weight"):
    print (f"Chocolate {i.getID()}: [{i.getPrice()}, {i.getWeight()}gm]")
print("")



#Here we define all chocolates and put them in a list.
#Do the same for students.
#We then sort the list and distribute the chocolates to the students.
#We then try to find a spesific chocolate and the holder using our function.
#You will see that our function is working as intended.
#Our chosen chocolate is choco10 because I like milk chocolate.
print ("Searching for a specific chocolate: ")
choco1 = Chocolate ("001", "Hazelnut", 2.5, 6.0)
choco2 = Chocolate ("002", "Almond", 2.0, 5.0)
choco3 = Chocolate ("003", "Peanut butter", 4.0, 7.0)
choco4 = Chocolate ("004", "Sour", 3.6, 10.0)
choco5 = Chocolate ("005", "Mint", 1.5, 3.0)
choco6 = Chocolate ("006", "Milk", 2.8, 7.0)
choco7 = Chocolate ("007", "Sour", 5.0, 9.0)
choco8 = Chocolate ("008", "Dark", 1.25, 3.5)
choco9 = Chocolate ("009", "Hazelnut", 2.75, 7.0)
choco10 = Chocolate ("010", "Milk", 3.5, 3.0)
choco11 = Chocolate ("011", "Almond", 2.01, 4.0)
chocolate_list = [choco1, choco2, choco3, choco4, choco5, choco6, choco7, choco8, choco9, choco10, choco11]

#Defining students and putting them in a list.
stud1 = Student ("202208928", "Ahmad Taher")
stud2 = Student ("202209842", "Stud 2")
stud3 = Student ("202201234", "Stud 3")
stud4 = Student ("202253234", "Stud 4")
stud5 = Student ("202209968", "Stud 5")
stud6 = Student ("202200000", "Stud 6")
stud7 = Student ("202201111", "Stud 7")
stud8 = Student ("202252222", "Stud 8")
stud9 = Student ("202203333", "Stud 9")
stud10 = Student ("202204444", "Stud 10")
stud11 = Student ("202205555", "Stud 11")
student_list = [stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, stud11]

#We will sort by price.
print ("Sorted list (by price): ")
chocolate_list = choco_merge_sort(chocolate_list, "price")
for i in chocolate_list:
    print (f"Chocolate {i.getID()}: [{i.getPrice()}, {i.getWeight()}gm]")
print ("")

#Here will distribute the chocolate to students.
#I used the recursive method because it is neat.
choco_distribution_recursive(chocolate_list, student_list)
print ("Chocolate we want: Choco10")

#Here we will use the function, then we will print all the students to confirm its accuracy.
print (f"Chocolate {choco10.getID()} holder is: {search_choco(student_list, choco10).getName()}")
print ("")

#Here is the full student list for confirmation.
#The code seems to work as intended.
print ("Full student list and their chocolate: ")
for i in student_list:
    i.displayStudChoco()

print ("")
print ("The code works as intended.")