class PatientNode:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.next = None
        self.prev = None

    def __lt__(self, other):
        if self.age == other.age:
            return self.patient_id < other.patient_id
        return self.age > other.age
    
    def __repr__(self):
        return f"Patient(name='{self.name}', age={self.age}, patient_id={self.patient_id})"
