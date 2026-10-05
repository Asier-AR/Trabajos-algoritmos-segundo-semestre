1 En una cola sobre lista enlazada, saco el último elemento. ¿Qué dos referencias tengo que actualizar y por qué?

Se tiene que actualizar la cima de la cola y el final de la cola 

Esto es para evitar problemas como que el final de la cola siga apuntando a un elemento que en teoria no existe en ella y el caso de que sea solo una lista de 2 elementos entonces se actualizarian el inicio y el ultimo porque el inicio y el ultimo pasan a ser el mismo 

2 En una cola circular de capacidad cinco, el frente está en tres y hay cuatro elementos. ¿En qué posición se guarda el siguiente que encole?

El elemento quedaria en la posicion 2 ya que el frente esta en la posicion 3, ed que la lista empieza a guardar arreglos en el siguiente ornde: primero en la posicion 3, luego en la posicion 4, luego en la posicion 0, luego en la posicion 1 y por ultimo en la posicion 2


3 Quiero deshacer las últimas tres operaciones. ¿Pila o cola? ¿Por qué? 

La mejor opcion seria usar una pila, gracias a su estructura LIFO (Last In First Out), que permitiria manejar de una mejor forma el historial, ya que los ultimos elementos en entrar son los que salen

4 Quiero atender por orden de llegada. ¿Pila o cola?

Cola ya que sigue una estructura FIFO (First In First Out) que basicamente consiste en que los primeros elementos que entraron son los primeros en salir