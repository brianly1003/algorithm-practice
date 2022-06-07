# Microsoft | SDE | Hyderabad | Dec 2019 [Accepted] and My failure experiences. Do read
### https://leetcode.com/discuss/interview-experience/458962/Microsoft-or-SDE-or-Hyderabad-or-Dec-2019-Accepted-and-My-failure-experiences.-Do-read.


## Question #1:
The question was to add a digit to a number that is represented by a linked list, where each node is a digit of the number. 
The constraint here was that the linked list couldn’t be modified, except the digits to be modified in answer and the number could be infinitely long. 
So you had to avoid the problem of memory overflow. 
So no recursion, no stack, no copy of linked list, no change to original linked list, as suggest the solutions on geeksforgeeks.

--> To keep track of carry to be added to previous digit iteratively, you basically have to keep a track of the digit before the last consecutive 9 that preceeds the last digit. For example in 9719938996, this would be the 4the digit from right, that is 8. So now in a single pass, you can figure out such a position of 9(if any) and also the last digit. Then the required digits can be changed easily.

# https://www.geeksforgeeks.org/add-the-given-digit-to-a-number-stored-in-a-linked-list/




