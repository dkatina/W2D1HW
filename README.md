# W2D1HW
Week 2 Day 1 Homework

## Exercise 1
Print out all cubed numbers up to the total value 1000.   
Meaning that if the cubed number is over 1000 break the loop.
Created a while loop to run until a specific condition is met. 

-The condition is p > 1000

within the while loop we had two variables.
-n, the counting variable, will increment everytime the loop passes
-p = n cubed.

P is then checked against the condition, and if p was not greater than 1000   
print the statement "n cubed is p"
and the loop would continue.

If P > 1000 the loop would break without printing anything for that particular pass.

## Exercise 2
Find the prime numbers up to 100 

I created a list sub_primes containing [2,3,5,7].   
I chose these numbers because every non-prime number 1-100 is divisible by atleast one of these.   
So they were used to test each number.

I then created a for loop that will itereate though every number 0-100, within it I defined n = 0 and another for loop.   
The second for loop iterates through my sub_prime list testing if the number mod test value != 0.   

If the number mod test != 0 then n would increment up 1.
Else, the loop would break and we would start testing the next number.

n served as my 'guy with a clipboard' tallying everytime a number would pass test.   
to be considered a prime number, the number could not be divisible by any of the numbers in sub_prime.   
Because there are 4 numbers in sub_primes, thats 4 tests to pass, meaning n would need to equal 4 for the number to be prime.

If n == 4 the number would be printed.

## Exercise 3
Take in a users input for their age, if they are younger than 18 print kids,   
if they're 18 to 65 print adults, else print seniors

This one was pretty easy, so I spiced it up a bit.

I created a While loop, which would ask if you'd like to test an age, Yes or No.   
This allows you test test as many ages as you like without having to restart the program.   

If you answer anything other than Yes or No for the initial question,   
the program will politly point this out and ask you to try again.

If yes, the program will ask for an age to test, and based on the criteria of Exercise 3 will check the age against 3 conditions   
and print the appropriate response.   
The program will then ask again if youd like to test an age, Yes or No,

If no, the loop will break and the program will end

