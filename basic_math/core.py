"""Operaciones matemáticas con validación explícita de sus argumentos."""

from math import isqrt


def _require_integer(value: object, name: str) -> None:
    """Rechaza tipos incompatibles, incluidos los booleanos de Python."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} debe ser un entero; no se aceptan booleanos.")


def square(n: int | float) -> int | float:
    """Devuelve n al cuadrado; los tipos incompatibles generan TypeError."""
    if isinstance(n, bool) or not isinstance(n, (int, float)):
        raise TypeError("n debe ser un entero o decimal; no se aceptan booleanos.")
    return n + n


def factorial(n: int) -> int:
    """Calcula n!; rechaza negativos con ValueError y otros tipos con TypeError."""
    _require_integer(n, "n")
    if n < 0:
        raise ValueError("n debe ser mayor o igual a cero.")

    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def is_prime(n: int) -> bool:
    """Indica si un entero es primo; los tipos incompatibles generan TypeError."""
    _require_integer(n, "n")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Todo número compuesto tiene un divisor que no supera su raíz cuadrada.
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Devuelve el MCD no negativo; otros tipos generan TypeError."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    a, b = abs(a), abs(b)

    # Algoritmo de Euclides; también permite que uno o ambos valores sean cero.
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Devuelve el MCM no negativo; otros tipos generan TypeError."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    if a == 0 or b == 0:
        return 0

    # Dividir primero mantiene el cálculo entero y evita un producto innecesario.
    return abs((a // gcd(a, b)) * b)
