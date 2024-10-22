# from Patient import Patient
from person import Person

class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms = []):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first__name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms
       
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f"{self.__first__name}  {self.__surname}"


    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def get_patient(self):
        return self.__patient

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_patient(first_name, surname, age, mobile, postcode, symptoms = [] ) :
        new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
        new_patient.save_records()
        print('New patient added successfully')

    def save_to_file(self) :
    #saves patient details to the records
        patient_data = f"{self.__first__name}, {self.__surname}, {self.__age}, {self.__mobile}, {self.__postcode}, {','.join(self.__symptoms)}\n"
        with open("patient.txt", 'a') as file :
            file.write(patient_data)    

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        print(self.__symptoms)
    def get_symptoms(self):
        return self.__symptoms
    
    def save_records(lst):
        try:
            with open("patient.txt", 'w') as fd:  # Use forward slash (/) for the file path
                fd.write('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode|    Symptoms \n')
                for index, c in enumerate(lst):
                    fd.write(f"{index+1:3}|{c.full_name():^30}|{c.get_doctor():^30}|{c._Patient__age:^5}|{c._Patient__mobile:^15}|{c._Patient__postcode:^10}|{c._Patient__symptoms:^20} \n")  # Access attributes using the correct name and convert the symptoms list to a comma-separated string
        except:
            return False
        else:
            return True   


    def read_records():
        patients = []
        try:
            with open("HMS/patient.txt", 'r') as fd:
                next(fd)  # Skip the header line
                for line in fd:
                    patient_data = line.strip().split('|')
                    # Extract the individual data fields
                    patient_id = patient_data[0].strip()
                    full_name = patient_data[1].strip()
                    doctor_name = patient_data[2].strip()
                    age = patient_data[3].strip()
                    mobile = patient_data[4].strip()
                    address = patient_data[5].strip()
                    symptoms = patient_data[6].strip()

                    # Create a Patient object and add it to the list
                    patient = Patient(full_name, age, mobile, address, symptoms.split(','))
                    patient.link(doctor_name)
                    patients.append(patient)
        except FileNotFoundError:
            print("Patients file not found.")
        return patients

    def __str__(self):
        symptoms_str = ', '.join(self.__symptoms)  # Convert list to a comma-separated string
        return (f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{symptoms_str:^20}")
