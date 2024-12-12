class Calendar:
    def __init__(self):
        self.appointments = []  # List of Appointment objects

    def display_calendar_list(self):
        return [f"{appt.date_time} - {appt.status} for {appt.patient.name}" for appt in self.appointments]

    def display_calendar(self):
        # Implementation for graphical calendar view
        return "Displaying calendar view"
