temp = float(input("Temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

if origem == "C" and destino == "F":
    result = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    result = temp + 273.15
elif origem == "F" and destino == "C":
    result = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    result = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    result = temp - 273.15
elif origem == "K" and destino == "F":
    result = (temp - 273.15) * 9/5 + 32
else:
    result = temp

print(f"Temperatura convertida: {result:.2f} {destino}")
