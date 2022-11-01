# Día 9: Listas Enlazadas Parte 2

Hola, el día de hoy seguiremos trabajando con las listas y vamos a comprobar si resolvimos el problema anterior de una manera adecuada, para esto:

1. Crea la siguiente lista enlazada:

```bash
1 -> 54 -> 20 -> 13 -> 43 ->18 -> 11-> 53
```

1. Muestra la lista anterior, para esto puedes construir un bloque o función que reciba una lista enlazada y devuelva lo anteriormente indicado (suma puntos si lo imprimes de manera creativa, clara o divertida).
2. Con los métodos shift y push inserta los valores 68, 95, 3, 7 y 37, aleatoriamente, en la lista y muéstrala por pantalla.
3. Crea un bloque o función que tome una lista y nos devuelva dos listas, una con los números pares y otra con los impares.

Para esto NO deberás modificar las funciones o métodos que creaste antes, tienes que trabajar con los mismos.

La idea de esto es comprobar si el código que creamos es implementable en proyectos futuros, si tienes que hacer algún cambio en el código inicial del proyecto documéntalo y cuéntanos que cambios o adaptaciones tuviste que desarrollar.

## Solución

En el día se implementó una forma de imprimir las listas enlazadas con el siguiente método:

```python
def __str__(self):
    s = ""
    current = self.node
    while current:
        s += f"[{current.val}]->"
        current = current.next
    s += "[None]"
    return s
```

Al crear la lista y modificarla como sugiere en el paso dos se obtienen las siguientes salidas:

```bash
python .\main.py

[1]->[54]->[20]->[13]->[43]->[18]->[11]->[53]->[None]

[95]->[68]->[1]->[54]->[20]->[13]->[43]->[18]->[11]->[53]->[3]->[7]->[37]->[None]

Pares: [68]->[54]->[20]->[18]->[None]

Impares: [95]->[1]->[13]->[43]->[11]->[53]->[3]->[7]->[37]->[None]
```

Para obtener los números pares e impares se creó el siguiente método. En el que se define una nueva lista para los pares y otra para los impares. Luego, recorriendo la lista y bajo una condición insertamos los valores en la lista correspondiente. Finalmente, se retorna una tupla con las dos listas.

```python
def pares(L: LinkedList):
    P = LinkedList(0)
    I = LinkedList(0)

    current = L.node
    while current:
        if current.val % 2 == 0:
            P.push(current.val)
        else:
            I.push(current.val)
        current = current.next

    P.node = P.node.next
    I.node = I.node.next
    return P, I
```

## Video Explicativo

<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@crixodia/video/7151539847562333446" data-video-id="7151539847562333446" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@crixodia" href="https://www.tiktok.com/@crixodia?refer=embed">@crixodia</a> Día 9 <a title="30daysofcode" target="_blank" href="https://www.tiktok.com/tag/30daysofcode?refer=embed">#30DaysOfCode</a> <a title="30daysofcodebyaeis" target="_blank" href="https://www.tiktok.com/tag/30daysofcodebyaeis?refer=embed">#30DaysOfCodeByAEIS</a> <a title="python" target="_blank" href="https://www.tiktok.com/tag/python?refer=embed">#Python</a> <a target="_blank" title="♬ original sound - Gabriel Bastidas" href="https://www.tiktok.com/music/original-sound-7151539891745098501?refer=embed">♬ original sound - Gabriel Bastidas</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
