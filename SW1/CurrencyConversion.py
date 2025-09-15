def convert_currency(dollars):
    peso_rate = 57.17
    yen_rate = 146.67
    pesos = dollars * peso_rate
    yen = dollars * yen_rate
    return pesos, yen

print("Currency Converter (Dollar to Peso and Yen)")
dollars = float(input("Enter currency in $: "))

pesos, yen = convert_currency(dollars)

print("\nDollar($)\tPhil Peso(P)\tJpn Yen(¥)")
print(f"{dollars}\t\t{pesos:.2f}\t\t{yen:.2f}")
