#student_list.py
"""
Purpose of code- To print all the students' name with the second lowest
                 and equal score.
"""
import heapq
def second_students(entry): #input list with names ex.(['Amit',65],['Harsh',50])
        
        trim_marks_list1=[]                             
        trim_marks_list2=[]
        second_smallest=[]
        Students=[]
        Students_list=[]
        marks_list=[]

        for i in range(0,len(entry)):
                marks=entry[i][1]               
                marks_list.append(marks)        #list containing only marks
                trim_marks_list1=list(set(marks_list))  #remove duplicate elements
                trim_mark_list2=heapq.nsmallest(2,trim_marks_list1) 
                second_smallest=heapq.nlargest(1,trim_mark_list2) #find second smallest no.    

        for x in range(0,len(entry)-1):
                if entry[x][1]==second_smallest[0]:  #Match list with every 
                        Students=entry[x][0]
                        Students_list.append(Students)

        print("Students are:",Students_list)
