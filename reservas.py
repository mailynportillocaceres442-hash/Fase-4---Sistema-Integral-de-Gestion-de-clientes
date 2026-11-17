import tkinter as tk
from tkinter import ttk, messagebox

# Lista para almacenar las reservas durante la ejecución
reservas_registradas = []


def mostrar(contenido):
    """
    Muestra el módulo de Reservas dentro del área central
    de la ventana principal main.py.
    """

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Colores
    COLOR_FONDO = "#F4F6F9"
    COLOR_AZUL = "#1F4E79"
    COLOR_BLANCO = "#FFFFFF"

    contenido.configure(bg=COLOR_FONDO)

    # Marco principal
    marco = tk.Frame(contenido, bg=COLOR_FONDO)
    marco.pack(fill="both", expand=True)

    # Título
    titulo = tk.Label(
        marco,
        text="GESTIÓN DE RESERVAS",
        font=("Arial", 20, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_AZUL
    )
    titulo.pack(anchor="w", pady=(0, 20))

    # Formulario
    formulario = tk.LabelFrame(
        marco,
        text="Registrar nueva reserva",
        font=("Arial", 11, "bold"),
        bg=COLOR_BLANCO,
        fg=COLOR_AZUL,
        padx=20,
        pady=15
    )
    formulario.pack(fill="x", pady=(0, 20))

    # Variables
    documento_var = tk.StringVar()
    servicio_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    tiempo_reserva_var = tk.StringVar()
    duracion_var = tk.StringVar()

    # Campo: Documento del cliente
    tk.Label(
        formulario,
        text="Documento del cliente:",
        bg=COLOR_BLANCO,
        font=("Arial", 10)
    ).grid(row=0, column=0, sticky="w", padx=10, pady=8)

    entrada_documento = tk.Entry(
        formulario,
        textvariable=documento_var,
        font=("Arial", 10),
        width=30
    )
    entrada_documento.grid(
        row=0, column=1, sticky="ew", padx=10, pady=8
    )

    # Campo: Servicio
    tk.Label(
        formulario,
        text="Servicio:",
        bg=COLOR_BLANCO,
        font=("Arial", 10)
    ).grid(row=1, column=0, sticky="w", padx=10, pady=8)

    servicios = [
        "Alquiler de sala",
        "Alquiler de equipos",
        "Asesoría",
       
    ]

    lista_servicios = ttk.Combobox(
        formulario,
        textvariable=servicio_var,
        values=servicios,
        state="readonly",
        font=("Arial", 10),
        width=28
    )
    lista_servicios.grid(
        row=1, column=1, sticky="ew", padx=10, pady=8
    )

    # Campo: Cantidad
    tk.Label(
        formulario,
        text="Cantidad:",
        bg=COLOR_BLANCO,
        font=("Arial", 10)
    ).grid(row=2, column=0, sticky="w", padx=10, pady=8)

    entrada_cantidad = tk.Entry(
        formulario,
        textvariable=cantidad_var,
        font=("Arial", 10),
        width=30
    )
    entrada_cantidad.grid(
        row=2, column=1, sticky="ew", padx=10, pady=8
    )

    # Campo: Tipo de reserva
    tk.Label(
        formulario,
        text="Tiempo de reserva:",
        bg=COLOR_BLANCO,
        font=("Arial", 10)
    ).grid(row=3, column=0, sticky="w", padx=10, pady=8)

    lista_tipo_reserva = ttk.Combobox(
        formulario,
        textvariable=tiempo_reserva_var,
        values=["Horas", "Días"],
        state="readonly",
        font=("Arial", 10),
        width=28
    )
    lista_tipo_reserva.grid(
        row=3, column=1, sticky="ew", padx=10, pady=8
    )

    # Campo: Duración de la ocupación
    tk.Label(
        formulario,
        text="Duración de la ocupación:",
        bg=COLOR_BLANCO,
        font=("Arial", 10)
    ).grid(row=4, column=0, sticky="w", padx=10, pady=8)

    entrada_duracion = tk.Entry(
        formulario,
        textvariable=duracion_var,
        font=("Arial", 10),
        width=30
    )
    entrada_duracion.grid(
        row=4, column=1, sticky="ew", padx=10, pady=8
    )

    formulario.grid_columnconfigure(1, weight=1)

    # Tabla de reservas
    marco_tabla = tk.LabelFrame(
        marco,
        text="Reservas registradas",
        font=("Arial", 11, "bold"),
        bg=COLOR_BLANCO,
        fg=COLOR_AZUL,
        padx=15,
        pady=15
    )
    marco_tabla.pack(fill="both", expand=True)

    columnas = ("codigo", 
                "cliente", 
                "servicio",
                "cantidad",
                "tiempo_reserva",
                "estado",
                )

    tabla = ttk.Treeview(
        marco_tabla,
        columns=columnas,
        show="headings",
        height=10
    )

    tabla.heading("codigo", text="CÓDIGO")
    tabla.heading("cliente", text="CLIENTE")
    tabla.heading("servicio", text="SERVICIO")
    tabla.heading("cantidad", text="CANTIDAD")
    tabla.heading("tiempo_reserva", text="TIEMPO DE RESERVA")
    tabla.heading("estado", text="ESTADO")

    tabla.column("codigo", width=110, anchor="center")
    tabla.column("cliente", width=110, anchor="center")
    tabla.column("servicio", width=110, anchor="center")
    tabla.column("cantidad", width=110, anchor="center")
    tabla.column("tiempo_reserva", width=110, anchor="center")
    tabla.column("estado", width=110, anchor="center")

    tabla.pack(fill="both", expand=True)

    # Mostrar reservas registradas anteriormente
    for reserva in reservas_registradas:
        tabla.insert(
            "",
            "end",
            values=(
                reserva["codigo"],
                reserva["cliente"],
                reserva["servicio"],
                reserva["cantidad"],
                reserva["tiempo_reserva"],
                reserva["estado"]
            )
        )

    # Función para registrar una reserva
    def crear_reserva():

        documento = documento_var.get().strip()
        servicio = servicio_var.get().strip()
        cantidad = cantidad_var.get().strip()
        tiempo_reserva = tiempo_reserva_var.get().strip()
        duracion = duracion_var.get().strip()

        # Validar campos vacíos
        if not documento or not servicio or not cantidad or not tiempo_reserva or not duracion:
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, completa todos los campos."
            )
            return

        # Validar valores numéricos
        try:
            cantidad_numero = float(cantidad.replace(",", "."))
            duracion_numero = float(duracion.replace(",", "."))

            if cantidad_numero <= 0 or duracion_numero <= 0:
                messagebox.showwarning(
                    "Datos inválidos",
                    "La cantidad y la duración deben ser mayores que cero."
                )
                return

        except ValueError:
            messagebox.showwarning(
                "Datos inválidos",
                "La cantidad y la duración deben ser valores numéricos."
            )
            return

        # Generar código de reserva
        numero = len(reservas_registradas) + 1
        codigo = f"RES-{numero:03d}"

        # Crear registro
        nueva_reserva = {
            "codigo": codigo,
            "cliente": documento,
            "servicio": servicio,
            "estado": "Confirmada",
            "cantidad": cantidad_numero,
            "tipo_reserva": tiempo_reserva,
            "duracion": duracion_numero
        }

        # Guardar reserva
        reservas_registradas.append(nueva_reserva)

        # Mostrar en la tabla
        tabla.insert(
            "",
            "end",
            values=(
                codigo,
                documento,
                servicio,
                cantidad_numero,
                tiempo_reserva,
                "Confirmada"
            )
        )

        messagebox.showinfo(
            "Reserva registrada",
            f"La reserva {codigo} fue creada y confirmada correctamente."
        )

        # Limpiar campos
        documento_var.set("")
        servicio_var.set("")
        cantidad_var.set("")
        tiempo_reserva_var.set("")
        duracion_var.set("")

        entrada_documento.focus()

    # Botón para registrar
    boton_registrar = tk.Button(
        formulario,
        text="CREAR Y CONFIRMAR RESERVA",
        font=("Arial", 10, "bold"),
        bg=COLOR_AZUL,
        fg="white",
        activebackground="#163A5A",
        activeforeground="white",
        cursor="hand2",
        relief="flat",
        padx=15,
        pady=10,
        command=crear_reserva
    )

    boton_registrar.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=15
    )
