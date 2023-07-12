from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name
        self.freebies = []
        self.companies = []
    #remember dipshit, these are lists of objects

    def add_freebie(self, new_freebie):
        self.freebies.append(new_freebie)
        self.companies.append(new_freebie.company)
        #you're already passing in freebie, which has the company information
        #classic two birds-one stone

    def received_one(self, item_name):
        has_item = False
        for freebie in self.freebies:
            if item_name == freebie.name:
                has_item = True
        return has_item
    
    def give_away(self, dev, freebie):
        if freebie.dev.name == self.name:
            freebie.dev = dev
        else:
            raise Exception("Don't give away my shit.")
    #you wanted to do freebie.dev... it HAS TO BE FREEBIE.DEV.NAME because 
    #freebie.dev is an OBJECT and you don't wanna compare obj to str