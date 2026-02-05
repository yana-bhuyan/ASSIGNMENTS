### Experiment 1: Arrays, Strings, Recursion, and Matrices in C

#### 1)  Find sum of all array elements using recursion

####  Aim:

To find the sum of all array elements using recursion.

#### Algorithm:
1. Start
2. Read number of elements `n`
3. Read `n` elements into an array
4. Call a recursive function to calculate sum
5. If `n` becomes 0, return 0
6. Otherwise, return last element + recursive call
7. Display the sum
8. Stop

#### Program:
![alt text](<Screenshot 2026-02-05 214003-1.png>)
#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 214205-1.png>)
![alt text](<Screenshot 2026-02-05 214237-1.png>)
#### Observation:
It was observed that recursion successfully calculates the sum of all array elements by repeatedly calling the function until the base condition is reached. The program correctly processes the input array and produces the expected output for different input sizes.

#### Result:
The program was executed successfully and the sum of all array elements was obtained correctly using recursion.

---

#### 2) Insert and delete element from array

#### Aim:
To insert an element at the ith position and delete an element from the jth position of an array.

#### Algorithm:
1. Start
2. Read size of array `n`
3. Read array elements
4. Read position `i` and element to insert
5. Shift elements and insert the value
6. Read position `j` to delete
7. Shift elements to remove the value
8. Display the final array
9. Stop

####  Program:
![alt text](<Screenshot 2026-02-05 214943-1.png>)
![alt text](<Screenshot 2026-02-05 215235-1.png>)

#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 225444-1.png>)
#### Observation:
It was observed that the array elements shift correctly during insertion at the specified position and deletion from the given position, and the array size updates accordingly.

#### Result:
The program was executed successfully and insertion and deletion operations in the array were performed correctly.

---

#### 3)  Convert uppercase string to lowercase

#### Aim:
To convert an uppercase string to lowercase using a for loop.

#### Algorithm:

1. Start
2. Read the string
3. Traverse the string using for loop
4. Convert uppercase characters to lowercase
5. Display the converted string
6. Stop

#### Program:
![alt text](<Screenshot 2026-02-05 220748-1.png>)

#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 230803-1.png>)
#### Observation:
It was observed that each uppercase character in the string was correctly converted to its corresponding lowercase character using a for loop.

#### Result:
The program was executed successfully and the string was converted from uppercase to lowercase.


---

#### 4) Find sum of rows and columns of matrix

#### Aim:
To find the sum of rows and columns of a given matrix.

#### Algorithm:

1. Start
2. Read number of rows and columns
3. Read matrix elements
4. Calculate sum of each row
5. Calculate sum of each column
6. Display results
7. Stop

#### Program:
![alt text](<Screenshot 2026-02-05 231141-1.png>)
![alt text](<Screenshot 2026-02-05 231234-1.png>)
![alt text](<Screenshot 2026-02-05 231340-1.png>)

#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 231903-1.png>)
#### Observation:
It was observed that the program correctly calculated the sum of each row and each column of the given matrix.

#### Result:
The program was executed successfully and the row-wise and column-wise sums of the matrix were displayed correctly.

---

#### 5) Find the product of two matrices using pointers

#### Aim:
To find the product of two matrices using pointers.

##### Algorithm:

1. Start
2. Read order of both matrices
3. Read matrix elements
4. Multiply matrices using pointer notation
5. Display the resultant matrix
6. Stop

#### Program:
![alt text](<Screenshot 2026-02-05 223904-1.png>)
![alt text](<Screenshot 2026-02-05 224118-1.png>)
#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 232042-1.png>)
####  Observation:
It was observed that the program multiplied the two matrices correctly using pointer notation, and all elements of the product matrix were calculated accurately.

#### Result
The program was executed successfully and the product of the two matrices was obtained correctly.

---

#### 6)  Linear search in an array

#### Aim:
To perform linear search on an array and report success or failure.

#### Algorithm:

1. Start
2. Read number of elements
3. Read array elements
4. Read element to search
5. Compare element with each array item
6. If found, display success message
7. Else, display failure message
8. Stop

#### Program:
![alt text](<Screenshot 2026-02-05 233026-1.png>)
![alt text](<Screenshot 2026-02-05 233110-1.png>)
#### Compilation and Execution:
![alt text](<Screenshot 2026-02-05 233432-1.png>)
#### Observation:
It was observed that the program successfully searched for the given element by checking each array element sequentially.

#### Result
The program was executed successfully and correctly reported whether the element was found or not.

---