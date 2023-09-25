print("Ｗｅｌｃｏｍｅ ｔｏ ｍｙ ｑｕｉｚ!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the current PM of India? ")
if answer.lower() == "Nsrender modi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("how many state in India? ")
if answer.lower() == "28 states":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("jaganath temple situated in? ")
if answer.lower() == "Odisha":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("First computer in the world? ")
if answer.lower() == "ENIAC":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")