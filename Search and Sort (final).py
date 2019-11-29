class Person(object):
    def __init__(self, name, ID, age, gpa):
        self.name = name
        self.id = ID
        self.age = age
        self.gpa = gpa

    def __str__(self):
        output = "\n\nStudent Record for ID# {}\n".format(self.id)
        output += "Name: {} \nAge: {} \nGPA: {}".format(self.name, self.age, self.gpa)
        return output

####################################################################################################
class List(object):
    def __init__(self):
        self.studentList = []
        self.getList()

    def getList(self):
        try:
            file = open("students.txt", "r")
            name = file.readline().rstrip("\n")
            while len(name) != 0:
                id = int(file.readline().rstrip("\n"))
                age = int(file.readline().rstrip("\n"))
                gpa = float(file.readline().rstrip("\n"))
                self.studentList.append(Person(name, id, age, gpa))
                name = file.readline().rstrip("\n")
        except:
            print("File could not be opened")

    def spaces(self, name):
        tab = 24 - len(name)
        temp = ''
        for j in range(tab):
            temp += " "
        return temp

    def displayStudent(self, index):
        print(self.studentList[index])

    def display(self, listInfo):
        print('\nDisplaying {}'.format(listInfo))
        print("\nStudent ID#      Student Name              Age        GPA")
        print("=============================================================")
        for person in self.studentList:
            print("{}           {}".format(person.id, person.name), self.spaces(person.name),
                  "{}         {}".format(person.age, person.gpa))

    def swap(self, x, y):
        temp = self.studentList[x]
        self.studentList[x] = self.studentList[y]
        self.studentList[y] = temp


    def gpaSort(self):
        """sort the students list in descending order of GPA: bubble sort"""
        for maxIndex in range(len(self.studentList) -1,0,-1):
            for i in range(maxIndex):
                firstStudent = self.studentList[i]
                nextStudent = self.studentList[i +1]
                if firstStudent.gpa < nextStudent.gpa:
                    self.swap(i, i+1)


    def ageSort(self):
        """sort the students list in ascending order of age: insertion sort"""
        for index in range(1, len(self.studentList)):
            currentValue = self.studentList[index]
            i = index
            while i > 0 and self.studentList[i -1].age > currentValue.age:
                self.studentList[i] = self.studentList[i -1]
                i = i-1
            self.studentList[i] = currentValue





    def idSort(self):
        """sort the student list in descending order of id numbers: Selection sort"""
        for i in range(len(self.studentList)-1):
            minIndex = i
            for j in range(i + 1, len(self.studentList)):
                studentOne = self.studentList[j]
                studentTwo = self.studentList[minIndex]
                if studentOne.id > studentTwo.id:
                    minIndex = j
            self.swap(i, minIndex)

    def search(self, studentID):
        """search for a student in the student list with the passed idNumber
        return the index of the student if found, return -1 if not found: using binary search"""
        first = 0
        last = len(self.studentList) - 1
        mid = (first + last) // 2
        ID = (self.studentList[mid]).id
        while first <= last and ID != studentID:
            if ID > studentID:
                first = mid + 1
            else:
                last = mid - 1
            mid = (first + last) // 2
            ID = (self.studentList[mid]).id
        if ID == studentID:
            return mid
        else:
            return -1




############################################################################################
def main():
    studentArray = List()
    studentArray.display("UNSORTED LIST OF STUDENTS")
    input("\nPRESS ENTER TO SORT BY GPA")

    studentArray.gpaSort()
    studentArray.display("STUDENTS SORTED IN DESCENDING ORDER BY GPA")
    input("\nPRESS ENTER TO SORT BY AGE")

    studentArray.ageSort()
    studentArray.display("STUDENTS SORTED IN ASCENDING ORDER BY AGE")
    input("\nPRESS ENTER TO SORT BY ID#")

    studentArray.idSort()
    studentArray.display("STUDENTS SORTED IN DESCENDING ORDER BY ID#")
    input("PRESS ENTER TO CONTINUE")

    if hasattr(studentArray, "search"):
        try:
            idNumber = int(input("\n\nEnter the ID number of a student to search for: "))
            location = studentArray.search(idNumber)
            if location == -1:
                print("Student Not Found")
            else:
                studentArray.displayStudent(location)
        except ValueError:
            print("Run it again and type an integer value")
    input("\n\nPRESS ENTER TO QUIT")

if __name__ == '__main__':
    main()