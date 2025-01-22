


class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory

    @property
    def cpu(self):
        return self.__cpu

    # Сеттер для атрибута cpu
    @cpu.setter
    def cpu(self, value: str):
        if not isinstance(value, str):
            raise ValueError("CPU должен быть строкой.")
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    #Сеттер для Memory
    @memory.setter
    def memory(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Memory должен быть положительным цел числом.")
        self.__memory = value

    def make_computations(self):
        return self.cpu * self.memory

    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    def __eq__(self, other):
        return self.memory == other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        if not isinstance(value, list):
            raise ValueError("sim_cards_list должен быть списком")
        self.__sim_cards_list = value


    def call(self, sim_card_number: int ,call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(
                f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}")
        else:
            print("Неверный номер сим-карты.")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: str, memory: int, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод для симуляции использования GPS
    def use_gps(self, location: str):
        print(f"Построение маршрута до {location}...")

    # Переопределение __str__
    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


computer = Computer("Intel i7", 4)
phone = Phone(["!O", "Megacom"])
smartphone1 = SmartPhone("APPLE IPHONE 11", 2, ["Beeline", "Tele2"])
smartphone2 = SmartPhone("XIAOMI POCO X6", 12, ["MTS", "Yota"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())
phone.call(1, "+996 553 80 07 61")
smartphone1.use_gps("Бишкек")

print(computer == smartphone1)




