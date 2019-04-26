def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temperatures = [10, -20, 100]

for temperature in temperatures:
    print(temperature, "degress to Fareheit:", cel_to_fahr(temperature), "degrees.")