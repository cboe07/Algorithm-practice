Bubble Sort

_ Start at the first elemnt and compare to the one next to it
- If the left is bigger, they are out of order, SWITCH
- Go tot he next one and repeat
- Do the entire list, n times, and the list MUST be sorted

var unsorted = [5,2,6,3,1,3]

First time through
 - check [0] and [1] ... 5 > 2? YES. Switch.
 2,5,6,3,1,3
 - Check [1] and [2] ... 5 > 6? No.
 - Check [2] and [3] ... 6 > 3? Yes. Switch.
 2,5,3,6,1,3
 - Check [3] and [4] ... 6 > 1? Yes. Switch.
 2,5,3,1,6,3
 - Check [4] and [6] ... 6 > 3? Yes. Switch.
 2,5,3,1,3,6

 Secont time through 
 - Check [0] and [1] ... 2 > 5? No.
 - Check [1] and [2] ... 5 > 3? Yes. Switch.
 2,3,5,1,3,6
 - Check [2] and [3] ... 5 > 1? Yes. Switch.
 2,3,1,5,3,6
 - Check [3] and [4] ... 5 > 3? Yes. Switch.
 2,3,1,3,5,6
 - Check [4] and [6] ... 5 > 6? No.

 If n is list length, the biggest number is at n after 1 time.
 If n is list length, the 2 biggest numbers are at the end afetr 2 times
 Run a loop that goes through the whole array and checks each one.
 We only have to actually loop through the whole array minus the number of times already through

 1st iteraton = loop whole array
 2nd iteration = loop whole array -1
 3rd iteration = loop whole array -2
 4th iteration = loop whole array -3

 Consider the cases...
List is in reverse: Have to got hrough n elements n times
List is in order: Still have to go through n elements, n times

To optimize (modified bubble sort), set up a bool to false and if a switch is made, change to true.
At the end of loop, if bool is STILL false, no switches were made
LIST IS IN ORDER!!! STOP. Saved you a bunch of time.

Now the cases are different....
List is in reverse: Have to go through n elements, n times
List is in order: Loop once, bool is still false, stop



















