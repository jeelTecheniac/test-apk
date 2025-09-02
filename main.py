from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label

class AmbulanceBookingApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        
        # Create screen manager
        self.sm = MDScreenManager()
        
        # Add booking screen
        booking_screen = MDScreen(name='booking')
        booking_screen.add_widget(self.create_booking_screen())
        self.sm.add_widget(booking_screen)
        
        # Add confirmation screen
        confirmation_screen = MDScreen(name='confirmation')
        confirmation_screen.add_widget(self.create_confirmation_screen())
        self.sm.add_widget(confirmation_screen)
        
        return self.sm
    
    def create_booking_screen(self):
        main_layout = MDBoxLayout(orientation='vertical')
        
        # Top toolbar
        toolbar = MDTopAppBar(
            title="Ambulance Booking System",
            elevation=2
        )
        main_layout.add_widget(toolbar)
        
        # Main content card
        card = MDCard(
            MDBoxLayout(
                orientation='vertical',
                padding=20,
                spacing=15,
                adaptive_height=True
            ),
            padding=20,
            elevation=2,
            size_hint=(0.9, None),
            height="500dp",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Subtitle
        subtitle = MDLabel(
            text="Book an ambulance by filling the details below.",
            font_style="Body1",
            halign="left",
            size_hint_y=None,
            height="30dp"
        )
        card.children[0].add_widget(subtitle)
        
        # Form fields - store references
        self.pickup_field = MDTextField(
            hint_text="Pickup Address",
            helper_text="e.g., 123 Main St, Anytown",
            helper_text_mode="on_focus"
        )
        card.children[0].add_widget(self.pickup_field)
        
        self.destination_field = MDTextField(
            hint_text="Destination Address (Optional)",
            helper_text="e.g., City Hospital",
            helper_text_mode="on_focus"
        )
        card.children[0].add_widget(self.destination_field)
        
        self.special_care_field = MDTextField(
            hint_text="Special Care Needs (Optional)",
            helper_text="e.g., Requires oxygen, diabetic, etc.",
            helper_text_mode="on_focus"
        )
        card.children[0].add_widget(self.special_care_field)
        
        self.notes_field = MDTextField(
            hint_text="Additional Notes (e.g., condition, number of patients)",
            helper_text="e.g., Patient is conscious, has a leg injury",
            helper_text_mode="on_focus",
            multiline=True
        )
        card.children[0].add_widget(self.notes_field)
        
        # Request button
        request_button = MDRaisedButton(
            text="Request Ambulance",
            size_hint=(1, None),
            height="50dp",
            on_release=self.request_ambulance
        )
        card.children[0].add_widget(request_button)
        
        main_layout.add_widget(card)
        return main_layout
    
    def create_confirmation_screen(self):
        main_layout = MDBoxLayout(orientation='vertical')
        
        # Top toolbar with back button
        toolbar = MDTopAppBar(
            title="Ambulance Confirmed!",
            elevation=2,
            left_action_items=[["arrow-left", lambda x: self.go_back()]]
        )
        main_layout.add_widget(toolbar)
        
        # Main content
        content = MDBoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20
        )
        
        # Success icon and message
        success_layout = MDBoxLayout(
            orientation='vertical',
            spacing=10,
            size_hint_y=None,
            height="100dp"
        )
        
        success_icon = Label(
            text="✓",
            font_size="48sp",
            color=[0, 0.7, 0, 1],  # Green color
            size_hint=(None, None),
            size=("48dp", "48dp"),
            pos_hint={'center_x': 0.5}
        )
        success_layout.add_widget(success_icon)
        
        success_msg = MDLabel(
            text="Your ambulance is on its way. An operator will be in touch.",
            font_style="Body1",
            halign="center",
            size_hint_y=None,
            height="30dp"
        )
        success_layout.add_widget(success_msg)
        content.add_widget(success_layout)
        
        # Details cards
        # Pickup Location Card
        pickup_card = MDCard(
            MDBoxLayout(
                Label(text="📍", font_size="20sp", size_hint_x=None, width="30dp"),
                MDBoxLayout(
                    MDLabel(text="Pickup Location", font_style="Subtitle2"),
                    MDLabel(text=self.get_pickup_text(), font_style="Body2"),
                    orientation='vertical',
                    spacing=5
                ),
                orientation='horizontal',
                padding=15,
                spacing=10
            ),
            size_hint_y=None,
            height="80dp",
            elevation=1
        )
        content.add_widget(pickup_card)
        
        # Destination Card
        destination_card = MDCard(
            MDBoxLayout(
                Label(text="🏥", font_size="20sp", size_hint_x=None, width="30dp"),
                MDBoxLayout(
                    MDLabel(text="Destination", font_style="Subtitle2"),
                    MDLabel(text=self.get_destination_text(), font_style="Body2"),
                    orientation='vertical',
                    spacing=5
                ),
                orientation='horizontal',
                padding=15,
                spacing=10
            ),
            size_hint_y=None,
            height="80dp",
            elevation=1
        )
        content.add_widget(destination_card)
        
        # Ambulance Details Card
        ambulance_card = MDCard(
            MDBoxLayout(
                Label(text="🚑", font_size="20sp", size_hint_x=None, width="30dp"),
                MDBoxLayout(
                    MDLabel(text="Ambulance Details", font_style="Subtitle2"),
                    MDLabel(text="Ambulance #402\nDriver: John Doe\nETA: 15 minutes", font_style="Body2"),
                    orientation='vertical',
                    spacing=5
                ),
                orientation='horizontal',
                padding=15,
                spacing=10
            ),
            size_hint_y=None,
            height="100dp",
            elevation=1
        )
        content.add_widget(ambulance_card)
        
        # Patient Details Card
        patient_card = MDCard(
            MDBoxLayout(
                Label(text="👤", font_size="20sp", size_hint_x=None, width="30dp"),
                MDBoxLayout(
                    MDLabel(text="Patient Details", font_style="Subtitle2"),
                    MDBoxLayout(
                        MDLabel(text="Special Care Needs", font_style="Caption"),
                        MDLabel(text=self.get_special_care_text(), font_style="Body2"),
                        MDLabel(text="Additional Notes", font_style="Caption"),
                        MDLabel(text=self.get_notes_text(), font_style="Body2"),
                        orientation='vertical',
                        spacing=3
                    ),
                    orientation='vertical',
                    spacing=5
                ),
                orientation='horizontal',
                padding=15,
                spacing=10
            ),
            size_hint_y=None,
            height="120dp",
            elevation=1
        )
        content.add_widget(patient_card)
        
        # New Request Button
        new_request_btn = MDFlatButton(
            text="Make a New Request",
            size_hint=(1, None),
            height="40dp",
            on_release=self.make_new_request
        )
        content.add_widget(new_request_btn)
        
        main_layout.add_widget(content)
        return main_layout
    
    def request_ambulance(self, *args):
        # Switch to confirmation screen
        self.sm.current = 'confirmation'
    
    def go_back(self, *args):
        self.sm.current = 'booking'
    
    def make_new_request(self, *args):
        # Clear form fields and go back to booking
        self.pickup_field.text = ""
        self.destination_field.text = ""
        self.special_care_field.text = ""
        self.notes_field.text = ""
        self.sm.current = 'booking'
    
    def get_pickup_text(self):
        return self.pickup_field.text if self.pickup_field.text else "Delhi"
    
    def get_destination_text(self):
        return self.destination_field.text if self.destination_field.text else "AIIMS Hospital"
    
    def get_special_care_text(self):
        return self.special_care_field.text if self.special_care_field.text else "None specified"
    
    def get_notes_text(self):
        return self.notes_field.text if self.notes_field.text else "None specified"

AmbulanceBookingApp().run()