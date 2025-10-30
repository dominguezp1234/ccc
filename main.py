 #----------------------------------------------------------------------
# IMPORTACIONES NECESARIAS
# ----------------------------------------------------------------------
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window
from math import sqrt
import random



# Se establece un tamaño de ventana inicial para la aplicación de escritorio
Window.size = (360, 640)

# ----------------------------------------------------------------------
# ARCHIVO DE DISEÑO KV INCRUSTADO COMO CADENA DE TEXTO
# ----------------------------------------------------------------------
kv_string = """
# Define el gestor de pantallas principal que contendrá todas las demás
AppManager:
    MenuScreen:
        name: 'menu'
    CalculatorScreen:
        name: 'calculator'
    GameScreen:
        name: 'game'

# ----------------------------------------------------------------------
# DISEÑO DE LA PANTALLA DEL MENÚ PRINCIPAL
# ----------------------------------------------------------------------
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: 'Aplicación Multifunción'
            font_size: '32sp'
            size_hint_y: 0.4
            color: (0.1, 0.1, 0.1, 1)

        Button:
            text: 'Calculadora'
            font_size: '24sp'
            on_press: app.root.current = 'calculator'
            background_color: (0.2, 0.6, 0.8, 1)
            color: (1, 1, 1, 1)

        Button:
            text: 'Juego de División'
            font_size: '24sp'
            on_press: app.root.current = 'game'
            background_color: (0.3, 0.7, 0.4, 1)
            color: (1, 1, 1, 1)

# ----------------------------------------------------------------------
# DISEÑO DE LA PANTALLA DE LA CALCULADORA
# ----------------------------------------------------------------------
<CalculatorScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 5

        Label:
            id: history_label
            text: root.history_text
            size_hint_y: 0.15
            halign: 'right'
            valign: 'middle'
            font_size: '16sp'
            color: (0.5, 0.5, 0.5, 1)
            text_size: self.width - 20, None

        TextInput:
            id: display
            text: root.display_text
            font_size: '48sp'
            readonly: True
            halign: 'right'
            size_hint_y: 0.25
            background_color: (0.9, 0.9, 0.9, 1)
            padding: [10, 20, 10, 20]

        GridLayout:
            cols: 4
            spacing: 5

            # Fila 1
            Button:
                text: 'C'
                on_press: root.on_special_button_press(self.text)
                background_color: (0.9, 0.5, 0.5, 1)
            Button:
                text: 'DEL'
                on_press: root.on_special_button_press(self.text)
                background_color: (0.9, 0.7, 0.5, 1)
            Button:
                text: '%'
                on_press: root.on_button_press(self.text)
            Button:
                text: '/'
                on_press: root.on_button_press(self.text)

            # Fila 2
            Button:
                text: '7'
                on_press: root.on_button_press(self.text)
            Button:
                text: '8'
                on_press: root.on_button_press(self.text)
            Button:
                text: '9'
                on_press: root.on_button_press(self.text)
            Button:
                text: '*'
                on_press: root.on_button_press(self.text)

            # Fila 3
            Button:
                text: '4'
                on_press: root.on_button_press(self.text)
            Button:
                text: '5'
                on_press: root.on_button_press(self.text)
            Button:
                text: '6'
                on_press: root.on_button_press(self.text)
            Button:
                text: '-'
                on_press: root.on_button_press(self.text)

            # Fila 4
            Button:
                text: '1'
                on_press: root.on_button_press(self.text)
            Button:
                text: '2'
                on_press: root.on_button_press(self.text)
            Button:
                text: '3'
                on_press: root.on_button_press(self.text)
            Button:
                text: '+'
                on_press: root.on_button_press(self.text)
            
            # Fila 5
            Button:
                text: 'SQRT'
                on_press: root.on_special_button_press(self.text)
            Button:
                text: '0'
                on_press: root.on_button_press(self.text)
            Button:
                text: '.'
                on_press: root.on_button_press(self.text)
            Button:
                text: '='
                on_press: root.on_special_button_press(self.text)
                background_color: (0.2, 0.8, 0.6, 1)
        
        Button:
            text: 'Volver al Menú'
            size_hint_y: 0.12
            on_press: app.root.current = 'menu'
            background_color: (0.5, 0.5, 0.5, 1)


# ----------------------------------------------------------------------
# DISEÑO DE LA PANTALLA DEL JUEGO
# ----------------------------------------------------------------------
<GameScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10

        Label:
            text: root.question_text
            font_size: '24sp'
            halign: 'center'
            valign: 'middle'
            size_hint_y: 0.5
            text_size: self.width - 20, None

        TextInput:
            id: answer_input
            hint_text: 'Escribe tu respuesta aquí'
            multiline: False
            font_size: '24sp'
            size_hint_y: 0.15
            on_text: root.answer_text = self.text

        GridLayout:
            cols: 2
            size_hint_y: 0.15
            spacing: 10
            
            Button:
                text: 'Comprobar'
                on_press: root.check_answer()
                background_color: (0.2, 0.6, 0.8, 1)

            Button:
                text: 'Siguiente'
                on_press: root.generate_question()
                background_color: (0.3, 0.7, 0.4, 1)

        Button:
            text: 'Volver al Menú'
            size_hint_y: 0.12
            on_press: app.root.current = 'menu'
            background_color: (0.5, 0.5, 0.5, 1)
"""

