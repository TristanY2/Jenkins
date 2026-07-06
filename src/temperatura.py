class Temperatura:
    def __init__(self, magnitud, unidad) -> None:
        self.magnitud = float(magnitud)

        up_unidad = unidad.upper()
        if up_unidad not in ["C", "K", "F"]:
            raise ValueError(
                f"La unidad '{unidad}' no está soportada, ingresa una valida (C, K, F)"
            )

        self.unidad = unidad.upper()

    def to_K(self):
        if self.unidad == "K":
            print("La unidad ya es K")
            return self.magnitud

        print(f"Convertido {self.magnitud} {self.unidad}", end=" ")
        if self.unidad == "C":
            self.magnitud += 273.15
        elif self.unidad == "F":
            self.magnitud = (self.magnitud - 32) * 5 / 9 + 273.15
        else:
            return "La unidad no es valida"

        self.unidad = "K"
        print(f"a {self.magnitud} {self.unidad}")

        return self.magnitud

    def to_C(self):
        if self.unidad == "C":
            print("La unidad ya es C")
            return self.magnitud

        print(f"Convertido {self.magnitud} {self.unidad}", end=" ")
        if self.unidad == "F":
            self.magnitud = (self.magnitud - 32) * 5 * 9 + 273.15
        elif self.unidad == "K":
            self.magnitud -= 273.15
        else:
            return "Ingresa una unidad válida"
        self.unidad = "C"
        print(f"a {self.magnitud} {self.unidad}")

        return self.magnitud

    def to_F(self):
        if self.unidad == "F":
            print("La unidad ya es F")
            return self.magnitud

        print(f"Convertido {self.magnitud} {self.unidad}", end=" ")
        if self.unidad == "C":
            self.magnitud = self.magnitud * 1.8 + 32
        elif self.unidad == "K":
            self.magnitud = (self.magnitud - 273.15) * 1.8 + 32
        else:
            return "Ingresa una unidad válida"
        self.unidad = "F"
        print(f"a {self.magnitud} {self.unidad}")

        return self.magnitud
