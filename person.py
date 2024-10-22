class Person:
    """Person Class"""

    def init(self, first_name, surname):
        self.first_name = first_name
        self.surname=surname

    def full_name(self):

        return f"{self.first_name}  {self.surname}"

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name= new_first_name

    def get_surname(self):
        return self.surname

    def get_surname(self):
        return self.surname

    def set_first_name(self, new_surname):
        self.surname= new_surname 