import Data from './Repository.py'

class Services:
     def __init__(self,Data,Routine):
         self.Data=Data
         self.Routine=Routine

class Routine:
    def __init__(self, dayIndex, hourIndex, courseIndex):
        self.dayIndex=dayIndex
        self.hourIndex=hourIndex
        self.courseIndex=courseIndex
    updatedRoutine=[]

    def createRoutine():
        print("Please provide input in the following format:")
        print("dayIndex(0 - 4) hourIndex(0 - 3) courseIndex")
        print("\n")
        inputList=[]
        for i in range(4):
            inputList.append(input().split())
        print(inputList)
        for i in range(4):
            index=inputList[i][2]
        updatedRoutine.append(Routine(inputList[i][0],inputList[i][1],Data.courses[index]))


class PrintServices(Services):
    def printData(data):
        for i in range(len(data)):
        print(data)

    def printRoutine(routineList):
        for i in range(4):
        print(f'{routineList[i].dayIndex} {routineList[i].hourIndex} {routineList[i].courseIndex}')

    def printCourseInfo(data):
        for i in range(data(list)):
            print (f'{i+1}. {data[i]}')


def main():
#Start of the app#
#Display service options
PrintServices().printData(self.Data.userPrompt)
#Take option input from user#
userInput=input()
#Go to the specific options
    if userInput=="A":
        PrintServices().printData(self.Data.courses)
        Routine.createRoutine()
        main()
    elif userInput=="B":
        PrintServices.printRoutine(self.Routine.updatedRoutine)
    elif userInput=="C":
        PrintServices.printCourseInfo(self.Data.classInfo)    
