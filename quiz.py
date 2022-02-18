print("Welcome To My Computer Quiz")

playing=input("Do You Want to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! Let's Play :)")
score=0

answer = input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 

answer = input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")                 

answer = input("What does ROM stands for? ")
if answer.lower()=="read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 

answer = input("What does ALU stands for? ")
if answer.lower()=="arithmetic logic unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 

print("You Got "+str(score)+" correct")    
print("You Got "+str((score/5)*100)+" %")