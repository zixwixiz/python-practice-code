# Add your code here
def celsius_to_fahrenheit(celsius: float)-> float:
  fahrenheit: float = (celsius * 9/5) + 32
  return fahrenheit

result = celsius_to_fahrenheit(25)
print(result)

def fahrenheit_to_celsius(fahrenheit):
  celsius: float = (fahrenheit - 32) * 5/9
  return celsius

result = fahrenheit_to_celsius(77)
print(result)

def convert_temperature(temperature, unit):
  if unit == 'C':
   return celsius_to_fahrenheit(temperature)
  elif unit == 'F' :
   return fahrenheit_to_celsius(temperature)  
  
