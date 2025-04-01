#Chay Dzul Edelmy
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return x**2 + 3*x + 1

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n_values = [10, 20, 50]  # Lista de números de subdivisiones

# Cálculo de la solución exacta
exact_solution = (b**3 / 3 + (3 * b**2) / 2 + b) - (a**3 / 3 + (3 * a**2) / 2 + a)  # Solución exacta

# Cálculo de la integral para cada n
for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)

    # Calcular el error
    error = abs(integral_approx - exact_solution)

    # Imprimir el resultado de la integral aproximada y el error
    print(f"Integral aproximada con n={n}: {integral_approx:.6f}, Error: {error:.6f}")

    # Gráfica de la función y la aproximación por trapecios
    x_fine = np.linspace(a, b, 100)
    y_fine = f(x_fine)

    plt.figure(figsize=(8, 5))
    plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x^2 + 3x + 1$', linewidth=2)
    plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
    plt.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")

    # Etiquetas y leyenda
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.title(f"Aproximación de la integral con la regla del trapecio (n={n})")
    plt.legend()
    plt.grid()

    # Guardar la figura
    plt.savefig(f"trapecio_n_{n}.png")
    plt.show()