Student name : Swayam Uddeepta Bhuyan
Sap id: 590021784
Batch : B-17
Course : Btech Cse
Subject : DSA
Experiment : 2
# Experiment 2:Linked List Data Structure and its Applications
## Objective: To experiment the concept of pointers, structure and dynamic memory allocation to realize linked list and its application.
## 1)  Implement single Linked List data structure and its operations like insert and delete in the beginning/end and nth position of the list, and display the items stored in the linked list.
###  Aim:
To implement a Single Linked List and perform operations such as:
Insertion at beginning
Insertion at end
Insertion at nth position
Deletion at beginning
Deletion at end
Deletion at nth position
Display the elements of the linked list
### Algorithm:
1.Start
2.Initialize head pointer to NULL
3.Create a node with given data
4.For insertion at beginning, link new node before head and update head
5.For insertion at end, traverse list to last node and attach new node
6.For insertion at nth position, traverse to (n-1) node and insert new node
7.For deletion at beginning, move head to next node and delete first node
8.For deletion at end, traverse to second last node and delete last node
9.For deletion at nth position, traverse to (n-1) node and delete nth node
10.Traverse the linked list from head to NULL and display elements
11.Stop
### Program:
![alt text](<Screenshot 2026-02-20 215657-1.png>)
![alt text](<Screenshot 2026-02-20 220013-1.png>)
![alt text](<Screenshot 2026-02-20 220102-1.png>)
![alt text](<Screenshot 2026-02-20 220139-1.png>)
![alt text](<Screenshot 2026-02-20 220218-1.png>)

### Compilation and Execution:
![alt text](<Screenshot 2026-02-20 220256-1.png>)
### Observation:
Linked list uses dynamic memory allocation.

Insertion and deletion are easier compared to arrays.

Pointer manipulation is essential.

Traversal is required to access elements.
### Result:
The single linked list was successfully implemented and operations like insertion, deletion, and display were performed correctly.

---
## 2)Using single linked list and functions implement Stack and its operations like insert, delete, and display.
###  Aim:
To implement Stack using Single Linked List and perform operations such as push, pop, and display.
### Algorithm:
1.Start
2.Initialize top pointer to NULL
3.push operation, create a new node and insert it at beginning (update top)
4.For pop operation, delete the first node and update top
5.For display, traverse from top to NULL and print elements
6.Stop
### Program:
![alt text](<Screenshot 2026-02-20 220617-1.png>)
![alt text](<Screenshot 2026-02-20 220644-1.png>)
![alt text](<Screenshot 2026-02-20 220714-1.png>)
### Compilation and Execution:
![alt text](<Screenshot 2026-02-20 221029-1.png>)
### Observation:
Stack follows LIFO principle.

Push and pop happen at the beginning.

Linked list allows dynamic memory allocation.
### Result:
Stack was successfully implemented using a linked list and push, pop, and display operations were performed.

---