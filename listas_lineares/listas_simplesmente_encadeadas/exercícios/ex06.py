def dividir_lista(head):

    low = fast = head

    while fast is not None and fast.next is not None:

        fast = fast.next.next
        low = low.next

    h1 = head
    h2 = low.next
    low.next = None

    return h1, h2