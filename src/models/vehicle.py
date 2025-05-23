# models/vehicle.py

class Vehicle:
    def __init__(self, id, capacity, range, fuel_efficiency, speed, fuel_capacity, available=0):
        """
        Classe que representa um veículo.

        :param id: Identificador único do veículo.
        :param capacity: Capacidade máxima de carga (em unidades de peso/volume).
        :param range: Autonomia máxima do veículo (em quilómetros).
        :param fuel_efficiency: Consumo de combustível por quilómetro.
        :param speed: Velocidade do veículo (km/h).
        :param fuel_capacity: Capacidade máxima de combustível.
        :param available: Número de unidades disponíveis deste tipo de veículo.
        """
        self.id = id
        self.capacity = capacity
        self.range = range
        self.fuel_efficiency = fuel_efficiency
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.current_load = 0
        self.current_fuel = fuel_capacity  # Inicializado com tanque cheio
        self.available = available  # Número de unidades disponíveis

    def load_cargo(self, amount):
        """
        Carrega o veículo com uma quantidade específica de carga.

        :param amount: Quantidade a carregar.
        """
        if self.current_load + amount > self.capacity:
            raise ValueError("Carga excede a capacidade do veículo.")
        self.current_load += amount

    def get_cargo(self, amount):
        """
        Remove carga do veículo.

        :param amount: Quantidade a descarregar.
        """
        if amount > self.current_load:
            raise ValueError("Quantidade a remover excede a carga atual.")
        self.current_load -= amount

    def load_fuel(self, amount):
        """
        Abastece o veículo com uma quantidade específica de combustível.

        :param amount: Quantidade de combustível a adicionar.
        """
        if self.current_fuel + amount > self.fuel_capacity:
            raise ValueError("Quantidade excede a capacidade máxima de combustível.")
        self.current_fuel += amount

    def __repr__(self):
        return (f"Vehicle(id={self.id}, capacity={self.capacity}, range={self.range}, "
                f"fuel_efficiency={self.fuel_efficiency}, speed={self.speed}, "
                f"fuel_capacity={self.fuel_capacity}, available={self.available}, "
                f"current_load={self.current_load}, current_fuel={self.current_fuel})")


class Car(Vehicle):
    def __init__(self, id, available=20):
        super().__init__(id, capacity=100000, range=400, fuel_efficiency=0.05, speed=60, fuel_capacity=200, available=available)


class Helicopter(Vehicle):
    def __init__(self, id, available=15):
        super().__init__(id, capacity=50000, range=300, fuel_efficiency=0.25, speed=150, fuel_capacity=75, available=available)


class Truck(Vehicle):
    def __init__(self, id, available=25):
        super().__init__(id, capacity=500000, range=600, fuel_efficiency=0.5, speed=40, fuel_capacity=300, available=available)
