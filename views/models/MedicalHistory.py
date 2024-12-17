class MedicalHistory:
    def __init__(self, history_id, patient, appointment):
        self.history_id = history_id
        self.patient = patient  # Instance of Patient class
        self.appointment = appointment  # Instance of Appointment class
        self.records = []  # List of Record objects

    def add_record(self, record):
        self.records.append(record)
        return "Record added successfully"

    def get_records(self):
        return self.records
