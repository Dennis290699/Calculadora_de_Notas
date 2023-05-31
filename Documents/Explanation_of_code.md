<div align="center">
  <h1 id="Calculadora">Calculator Grades</h1>
</div>

The code defines a class called `CalculadoraNotas` (CalculatorGrades), which provides functions to perform calculations related to grades. This class has the following methods:

- `__init__(self)`: The class initialization method, which is automatically called when an instance of the class is created. This method initializes an empty list called `notas` (grades), which is used to store the entered grades.

- `ingresar_notas(self, cantidad)`: This method prompts the user to enter a specific number of grades and stores them in the `notas` list using a `for` loop. Each grade is converted to the `float` type and added to the list.

- `obtener_nota_mas_alta(self)`: This method returns the highest grade in the `notas` list, using the `max()` function.

- `obtener_nota_mas_baja(self)`: This method returns the lowest grade in the `notas` list, using the `min()` function.

- `obtener_promedio(self)`: This method calculates and returns the average of all the grades in the `notas` list, using the `sum()` function to add up all the grades and dividing by the number of grades using `len()`.

Then, an instance of the `CalculadoraNotas` class named `calculadora` (calculator) is created. The program prompts the user to enter the number of grades they want to input and calls the `ingresar_notas()` method of the `calculadora` instance to let the user enter the grades.

Next, the `obtener_promedio()` (get_average), `obtener_nota_mas_alta()` (get_highest_grade), and `obtener_nota_mas_baja()` (get_lowest_grade) methods of the `calculadora` instance are called to obtain the average, highest grade, and lowest grade, respectively.

Finally, the program displays the results on the screen using `print()`, showing the average, lowest grade, and highest grade.

<p>
