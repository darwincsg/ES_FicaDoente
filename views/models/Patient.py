class Patient:
    def __init__(self, patient_id, name, date_of_birth, address, phone_number, email, healthcare_id):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.healthcare_id = healthcare_id

    def update_info(self, name=None, address=None, phone_number=None, email=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        return "Patient info updated successfully"

    def get_details(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
            "healthcare_id": self.healthcare_id,
        }

