from patientNode import PatientNode
from consultQueue import MaxHeap

class PatientRecord:
    def __init__(self):
        self.head = None
        self.consultQueue = MaxHeap()
        self.count = 0

    # Precondition: An input file “input.txt” is ready and contains the initial set of patient names and ages. 
    # Effect: This function registers the name and age of the patient entering the hospital and assigns 
    # them an ID that is returned to the calling function. When the program is executed for the first time, 
    # the patient details are loaded from an input file. This is analogous to the list of patients present at 
    # the hospital before the registration counter opens. Thereafter, new patients will be input with the 
    # help of menu options and console-based input. 
    def registerPatient(self, name, age):
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
        self.consultQueue.enqueuePatient(new_patient)
        return new_patient.patient_id

    # Precondition: Both the patient DLL and Heap are not empty 
    # Effect: This function removes the patient ID from the queue that has consulted the doctor and 
    # updates the queue. The function is called from the nextPatient function itself after the next patients 
    # name is displayed.  
    def dequeuePatient(self, patient_id):
        curr = self.head
        while curr is not None:
            if curr.patient_id == patient_id:
                self.count = self.count - 1
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    # Precondition: Both the patient DLL and Heap are not empty 
    # Effect: This function prints the patient_ID and name of the patient that is next in line to meet the 
    # doctor. This function is called either through a menu option of every time a new patient registers and 
    # the patient is added to the queue. 
    def nextPatient(self):
        if self.count > 1:
            patient = self.consultQueue.extract_max()
            self.dequeuePatient(patient.patient_id)
        elif self.count == 1:
            patient = self.head
            self.dequeuePatient(patient.patient_id)
        elif self.count == 0:
            return None
        return patient

    # Precondition: Both the patient DLL and Heap are not empty 
    # Effect: This function displays all the remaining patients in the queue in the following format: 
    # <sequence number> , <patient id>, <patient name>, <age> 
    # where sequence number is the order in which the patient will meet the doctor. This output should 
    # be written in an output.txt file. 
    def displayQueue(self):
        curr = self.head
        if curr is None:
            print("No patient in the consultation queue")
            return
        with open('output.txt', 'w') as f:
            while curr is not None:
                print(curr)
                f.write(str(curr.name) + "," + str(curr.age) + "," + str(curr.patient_id) + "\n")
                curr = curr.next
            print("Consultation queue output written to output.txt successfully.")