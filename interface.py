import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import DosiDosi

class DosiDosiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DosiDosi - Sistema de Cálculo de Dosimetria da Pena")
        self.geometry("360x640")  # Tamanho de um celular
        self.config(bg="#2E4053")  # Cor de fundo azul-marinho



        self.crimes = DosiDosi.crimes

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.frame_crime = tk.Frame(self.notebook, bg="#2E4053")
        self.frame_crime.pack(fill="both", expand=True)
        self.notebook.add(self.frame_crime, text="Crime")

        self.frame_circunstancias = tk.Frame(self.notebook, bg="#2E4053")
        self.frame_circunstancias.pack(fill="both", expand=True)
        self.notebook.add(self.frame_circunstancias, text="Circunstâncias")

        self.frame_resultado = tk.Frame(self.notebook, bg="#2E4053")
        self.frame_resultado.pack(fill="both", expand=True)
        self.notebook.add(self.frame_resultado, text="Resultado")

        self.criar_frame_crime()
        self.criar_frame_circunstancias()
        self.criar_frame_resultado()

    def criar_frame_crime(self):
        tk.Label(self.frame_crime, text="Selecione o crime:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.crime_var = tk.StringVar()
        self.crime_var.set(list(self.crimes.keys())[0])
        self.crime_menu = ttk.OptionMenu(self.frame_crime, self.crime_var, *self.crimes.keys(), style="TMenubutton")
        self.crime_menu.pack(pady=10)

    def criar_frame_circunstancias(self):
        tk.Label(self.frame_circunstancias, text="Circunstâncias judiciais desfavoráveis:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.circunstancias_var = tk.IntVar()
        self.circunstancias_var.set(0)
        self.circunstancias_scale = tk.Scale(self.frame_circunstancias, from_=0, to=7, variable=self.circunstancias_var, orient="horizontal", bg="#2E4053", fg="white", font=("Arial", 10))
        self.circunstancias_scale.pack(pady=10)

        tk.Label(self.frame_circunstancias, text="Agravantes:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.agravantes_var = tk.IntVar()
        self.agravantes_var.set(0)
        self.agravantes_scale = tk.Scale(self.frame_circunstancias, from_=0, to=7, variable=self.agravantes_var, orient="horizontal", bg="#2E4053", fg="white", font=("Arial", 10))
        self.agravantes_scale.pack(pady=10)

        tk.Label(self.frame_circunstancias, text="Atenuantes:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.atenuantes_var = tk.IntVar()
        self.atenuantes_var.set(0)
        self.atenuantes_scale = tk.Scale(self.frame_circunstancias, from_=0, to=7, variable=self.atenuantes_var, orient="horizontal", bg="#2E4053", fg="white", font=("Arial", 10))
        self.atenuantes_scale.pack(pady=10)

        tk.Label(self.frame_circunstancias, text="Causas de aumento (majorantes):", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.majorantes_var = tk.IntVar()
        self.majorantes_var.set(0)
        self.majorantes_scale = tk.Scale(self.frame_circunstancias, from_=0, to=7, variable=self.majorantes_var, orient="horizontal", bg="#2E4053", fg="white", font=("Arial", 10))
        self.majorantes_scale.pack(pady=10)

        tk.Label(self.frame_circunstancias, text="Causas de diminuição (minorantes):", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.minorantes_var = tk.IntVar()
        self.minorantes_var.set(0)
        self.minorantes_scale = tk.Scale(self.frame_circunstancias, from_=0, to=7, variable=self.minorantes_var, orient="horizontal", bg="#2E4053", fg="white", font=("Arial", 10))
        self.minorantes_scale.pack(pady=10)

        calcular_button = tk.Button(self.frame_circunstancias, text="Calcular", command=self.calcular_pena, bg="#007bff", fg="white", font=("Arial", 12, "bold"))
        calcular_button.pack(pady=10)

    def criar_frame_resultado(self):
        tk.Label(self.frame_resultado, text="Pena-base:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.pena_base_label = tk.Label(self.frame_resultado, text="", bg="#2E4053", font=("Arial", 12), fg="white")
        self.pena_base_label.pack(pady=10)

        tk.Label(self.frame_resultado, text="Pena provisória:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.pena_provisoria_label = tk.Label(self.frame_resultado, text="", bg="#2E4053", font=("Arial", 12), fg="white")
        self.pena_provisoria_label.pack(pady=10)

        tk.Label(self.frame_resultado, text="Pena definitiva:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.pena_definitiva_label = tk.Label(self.frame_resultado, text="", bg="#2E4053", font=("Arial", 12), fg="white")
        self.pena_definitiva_label.pack(pady=10)

        tk.Label(self.frame_resultado, text="Regime de pena:", bg="#2E4053", font=("Arial", 12, "bold"), fg="white").pack(pady=10)
        self.regime_label = tk.Label(self.frame_resultado, text="", bg="#2E4053", font=("Arial", 12), fg="white")
        self.regime_label.pack(pady=10)

    def calcular_pena(self):
        crime = self.crime_var.get()
        circunstancias = self.circunstancias_var.get()
        agravantes = self.agravantes_var.get()
        atenuantes = self.atenuantes_var.get()
        majorantes = self.majorantes_var.get()
        minorantes = self.minorantes_var.get()

        pena_base_dias = DosiDosi.calcular_pena_base(crime, circunstancias)
        anos_base, meses_base, dias_base = DosiDosi.calcular_dias_para_anos_meses_dias(pena_base_dias)
        self.pena_base_label.config(text=f"{anos_base} anos, {meses_base} meses e {dias_base} dias")

        pena_provisoria_dias = DosiDosi.calcular_pena_provisoria(pena_base_dias, agravantes, atenuantes)
        anos_prov, meses_prov, dias_prov = DosiDosi.calcular_dias_para_anos_meses_dias(pena_provisoria_dias)
        self.pena_provisoria_label.config(text=f"{anos_prov} anos, {meses_prov} meses e {dias_prov} dias")

        pena_definitiva_dias = DosiDosi.calcular_pena_definitiva(pena_provisoria_dias, majorantes, minorantes)
        anos_def, meses_def, dias_def = DosiDosi.calcular_dias_para_anos_meses_dias(pena_definitiva_dias)
        self.pena_definitiva_label.config(text=f"{anos_def} anos, {meses_def} meses e {dias_def} dias")

        anos_definitivos = anos_def + (meses_def / 12)
        if anos_definitivos < 4:
            regime = "Regime Aberto"
        elif anos_definitivos < 8:
            regime = "Regime Semiaberto"
        else:
            regime = "Regime Fechado"
        self.regime_label.config(text=regime)

if __name__ == "__main__":
    app = DosiDosiApp()
    app.mainloop()