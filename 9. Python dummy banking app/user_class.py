# Class used for user details
class User:
    def __init__(self, username, balance):
        self.id = username
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def get_username(self):
        return self.id  

    def set_new_balance(self, newBalance):
        self.balance = newBalance 