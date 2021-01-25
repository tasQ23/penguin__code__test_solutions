class Routine:

        def __init__(self,course,teacher):
            self.course=course
            self.teacher=teacher

        def __str__(self):
            return f"{self.course},{self.teacher}"


class AdvancedRoutine():
    def __init__(self, dayIndex, hourIndex, courseIndex):
        self.dayIndex=dayIndex
        self.hourIndex=hourIndex
        self.courseIndex=courseIndex

updatedRoutine=[]
courses=['English Grammar','Mathematics','Physics','Chemistry','Biology']
teachers=['John Smith','Lara Gilbert','Johanna Kabir','Danniel Robertson','Larry Cooper']

list=[]

for i in range(len(courses)):
    list.append(Routine(courses[i],teachers[i]))

def printList(l):
    for i in range(5):
        print(l[i])

def printCourses():
    for i in range(len(list)):
        print (f'{i+1}. {list[i].course}')

def optionA():
    printCourses()
    print("Please provide input in the following format:")
    print("dayIndex(0 - 4) hourIndex(0 - 3) courseIndex")
    print("\n")
    inputList=[]
    for i in range(4):
        inputList.append(input().split())
    print(inputList)
    for i in range(4):
        index=inputList[i][2]
        updatedRoutine.append(AdvancedRoutine(inputList[i][0],inputList[i][1],list[int(index)].course))


def optionB():
    for i in range(4):
        print(f'{updatedRoutine[i].dayIndex} {updatedRoutine[i].hourIndex} {updatedRoutine[i].courseIndex}')

def prompt():
    prompts=['A. Create Routine','B. Show Routine','C. List Courses with Teachers Name']
    for i in range(len(prompts)):
        print(prompts[i])


def main():
    prompt()
    userInput = input()
    if userInput=="A":
       optionA()
       main()
    elif userInput=="B":
       optionB()
    elif userInput=="C":
       printList(list)

if __name__ == "__main__":
    main()
