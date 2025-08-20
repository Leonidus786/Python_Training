
## loops -- Loops are like instructions you give to the computer:- "Keep doing this again and again until I say stop!".


## in python there are two types of loops --

# 1. for loop -- repeat a fixed number of times. -- In this loop you know how many time it is going to run.

# 2. while loop -- repeat while or until a condition is true. -- In this loop you don't know how many time it has to run.


# for loop -- The for loop is like: - Do this action for each number in a list or for each step in a range.


# coubting from 1 to 10

#for i in range(1,11): # range()  goes from 1 to 10
#    print(i)


#for i in range(1,11,2):
 #   print(i)
 

#count = 1

#while count<=10:
#    print(count)
#    count += 1  #(count + 1)
 
 
 
# Counting even numbers between 1 to 20


#for a in range(2,21,2): # starting from 2 , end = 21, step - 2
#    print(a)
    
    
#for a in range(1,21,2): # starting from 1 , end = 21, step - 1
#    print(a)


n = 19

print(f"Multiplication Table of {n}")

for i in range(1,11):
    print(f"{n} * {i} = {n * i}")
    

