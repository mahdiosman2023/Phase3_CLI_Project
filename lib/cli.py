from function import list_dentists, date_appointment

def main():
    while True:
        print("1.Select dentist")
		
        print("2.Schedule an appointment")
		
        print("3.Exit application")
		
        userchoice = input("Select an option")
		
        if  userchoice == "1":
            list_dentists
            input("Enter to continue")
            
        elif userchoice == "2":
            date_appointment
            input("Enter to continue")
        
        elif userchoice == "3":
            print("Exit application")
            return 0
        
        else:
            print("Not applicable")
		
if __name__ == '__main__':
    main()
	