#Write a phonebook app

print("""
Electronic Phone Book
 ====================
 1. Look Up an Entry
 2. Set an Entry
 3. Delete an Entry
 4. List All Entries
 5. Quit""")

phonebook_dict = {
    "Jazz": "334-584-2345",
    "Igor": "857-485-2935",
    "Melissa": "584-394-5857",
    "Gregory": "382-129-8376",
    "Trevor": "193-028-9135"
}


choice = input("What Do You Want to Do? (1 - 5)\n")

# 1.When they look up, ask fo rthe person's name
for phonebook in str(choice):                        
    if choice == 1:
        look_up = input("What is the person's name?")
        print("Name: " + str(look_up) + " Phone Number: " + str(phonebook_dict.get(look_up)) + "\nEntry stored for " + look_up + ".")

# 2. Set an Entry - Prompt user for a name and phone number
    elif choice == 2:
        set_name = input("What is the name you are adding?")
        set_number = input("What is their phone number?")
        phonebook_dict[set_name] = set_number
        print("Name: " + str(set_name) + "\nPhone number: " + str(set_number) + "\nEntry stored for " + str(set_name) + ".")

# 3. Delete an Entry - Prompt for the Person's Name and Delete the given person
    elif choice == 3:
        del_name = input("What is the person's name?")
        del phonebook_dict[del_name]
        print("Entry deleted for " + str(del_name) + ".")

 # 4. List All Entries - Print out Each Entry   
    elif choice == 4:
        print(phonebook_dict)

# 5. Quit - Ends the Program
    elif choice == 5:
        print("Bye")
        break
    
    else:
        print("Sorry that option does not exist.")
        break                                                     
                                                                    


