# Día 7: Acrónimos

Un poco de contexto:

Las palabras resaltadas son acrónimos, NASA viene de National Aeronautics and Space Administration. IA viene de Inteligencia Artificial. OVNI viene de Objeto Volador No Identificado. Los otros términos los puedes Googlear 😅.

Nos damos cuenta que las abreviaciones de estos términos estás compuestas por las letras mayúsculas de la cadena original

¿Qué deberías presentar?

1. Programa un bloque o función que nos ayude a conocer el acrónimo de una frase dada. No importa si el acrónimo existe o no, sin embargo ten las siguientes consideraciones:

- Infrastructure as a service -> IaaS
- One-Time Password as a service -> OTPaaS
- Liquid-crystal display -> LDC

Explica, que consideraciones tomaste a la hora de desarrollar tu algoritmo y diseña un diagrama de flujo que te ayude a entender mejor tu solución.

## Solucón

Para solucionar este problema dividiremos la cadena ingresada en base a los siguientes tres caracteres: espacio, guión y guión bajo. Usaremos re.split() para dividir la cadena en base a estos caracteres. Luego mapeamos la cadena y obtenemos la primera letra de cada palabra. Finalmente unimos las letras obtenidas en una cadena.

Si la longitud de la cadena es menor o igual a 3 entonces se tomará el primer caracter sin modificaciones, caso contrario se transformará a mayúsculas.

```python
import re


def criteria(s: str) -> str:
    if len(s) <= 3:
        return s[0]

    return s[0].capitalize()


def acronimo(s: str) -> str:
    words = re.split("[-_ ]", s)

    acron = map(criteria, words)
    return "".join(list(acron))

```

## Video Explicativo

[TikTok](https://www.tiktok.com/@crixodia/video/7150816055017950469)
