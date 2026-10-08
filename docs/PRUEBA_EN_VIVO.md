# Prueba en vivo - Opción A

Procedimiento para comprobar las funciones y demostrar el bloqueo de un
Pull Request con pruebas fallidas. Los comandos se ejecutan en PowerShell
desde la raíz del repositorio.

## 1. Requisitos de la demostración

- Python 3.12 y cambios del proyecto confirmados en Git.
- Librería integrada en `qa` y pruebas disponibles en `tests/test_core.py`.
- Pruebas basadas en `unittest.TestCase`, con métodos llamados `test_*`.
- Tests y workflow publicados en GitHub, con `main` protegida.

Para integrar los cambios confirmados de desarrollo en la rama de validación:

```powershell
git switch qa
git merge dev
```

Las pruebas verifican resultados con `assertEqual`, `assertTrue` o
`assertFalse`, y excepciones con `assertRaises`.

## 2. Casos que deben cubrir los tests

| Función | Dos casos exitosos | Casos borde y de error |
| --- | --- | --- |
| `square` | `square(3) == 9`; `square(-4) == 16` | `square(0) == 0`; `square("3")` genera `TypeError`. |
| `factorial` | `factorial(3) == 6`; `factorial(5) == 120` | `factorial(0) == 1`; `factorial(-1)` genera `ValueError`. |
| `is_prime` | `is_prime(2) is True`; `is_prime(9) is False` | `is_prime(1) is False`; `is_prime(2.5)` genera `TypeError`. |
| `gcd` | `gcd(12, 18) == 6`; `gcd(7, 5) == 1` | `gcd(0, 0) == 0`; `gcd(-12, 18) == 6`; `gcd("12", 18)` genera `TypeError`. |
| `lcm` | `lcm(4, 6) == 12`; `lcm(3, 5) == 15` | `lcm(0, 5) == 0`; `lcm(-4, 6) == 12`; `lcm(4, 2.5)` genera `TypeError`. |

La cobertura incluye también el rechazo de booleanos y argumentos inválidos
en ambas posiciones de `gcd` y `lcm`, incluso si el otro argumento es cero.

Comando de ejecución de la suite, que requiere la carpeta `tests/`:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Debe ejecutar casos de las cinco funciones y finalizar con `OK`.
**`Ran 0 tests` no valida la práctica.**

## 3. Requisitos de integración continua

- Repositorio público y código, tests y workflow publicados en `qa`.
- Workflow ejecutado en cada PR hacia `main`, con el comando anterior.
- Job de pruebas identificado mediante una ejecución antes de seleccionarlo como check obligatorio.
- Protección de `main`: PR obligatorio y check de pruebas obligatorio.
- Restricciones aplicadas también al administrador, sin permitir bypass.
- Force pushes y eliminación de `main` bloqueados.

Referencia de configuración:
[protección de ramas de GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## 4. Demostrar fallo y corrección

Con los tests y la protección listos, trabaja en `qa`. Cambia temporalmente en
`basic_math/core.py` el retorno de `square` de `return n * n` a `return n + n`.
Ejecuta los tests: `square(3)` devuelve `6` y su prueba debe fallar.

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
git add basic_math/core.py
git commit -m "demo: provoca un fallo en square"
git push origin qa
```

Abre manualmente el PR **`qa` hacia `main`**. Muestra la ejecución fallida de
Actions y el merge bloqueado. Mantén el PR abierto para corregirlo.

Restaura `return n * n` en `square` y ejecuta:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
git add basic_math/core.py
git commit -m "fix: restaura el calculo de square"
git push origin qa
```

En el mismo PR, muestra las pruebas aprobadas y el merge habilitado. Realiza el
merge desde GitHub después de verificar el resultado.
