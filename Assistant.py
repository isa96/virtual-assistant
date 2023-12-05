# Case Study: Virtual Assistant using Python (Assistant.py)

# import library
import smtplib
import random

class Assistant():

    # attribute
    def __init__(self, name):
    
        self.name = name
        self.initialize() # call initialize function, that function is written below

    # method        
    def run(self):
        
        # making menu option
        while True:

            menu_option = "1. Change My Name\n2. Create Schedule\n3. View Schedule\n4. Send Email\n5. Random Jokes\n0. Exit"

            print("\n*********************************************")
            print(f"Hello Python Folks, my name is {self.name}, how can I help you?")
            print(menu_option)
            print("*********************************************")

            menu = input("Which one do you want? ")

            if menu == "1":
                name = input("Input new name: ")
                self.change_name(name) # change the attribute of name
            elif menu == "2":
                self.create_schedule() # call create_schedule function that is written below
            elif menu == "3":
                self.view_schedule() # call view_schedule function that is written below
            elif menu == "4":
                self.send_email() # call send_email function that is written below
            elif menu == "5":
                self.random_jokes() # call random_jokes function that is written below
            elif menu == "0":
                print("Good bye!")
                break # the program stops and does not continue
            else:
                print("Invalid menu, please try again!")
    
    # making initialize function
    def initialize(self):
        print("New Virtual Assistant has been created successfully.")
        input("- Press ENTER -") # this function is executed at the beginning of the program, 
                                 # after pressing ENTER then the method section is executed

    # making change_name function
    def change_name(self, name):
        self.name = name # recall this statement which was previously created in the attribute section 
        print("\nMy name has been changed.")
        input("- Press ENTER -")
    
    # making create_schedule function
    # create a schedule using existing files "schedule.txt"
    def create_schedule(self):
        file = open("schedule.txt", "a") # append mode
        schedule = input("\nPlease input your agenda: (format: dd/mm/yyyy - agenda_name)\n")
        file.write(schedule + "\n") # add a agenda
        file.close()
        print("New schedule has been created.")
        input("- Press ENTER -")
    
    # making view_schedule function
    def view_schedule(self):
        print("\nHere is list of your schedule: ")
        file = open("schedule.txt", "r") # read mode
        print(file.read())
        file.close()
        input("- Press ENTER -")
    
    # making random_jokes function
    def random_jokes(self):
        jokes = [
        "Debugging is like being the detective in a crime movie where you're also the murderer at the same time.", 
        "Algorithm: A word used by programmers when they don't want to explain how their code works.", 
        "To whoever stole my copy of Microsoft Office, I will find you. You have my Word!",
        "I visited my friend at his new house. He told me to make myself at home. So I threw him out. I hate having visitors.",
        "A perfectionist walked into a bar... apparently, the bar was not set high enough."
        ]

        # making loop of jokes request
        while True:

            print(random.choice(jokes))
            is_again = input("Again [Yes/No]? ")

            # if Yes, the program is repeated
            # if No, the program stops
            if is_again.lower() == "no" or is_again.lower() == "tidak" or is_again.lower() == "0":
                break
    
    # making send_email function
    def send_email(self):
        sender = "fatahabduljalil@gmail.com" # email as a sender
        password = "kuvustfbivvylcgp" # apps password from gmail account setting
        receiver = []

        file = open("receiver_list.txt", "r") # read mode
        
        # loop for adding receiver
        for i in file:
            receiver.append(i)

        subject = "Greetings"
        body = "Hello, I hope you have a great day!"

        message = "Subject: %s\n\n%s\n\nSent from %s." % (subject, body, self.name)

        # program for sending email
        try:
            #Create your SMTP session 
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 

            #Use TLS to add security 
            smtp.starttls() 

            #User Authentication 
            smtp.login(sender, password)

            #Sending the Email
            smtp.sendmail(sender, receiver, message) 

            #Terminating the session 
            smtp.quit() 
            print ("Email sent successfully!") 
        
        except Exception as e:
            print("Oops! I found", e.__class__, "occurred.")
            print("Error message:", str(e))
            input("- Press ENTER -")
