class BackEnd:
    def __init__(self, test_data=None):
        self.patients = test_data if test_data else [[] for _ in range(20)]  

    def add_patient(self, specialization, name, status):
        queue = self.patients[specialization - 1]
        if len(queue) >= 10:
            return False
        if status == 2:
            queue.insert(0, {'name': name, 'status': 'Super Urgent'})
        elif status == 1:  
            idx = next((i for i, p in enumerate(queue) if p['status'] == 'Normal'), len(queue))
            queue.insert(idx, {'name': name, 'status': 'Urgent'})
        else:
            queue.append({'name': name, 'status': 'Normal'})
        return True

    def get_next_patient(self, specialization):
        queue = self.patients[specialization - 1]
        if queue:
            return queue.pop(0)
        return None

    def remove_patient(self, specialization, name):
        queue = self.patients[specialization - 1]
        for idx, patient in enumerate(queue):
            if patient['name'] == name:
                del queue[idx]
                return True
        return False

    def get_all_patients(self):
        return self.patients
