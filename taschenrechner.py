import tkinter as tk

# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Taschenrechner")

# Erstelle die Eingabefelder für die Operanden
operand1_entry = tk.Entry(window)
operand2_entry = tk.Entry(window)

# Erstelle die Buttons für die Grundrechenarten
add_button = tk.Button(window, text="+", command=lambda: perform_operation("add"))
subtract_button = tk.Button(window, text="-", command=lambda: perform_operation("subtract"))
multiply_button = tk.Button(window, text="*", command=lambda: perform_operation("multiply"))
divide_button = tk.Button(window, text="/", command=lambda: perform_operation("divide"))

# Erstelle das Ausgabefeld
result_label = tk.Label(window, text="")

# Platziere die Widgets im Fenster
operand1_entry.grid(row=0, column=0)
operand2_entry.grid(row=0, column=1)
add_button.grid(row=0, column=2)
subtract_button.grid(row=1, column=0)
multiply_button.grid(row=1, column=1)
divide_button.grid(row=1, column=2)
result_label.grid(row=2, column=0, columnspan=3)

# Definiert die Funktion zum Ausführen der Berechnungen
def perform_operation(operation):
  operand1 = float(operand1_entry.get())
  operand2 = float(operand2_entry.get())

  if operation == "add":
    result = operand1 + operand2
  elif operation == "subtract":
    result = operand1 - operand2
  elif operation == "multiply":
    result = operand1 * operand2
  elif operation == "divide":
    result = operand1 / operand2

  result_label.config(text=str(result))

# Starte die GUI-Schleife
window.mainloop()
