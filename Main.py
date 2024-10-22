# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Commoncold'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','Stomach Pain'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','Fever')]
    discharged_patients = []
    Patient.save_records(patients)

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- View patient')
        print(' 5- Assign doctor to a patient')
        print(' 6- Update admin details')
        print(' 7- Relocate Doctor to Patient')
        print(' 8 - Add a new patient')
        print(' 9- Print Patient of Same Family')
        print(' 10- Book an appointment')
        print(' 11- Management Report ')
        print(' 12- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients,discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- view patients
            #ToDo4
            admin.view_patient(patients)

        elif op == '5':
            # 5- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '6':
            # 6- Update admin detais
            admin.update_details()
        
        elif op == '7':
            # 8 - Relocate doctor to a patient
            admin.doctor_relocate(patients, doctors)

        elif op == '8' :
            #8 - Add a new patient to the file
            admin.add_new_patient(patients)    
        
        elif op == '9':
            # 8 - Relocate doctor to a patient
            admin.print_patients_of_same_family(patients)

        elif op == '10':
            # 10 - Book an appointment with a doctor
            admin.book_appointment(doctors) 

        elif op == '11':
            # 10 - Book an appointment with a doctor
            admin.get_management_report(doctors,patients)    

        elif op == '12':
            # 7 - Quit
            #ToDo7
            print('System terminated')
            quit()
        
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