# ----------------------------------------------------------------------
# LÓGICA DE PYTHON PARA LAS PANTALLAS
# ----------------------------------------------------------------------

# Gestor de pantallas (no necesita lógica adicional aquí)
class AppManager(ScreenManager):
    pass

# Pantalla del Menú (no necesita lógica adicional aquí)
class MenuScreen(Screen):
    pass

# Pantalla y lógica de la Calculadora
class CalculatorScreen(Screen):
    display_text = StringProperty('0')
    history_text = StringProperty('')

    def on_button_press(self, text):
        """ Se activa al presionar números y operadores básicos. """
        if self.display_text == '0' or self.display_text == 'Error':
            self.display_text = text
        else:
            self.display_text += text
    
    def on_special_button_press(self, text):
        """ Se activa al presionar botones de funciones especiales. """
        if text == 'C':
            self.display_text = '0'
            self.history_text = ''
        elif text == 'DEL':
            if len(self.display_text) > 1 and self.display_text != 'Error':
                self.display_text = self.display_text[:-1]
            else:
                self.display_text = '0'
        elif text == 'SQRT':
            try:
                num = float(self.display_text)
                if num >= 0:
                    self.history_text = f"sqrt({num}) ="
                    self.display_text = str(round(sqrt(num), 9))
                else:
                    self.display_text = 'Error'
            except:
                self.display_text = 'Error'
        elif text == '=':
            try:
                # La función eval() es poderosa pero debe usarse con cuidado.
                # Aquí es segura porque solo procesa números y operadores de la calculadora.
                self.history_text = self.display_text + ' ='
                result = eval(self.display_text)
                self.display_text = str(result)
            except Exception as e:
                self.display_text = 'Error'

# Pantalla y lógica del Juego
class GameScreen(Screen):
    question_text = StringProperty('¡Presiona "Siguiente" para empezar!')
    answer_text = StringProperty('')
    correct_answer = NumericProperty(0)

    def generate_question(self):
        """ Genera una nueva pregunta de división. """
        divisor = random.randint(2, 12)
        # Aseguramos que el resultado sea un número entero
        resultado = random.randint(2, 12)
        dividendo = divisor * resultado
        
        self.question_text = f"¿Cuánto es {dividendo} / {divisor}?"
        self.correct_answer = resultado
        self.answer_text = ''
        # Limpia el campo de texto en la UI
        if self.ids.answer_input:
            self.ids.answer_input.text = ''

    def check_answer(self):
        """ Comprueba si la respuesta del usuario es correcta. """
        try:
            user_answer = int(self.answer_text)
            if user_answer == self.correct_answer:
                self.question_text = f"¡Correcto! {self.correct_answer} es la respuesta.\n\nPresiona 'Siguiente' para otra pregunta."
            else:
                self.question_text = f"Incorrecto. La respuesta era {self.correct_answer}.\n\n¡Intenta con otra! Presiona 'Siguiente'."
        except ValueError:
            self.question_text = "Por favor, introduce un número válido."

# ----------------------------------------------------------------------
# CLASE PRINCIPAL DE LA APLICACIÓN
# ----------------------------------------------------------------------
class CalculadoraApp(App):
    def build(self):
        """ Carga el diseño desde la cadena de texto. """
        return Builder.load_string(kv_string)

# ----------------------------------------------------------------------
# INICIAR LA APLICACIÓN
# ----------------------------------------------------------------------
if __name__ == '__main__':
    CalculadoraApp().run()
