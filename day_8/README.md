# Día 8: Lista simplemente enlazada

Hola, el día de voy volveremos a las bases de la materia de Estructura de Datos y Algoritmos.
Para esto, vamos a construir una de las estructuras de datos más clásicas y que será la base para algunos retos que vienen de aquí en adelante.
Vamos a construir una Lista enlazada, recordemos que una lista enlazada tiene la siguiente forma:

![linked_list.png](linked_list.png)

En este caso la lista no está ordenada, eso lo dejaremos para más adelante 😂.

¿Qué deberías presentar?

1. Implementa una función o bloque que nos permita crear una lista enlazada, es decir, nodos, enlaces, etc. No hagas uso de las funciones propias del lenguaje que estés implementado para el reto.
2. Implementa los métodos:
    a. push: ingresa un elemento al final de la lista.
    b. pop: retira un elemento del final de la lista.
    c. shift: remueve un elemento del inicio de la lista
    d. unshift: inserta un elemento al inicio de la lista.

**Nota:** Se te otorgará puntos extras nos indicas la complejidad algorítmica de los métodos pop y shift.
**Nota:** Te recomendamos que diseñes la lista para que permita aceptar como elementos de esta algo más complejo que números.

## Solución

Para implementar una lista enlazada, primero creamos una clase nodo:

```python
class ListNode(object):
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next
```

Luego, creamos otra clase sqe será en sí la Lista Enlazada y anidaremos la clase nodo dentro de ella:

```python
class LinkedList(object):
    # ListNode won't be used out of LinkedList, so it is better to create an Inner Class
    class ListNode(object):

        def __init__(self, val, _next=None):
            self.val = val
            self.next = _next

    def __init__(self, val, next=None):
        self.node = self.ListNode(val, next)
```

### Push

Este método consiste en insertar al final de la lista enlazada, para esto, recorremos la lista hasta llegar al último nodo y le asignamos el nuevo nodo como su siguiente nodo. Este método tiene una complejidad de O(n) ya que recorre toda la lista.

```python
def push(self, val):
    if not self.node:
        self.node = self.ListNode(val)

    current = self.node
    while current.next:
        current = current.next
    current.next = self.ListNode(val)
```

### Pop

Este método consiste en eliminar el último nodo de la lista enlazada, para esto, recorremos la lista hasta llegar al penúltimo nodo y le asignamos None como su siguiente nodo. Este método tiene una complejidad de O(n) ya que recorre toda la lista.

```python
def pop(self) -> object:
    if not self.node:
        return None

    if not self.node.next:
        r = self.node.val
        self.node = None
        return r

    current = self.node
    last = current
    while current.next:
        last = current
        current = current.next

    last.next = None
    return current.val
```

### Shift

Este método consiste en eliminar el primer nodo de la lista enlazada, para esto, asignamos el siguiente nodo como el primer nodo. Este método tiene una complejidad de O(1) ya que solo accede al primer nodo.

```python
def shift(self) -> object:
    if not self.node:
        return None

    r = self.node.val
    self.node = self.node.next
    return r
```

### Unshift

Este método consiste en insertar un nodo al inicio de la lista enlazada, para esto, asignamos el nuevo nodo como el primer nodo y le asignamos el siguiente nodo como el siguiente nodo del nuevo nodo. Este método tiene una complejidad de O(1) ya que solo accede al primer nodo.

```python
def unshift(self, val) -> object:
    if not self.node:
        self.node = self.ListNode(val)

    self.node = self.ListNode(val, self.node)
```

Además como bonus, implementamos el método **str** para poder imprimir la lista enlazada:

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

La solución completa se encuentra en el archivo [main.py](main.py).

## Video Explicativo

[TikTok](https://www.tiktok.com/@crixodia/video/7151226834556964101)
