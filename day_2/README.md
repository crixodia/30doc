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

[TikTok](https://www.tiktok.com/@crixodia/video/7148312688291007749)

## Otras soluciones

- [@el_de_men_cial](https://www.instagram.com/p/CjBqHuJrEZ0/)
- [@anthojosue05](https://www.instagram.com/p/CjCWS-RMvGs/)
