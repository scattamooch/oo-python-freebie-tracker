from .freebie import Freebie

class Company:

    all_companies = []
   
    def __init__(self, name, founding):
        self.name = name
        self.founding = founding
        self.freebies = []
        self.devs = []
        Company.add_company(self)
        #when defaulting to an empty list; don't need to include in parameters

    def add_freebie(self, new_freebie):
        self.freebies.append(new_freebie)

    def add_dev(self, new_dev):
        self.devs.append(new_dev)

    def give_freebie(self, dev, item_name, value):
        f1 = Freebie(item_name, value, dev, self)
        self.add_freebie(f1)
        self.add_dev(dev)
        dev.add_freebie(f1)
        #"instance of a class" --> think OBJECT; not CLASS.notation

    @classmethod
    def add_company(cls, company):
        cls.all_companies.append(company)

    @classmethod
    def oldest_company(cls):
        oldest_company_year = cls.all_companies[0].founding
        for company in cls.all_companies:
            if oldest_company_year > company.founding:
                oldest_company_year = company.founding
        return oldest_company_year
    #make sure your return statement is in the right scope (for loop)
    #is this company's founding year greater than or less than the next?