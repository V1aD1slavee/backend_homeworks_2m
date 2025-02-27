class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        print(f"Cpu:{self.__cpu} + memory:{self.__memory} = {self.__cpu + self.__memory}")
        print(f"Cpu:{self.__cpu} - memory:{self.__memory} = {self.__cpu - self.__memory}")
        print(f"Cpu:{self.__cpu} * memory:{self.__memory} = {self.__cpu * self.__memory}")
        if self.__memory == 0:
            print("Ошибка: На ноль делить нельзя!")
        else:
            print(f"Cpu:{self.__cpu} / memory:{self.__memory} = {self.__cpu / self.__memory}")

    def private_metod(self):
        self.__make_computations()

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    def info(self):
        print(f"Cpu:{self.cpu}\nMemory:{self.memory}")

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"Cpu:{self.cpu}, Memory:{self.memory}, Memory card:{self.memory_card}")


objekt_1 = Computer(28,6)
objekt_1.private_metod()
objekt_1.info()


objekt_2 = Laptop(32, 64, 256)
objekt_2.private_metod
objekt_2.info()
