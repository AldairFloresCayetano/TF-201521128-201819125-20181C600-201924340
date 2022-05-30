"""
  ID_calle NOMBRE_calle N_INTERSECCIONES -> calles
  id-id_calle--nombre_calle-id_ogn---id_dest-dst-vel-costo-???-cost_inv-????????-coordenadas(x,y) -> intersecciones
  
  Formato coordenadas (LAT,LON) (y,x)
  Origen -> -12.0459308;-77.0427831
  Destino -> -12.0460958;-77.0430896
"""


class Nodo:
    def __init__(self, id, nombre, intersecciones) -> None:
        self.id = id
        self.nombre = nombre
        self.cantidad_intersecciones = intersecciones
        self.intersecciones = []

    def agregarInterseccion(self, interseccion) -> None:
        # self.intersecciones.append( ( nodoDestino, peso ) )
        self.intersecciones.append(
            {
                "data": interseccion,
            }
        )


class Grafo:
    def __init__(self, calles, intersecciones):
        self.calles = calles
        self.intersecciones = intersecciones
        self.G = []

    def generar_grafo(self):
        interseccion_actual = 0
        for (id, nombre, n_intersecciones) in self.calles.split(";"):
            nodo = Nodo(id, nombre, n_intersecciones)
            for i in range(interseccion_actual, interseccion_actual + n_intersecciones):
                nodo.agregarInterseccion(self.intersecciones[i])
            interseccion_actual += n_intersecciones
            self.agregarNodo(self, nodo)

    def agregarNodo(self, nodo):
        self.G.append(nodo)


# Crear una funcion para leer un archivo csv y devolver una lista de tuplas con los datos de cada linea
def leer_archivo_formato(archivo, formato):
    with open(archivo, "r", encoding="utf-8-sig") as f:
        lista = []
        for linea in f:
            # if linea.find("\"") != -1
            data = linea.strip().split(";")
            formato(lista, data)
    return lista


def obtener_formato_calles(lista, data):
    lista.append((int(data[0]), data[1], int(data[2])))


def obtener_formato_intersecciones(lista, data):
    lista.append(
        (
            int(data[0]),
            int(data[1]),
            data[2],
            int(data[3]),
            int(data[4]),
            int(data[5]),
            int(data[6]),
            float(data[7]),
            int(data[8]),
            float(data[9]),
            float(data[10]),
        )
    )


calles = leer_archivo_formato("assets/Lima-calles.csv", obtener_formato_calles)
print(calles)

# intersecciones = leer_archivo_formato("assets/Lima-intersecciones.csv", obtener_formato_intersecciones)
# print(intersecciones)

# Graph = Grafo(calles, intersecciones)

# print(Graph)
