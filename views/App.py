from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime, timedelta
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from models.Users import Users
from models.Patient import Patient

Builder.load_file('./kivy_files/login_screen.kv')
Builder.load_file('./kivy_files/forgot_password_screen.kv')
Builder.load_file('./kivy_files/main_screen.kv')
Builder.load_file('./kivy_files/search_screen.kv')
Builder.load_file('./kivy_files/patient_detail_screen.kv')
Builder.load_file('./kivy_files/schedule_screen.kv')

Window.size = (400, 600) 

patients = [
    Patient(101, "Pam Beesly", "1991-01-30", "123 Main St", "555-1234", "johndoe@example.com", "H12345"),
    Patient(102, "Pam Trump", "1991-01-30", "456 Elm St", "555-5678", "Pam@example.com", "H12346"),
    Patient(103, "Bob Johnson", "1978-03-20", "789 Oak St", "555-9101", "bobjohnson@example.com", "H12347")
]

class LoginScreen(Screen):
    def attempt_login(self, email, password):
        user = Users(user_id=1, name="Ryan", email="ryan@gmail.com", password="secret", role="Recepcionist")
        success, message = user.login(email, password)
        if success:
            # Transition to main app screen
            self.manager.current = "main_screen"
        else:
            # Show error message
            self.ids.login_message.text = "Email and Password don’t match"
    
    def show_forgot_password_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password_screen"

class ForgotPasswordScreen(Screen):
    def reset_password(self, code, new_password, confirm_password):
        # Implement logic here
        pass

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class MainScreen(Screen):
    def show_search_patient(self):
        self.manager.transition.direction = 'left' 
        self.manager.current = "search_screen"

class SearchScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = 'right'  # set direction if you want reverse animation
        self.manager.current = "main_screen"

    def perform_search(self, name, day, month, year):
        # Limpiar los resultados anteriores
        self.ids.results_container.clear_widgets()

        # Filtrar pacientes por nombre y fecha de nacimiento
        print(f'{name}-{day}-{month}-{year}')

        filtered_patients = [
            patient for patient in patients
            if (name.lower() in patient.name.lower() and
                str(day) == patient.date_of_birth.split("-")[2] and  # Día de la fecha de nacimiento
                str(month) == patient.date_of_birth.split("-")[1] and  # Mes de la fecha de nacimiento
                str(year) == patient.date_of_birth.split("-")[0])  # Año de la fecha de nacimiento
        ]

        # Si no se encuentran pacientes
        if not filtered_patients:
            no_results_label = Label(text="No patients found")
            self.ids.results_container.add_widget(no_results_label)

        # Agregar un botón para cada paciente encontrado
        for patient in filtered_patients:
            patient_button = Button(
                text=patient.name,
                size_hint_x=1,   # Take up the full width of the parent container
                size_hint_y=None,  # Disable vertical stretching
                height="60dp",     # Set fixed height for the button
                background_normal='',  # Remove default background
                background_color=(0.6, 0.8, 1, 1),  # Light blue background
                color=(0, 0, 0, 1),  # Black text
                font_size='18sp',  # Clear, large text
                on_press=lambda instance, patient=patient: self.show_patient_details(patient)
            )
            self.ids.results_container.add_widget(patient_button)

    def show_patient_details(self, patient):
        detail_screen = self.manager.get_screen("patient_details_screen")
        detail_screen.load_patient_details(patient)
        self.manager.transition.direction = 'left'
        self.manager.current = "patient_details_screen"

    def next_page(self):
        # Implement pagination if needed.
        pass

class PatientDetailScreen(Screen):
    def load_patient_details(self, patient):
        """
        Load patient details into the UI.
        """
        self.ids.patient_name.text = patient.name
        self.ids.patient_doctor.text = "Dwight Schrute"
        self.ids.patient_gender.text = "Female"
        self.ids.patient_dob.text = patient.date_of_birth
        self.ids.patient_address.text = patient.address
        self.ids.patient_phone.text = patient.phone_number
        self.ids.patient_email.text = patient.email
        self.ids.patient_healthcare.text = patient.healthcare_id
    
    def go_to_schedule(self, patient_name):
    
    #Navigate to the ScheduleScreen and pass patient information.
    
        schedule_screen = self.manager.get_screen("schedule_screen")
        schedule_screen.ids.patient_info.text = f"Patient: {patient_name}"
        self.manager.transition.direction = 'left'
        self.manager.current = "schedule_screen"


    def go_back(self):
        """
        Go back to the previous screen with reverse animation.
        """
        self.manager.transition.direction = 'right'  # Reverse transition
        self.manager.current = "search_screen"  # Return to the search screen

class ScheduleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_time = None
        self.unavailable_slots = ["9:00 AM", "11:00 AM", "12:30 AM", "1:30 PM", "2:30 PM", "3:00 PM"]  # Mock unavailable slots

    def on_enter(self):
        """
        Called when the ScheduleScreen is loaded.
        """
        self.load_time_slots()

    def load_time_slots(self):
        """
        Generate time slots and display them in the grid.
        """
        self.ids.time_slot_grid.clear_widgets()  # Clear previous slots

        start_time = datetime.strptime("09:00", "%H:%M")
        time_slots = [start_time + timedelta(minutes=30 * i) for i in range(18)]  # Generate 30-min intervals

        for slot in time_slots:
            time_str = slot.strftime("%I:%M %p")  # Format: 09:00 AM
            button = Button(
                text=time_str,
                size_hint_y=None,
                height="50dp",
                background_normal='',
                background_color=(1, 0.6, 0.6, 1) if time_str in self.unavailable_slots else (0.8, 0.9, 1, 1),
                color=(0, 0, 0, 1),
                disabled=time_str in self.unavailable_slots
            )
            button.bind(on_release=lambda instance, t=time_str: self.select_time(t))
            self.ids.time_slot_grid.add_widget(button)

    def select_time(self, time):
        """
        Mark a time slot as selected.
        """
        self.selected_time = time
        print(f"Selected time slot: {time}")

    def confirm_appointment(self):
        """
        Confirm the appointment and navigate to the main screen.
        """
        if self.selected_time:
            print(f"Appointment confirmed for {self.selected_time}")
            self.manager.transition.direction = 'right'
            self.manager.current = "main_screen"  # Go back to the main screen
        else:
            print("No time slot selected!")

    def go_back(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "patient_details_screen"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(SearchScreen(name='search_screen'))
        sm.add_widget(PatientDetailScreen(name='patient_details_screen'))
        sm.add_widget(ScheduleScreen(name='schedule_screen'))

        return sm

if __name__ == '__main__':
    MyApp().run()