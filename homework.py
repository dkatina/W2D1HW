#Exercise 1: Print out all cubed numbers up to the total value 1000. 
#Meaning that if the cubed number is over 1000 break the loop.
n = 0
while True:
    n +=1
    p = n ** 3
    if p > 1000:
        break
    else:
        print(f"{n} cubed is {p}")
print('end of cubed numbers <= 1000')
print()

#Exercise 2: Find the prime numbers up to 100 

sub_primes = [2,3,5,7]

for number in range(101):
    n = 0
    for test in sub_primes:
        if number == 1:
            break
        elif test == number:
            print(number)
        elif number % test != 0:
            n += 1
    if n == 4:
        print(number)
print("End of prime numbers")
print()

#Exercise 3: Take in a users input for their age,
#  if they are younger than 18 print kids,
#  if they're 18 to 65 print adults, else print seniors

while True:
    survey = input('Would you like to test an age to see if that age is elligible to vote? yes/no: ')
    if survey.lower() == 'yes':
        age = int(input("What age would you like to test?: "))
        if age < 18:
            print(f'\nFortunatly {age} year olds are considered kids and cannot vote\n')   
        elif age <= 65:
            print(f"\nYes! people who are {age} are considered adults and can vote!\n")
        else:
            print(f'\nDespite {age} year olds brains being in bad shape, \nand their ideas out of date, seniors actually CAN vote.\n')
    elif survey.lower() == 'no':
        print("I hope you've learned somthing today! Please don't come back.")
        break 
    else:
        print('\nIt seems you entered somthing other than YES or NO.......\nTry again Dummy!\n')


   

