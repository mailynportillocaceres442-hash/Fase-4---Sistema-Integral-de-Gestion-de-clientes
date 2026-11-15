import tkinter as tk
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod
from pathlib import Path
import datetime
import math


# ==========================================
# EXCEPCIÓN PERSONALIZADA Y SISTEMA DE LOGS
# ==========================================

class ServicioError(Exception):
    """Excepción personalizada para errores de servicios."""
    pass


def registrar_log(mensaje: str):
    """Registra eventos y errores en un archivo local."""
    try:
        ruta_log = Path(file).resolve().parent / "sistema_errores.log"
        tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ruta_log, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[{tiempo_actual}] LOG_SERVICIOS: {mensaje}\n"
            )

    except Exception as e:
        print(f"Error al escribir en el archivo de log: {e}")


# ==========================================
# CLASE ABSTRACTA: SERVICIO
# ==========================================

class Servicio(ABC):
    """Clase abstracta base para los servicios de SOFTWARE FJ."""

    def _init_(self, codigo: str, descripcion: str, tarifa_base: float):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ServicioError("El código del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ServicioError("La descripción del servicio es obligatoria.")

        if not isinstance(tarifa_base, (int, float)):
            raise ServicioError("La tarifa debe ser numérica.")

        if not math.isfinite(tarifa_base) or tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor que cero.")

        self._codigo = codigo.strip()
        self._descripcion = descripcion.strip()
        self._tarifa_base = float(tarifa_base)

    @abstractmethod
    def calcular_costo(self, cantidad: float) -> float:
        """Calcula el costo según el tipo de servicio."""
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        """Devuelve la descripción del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, cantidad: float) -> bool:
        """Valida los parámetros utilizados en el servicio."""
        pass

    def obtener_codigo(self) -> str:
        return self._codigo


# ==========================================
# SERVICIO ESPECIALIZADO 1: SALAS
# ==========================================

class ServicioSalas(Servicio):
    """Servicio especializado en reservas de salas."""

    def validar_parametros(self, horas: float) -> bool:

        if not isinstance(horas, (int, float)):
            raise ServicioError("Las horas deben ser un valor numérico.")

        if not math.isfinite(horas) or horas <= 0:
            raise ServicioError(
                "Las horas de reserva deben ser mayores a cero."
            )

        return True

    def calcular_costo(self, horas: float) -> float:

        self.validar_parametros(horas)

        return self._tarifa_base * horas

    def describir_servicio(self) -> str:

        return (
            f"[Sala] Código: {self._codigo} | "
            f"{self._descripcion} | "
            f"Tarifa/Hora: ${self._tarifa_base:,.2f}"
        )


# ==========================================
# SERVICIO ESPECIALIZADO 2: ALQUILER EQUIPOS
# ==========================================

class ServicioAlquilerEquipos(Servicio):
    """Servicio especializado en alquiler de equipos tecnológicos."""

    def validar_parametros(self, dias: float) -> bool:

        if not isinstance(dias, (int, float)):
            raise ServicioError("Los días deben ser un valor numérico.")

        if not math.isfinite(dias) or dias <= 0:
            raise ServicioError(
                "Los días de alquiler deben ser mayores a cero."
            )

        return True

    def calcular_costo(self, dias: float) -> float:

        self.validar_parametros(dias)

        return self._tarifa_base * dias

    def describir_servicio(self) -> str:

        return (
            f"[Equipo] Código: {self._codigo} | "
            f"{self._descripcion} | "
            f"Tarifa/Día: ${self._tarifa_base:,.2f}"
        )


# ==========================================
# SERVICIO ESPECIALIZADO 3: ASESORÍAS
# ==========================================

class ServicioAsesorias(Servicio):
    """Servicio especializado en asesorías profesionales."""

    def validar_parametros(self, sesiones: float) -> bool:

        if not isinstance(sesiones, (int, float)):
            raise ServicioError("Las sesiones deben ser numéricas.")

        if not math.isfinite(sesiones) or sesiones <= 0:
            raise ServicioError(
                "Las sesiones de asesoría deben ser mayores a cero."
            )

        return True

    def calcular_costo(self, sesiones: float) -> float:

        self.validar_parametros(sesiones)

        return self._tarifa_base * sesiones

    def describir_servicio(self) -> str:

        return (
            f"[Asesoría] Código: {self._codigo} | "
            f"{self._descripcion} | "
            f"Tarifa/Sesión: ${self._tarifa_base:,.2f}"
        )


# ==========================================
# INTERFAZ GRÁFICA DEL MÓDULO SERVICIOS
# ==========================================

def mostrar(contenedor):
    """Carga el módulo dentro del panel principal de SOFTWARE FJ."""

    for widget in contenedor.winfo_children():
        widget.destroy()

    # Título del módulo

    tk.Label(
        contenedor,
        text="GESTIÓN DE SERVICIOS Y POLIMORFISMO",
        font=("Arial", 18, "bold"),
        bg="#F2F5FA",
        fg="#173B63"
    ).pack(anchor="w", pady=(10, 15))

    # Marco principal

    marco_contenido = tk.Frame(
        contenedor,
        bg="#FFFFFF",
        highlightbackground="#DCE4EE",
        highlightthickness=1
    )

    marco_contenido.pack(
        fill="both",
        expand=True,
        padx=5,
        pady=5
    )

    # Servicios disponibles

    servicios_disponibles = [
        ServicioSalas(
            "SALA-01",
            "Sala Ejecutiva de Reuniones",
            50000.0
        ),

        ServicioAlquilerEquipos(
            "EQ-01",
            "Kit de Desarrollo Portátil i7",
            35000.0
        ),

        ServicioAsesorias(
            "ASES-01",
            "Consultoría en Arquitectura de Software",
            120000.0
        )
    ]

    tk.Label(
        marco_contenido,
        text=(
            "Seleccione un servicio y digite la cantidad "
            "(horas, días o sesiones) para calcular el costo:"
        ),
        font=("Arial", 11),
        bg="#FFFFFF",
        fg="#263445",
        wraplength=650,
        justify="left"
    ).pack(anchor="w", padx=25, pady=(20, 10))

    # Selector de servicios

    frame_selector = tk.Frame(
        marco_contenido,
        bg="#FFFFFF"
    )

    frame_selector.pack(
        anchor="w",
        padx=25,
        pady=5
    )

    tk.Label(
        frame_selector,
        text="Servicio:",
        font=("Arial", 10, "bold"),
        bg="#FFFFFF",
        fg="#263445"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 10)
    )

    combo_servicios = ttk.Combobox(
        frame_selector,
        values=[
            servicio.describir_servicio()
            for servicio in servicios_disponibles
        ],
        width=65,
        state="readonly"
    )

    combo_servicios.grid(
        row=0,
        column=1,
        sticky="w"
    )

    combo_servicios.current(0)

    # Entrada de cantidad

    frame_cantidad = tk.Frame(
        marco_contenido,
        bg="#FFFFFF"
    )

    frame_cantidad.pack(
        anchor="w",
        padx=25,
        pady=15
    )

    tk.Label(
        frame_cantidad,
        text="Cantidad:",
        font=("Arial", 10, "bold"),
        bg="#FFFFFF",
        fg="#263445"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 18)
    )

    entry_cantidad = tk.Entry(
        frame_cantidad,
        font=("Arial", 11),
        width=15
    )

    entry_cantidad.grid(
        row=0,
        column=1,
        sticky="w"
    )

    # Resultado

    lbl_resultado = tk.Label(
        marco_contenido,
        text="El resultado del cálculo aparecerá aquí...",
        font=("Arial", 11, "bold"),
        bg="#FFFFFF",
        fg="#2878B5",
        wraplength=650,
        justify="left"
    )

    lbl_resultado.pack(
        anchor="w",
        padx=25,
        pady=15
    )

    # ==========================================
    # FUNCIÓN PARA CALCULAR EL COSTO
    # ==========================================

    def ejecutar_calculo():

        try:

            seleccion_idx = combo_servicios.current()

            if seleccion_idx < 0:
                raise ServicioError(
                    "Debe seleccionar un servicio."
                )

            servicio_seleccionado = servicios_disponibles[
                seleccion_idx
            ]

            texto_cantidad = entry_cantidad.get().strip()

            if not texto_cantidad:
                raise ValueError(
                    "La cantidad no puede estar vacía."
                )

            cantidad = float(texto_cantidad)

            # Cálculo polimórfico

            costo_total = servicio_seleccionado.calcular_costo(
                cantidad
            )

        except ValueError as ve:

            error_msg = (
                f"Error de formato en la cantidad ingresada: {ve}"
            )

            messagebox.showerror(
                "Error de validación",
                error_msg
            )

            registrar_log(error_msg)

            lbl_resultado.config(
                text="Estado: Error en los datos de entrada.",
                fg="red"
            )

        except ServicioError as se:

            error_msg = f"Error en el servicio: {se}"

            messagebox.showwarning(
                "Restricción del sistema",
                error_msg
            )

            registrar_log(error_msg)

            lbl_resultado.config(
                text=f"Estado: {se}",
                fg="orange"
            )

        except Exception as e:

            error_msg = f"Error inesperado: {e}"

            messagebox.showerror(
                "Error crítico",
                error_msg
            )

            registrar_log(error_msg)

            lbl_resultado.config(
                text="Estado: Error crítico registrado.",
                fg="red"
            )

        else:

            exito_msg = (
                f"Cálculo exitoso para "
                f"{servicio_seleccionado.obtener_codigo()}. "
                f"Total a pagar: ${costo_total:,.2f}"
            )

            lbl_resultado.config(
                text=exito_msg,
                fg="green"
            )

            registrar_log(
                f"Operación exitosa: {exito_msg}"
            )

        finally:

            print(
                "Depuración: Ciclo de evaluación finalizado."
            )

    # Botón de cálculo

    btn_calcular = tk.Button(
        marco_contenido,
        text="Calcular Costo del Servicio",
        font=("Arial", 10, "bold"),
        bg="#173B63",
        fg="#FFFFFF",
        activebackground="#245581",
        activeforeground="#FFFFFF",
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2",
        command=ejecutar_calculo
    )

    btn_calcular.pack(
        anchor="w",
        padx=25,
        pady=10
    )
