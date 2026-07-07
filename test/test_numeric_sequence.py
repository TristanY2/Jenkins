from _pytest.reports import _report_kwargs_from_json
import pytest
from src.numeric_sequence import SequenceAnalyzer


def test_arithmetic():
    report = SequenceAnalyzer().analyze([2, 4, 6, 8, 10])
    assert report.classification == "ARITHMETIC"
    assert report.prediction == 12


def test_geometric():
    report = SequenceAnalyzer().analyze([3, 9, 27, 81])
    assert report.classification == "GEOMETRIC"
    assert report.prediction == 243


def test_fibonacci():
    report = SequenceAnalyzer().analyze([1, 1, 2, 3, 5, 8])
    assert report.classification == "FIBONACCI"
    assert report.prediction == 13


def test_unkown():
    report = SequenceAnalyzer().analyze([1, 11, 13, 21])
    assert report.classification == "UNKOWN"
    assert report.prediction is None


def test_short():
    with pytest.raises(ValueError):
        SequenceAnalyzer().analyze([1, 2])
