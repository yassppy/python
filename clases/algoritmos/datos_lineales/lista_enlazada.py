class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None # Apunta al vacio

class LinkedList:
    """Estructura que gestiona el inicio y el fin de los nodos enlazados."""
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al principio de la lista."""
        new_node = Node(data)

        if self.head is None: # Escenario A: La lista está vacía
            self.head = new_node
            self.tail = new_node
        else: # Escenario B: La lista ya tiene elementos
            new_node.next = self.head
            self.head = new_node

    def search(self, target_data):
        """Busca un valor y devuelve el nodo si existe, o None si no. Complejidad: O(n)"""
        current_node = self.head  # Empezamos en la cabecera
        
        while current_node is not None:  # Mientras haya nodos que revisar
            if current_node.data == target_data:
                return current_node      # ¡Encontrado! Devolvemos el nodo completo
            current_node = current_node.next  # Avanzamos al siguiente nodo
            
        return None  # Si salimos del bucle, el elemento no existe en la lista

    def print_list(self):
        """Método auxiliar para imprimir la lista y comprobar visualmente"""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")
    
    def delete(self, value):
        """Elimina la primera coincidencia"""
        if self.head is None: 
            return
            
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None: 
                self.tail = None
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

mi_lista = LinkedList()
print("--- Prueba 1: Lista recién creada ---")
print(f"Cabecera (Head): {mi_lista.head}")
print(f"Cola (Tail): {mi_lista.tail}")

# 2. Insertamos el primer elemento (Lista Vacía originalmente)
mi_lista.insert_at_beginning(10)
print("\n--- Prueba 2: Insertamos el 10 ---")
mi_lista.print_list()
print(f"¿Quién es Head?: {mi_lista.head.data}")
print(f"¿Quién es Tail?: {mi_lista.tail.data}")

# 3. Insertamos un segundo elemento (Ya hay datos en la lista)
mi_lista.insert_at_beginning(20)
print("\n--- Prueba 3: Insertamos el 20 al inicio ---")
mi_lista.print_list()
print(f"¿Quién es el nuevo Head?: {mi_lista.head.data}")
print(f"¿Quién sigue después del Head (head.next)?: {mi_lista.head.next.data}")
print(f"¿Quién sigue siendo el Tail?: {mi_lista.tail.data}")


resultado_exito = mi_lista.search(20)
if resultado_exito:
    print(f"¡Encontrado! El nodo contiene el dato: {resultado_exito.data}")
else:
    print("No se encontró el elemento.")

mi_lista.delete(20)
mi_lista.print_list()
print(f"Head: {mi_lista.head.data}, Tail: {mi_lista.tail.data}\n")