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
from kivymd.uix.widget import MDWidget
from kivy.metrics import dp
from kivymd.uix.anchorlayout import MDAnchorLayout

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
        # Main scrollable container with white background
        main_layout = MDBoxLayout(
            orientation='vertical',
            md_bg_color=(1, 1, 1, 1),  # Pure white background
            padding=[dp(32), dp(24), dp(32), dp(24)]  # More horizontal padding
        )
        
        # Center everything using anchor layout
        center_container = MDAnchorLayout(
            anchor_x='center',
            anchor_y='center'
        )
        
        # Content container with fixed width to center properly
        content_layout = MDBoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            width=dp(400),  # Fixed width for better centering
            height=dp(650),  # Fixed height
            spacing=dp(20)
        )
        
        # Red circular icon with white cross - exact match to image
        icon_container = MDAnchorLayout(
            anchor_x='center',
            size_hint_y=None,
            height=dp(70)
        )
        
        # Red circle background
        red_circle = MDCard(
            md_bg_color=(0.85, 0.18, 0.18, 1),  # Exact red color from image
            size_hint=(None, None),
            size=(dp(56), dp(56)),
            radius=[dp(28)],  # Perfect circle
            elevation=0
        )
        
        # White cross/plus symbol
        cross_symbol = MDLabel(
            text="+",  # Simple plus symbol
            font_size=dp(32),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # Pure white
            halign="center",
            valign="center",
            bold=True
        )
        
        red_circle.add_widget(cross_symbol)
        icon_container.add_widget(red_circle)
        content_layout.add_widget(icon_container)
        
        # Title - exact text from image
        title_label = MDLabel(
            text="Ambulance Booking System",
            font_style="H6",
            theme_text_color="Custom",
            text_color=(0.2, 0.2, 0.2, 1),  # Dark gray
            halign="center",
            size_hint_y=None,
            height=dp(40),
            bold=True
        )
        content_layout.add_widget(title_label)
        
        # Subtitle - exact text from image  
        subtitle_label = MDLabel(
            text="Book an ambulance by filling the details below.",
            font_style="Body2",
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),  # Gray text
            halign="center",
            size_hint_y=None,
            height=dp(30)
        )
        content_layout.add_widget(subtitle_label)
        
        # Extra spacing between subtitle and first form label to avoid visual overlap
        content_layout.add_widget(MDWidget(size_hint_y=None, height=dp(14)))
        
        # Form fields container with labels
        form_container = MDBoxLayout(
            orientation='vertical',
            spacing=dp(20),
            size_hint_y=None,
            height=dp(360)
        )
        
        # Pickup Address field with label
        pickup_container = MDBoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None, height=dp(80))
        pickup_label = MDLabel(
            text="Pickup Address",
            font_style="Subtitle2",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(20)
        )
        pickup_container.add_widget(pickup_label)
        self.pickup_field = MDTextField(
            hint_text="e.g., 123 Main St, Anytown",
            mode="rectangle",
            size_hint_y=None,
            height=dp(52),
            line_color_focus=(0.85, 0.18, 0.18, 1)
        )
        pickup_container.add_widget(self.pickup_field)
        form_container.add_widget(pickup_container)
        
        # Destination Address field with label
        destination_container = MDBoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None, height=dp(80))
        destination_label = MDLabel(
            text="Destination Address (Optional)",
            font_style="Subtitle2",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(20)
        )
        destination_container.add_widget(destination_label)
        self.destination_field = MDTextField(
            hint_text="e.g., City Hospital",
            mode="rectangle",
            size_hint_y=None,
            height=dp(52),
            line_color_focus=(0.85, 0.18, 0.18, 1)
        )
        destination_container.add_widget(self.destination_field)
        form_container.add_widget(destination_container)
        
        # Special Care Needs field with label
        special_care_container = MDBoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None, height=dp(80))
        special_care_label = MDLabel(
            text="Special Care Needs (Optional)",
            font_style="Subtitle2",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(20)
        )
        special_care_container.add_widget(special_care_label)
        self.special_care_field = MDTextField(
            hint_text="e.g., Requires oxygen, diabetic, etc.",
            mode="rectangle",
            size_hint_y=None,
            height=dp(52),
            line_color_focus=(0.85, 0.18, 0.18, 1)
        )
        special_care_container.add_widget(self.special_care_field)
        form_container.add_widget(special_care_container)
        
        # Additional Notes field with label
        notes_container = MDBoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None, height=dp(100))
        notes_label = MDLabel(
            text="Additional Notes (e.g., condition, number of patients)",
            font_style="Subtitle2",
            theme_text_color="Custom",
            text_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(20)
        )
        notes_container.add_widget(notes_label)
        self.notes_field = MDTextField(
            hint_text="e.g., Patient is conscious, has a leg injury",
            mode="rectangle",
            multiline=True,
            size_hint_y=None,
            height=dp(72),
            line_color_focus=(0.85, 0.18, 0.18, 1)
        )
        notes_container.add_widget(self.notes_field)
        form_container.add_widget(notes_container)
        
        content_layout.add_widget(form_container)
        
        # Request Ambulance button - full width red button with rounded corners
        request_button = MDRaisedButton(
            text="Request Ambulance",
            md_bg_color=(0.85, 0.18, 0.18, 1),  # Same red as icon
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            size_hint=(1, None),  # Full width
            height=dp(52),
            font_size=dp(16),
            elevation=2,
            rounded_button=True,  # Rounded corners in KivyMD 1.x
            on_release=self.request_ambulance
        )
        content_layout.add_widget(request_button)
        
        center_container.add_widget(content_layout)
        main_layout.add_widget(center_container)
        
        return main_layout
    
    def create_confirmation_screen(self):
        # Outer container (white background)
        outer = MDBoxLayout(
            orientation='vertical',
            md_bg_color=(1, 1, 1, 1),
            padding=[dp(32), dp(24), dp(32), dp(24)]
        )
        
        # Centered content container with same fixed width as first screen
        center = MDAnchorLayout(anchor_x='center', anchor_y='center')
        content = MDBoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            width=dp(400),
            height=dp(700),
            spacing=dp(16)
        )
        
        # Header: centered green circle with check, title and subtitle
        header = MDBoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None, height=dp(140))
        icon_row = MDAnchorLayout(anchor_x='center', size_hint_y=None, height=dp(48))
        green_circle = MDCard(md_bg_color=(0.2, 0.75, 0.35, 1), size_hint=(None, None), size=(dp(42), dp(42)), radius=[dp(21)], elevation=0)
        check = MDLabel(text="✓", font_size=dp(26), theme_text_color="Custom", text_color=(1,1,1,1), halign="center", valign="center")
        green_circle.add_widget(check)
        icon_row.add_widget(green_circle)
        header.add_widget(icon_row)
        title = MDLabel(text="Ambulance Confirmed!", font_style="H6", halign="center")
        subtitle = MDLabel(text="Your ambulance is on its way. An operator will be in touch.", font_style="Body2", halign="center", theme_text_color="Secondary")
        header.add_widget(title)
        header.add_widget(subtitle)
        content.add_widget(header)
        
        # Card 1: Locations (Pickup and Destination in one card)
        locations_card = MDCard(md_bg_color=(1,1,1,1), elevation=1, radius=[dp(12)], padding=dp(14))
        loc_container = MDBoxLayout(orientation='vertical', spacing=dp(10))
        pickup_row = MDBoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(40))
        pickup_row.add_widget(Label(text="📍", font_size="18sp", size_hint_x=None, width=dp(24)))
        pickup_col = MDBoxLayout(orientation='vertical', spacing=dp(2))
        pickup_col.add_widget(MDLabel(text="Pickup Location", font_style="Caption"))
        pickup_col.add_widget(MDLabel(text=self.get_pickup_text(), font_style="Body2"))
        pickup_row.add_widget(pickup_col)
        loc_container.add_widget(pickup_row)
        dest_row = MDBoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(40))
        dest_row.add_widget(Label(text="🏥", font_size="18sp", size_hint_x=None, width=dp(24)))
        dest_col = MDBoxLayout(orientation='vertical', spacing=dp(2))
        dest_col.add_widget(MDLabel(text="Destination", font_style="Caption"))
        dest_col.add_widget(MDLabel(text=self.get_destination_text(), font_style="Body2"))
        dest_row.add_widget(dest_col)
        loc_container.add_widget(dest_row)
        locations_card.add_widget(loc_container)
        content.add_widget(locations_card)
        
        # Card 2: Ambulance Details
        ambulance_card = MDCard(md_bg_color=(1,1,1,1), elevation=1, radius=[dp(12)], padding=dp(14))
        amb_row = MDBoxLayout(orientation='horizontal', spacing=dp(12))
        siren_circle = MDCard(md_bg_color=(0.97, 0.35, 0.35, 1), size_hint=(None, None), size=(dp(36), dp(36)), radius=[dp(18)], elevation=0)
        siren_circle.add_widget(MDLabel(text="🚨", halign="center"))
        amb_row.add_widget(siren_circle)
        amb_col = MDBoxLayout(orientation='vertical', spacing=dp(2))
        amb_col.add_widget(MDLabel(text="Ambulance Details", font_style="Caption"))
        amb_col.add_widget(MDLabel(text="Ambulance #402", font_style="Subtitle2"))
        amb_col.add_widget(MDLabel(text="Driver: John Doe", font_style="Caption"))
        amb_col.add_widget(MDLabel(text="ETA: 7 minutes", font_style="Caption"))
        amb_row.add_widget(amb_col)
        ambulance_card.add_widget(amb_row)
        content.add_widget(ambulance_card)
        
        # Card 3: Patient Details
        patient_card = MDCard(md_bg_color=(1,1,1,1), elevation=1, radius=[dp(12)], padding=dp(14))
        patient_col = MDBoxLayout(orientation='vertical', spacing=dp(10))
        care_col = MDBoxLayout(orientation='vertical', spacing=dp(2))
        care_col.add_widget(MDLabel(text="Special Care Needs", font_style="Caption"))
        care_col.add_widget(MDLabel(text=self.get_special_care_text(), font_style="Body2"))
        patient_col.add_widget(care_col)
        notes_col = MDBoxLayout(orientation='vertical', spacing=dp(2))
        notes_col.add_widget(MDLabel(text="Additional Notes", font_style="Caption"))
        notes_col.add_widget(MDLabel(text=self.get_notes_text(), font_style="Body2"))
        patient_col.add_widget(notes_col)
        patient_card.add_widget(patient_col)
        content.add_widget(patient_card)
        
        # Tips card (blue accent)
        tips_card = MDCard(md_bg_color=(0.95,0.98,1,1), elevation=0, radius=[dp(10)], padding=dp(12))
        tips_col = MDBoxLayout(orientation='vertical', spacing=dp(4))
        tips_col.add_widget(MDLabel(text="Specialized Dispatcher Tips ✨", font_style="Subtitle2", theme_text_color="Custom", text_color=(0.0,0.28,0.62,1)))
        tips_col.add_widget(MDLabel(text="Prepare to confirm the exact location and a reliable callback number for the responding crew.", font_style="Caption", theme_text_color="Secondary"))
        tips_card.add_widget(tips_col)
        content.add_widget(tips_card)
        
        # Make a New Request button (light style, rounded)
        new_request_btn = MDRaisedButton(
            text="Make a New Request",
            md_bg_color=(0.96,0.96,0.96,1),
            theme_text_color="Custom",
            text_color=(0.1,0.1,0.1,1),
            size_hint=(1, None),
            height=dp(48),
            rounded_button=True,
            on_release=self.make_new_request
        )
        content.add_widget(new_request_btn)
        
        center.add_widget(content)
        outer.add_widget(center)
        
        return outer
    
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