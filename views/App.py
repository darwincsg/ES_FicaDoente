from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window 

from models.Users import Users

Window.size = (450, 800)

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.user = Users(user_id=1,name="Gatito", email="admin@example.com", password="1234", role="Receptionist")

        self.email_input = TextInput(hint_text="Email", multiline=False)
        self.add_widget(self.email_input)
        
        self.password_input = TextInput(hint_text="Password", password=True, multiline=False)
        self.add_widget(self.password_input)
        
        login_button = Button(text="Login")
        login_button.bind(on_press=self.check_login)
        self.add_widget(login_button)

    def check_login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        result = self.user.login(email, password)

        popup = Popup(title="Login Result", content=Label(text=str(result)), size_hint=(0.5, 0.5))
        popup.open()

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
