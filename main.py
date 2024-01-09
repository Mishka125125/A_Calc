from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_text = self.result.text

        if instance.text == '=':
            try:
                result = str(eval(current_text))
                self.result.text = result
            except Exception as e:
                self.result.text = 'Error'

        elif instance.text == 'C':
            self.result.text = ''
            
        else:
            self.result.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()