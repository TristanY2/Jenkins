from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SequenceReport:
    classification: str
    prediction: Optional[float]


class Sequence:
    def __init__(self, sequence) -> None:
        if not isinstance(sequence, (list, tuple)):
            raise ValueError("La serie debe ser una lista o tupla")

        for elem in sequence:
            if not isinstance(elem, (float, int)) or isinstance(elem, bool):
                raise ValueError(f"El elemento {elem} no es un número")

        if len(sequence) < 3:
            raise ValueError("La serie debe tener por lo menos 3 elementos")

        self.seq = sequence


class SequenceRule:
    name = "UNKOWN"

    def matches(self, sequence: Sequence) -> bool:
        raise NotImplementedError

    def predict(self, sequence: Sequence):
        raise NotImplementedError


class FibonacciRule(SequenceRule):
    name = "FIBONACCI"

    def matches(self, sequence: Sequence) -> bool:
        for i in range(2, len(sequence.seq)):
            if sequence.seq[i] != (sequence.seq[i - 2] + sequence.seq[i - 1]):
                return False
        return True

    def predict(self, sequence: Sequence):
        return sequence.seq[-1] + sequence.seq[-2]


class ArithmeticRule(SequenceRule):
    name = "ARITHMETIC"

    def matches(self, sequence: Sequence) -> bool:
        dif = [
            actual - previous
            for previous, actual in zip(sequence.seq, sequence.seq[1:])
        ]
        total = set(dif)
        if len(total) == 1:
            return True
        return False

    def predict(self, sequence: Sequence):
        dif = sequence.seq[-1] - sequence.seq[-2]
        return sequence.seq[-1] + dif


class GeometricRule(SequenceRule):
    name = "GEOMETRIC"

    def matches(self, sequence: Sequence) -> bool:
        razon = sequence.seq[1] / sequence.seq[0]
        for i in range(1, len(sequence.seq)):
            if sequence.seq[i] / sequence.seq[i - 1] != razon:
                return False
        return True

    def predict(self, sequence: Sequence):
        return sequence.seq[-1] * sequence.seq[0]


class SequenceAnalyzer:
    def __init__(self) -> None:
        self.rules = [FibonacciRule(), ArithmeticRule(), GeometricRule()]

    def analyze(self, values) -> SequenceReport:
        sequence = Sequence(values)
        for rule in self.rules:
            if rule.matches(sequence):
                return SequenceReport(rule.name, rule.predict(sequence))
        return SequenceReport("UNKOWN", None)
