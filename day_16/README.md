# Día 16: Hill 2

Bienvenido al reto número 16, el día de hoy vamos a completar el reto de cifrado de Hill, para esto vamos a realizar el proceso inverso. Es decir, le daremos a nuestro bloque o función un texto encriptado y una matriz, con la finalidad de producir el texto en claro.

¿Qué deberías presentar?

- Un bloque o función que reciba como parámetros un texto encriptado y una matriz para producir un texto claro, es decir una función que desencripte el mensaje.
- [OPCIONAL] Comprueba si el método de entrega que planteaste en la solución anterior serviría para compartir mensajes de manera totalmente secreta

## Solución

Para desencriptar el mensaje, debemos obtener la matriz inversa de la matriz de encriptación, para ello usamos la función `inv` de numpy.

```python
def unhill(C, key, symb):
    n = int(np.sqrt(len(key)))

    K = map(lambda c: symb.index(c), key)
    K = np.array(list(K)).reshape(n, n)
    K = np.linalg.inv(K)  # Inversa

    M = np.dot(K, C)
    M = np.mod(M.round(5), 26)
    M = M.flatten().astype(int)

    M = "".join(map(lambda c: symb[c], M.tolist()))
    return M
```

## Otras soluciones

- [@el_de_men_cial](https://www.instagram.com/p/Cj4rktrutnU/)
- [@jamenajamena173](https://www.instagram.com/p/Cj11nxOtn8x/)
