import tkinter as tk
from fractions import Fraction

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación Tkinter con tamaño proporcional")

# Obtener la resolución de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la relación de aspecto de la pantalla
aspect_ratio = screen_width / screen_height

# Convertir la relación de aspecto a una fracción y simplificarla
aspect_ratio_fraction = Fraction(aspect_ratio).limit_denominator()
aspect_ratio_str = f"{aspect_ratio_fraction.numerator}:{aspect_ratio_fraction.denominator}"

# Calcular el tamaño de la ventana en proporciones relativas a la resolución de la pantalla
# Por ejemplo, queremos que la ventana ocupe el 50% del área de la pantalla
window_area_ratio = 0.5
window_area = screen_width * screen_height * window_area_ratio
window_height = int((window_area / aspect_ratio) ** 0.5)
window_width = int(window_height * aspect_ratio)

print(f"Resolución de la pantalla: {screen_width}x{screen_height}")
print(f"Relación de aspecto: {aspect_ratio_str}")
print(f"Tamaño de la ventana: {window_width}x{window_height}")

# Establecer el tamaño de la ventana principal
root.geometry(f"{window_width}x{window_height}")

# Desactivar la capacidad de redimensionar la ventana (opcional)
root.resizable(False, False)

# Crear un LabelFrame
labelframe = tk.LabelFrame(root, text="Este es un LabelFrame")
labelframe.pack(padx=10, pady=10, fill="both", expand=True)

# Crear y colocar un widget dentro del LabelFrame
label = tk.Label(labelframe, text="Hola, Tkinter!")
label.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()