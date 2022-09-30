# Día 5: Luhn

Un poco de contexto:

Para esto, vamos a hacer uso del algoritmo de módulo 10 o también conocido como Fórmula de Luhn. Este algoritmo se aplica para validar diversidad de números de verificación, tarjetas de débito o crédito e incluso números IMEI.

Lo aplicaremos para validar un número de tarjeta de crédito:

| 4   | 5   | 3   | 9   | 3   | 1   | 9   | 5   | 0   | 3   | 4   | 3   | 6   | 4   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

El primer paso del algoritmo es duplicar cada segundo dígito empezando desde la derecha

| 4     | 5   | 3     | 9   | 3     | 1   | 9      | 5   | 0     | 3   | 4     | 3   | 6      | 4   | 6      | 7   |
| ----- | --- | ----- | --- | ----- | --- | ------ | --- | ----- | --- | ----- | --- | ------ | --- | ------ | --- |
| **8** | 5   | **6** | 9   | **6** | 1   | **18** | 5   | **0** | 3   | **8** | 3   | **12** | 4   | **12** | 7   |

Ahora, en este duplicado si el resultado es mayor que 9 le restamos 9

| 4     | 5   | 3     | 9   | 3     | 1   | 9      | 5   | 0     | 3   | 4     | 3   | 6      | 4   | 6      | 7   |
| ----- | --- | ----- | --- | ----- | --- | ------ | --- | ----- | --- | ----- | --- | ------ | --- | ------ | --- |
| **8** | 5   | **6** | 9   | **6** | 1   | **18** | 5   | **0** | 3   | **8** | 3   | **12** | 4   | **12** | 7   |
| **8** | 5   | **6** | 9   | **6** | 1   | **9**  | 5   | **0** | 3   | **8** | 3   | **3**  | 4   | **3**  | 7   |

Finalmente comprobaremos que la suma de todos los dígitos sea divisible para 10. Si esto ocurre, tenemos que indicarle al usuario que el número de tarjeta es válido o no. 😎

¿Qué deberías presentar?

1. Programa una función o bloque de código que nos permita comprobar si un número de tarjeta es válido o no, esto aplicando el algoritmo anterior.
2. Como te comentamos, el algoritmo es conocido como algoritmo de modulo 10, ¿Cuál sería la adaptación si se pide implementar el mismo algoritmo, pero de modulo n?

**Nota:** Puedes utilizar el mismo número de tarjeta para validar tu algoritmo.

## Solución

Resolveremos la parte 1 del problema para tener un mejor panorama de como resolver la parte 2.

### Parte 1

Crearemos una función que reciba un número de tarjeta como string y lo valide.

Validaremos la longitud del número de tarjeta. Luego mapearemos los dígitos a un arreglo de enteros. Gracias a la notación slice de Python, podemos obtener los dígitos a duplicar y los que no de forma sencilla.

Luego usamos map para duplicar los dígitos y otro map para aplicar la fórmula de Luhn. Finalmente sumamos todos los dígitos y comprobamos si es divisible por 10.

```python
def is_valid_card(number: str) -> bool:
    number = number.strip().replace(" ", "")

    # Logitud de número de tarjeta de crédito
    if len(number) != 16:
        return False

    # Fórmula de Luhn
    digits = list(map(int, number))
    A = digits[::2]  # Dígitos con índice par
    B = digits[1::2]  # Dígitos con índice impar

    A = list(map(lambda x: 2*x, A))  # El factor se puede modificar
    A = list(map(lambda x: sum(divmod(x, 10)), A))

    return sum(list(A) + B) % 10 == 0
```

### Parte 2

Para resolver la parte 2 del problema, crearemos una función que reciba una cadena a validar y un conjunto de caracteres válidos (como string). Obtenemos la longitud del conjunto pues será nuestro `N`. Mapearemos cada carácter a su respectiva posición en el conjunto de caracteres válidos. Y extrapolamos la solución de la [parte 1](#parte-1) cambiando `10` por `N`.

```python
def luhn_n(s: str, symbols: list = SYMBOLS) -> bool:
    # Validación generalizada de Luhn (Luhn N)
    N = len(symbols)
    s = s.strip().replace(" ", "")

    chars = list(map(symbols.index, s))
    A = chars[::2]
    B = chars[1::2]

    A = list(map(lambda x: 2*x, A))
    A = list(map(lambda x: sum(divmod(x, N)), A))

    return sum(list(A) + B) % N == 0
```

Dado que en la generalización del Algoritmo de Luhn el conjunto de caracteres válidos es dinámico. Crearemos una función que permita generar una cadena junto a su código de verificación. Realmente aquí repetimos el algoritmo anterior con un único detalle en el valor a retornar. Aquí retornamos un entero y no un booleano. Este entero se conoce como el **carácter de verificación**.

```python
def luhn_check_n(s: str, symbols: list = SYMBOLS) -> int:
    # Generación de caracter de comprobación de Luhn
    N = len(symbols)
    s = s.strip().replace(" ", "")

    chars = list(map(symbols.index, s))
    A = chars[::2]
    B = chars[1::2]

    A = list(map(lambda x: 2*x, A))
    #A = list(map(lambda x: x - (N - 1) if x > (N - 1) else x, A))
    A = list(map(lambda x: sum(divmod(x, N)), A))

    check = (N - sum(list(A) + B)) % N
    return 0 if check == N else check
```

Por último, crearemos una función que permita generar una cadena de caracteres válidos junto a su código de verificación. Obtendremos el carácter correspondiente buscando en el conjunto de caracteres válidos. Finalmente concatenamos el carácter de verificación al final de la cadena.

```python
def luhn_encode_n(s: str, symbols: list = SYMBOLS) -> str:
    # Creación de string con carácter de comprobación al Final
    return s + symbols[luhn_check_n(s, symbols)]
```

Puedes encontrar el código completo [aquí](main.py).

Validamos un número de tarjeta de crédito.

```bash
python main.py "5387 0772 9033 3852"
python main.py "5387 0772 9033 3855"
```

Salida:

```bash
>> 5387 0772 9033 3852 -> False
>> 5387 0772 9033 3855 -> True
```

Validamos un número de tarjeta de crédito con el algoritmo de Luhn N ingresando un conjunto de caracteres válidos y un número de tarjeta de crédito sin su último dígito.

```bash
python main.py "0123456789" "5387 0772 9033 385"
```

Salida:

```bash
symbols: 0123456789
string: 5387 0772 9033 385
check char: 5
encoded string: 5387 0772 9033 3855
is valid: True
```
