class Transaction:
    date = 0
    address = 0
    cleared = 0
    id_number = 0
    description = 0
    category = 0
    amount = 0
    # def __init__(self):
    #     date = 0
    #     address = 0
    #     cleared = 0
    #     id_number = 0
    #     description = 0
    #     category = 0
    #     amount = 0
    def set_date(self, date):
        self.date = date
    def get_date(self):
        return self.date
    def set_address(self, address):
        self.address = address
    def get_address(self):
        return self.address
    def set_cleared(self, cleared):
        self.amount = cleared
    def get_cleared(self):
        return self.cleared
    def set_id_number(self, id_number):
        self.amount = id_number
    def get_id_number(self):
        return self.id_number
    def set_description(self, description):
        self.amount = description
    def get_description(self):
        return self.description
    def set_category(self, category):
        self.amount = category
    def get_category(self):
        return self.category
    def set_amount(self, amount):
        self.amount = amount
    def get_amount(self):
        return self.amount
    def print_transaction(self):
        print "Date: %s" % self.date
        print "Address: %s" % self.address
        print "Cleared: %s" % self.cleared
        print "ID Number: %s" % self.id_number
        print "Description: %s" % self.description
        print "Category: %s" % self.category
        print "Amount: %s" % self.amount
