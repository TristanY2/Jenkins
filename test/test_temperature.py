import pytest

from src.temperature import InvalidTempError, TempMeasurement, TempRangeValidator


def test_C_F():
    assert TempMeasurement(100, "C").to("F") == 212


def test_F_C():
    assert TempMeasurement(32, "F").to("C") == 0


def test_C_K():
    assert TempMeasurement(0, "C").to("K") == 273.15


def test_K_C():
    assert TempMeasurement(273.15, "K").to("C") == 0


def test_F_K():
    assert TempMeasurement(32, "F").to("K") == 273.15


def test_K_F():
    assert TempMeasurement(373.15, "K").to("F") == 212


def test_validation_at_upper_boundary():
    validator = TempRangeValidator(0, 100)
    result = validator.validate(TempMeasurement(212, "F"))
    assert result.status == "VALID"


def test_validation_high():
    validator = TempRangeValidator(0, 100)
    result = validator.validate(TempMeasurement(500, "K"))
    assert result.status == "HIGH"


def test_validation_low():
    validator = TempRangeValidator(0, 100)
    result = validator.validate(TempMeasurement(-100, "C"))
    assert result.status == "LOW"


def test_kelvin_below_zero():
    with pytest.raises(InvalidTempError):
        TempMeasurement(-1, "K")


def test_invalid_unit():
    with pytest.raises(InvalidTempError):
        TempMeasurement(100, "Z")
