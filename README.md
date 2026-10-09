# ADM_Ses07 - Matemática básica

Opción A de la sesión práctica 07 de Integración Continua. Requiere Python 3.12;
la librería usa únicamente herramientas incluidas en Python.

## Estructura

```text
basic_math/
    __init__.py          # Exporta las cinco funciones.
    core.py              # Implementación y validaciones.
docs/
    PRUEBA_EN_VIVO.md     # Casos, comandos y demostración.
images/
    *.png                # Capturas de la validación del Pull Request.
tests/
    test_core.py         # Pruebas unitarias de las cinco funciones.
.github/workflows/
    ci.yml               # Integración continua con GitHub Actions.
```

## Uso

Ejecuta Python desde la raíz del repositorio. No necesitas instalar paquetes.

```python
from basic_math import square, factorial, is_prime, gcd, lcm

print(square(2.5))     # 6.25
print(factorial(5))    # 120
print(is_prime(17))    # True
print(gcd(-12, 18))    # 6
print(lcm(4, 6))       # 12
```

Comprobación rápida en PowerShell:

```powershell
python --version
python -c "from basic_math import square; print(square(3))"
```

El segundo comando debe imprimir `9`.

## Reglas de entrada

| Función | Entradas y casos especiales |
| --- | --- |
| `square(n)` | Enteros o decimales, incluidos negativos y cero. |
| `factorial(n)` | Enteros no negativos; `factorial(0) = 1`. Un negativo genera `ValueError`. |
| `is_prime(n)` | Enteros; los valores menores que 2 no son primos. |
| `gcd(a, b)` | Enteros; resultado no negativo y `gcd(0, 0) = 0`. |
| `lcm(a, b)` | Enteros; resultado no negativo y cero si algún argumento es cero. |

Los tipos incompatibles, incluidos `True` y `False`, generan `TypeError`.
Las excepciones se dejan disponibles para verificarlas con `assertRaises` en los tests.

## Pruebas

Ejecuta la suite desde la raíz del repositorio:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## Organización de ramas

- `dev`: desarrollo de la librería y documentación.
- `qa`: integración y validación mediante pruebas unitarias con `unittest`.
- `main`: versión estable, destino de los Pull Requests de `qa`.

El proceso de integración sigue el recorrido `dev` → `qa` → `main`.
El workflow ejecuta las pruebas en pushes a `qa` y `main`, y en cada PR hacia
`main`. Usa Python 3.12, permisos de lectura y el job `unit-tests`; una suite
sin pruebas produce un fallo.

Para impedir merges con pruebas fallidas, la protección de `main` requiere
configuración en GitHub: PR obligatorio y check `unit-tests` obligatorio.

Consulta la [guía de prueba en vivo](docs/PRUEBA_EN_VIVO.md).

## Evidencias

Las [cuatro capturas de validación](docs/PRUEBA_EN_VIVO.md#5-evidencias) muestran
el estado inicial aprobado, el commit que introduce el fallo, el merge bloqueado
y las pruebas aprobadas tras la corrección.
