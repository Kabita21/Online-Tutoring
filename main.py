class OnlineTutoringApp:

    def __init__(self):
        
        self.students ={}
        self.tutors ={}
        self.sessions = []

    def register_student(self):

        name =input("Enter Student Name:")
        email =input("Enter Student Email:")

        self.students[email] = {"name":name ,"email":email}

        print(f"Student '{name}' registered successfully!\n")

    def register_tutor(self):

        name =input("Enter Tutor Name: ")
        email =input("Enter Tutor Email: ")
        subject =input("Enter Subject Expertise: ")

        self.tutors[email] ={"name":name, "email":email, "subject":subject}

        print(f"Tutor '{name}'registered successfully!\n")    
 
    def view_tutors(self):

        if not self.tutors:

            print("No tutors registered yet.\n")

            return
        
        print("Available Tutors:")

        for tutor in self.tutors.values():

            print(f"-{tutor['name']} - {tutor['subject']} -{tutor['email']}")

            print()

        def schedule_session(self):

            student_email = input("Enter your email (student): ")   

            if student_email not in self.students:

                print("Student not found. Please register first.\n") 

                return
            
            tutor_email =input("Enter tutor email: ")

            if tutor_email not in self.tutors:

                print(f"Tutor not found.please check the email and try again.\n")
                return
            
            date = input("Enter session date (YYYY-MM-DD): ")

            time = input("Enter session time(HH:MM): ")

            self.sessions.append({

                "student" : self.students[student_email],
                "tutor" : self.tutors[tutor_email],
                "date" : date,
                "time" : time
            })

            print(f"Session scheduled successfully with {self.tutors[tutor_email]['name']} on {date} at {time}.\n")

        def view_sessions(self):

            if not self.sessions:

                print("No session scheduled yet.\n")

                return

            print("scheduled Session:")

            for session in self.session:

                print(f"{session['student']['name']} with {session['tutor']['name'] } on {session['date']} at {session['time']}")

                print()

            def run(self):

                while True:

                    print("Online Tutoring App")
                    print("1. Register as Student")
                    print("2. Register as Tutor")
                    print("3. View Tutors")
                    print("4. Schedule a Session")  
                    print("5. View Schedule Sessions")
                    print("6. Exit")

                    choice =input("Enter your Choice:")

                    if choice =="1":

                        self.register_student()

                    elif choice =="2":

                        self.register_tutor()

                    elif choice =="3":

                        self.view_tutors()

                    elif choice =="4":

                        self.schedule_session()

                    elif choice =="5":

                        self.view_session()

                    elif choice =="6":

                        print("Thank you for using the Online Tutoring App. Goodbye!")

                        break

                    else:
                        print("Invalid choice. Please try again.\n")
                        
                        
                    if __name__ =="_main_":
                        
                        app = OnlineTutoringApp()
                        app.run()    


     
      


                                                