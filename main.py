"""
  ID_calle NOMBRE_calle N_INTERSECCIONES -> calles
  id-id_calle--nombre_calle-id_ogn---id_dest-dst-vel-costo-???-cost_inv-????????-coordenadas(x,y) -> intersecciones
  
  Formato coordenadas (LAT,LON) (y,x)
  Origen -> -12.0459308;-77.0427831
  Destino -> -12.0460958;-77.0430896
"""
import math


class Nodo:
    def __init__(self, id, nombre, intersecciones) -> None:
        self.id = id
        self.nombre = nombre
        self.cantidad_intersecciones = intersecciones
        self.intersecciones = []

    def agregarInterseccion(self, interseccion) -> None:
        self.intersecciones.append(
            {
                "data": interseccion,
            }
        )

    def mostrarNodo(self):
        print(self.id, self.nombre, self.cantidad_intersecciones)
        for interseccion in self.intersecciones:
            print(interseccion)


class Grafo:
    def __init__(self, calles, intersecciones):
        self.calles = calles
        self.intersecciones = intersecciones
        self.Ciudad = []
        self.generar_grafo()

    def generar_grafo(self):
        interseccion_actual = 0
        for (id, nombre, n_intersecciones) in self.calles:
            nodo = Nodo(id, nombre, n_intersecciones)
            for i in range(interseccion_actual, interseccion_actual + n_intersecciones):
                nodo.agregarInterseccion(self.intersecciones[i])
            interseccion_actual += n_intersecciones
            self.agregarNodo(nodo)

    def agregarNodo(self, nodo):
        self.Ciudad.append(nodo)

    def getCiudad(self):
        return self.Ciudad


def obtener_formato_calles(lista, data):
    lista.append((int(data[0]), data[1], int(data[2])))


def leer_archivo_calles(archivo, formatear_calles):
    with open(archivo, "r", encoding="utf-8-sig") as f:
        lista = []
        for linea in f:
            data = linea.strip().split(";")
            formatear_calles(lista, data)
    return lista


def leer_archivo_intersecciones(archivo, formatear_intersecciones, hora):
    with open(archivo, "r", encoding="utf-8-sig") as f:
        lista = []
        for linea in f:
            data = linea.strip().split(";")
            formatear_intersecciones(lista, data, hora)
    return lista


def obtener_formato_intersecciones(lista, data, hora):

    lista.append(
        (  # item
            int(data[0]),
            # Id de la calle
            int(data[1]),
            # Nombre de la calle
            data[2],
            # Id de la calle Origen
            int(data[3]),
            # Id de la calle final
            int(data[4]),
            # Id origen Intersección
            int(data[5]),
            # Id destino Intersección
            int(data[6]),
            # Distancia en Km/h entre Id origen de la intersección/ Id destino de la intersección
            float(data[7]),
            # Velocidad km/h permitida
            int(data[8]),
            # Costo 1
            float(data[9]),
            # Costo 2
            float(data[10]),
            # Latitud de 6
            float(data[11]),
            # Longitud de 6
            float(data[12]),
            # Latitud de 7
            float(data[13]),
            # Longitud de 7
            float(data[14]),
            # Costo 1 modificado: (Distancia(km)/velocidad(km/h))*3
            (float(data[6]) / float(data[7])) * 3,
            # Costo 2 modificado: (Distancia entre 2 puntos x1000000)= raiz[ (latitud1-latitud2)^2+(longitud1-longitud2)^2]X1000000
            (
                (math.sqrt((float(data[11]) - float(data[13])) ** 2 + (float(data[12]) - float(data[14])) ** 2))
                * 1000000
            ),
            # Costo Factor trafico:Distancia(km)*650000/velocidad((100-h)/100)
            float(data[7]) * 650000 / (int(data[8]) * ((100 - hora) / 100)),
        )
    )


calles = leer_archivo_calles("assets/Lima-calles.csv", obtener_formato_calles)
hora = int(input("Digite la hora: "))
intersecciones = leer_archivo_intersecciones("assets/Lima-intersecciones.csv", obtener_formato_intersecciones, hora)

Graph = Grafo(calles, intersecciones)

Ciudad = Graph.getCiudad()

limiteCalles = 10
contador = 0
for nodo in Ciudad:
    if contador < limiteCalles:
        nodo.mostrarNodo()
        contador += 1
        print("\n--------------------------------------------------------------------------------------------")
    else:
        break
