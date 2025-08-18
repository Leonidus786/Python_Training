
print("🎉 Welcome to the Mini Quiz Game! 🎉")


score = 0 # We are using a variable to count points.

# Question -1

answer1 = input("Q1- What is 2+2 ?: ")

if answer1 == "4":
    print("correct")
    score += 1
else:
    print("Oops! The right answer is 4")
    
    
# Question - 2

answer2 = input("Q2- Which one is bigger? A cat or an elephant?")

if answer2.lower() == "elephant":
    print("correct Elephants are huge")
    score += 1
else:
    print("Nope!, it's the elephant")
    

print("Total score out of 2 is :",score)



