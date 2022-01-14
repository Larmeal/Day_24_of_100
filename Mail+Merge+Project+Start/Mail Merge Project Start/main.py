#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as invited:
    invite = invited.readlines()

with open("/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_write = letter.read()
    for name in invite:
        invite_people = name.strip()
        each_letter = letter_write.replace("[name]", invite_people)

        with open(f"/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/letter_for_{invite_people}.txt", mode="a") as sent:
            sent.write(each_letter)