class CalculadoraNotas:
    def __init__(self):
        self.notas = []

    def ingresar_notas(self, cantidad):
        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            self.notas.append(nota)

    def obtener_nota_mas_alta(self):
        return max(self.notas)

    def obtener_nota_mas_baja(self):
        return min(self.notas)

    def obtener_promedio(self):
        return sum(self.notas) / len(self.notas)


calculadora = CalculadoraNotas()

cantidad_notas = int(input("Ingrese la cantidad de notas a ingresar: "))
calculadora.ingresar_notas(cantidad_notas)

promedio = calculadora.obtener_promedio()
nota_mas_alta = calculadora.obtener_nota_mas_alta()
nota_mas_baja = calculadora.obtener_nota_mas_baja()

print("El promedio es:", promedio)
print("La nota más baja es:", nota_mas_baja)
print("La nota más alta es:", nota_mas_alta)
