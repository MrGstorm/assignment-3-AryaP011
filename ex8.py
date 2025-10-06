################################################################################
#Project Name: ex.8py
#Author: Arya Patel
#Task: write a program that keeps asking the user for words until they type exit
################################################################################
while True:
    word=input("enter a word(type'exit' to quit):")
    if word.lower()=="exit":
        print("goodbye")
        break
else:
    print(f"you entered: {word}")
    
