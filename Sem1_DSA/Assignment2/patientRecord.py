from patientNode import PatientNode

class PatientRecord:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_patient(self, name, age):
        self.count += 1
        new_patient = PatientNode(name, age, self.count)
        if self.head is None:
            self.head = new_patient
            return new_patient.patient_id

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_patient
        new_patient.prev = curr
        return new_patient.patient_id

    def delete_patient(self, patient_id):
        curr = self.head
        while curr is not None:
            if curr.patient_id == patient_id:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.name, "\t", curr.age, "\t", curr.patient_id)
            curr = curr.next