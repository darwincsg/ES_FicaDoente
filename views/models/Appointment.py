class Appointment:
    def __init__(self, appointment_id, date_time, status, patient, doctor):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.status = status  # e.g., Scheduled, Cancelled
        self.patient = patient  # Instance of Patient class
        self.doctor = doctor  # Instance of Users class

    def schedule(self):
        self.status = "Scheduled"
        return f"Appointment {self.appointment_id} scheduled successfully for {self.date_time}"

    def cancel(self):
        self.status = "Cancelled"
        return f"Appointment {self.appointment_id} has been cancelled"
