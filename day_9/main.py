from linkedlist import LinkedList


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


if __name__ == "__main__":
    L = LinkedList(1)
    L.push(54)
    L.push(20)
    L.push(13)
    L.push(43)
    L.push(18)
    L.push(11)
    L.push(53)

    print(L)

    L.unshift(68)
    L.unshift(95)
    L.push(3)
    L.push(7)
    L.push(37)

    print(L)

    P, I = pares(L)
    print("Pares:", P)
    print("Impares:", I)
