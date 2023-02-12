class PatientNode:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.next = None
        self.prev = None