# ------------------------------
# Name: temperatureconverter.py
# Author: Hayden Lansinger
# Date: 11/2/2026
# Description: This program will convert temperatures between Fahrenheit and Celsius using BreezyPythonGUI.
# ------------------------------

import breezypythongui
frame = breezypythongui.EasyFrame

class TemperatureConverter(frame):
    def __init__(self):
        super().__init__()

        # fahrenheit
        self.addLabel("Fahrenheit", 0, 0)
        self.fah = self.addFloatField(32.0, 1, 0)
        self.addButton(">>>>", 2, 0, command=self.convert)
        # celsius
        self.addLabel("Celsius", 0 ,1)
        self.cel = self.addFloatField(0.0, 1, 1)
        self.addButton("<<<<", 2, 1, command=self.inverse)

    def convert(self):
        # gets fahrenheit value
        deg = float(self.fah.getValue())
        # converts
        cel = (deg - 32) / 1.8
        # changes value on screen
        self.cel.setValue(cel)
        return

    def inverse(self):
        # gets celsius value
        cel = float(self.cel.getValue())
        # converts
        deg = cel * 1.8 + 32
        # changes value on screen
        self.fah.setValue(deg)
        return

# opens the window and runs feedback loop     
def main():
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()