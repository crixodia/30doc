class Persona:
    def __init__(self, nombre, edad, estatura, nacional):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.nacional = nacional

    def regalos(self):
        letras = len(self.nombre.replace(" ", ""))
        a_cumplidos = self.edad // 4
        cm_estatura = self.estatura // 4

        suma = letras + a_cumplidos + cm_estatura
        c = "🍬"
        if self.nacional == True:
            c = "🥖🥤"

        return c * int(suma)


if __name__ == "__main__":
    persona = Persona(
        input("Dame tu nombre: "),
        int(input("Edad: ")),
        float(input("Estatura cm: ")),
        bool(int(input("Ecuatoriano: "))),
    )

    print(f"Te mereces {persona.regalos()}")
