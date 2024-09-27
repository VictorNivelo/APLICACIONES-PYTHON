class Usuario:
    def __init__(self, id, nombre, secretarias=None):
        self.id = id
        self.nombre = nombre
        self.secretarias = secretarias if secretarias is not None else []


class Docente:
    def __init__(self, id, nombre, datos=None):
        self.id = id
        self.nombre = nombre
        self.datos = datos if datos is not None else []


class Secretaria:
    def __init__(self, id, nombre, usuario=None, informes=None):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.informes = informes if informes is not None else []


class Datos:
    def __init__(self, id, descripcion, docente=None, prediccion=None):
        self.id = id
        self.descripcion = descripcion
        self.docente = docente
        self.prediccion = prediccion


class Prediccion:
    def __init__(self, id, resultado, datos=None, informes=None):
        self.id = id
        self.resultado = resultado
        self.datos = datos if datos is not None else []
        self.informes = informes if informes is not None else []


class ListaFactor:
    def __init__(self, id, descripcion, factores=None):
        self.id = id
        self.descripcion = descripcion
        self.factores = factores if factores is not None else []


class Factor:
    def __init__(self, id, nombre, valor, lista_factor=None):
        self.id = id
        self.nombre = nombre
        self.valor = valor
        self.lista_factor = lista_factor


class Informe:
    def __init__(
        self,
        id,
        fecha,
        secretaria=None,
        prediccion=None,
        materia=None,
        ciclo=None,
        carrera=None,
    ):
        self.id = id
        self.fecha = fecha
        self.secretaria = secretaria
        self.prediccion = prediccion
        self.materia = materia
        self.ciclo = ciclo
        self.carrera = carrera


class Materia:
    def __init__(self, id, nombre, informes=None):
        self.id = id
        self.nombre = nombre
        self.informes = informes if informes is not None else []


class Ciclo:
    def __init__(self, id, nombre, informes=None):
        self.id = id
        self.nombre = nombre
        self.informes = informes if informes is not None else []


class Carrera:
    def __init__(self, id, nombre, informes=None):
        self.id = id
        self.nombre = nombre
        self.informes = informes if informes is not None else []
