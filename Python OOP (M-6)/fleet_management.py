
class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.drivers = []
        self.routes = []
        self.counter = []
        self.manager = []
        self.supervisors = []

class Driver:
    def __init__(self, name, licence) -> None:
        self.name = name
        self.licence = licence