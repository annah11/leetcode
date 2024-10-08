class Solution:
    def convertTemperature(self, celsius: float) -> list:
        kelvin = celsius + 273.15
        
        fahrenheit = celsius * 1.80 + 32.00
        
        return [round(kelvin, 5), round(fahrenheit, 5)]
