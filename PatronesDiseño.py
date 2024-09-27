from abc import ABC, abstractmethod
from typing import List


# --------- Patrón Singleton ---------
class Logger:
    """
    Implementación del patrón Singleton para un sistema de logging.

    El patrón Singleton garantiza que una clase tenga una única instancia y proporciona
    un punto de acceso global a ella. Es útil para recursos compartidos como sistemas
    de logging, pools de conexiones o caches.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_history = []
        return cls._instance

    def log(self, message: str) -> None:
        self.log_history.append(message)
        print(f"Log: {message}")

    def get_history(self) -> List[str]:
        return self.log_history


# --------- Patrón Factory ---------
class Animal(ABC):
    """
    Clase base abstracta para el patrón Factory.

    El patrón Factory Method define una interfaz para crear objetos, pero permite
    a las subclases decidir qué clase instanciar. Facilita la creación de objetos
    sin especificar la clase exacta del objeto que se creará.
    """

    @abstractmethod
    def hablar(self) -> str:
        pass


class Perro(Animal):
    def hablar(self) -> str:
        return "Guau!"


class Gato(Animal):
    def hablar(self) -> str:
        return "Miau!"


class FabricaAnimales:
    @staticmethod
    def crear_animal(tipo_animal: str) -> Animal:
        if tipo_animal.lower() == "perro":
            return Perro()
        elif tipo_animal.lower() == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal no soportado")


# --------- Patrón Observer ---------
class Sujeto:
    """
    Implementación del Sujeto en el patrón Observer.

    El patrón Observer define una dependencia uno-a-muchos entre objetos, de modo
    que cuando un objeto cambia su estado, todos sus dependientes son notificados
    y actualizados automáticamente. Es útil para implementar sistemas de eventos
    distribuidos y desacoplar componentes de software.
    """

    def __init__(self):
        self._observadores: List[Observador] = []

    def agregar(self, observador: "Observador") -> None:
        self._observadores.append(observador)

    def eliminar(self, observador: "Observador") -> None:
        self._observadores.remove(observador)

    def notificar(self, mensaje: str) -> None:
        for observador in self._observadores:
            observador.actualizar(mensaje)


class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str) -> None:
        pass


class ObservadorConcreto(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, mensaje: str) -> None:
        print(f"{self.nombre} recibió el mensaje: {mensaje}")


# --------- Patrón Decorator ---------
class Cafe(ABC):
    """
    Clase base para el patrón Decorator.

    El patrón Decorator permite añadir nuevas funcionalidades a un objeto existente
    sin alterar su estructura. Proporciona una alternativa flexible a la herencia
    para extender la funcionalidad y es útil cuando se necesita añadir responsabilidades
    a objetos de forma dinámica y transparente.
    """

    @abstractmethod
    def costo(self) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass


class CafeSimple(Cafe):
    def costo(self) -> float:
        return 1.0

    def descripcion(self) -> str:
        return "Café simple"


class DecoradorCafe(Cafe):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    def costo(self) -> float:
        return self._cafe.costo()

    def descripcion(self) -> str:
        return self._cafe.descripcion()


class DecoradorLeche(DecoradorCafe):
    def costo(self) -> float:
        return super().costo() + 0.5

    def descripcion(self) -> str:
        return f"{super().descripcion()}, leche"


class DecoradorAzucar(DecoradorCafe):
    def costo(self) -> float:
        return super().costo() + 0.2

    def descripcion(self) -> str:
        return f"{super().descripcion()}, azúcar"


# --------- Pruebas y Demostración ---------
def test_singleton():
    print("\n--- Prueba del Patrón Singleton ---")
    logger1 = Logger()
    logger2 = Logger()
    logger3 = Logger()
    print(f"¿Las instancias son iguales?: {logger1 is logger3}")

    logger1.log("Mensaje desde logger1")
    logger3.log("Mensaje desde logger2")

    print("Historial de logs:")
    for log in logger1.get_history():
        print(f"  {log}")


def test_factory():
    print("\n--- Prueba del Patrón Factory ---")
    fabrica = FabricaAnimales()

    animales = ["perro", "gato", "perro"]
    for tipo_animal in animales:
        animal = fabrica.crear_animal(tipo_animal)
        print(f"El {tipo_animal} dice: {animal.hablar()}")

    try:
        fabrica.crear_animal("elefante")
    except ValueError as e:
        print(f"Error esperado: {e}")


def test_observer():
    print("\n--- Prueba del Patrón Observer ---")
    sujeto = Sujeto()
    observador1 = ObservadorConcreto("Observador 1")
    observador2 = ObservadorConcreto("Observador 2")

    sujeto.agregar(observador1)
    sujeto.agregar(observador2)

    sujeto.notificar("Primer mensaje")
    sujeto.eliminar(observador1)
    sujeto.notificar("Segundo mensaje")


def test_decorator():
    print("\n--- Prueba del Patrón Decorator ---")
    cafe_simple = CafeSimple()
    print(
        f"Café simple - Descripción: {cafe_simple.descripcion()}, Costo: ${cafe_simple.costo():.2f}"
    )

    cafe_con_leche = DecoradorLeche(cafe_simple)
    print(
        f"Café con leche - Descripción: {cafe_con_leche.descripcion()}, Costo: ${cafe_con_leche.costo():.2f}"
    )

    cafe_completo = DecoradorAzucar(cafe_con_leche)
    print(
        f"Café completo - Descripción: {cafe_completo.descripcion()}, Costo: ${cafe_completo.costo():.2f}"
    )


def main():
    test_singleton()
    test_factory()
    test_observer()
    test_decorator()


if __name__ == "__main__":
    main()
