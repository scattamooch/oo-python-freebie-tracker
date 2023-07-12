
class Freebie:
    
    def __init__(self, name, value, dev, company):
        self.name = name
        self.value = value
        self.dev = dev
        self.company = company

    def print_details(self):
        print(f"{self.dev.name} owns a {self.name} from {self.company.name}")