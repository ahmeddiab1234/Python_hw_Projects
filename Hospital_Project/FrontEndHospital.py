

class FrontEnd:
    def menu_options(self):
        print('Program Options:')
        message = [
            '1) Add new patient',
            '2) Print all patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End the program'
        ]
        print('\n'.join(message))

    def get_choice(self):
        while True:
            try:
                choice = int(input('Enter your choice (from 1 to 5): '))
                if 1 <= choice <= 5:
                    return choice
                print("Invalid range. Please enter a number between 1 and 5.")
            except ValueError:
                print('Invalid input, Please Enter an integer.')

    def get_specialization(self):
        while True:
            try:
                specialization = int(input('Enter specialization (1-20): '))
                if 1 <= specialization <= 20:
                    return specialization
                print("Invalid specialization. Please enter a number between 1 and 20.")
            except ValueError:
                print('Invalid input. Please enter a valid integer.')

    def get_patient_data(self):
        specialization = self.get_specialization()
        name = input('Enter patient name: ')
        while True:
            try:
                status = int(input('Enter status (0: Normal, 1: Urgent, 2: Super Urgent): '))
                if 0 <= status <= 2:
                    return specialization, name, status
                print('Invalid status. Please enter 0, 1, or 2.')
            except ValueError:
                print('Invalid input. Please enter an integer.')

    def print_all_patients(self, patients):
        for spec_id, queue in enumerate(patients, 1):
            if queue:
                print(f"Specialization {spec_id}:")
                for idx, patient in enumerate(queue):
                    print(f"  {idx+1}. {patient['name']} (Status: {patient['status']})")
        print()

    def print_next_patient(self, patient):
        if patient:
            print(f"{patient['name']}, please proceed to the doctor.")
        else:
            print("No patients are available.")

    def notify_patient_removed(self, success, name):
        if success:
            print(f"Patient {name} has been successfully removed.")
        else:
            print(f"Patient {name} not found.")
