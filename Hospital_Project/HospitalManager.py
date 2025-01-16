from FrontEndHospital import FrontEnd
from BackEndHospital import BackEnd
from Test_ import Test

class HospitalManager:
    def __init__(self):
        test_data = Test().test() 
        self.front = FrontEnd()
        self.back = BackEnd(test_data)

    def run(self):
        while True:
            self.front.menu_options()
            choice = self.front.get_choice()
            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.print_all_patients()
            elif choice == 3:
                self.get_next_patient()
            elif choice == 4:
                self.remove_patient()
            elif choice == 5:
                print("Ending the program. Goodbye!")
                break

    def add_patient(self):
        spec, name, status = self.front.get_patient_data()
        success = self.back.add_patient(spec, name, status)
        if not success:
            print("Sorry, the specialization is full. Cannot add more patients.")

    def print_all_patients(self):
        patients = self.back.get_all_patients()
        self.front.print_all_patients(patients)

    def get_next_patient(self):
        spec = self.front.get_specialization()
        patient = self.back.get_next_patient(spec)
        self.front.print_next_patient(patient)

    def remove_patient(self):
        spec = self.front.get_specialization()
        name = input("Enter the name of the patient to remove: ")
        success = self.back.remove_patient(spec, name)
        self.front.notify_patient_removed(success, name)


if __name__ == '__main__':
    manager = HospitalManager()
    manager.run()

