# ------------------------------
# Name: temperatureconverter.py
# Author: Hayden Lansinger
# Date: 11/2/2026
# Description: This program will convert temperatures between Fahrenheit and Celsius using BreezyPythonGUI.
# ------------------------------

import breezypythongui

class ApplicationName(breezypythongui.EasyFrame):
    def __init__(self):
        super().__init__()
        
def main():
    ApplicationName().mainloop()

if __name__ == "__main__":
    main()