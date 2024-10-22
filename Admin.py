from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == self.__username and password == self.__password :
            return True
        else:
            return False
       
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        # print('Enter the doctor\'s details:')
        first_name=input("Enter the first name:")
        surname=input("Enter the surname:")
        speciality=input("Enter the speciality:")
        return first_name,surname,speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op=input("Input:")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            # get the doctor details
            doctor_fname,doctor_surname,doctor_speciality=self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if doctor_fname == doctor.get_first_name() and doctor_surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists=True
                    break

            #ToDo6
            if(name_exists == False):
                doctors.append(Doctor(doctor_fname,doctor_surname,doctor_speciality))
                print('Doctor registered.')


        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                if(len(doctors)!=0):
                    try:
                        index = int(input('Enter the ID of the doctor: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index!=False:
                            break
                        else:
                            print("Doctor not found")
    
                        
                        # doctor_index is the ID mines one (-1)
                        

                    except ValueError: # the entered id could not be changed into an int
                        print('The ID entered is incorrect')

            # menu
            if(len(doctors)!=0):
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
                op = int(input('Input: ')) # make the user input lowercase

                if(op==1):
                    new_first_name=input("Enter the new first name:")
                    doctors[index].set_first_name(new_first_name)
                    print("Doctor Details Updated")
                elif(op==2):
                    new_surname=input("Enter the new surname:")
                    doctors[index].set_surname(new_surname)
                    print("Doctor Details Updated")
                
                elif(op==3):
                    new_speciality=input("Enter the new speciality:")
                    doctors[index].set_speciality(new_speciality)
                    print("Doctor Details Updated")
                else:
                    print("Invalid input!!")
       
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            if(len(doctors)!=0):
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                if(doctor_index>=0 and doctor_index < len(doctors)):
                    del doctors[doctor_index]
                else:
                    print('The id entered is incorrect')

        #if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        for index, item in enumerate(patients):
            print(f'{index+1:3}|{item}')


    def assign_doctor_to_patient(self, patients, doctors):
        assign = []
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(patients):
            print(f'{index+1:3}|{item}')

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID minus one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()  # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        for index, item in enumerate(doctors):
            print(f'{index+1:3}|{item}')
        doctor_index = int(input('Please enter the doctor ID: '))

        try:
            # doctor_index is the doctor ID minus one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index, doctors) != False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
            
                # link the patient to the doctor and vice versa
                print('The patient is now assigned to the doctor.')

                # Update the patient records in the file
                if Patient.save_records(patients):
                    print("Patient records successfully updated in patient.txt.")
                else:
                    print("Failed to update patient records.")

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')



    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)
        discharge_patient=[]
        if(len(patients)!=0):
            patient_index = int(input('Please enter the patient ID: '))-1
            discharge_patient.append(patients[patient_index])
            if patient_index  in range(len(patients)):
                    discharge_patients.append(patients.pop(patient_index))
                    print(f"Patient with ID:'{patient_index+1}' has been discharged")

                

    def view_discharge(self, discharged_patient):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, item in enumerate(discharged_patient):
            print(f'{index+1:3}|{item}')
        #ToDo13

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter the new username: ')
            self.__username = username
            print("username successfully changed.")
        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if(password == input('Enter the new password again: ') and self.__password!=password):
                self.__password = password
                print("password successfully changed.")
            else:
                print("Sorry something went wrong")
        elif op == 3:
            address = input('Enter the new address: ')
            self.__address= address
            print("address successfully changed.")
        else:
            print("Invaild input!!!")

    
    def read_records():
        patients = []
        try:
            with open("responsiveness/patient.txt", 'r') as fd:
                # Skip the header line
                next(fd)

                for line in fd:
                    line = line.strip()
                    if line:
                        parts = line.split('|')
                        full_name = parts[1].strip()
                        doctor_name = parts[2].strip()
                        age = int(parts[3].strip())
                        mobile = parts[4].strip()
                        address = parts[5].strip()
                        symptoms = [symptom.strip() for symptom in parts[6].split(',')]

                        patient = Patient(full_name.split()[0], full_name.split()[1], age, mobile, address, symptoms)
                        patient.link(doctor_name)
                        patients.append(patient)

            return patients

        except FileNotFoundError:
            print("Patient records file not found.")
            return []
        except Exception as e:
            print("Failed to read patient records:", str(e))
            return []
        
    def doctor_relocate(self, patients, doctors):
        print('Select the doctor that you need to relocate:')
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            doctor_index = input('Please enter the doctor ID to relocate: ')
            doctor_index = int(doctor_index) - 1

            if self.find_index(doctor_index, doctors) != False:
                print('The entered ID is found')
            else:
                print('The entered ID is not found')
                return

        except ValueError:
            print('Invalid ID')
            return

        print("-----Relocate-----")
        self.view(patients)

        try:
            patient_index = input('Please enter the patient ID to relocate doctor: ')
            patient_index = int(patient_index) - 1

            if patient_index in range(len(patients)):
                old_doctor = patients[patient_index].get_doctor()  # Get the old doctor's name
                patients[patient_index].link(doctors[doctor_index].full_name())
                new_doctor = doctors[doctor_index].full_name()

                doctors[doctor_index].add_patient(patients[patient_index].full_name())

                print("Successfully Relocated!")
                print(f"The patient is now assigned to {new_doctor}.")

                # Remove patient from old doctor's patient list
                for doctor in doctors:
                    if doctor.full_name() == old_doctor:
                       doctor.remove_patient(patients[patient_index].full_name())
                       break

                # Update the patient records in the file
                if Patient.save_records(patients):
                    print("Patient records successfully updated in patients.txt.")
                else:
                    print("Failed to update patient records.")

            else:
                print('The entered ID was not found.')

        except ValueError:
            print('Incorrect ID')

    def print_patients_of_same_family(self, patients):
        family_name = input("Enter the family name: ")
        family_patients = []

        for patient in patients:
            if patient._Patient__surname.lower() == family_name.lower():
                family_patients.append(patient)

        if len(family_patients) > 0:
            print("Patients of the same family:")

            self.view(family_patients)
        else:
            print("No patients found from the specified family.")

    def add_new_patient(self, patients):
        first_name = input('Enter patient\'s first name: ')
        surname = input('Enter patient\'s surname: ')
        age = int(input('Enter patient\'s age: '))
        mobile = int(input('Enter patient\'s phone number: '))
        postcode = input('Enter patient\'s postcode: ')
        symptoms = input('Enter patient\'s symptoms: ').split(',')

        new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms)

        patients.append(new_patient)

        new_patient.save_to_file()

        print('New patient added successfully')

    def book_appointment(self, doctors):
        print('----------Doctor Select----------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            doctor_index = int(input('Please enter the doctor ID to book an appointment: '))
            doctor_index = doctor_index - 1

            if self.find_index(doctor_index, doctors) != False:
                doctor = doctors[doctor_index]
                print('Doctor selected:', doctor.full_name())
                date = input('Enter the appointment date: ')
                time = input('Enter the appointment time: ')

                # You can add code here to handle the appointment booking logic,
                # such as updating the doctor's schedule, creating a new appointment object, etc.

                print(f'Appointment booked successfully on {date}, {time}.')
                
            else:
                print('An error occurred.')
                return

        except ValueError:
            print('Invalid ID')
            return
        
    def get_management_report(self,doctors,patients):
        print("------Reports-------")
        print('Choose the operation:')
        print('1 - Total number of doctors in the system')
        print('2 - Total number of patients per doctor')
        print('3 - Total number of appointments per month per doctor')
        print('4 - Total number of patients based on the illness type.')
        s = input('Choose an option: ')


        if s == '1':
            # Total number of doctors in the system
            print(f'Total number of doctors in the system is {len(doctors)}')

        elif s == '2':
            # Total number of patients per doctor
            for doctor in doctors:
                    totalPatients = doctor.get_total_patients()
                    
                    
                    print(f"{doctor.full_name()} has {totalPatients} patients.")
                   

        elif s == '3':
                for i in doctors:
                    total_appointment = i.get_total_appointment()
                    print(f"{i.full_name()} has {total_appointment} this month.")


        elif s == '4':

            for i in patients:
                symptoms = i.get_symptoms()
                t=0
                for p in patients:
                    if p.get_symptoms() == symptoms:
                        t+=1
                print(f'{t} for {symptoms}')

        else:
            print('Invalid option. Try again.')
