from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock
from kivy.core.window import Window
import datetime
import jdatetime


class Card(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.08, 0.10, 0.14, 1)

            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[
                    (20, 20),
                    (20, 20),
                    (20, 20),
                    (20, 20)
                ]
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size


class DateTimeApp(App):

    def build(self):

        Window.clearcolor = (0.03, 0.04, 0.06, 1)

        main = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.title_label = Label(
            text="[b]DateTimeApp[/b]",
            markup=True,
            font_size=58,
            size_hint_y=0.11,
            color=(0.25, 0.75, 1, 1)
        )

        self.creator_label = Label(
            text="AMIR DGT",
            font_size=25,
            size_hint_y=0.055,
            color=(0.65, 0.68, 0.75, 1)
        )

        time_card = Card(
            orientation="vertical",
            padding=12,
            spacing=1,
            size_hint_y=0.32
        )

        time_title = Label(
            text="[b]TIME[/b]",
            markup=True,
            font_size=60,
            color=(0.25, 0.75, 1, 1),
            size_hint_y=0.25
        )

        self.time_label = Label(
            text="00:00:00",
            font_size=80,
            color=(1, 1, 1, 1),
            size_hint_y=0.75
        )

        time_card.add_widget(time_title)
        time_card.add_widget(self.time_label)

        gregorian_card = Card(
            orientation="vertical",
            padding=10,
            spacing=0,
            size_hint_y=0.235
        )

        gregorian_title = Label(
            text="[b]GREGORIAN DATE[/b]",
            markup=True,
            font_size=45,
            color=(0.35, 0.85, 0.65, 1),
            size_hint_y=0.28
        )

        self.gregorian_label = Label(
            text="0000/00/00",
            font_size=65,
            color=(1, 1, 1, 1),
            size_hint_y=0.45
        )

        self.gregorian_day_label = Label(
            text="Friday",
            font_size=45,
            color=(0.70, 0.75, 0.82, 1),
            size_hint_y=0.27
        )

        gregorian_card.add_widget(gregorian_title)
        gregorian_card.add_widget(self.gregorian_label)
        gregorian_card.add_widget(self.gregorian_day_label)

        jalali_card = Card(
            orientation="vertical",
            padding=10,
            spacing=0,
            size_hint_y=0.235
        )

        jalali_title = Label(
            text="[b]JALALI DATE[/b]",
            markup=True,
            font_size=45,
            color=(1, 0.65, 0.25, 1),
            size_hint_y=0.28
        )

        self.jalali_label = Label(
            text="0000/00/00",
            font_size=65,
            color=(1, 1, 1, 1),
            size_hint_y=0.45
        )

        self.jalali_day_label = Label(
            text="Friday",
            font_size=45,
            color=(0.70, 0.75, 0.82, 1),
            size_hint_y=0.27
        )

        jalali_card.add_widget(jalali_title)
        jalali_card.add_widget(self.jalali_label)
        jalali_card.add_widget(self.jalali_day_label)

        converter_card = Card(
            orientation="vertical",
            padding=8,
            spacing=5,
            size_hint_y=0.10
        )

        converter_button = Button(
            text="[b]DATE CONVERTER[/b]",
            markup=True,
            font_size=30,
            background_normal="",
            background_color=(0.15, 0.45, 0.65, 1)
        )

        converter_button.bind(
            on_press=self.open_converter
        )

        converter_card.add_widget(converter_button)

        main.add_widget(self.title_label)
        main.add_widget(self.creator_label)
        main.add_widget(time_card)
        main.add_widget(gregorian_card)
        main.add_widget(jalali_card)
        main.add_widget(converter_card)

        Window.bind(
            size=self.update_sizes
        )

        Clock.schedule_interval(
            self.update_time,
            1
        )

        self.update_time(0)

        return main

    def responsive_size(self, size):

        width = Window.width

        if width < 500:
            return size

        if width < 900:
            return size * 0.98

        return size

    def update_sizes(self, *args):

        self.title_label.font_size = self.responsive_size(58)
        self.creator_label.font_size = self.responsive_size(17)
        self.time_label.font_size = self.responsive_size(80)
        self.gregorian_label.font_size = self.responsive_size(65)
        self.jalali_label.font_size = self.responsive_size(65)
        self.gregorian_day_label.font_size = self.responsive_size(45)
        self.jalali_day_label.font_size = self.responsive_size(45)

    def update_time(self, dt):

        now = datetime.datetime.now()

        jalali = jdatetime.datetime.fromgregorian(
            datetime=now
        )

        self.time_label.text = now.strftime("%H:%M:%S")
        self.gregorian_label.text = now.strftime("%Y/%m/%d")
        self.jalali_label.text = jalali.strftime("%Y/%m/%d")

        english_day = now.strftime("%A")

        self.gregorian_day_label.text = english_day
        self.jalali_day_label.text = english_day

    def open_converter(self, instance):

        converter_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        converter_title = Label(
            text="[b]DATE CONVERTER[/b]",
            markup=True,
            font_size=50,
            color=(0.25, 0.75, 1, 1),
            size_hint_y=0.18
        )

        date_input_layout = BoxLayout(
            orientation="horizontal",
            spacing=8,
            size_hint_y=0.20
        )

        self.day_input = TextInput(
            hint_text="DD",
            multiline=False,
            input_filter="int",
            font_size=45,
            halign="center",
            size_hint_x=0.27
        )

        slash1 = Label(
            text="/",
            font_size=45,
            size_hint_x=0.08
        )

        self.month_input = TextInput(
            hint_text="MM",
            multiline=False,
            input_filter="int",
            font_size=45,
            halign="center",
            size_hint_x=0.27
        )

        slash2 = Label(
            text="/",
            font_size=45,
            size_hint_x=0.08
        )

        self.year_input = TextInput(
            hint_text="YYYY",
            multiline=False,
            input_filter="int",
            font_size=45,
            halign="center",
            size_hint_x=0.43
        )

        date_input_layout.add_widget(self.day_input)
        date_input_layout.add_widget(slash1)
        date_input_layout.add_widget(self.month_input)
        date_input_layout.add_widget(slash2)
        date_input_layout.add_widget(self.year_input)

        self.day_input.bind(text=self.day_changed)
        self.month_input.bind(text=self.month_changed)
        self.year_input.bind(text=self.year_changed)

        gregorian_button = Button(
            text="[b]GREGORIAN -> JALALI[/b]",
            markup=True,
            font_size=55,
            background_normal="",
            background_color=(0.20, 0.55, 0.35, 1),
            size_hint_y=0.18
        )

        gregorian_button.bind(
            on_press=self.convert_gregorian
        )

        jalali_button = Button(
            text="[b]JALALI -> GREGORIAN[/b]",
            markup=True,
            font_size=55,
            background_normal="",
            background_color=(0.65, 0.40, 0.15, 1),
            size_hint_y=0.18
        )

        jalali_button.bind(
            on_press=self.convert_jalali
        )

        self.converter_result = Label(
            text="Result",
            font_size=45,
            color=(1, 1, 1, 1),
            size_hint_y=0.18
        )

        converter_layout.add_widget(converter_title)
        converter_layout.add_widget(date_input_layout)
        converter_layout.add_widget(gregorian_button)
        converter_layout.add_widget(jalali_button)
        converter_layout.add_widget(self.converter_result)

        self.converter_popup = Popup(
            title="",
            content=converter_layout,
            size_hint=(0.92, 0.75),
            auto_dismiss=True
        )

        self.converter_popup.open()

        Clock.schedule_once(
            lambda dt: self.focus_day(),
            0.2
        )

    def focus_day(self):
        self.day_input.focus = True

    def day_changed(self, instance, value):

        if len(value) >= 2:

            self.day_input.text = value[:2]

            Clock.schedule_once(
                lambda dt: self.focus_month(),
                0.05
            )

    def focus_month(self):
        self.month_input.focus = True

    def month_changed(self, instance, value):

        if len(value) >= 2:

            self.month_input.text = value[:2]

            Clock.schedule_once(
                lambda dt: self.focus_year(),
                0.05
            )

    def focus_year(self):
        self.year_input.focus = True

    def year_changed(self, instance, value):

        if len(value) >= 4:

            self.year_input.text = value[:4]
            self.year_input.focus = False

    def get_entered_date(self):

        day = self.day_input.text.strip()
        month = self.month_input.text.strip()
        year = self.year_input.text.strip()

        if (
            len(day) != 2
            or len(month) != 2
            or len(year) != 4
        ):
            raise ValueError

        return int(year), int(month), int(day)

    def convert_gregorian(self, instance):

        try:

            year, month, day = self.get_entered_date()

            gregorian_date = datetime.date(
                year,
                month,
                day
            )

            jalali_date = jdatetime.date.fromgregorian(
                date=gregorian_date
            )

            english_day = gregorian_date.strftime("%A")

            self.converter_result.text = (
                f"{jalali_date.strftime('%Y/%m/%d')}\n"
                f"{english_day}"
            )

        except (ValueError, TypeError):

            self.converter_result.text = "Invalid date"

    def convert_jalali(self, instance):

        try:

            year, month, day = self.get_entered_date()

            jalali_date = jdatetime.date(
                year,
                month,
                day
            )

            gregorian_date = (
                jalali_date.togregorian()
            )

            english_day = gregorian_date.strftime("%A")

            self.converter_result.text = (
                f"{gregorian_date.strftime('%Y/%m/%d')}\n"
                f"{english_day}"
            )

        except (ValueError, TypeError):

            self.converter_result.text = "Invalid date"


DateTimeApp().run()
