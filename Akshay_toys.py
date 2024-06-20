'''Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''

marks=list(map(int,input("enter the marks").split()))
min_marks=min(marks)
print(min_marks)