from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationResult:
    status: str
    message: str


class InvalidTempError(Exception):
    pass


class TempMeasurement:
    def __init__(self, valor, unit: str) -> None:
        self.valor = float(valor)

        up_unidad = unit.upper()
        if up_unidad not in ["C", "K", "F"]:
            raise InvalidTempError(
                f"La unidad '{unit}' no está soportada, ingresa una valida ('C', 'K' o 'F')"
            )
        if up_unidad == "K" and valor < 0:
            raise InvalidTempError("Valor invalido para K")

        self.unit = up_unidad

    def to(self, unit):
        converted = TempConverter()
        return converted.convertion(self, unit)


class TempConverter:
    @staticmethod
    def convertion(measurement: TempMeasurement, unit: str):
        og_unit = measurement.unit
        orden = (og_unit, unit)

        if og_unit == unit:
            return measurement.valor

        routes = {
            ("C", "F"): TempConverter.C_to_F,
            ("C", "K"): TempConverter.C_to_K,
            ("F", "C"): TempConverter.F_to_C,
            ("F", "K"): TempConverter.F_to_K,
            ("K", "F"): TempConverter.K_to_F,
            ("K", "C"): TempConverter.K_to_C,
        }

        if orden not in routes:
            raise InvalidTempError("Convertion doesnt exist")

        function = routes[orden]
        measurement.valor = round(function(measurement.valor), 2)
        measurement.unit = unit
        print(measurement.valor, measurement.unit)
        return measurement.valor

    @staticmethod
    def C_to_F(measurement):
        return measurement * 1.8 + 32

    @staticmethod
    def C_to_K(measurement):
        return measurement + 273.15

    @staticmethod
    def F_to_C(measurement):
        return (measurement - 32) * 5 / 9

    @staticmethod
    def F_to_K(measurement):
        return (measurement - 32) * 5 / 9 + 273.15

    @staticmethod
    def K_to_F(measurement):
        return (measurement - 273.15) * 1.8 + 32

    @staticmethod
    def K_to_C(measurement):
        return measurement - 273.15

    @staticmethod
    def to_celsius(measurement: TempMeasurement):
        if measurement.unit == "F":
            return TempConverter.F_to_C(measurement.valor)
        elif measurement.unit == "K":
            return TempConverter.K_to_C(measurement.valor)
        else:
            raise InvalidTempError("Insert a valid measurement unit")


class TempRangeValidator:
    def __init__(self, min, max) -> None:
        self.min = float(min)
        self.max = float(max)

    def validate(self, measurement: TempMeasurement):
        if measurement.unit != "C":
            celsius = TempConverter.to_celsius(measurement)
        else:
            celsius = measurement.valor

        status = "VALID"
        message_output = "VALID"

        if celsius < self.min:
            message_output = "The measure is below the range"
            status = "LOW"
        elif celsius > self.max:
            message_output = "The measure is above the range"
            status = "HIGH"

        return ValidationResult(status, message_output)
