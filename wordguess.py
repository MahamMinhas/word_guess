#Take a string (hardcode) take input from user for a variable guess (user input). Match the length of the 
# both words if length not equal then wrong else if length is equal then check if string is same character by 
# character if not wrong else the print the characters that are at correct index and are matched and # for those 
# that are  present but not on right index and ~ for those that are toto wrong.

word="hello"
guess=input("Enter the word: ")

if(len(word)==len(guess)):
    guessed=""
    for i in range(len(word)):
        if(guess[i]==word[i]):
           guessed+=guess[i]
        elif(word.find(guess[i]) != -1):
             guessed+="#"
        else:
             guessed+="~"
    print(guessed)
       
else:
    print("OOPS! your guess is wrong")