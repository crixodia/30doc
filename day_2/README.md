# Día 2: Cadenas

Un poco de contexto:
Supongamos que tenemos la siguiente cadena de caracteres que es ingresada por el usuario:

```4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^```

En esta cadena existen 5 caracteres especiales los cuales pueden ser `!@#$%^&*` y 5 números.

¿Qué deberías presentar?

1.Programa un bloque o función que retorne la cantidad de letras que existe en la cadena.
2.Programa un bloque o función que retorne la cantidad de dígitos que existe en la cadena.
3.Programa un bloque o función que retorne la cantidad de dígitos indicado por el usuario, sea mayúscula o minúscula de la cadena; es decir el usuario ingresa `^` y el programa muestra 1, esto para el ejemplo de la cadena anterior.

## Solución

Aplicamos un filtro a la cadena para cada item del problema. Luego, contamos la cantidad de elementos en cada filtro. Para ello usaremos los métodos `filter` y `len` además de los metodos para strings `isalpha` y `isdigit`. Para el tercer punto usamos una expresion lambda para filtrar los elementos que sean iguales al caracter ingresado por el usuario.

En el archivo [main.py](main.py) se encuentra el código de la solución.

## Test

```bash
pytest .\test.py -v --no-header
```

## Video Explicativo

<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@crixodia/video/7148312688291007749" data-video-id="7148312688291007749" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@crixodia" href="https://www.tiktok.com/@crixodia?refer=embed">@crixodia</a> Día 2 <a title="30daysofcode" target="_blank" href="https://www.tiktok.com/tag/30daysofcode?refer=embed">#30DaysOfCode</a> <a title="30daysofcodebyaeis" target="_blank" href="https://www.tiktok.com/tag/30daysofcodebyaeis?refer=embed">#30DaysOfCodeByAEIS</a> <a title="python" target="_blank" href="https://www.tiktok.com/tag/python?refer=embed">#Python</a> <a target="_blank" title="♬ original sound - Gabriel Bastidas" href="https://www.tiktok.com/music/original-sound-7148312754623056645?refer=embed">♬ original sound - Gabriel Bastidas</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
