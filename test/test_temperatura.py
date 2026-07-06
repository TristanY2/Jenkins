import pytest
from src.temperatura import Temperatura


@pytest.mark.parametrize(
    "celsius_entrada, fahrenheit_esperado",
    [(0, 32.0), (100, 212.0), (-40, -40), (37, 98.6)],
)
def test_C_a_F(celsius_entrada, fahrenheit_esperado):
    temp = Temperatura(celsius_entrada, "C")

    res = temp.to_F()

    assert res - fahrenheit_esperado < 1e-5


def test_unidad_invalida():
    with pytest.raises(ValueError):
        Temperatura(100, "z")
