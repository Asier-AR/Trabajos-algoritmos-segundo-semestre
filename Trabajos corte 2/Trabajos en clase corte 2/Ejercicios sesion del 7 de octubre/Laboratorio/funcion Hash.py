class TablaHash:
    def __init__(self, capacidad=8):
        self.cap = capacidad
        self.cubetas = [[] for _ in range(self.cap)]
        self.n=0
    def _hash(self, clave):
        h = 0
        for c in str(clave):
            h = (h * 31 + ord(c)) % self.cap
        return h
    def insertar(self, clave, valor):
        i = self._hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor          # ACTUALIZA, no duplica
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1
    def buscar(self, clave):
        i = self._hash(clave)
        for k, v in self.cubetas[i]:    # recorre SOLO esa cubeta
            if k == clave:
                return v
        return None
    def eliminar(self, clave):
        i = self._hash(clave)
        for idx, (k, _) in enumerate(self.cubetas[i]):
            if k == clave:
                self.cubetas[i].pop(idx)
                self.n -= 1
                return True
        return False
        
        #Con los 8 códigos REC-001, REC-002, REC-003, EQ-100, 
        # EQ-101, PA-007, PA-008, EST-42
        #mostrar distribución de cubetas y factor de carga
        #buscar un código y mostrar su valor
        #buscar un código que no existe y mostrar el resultado
        #actualizar un código y mostrar el resultado
        #eliminar un código y mostrar el resultado
        #distribución de cubetas y factor de carga después de eliminar 
        # un código
        # revisar si hay colisiones y mostrar la lista 
        # enlazada de esa cubeta
