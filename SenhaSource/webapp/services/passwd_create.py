from random import choice
import string

class Passwd:
    
    def __init__(self) -> None:
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation


    def create(
        self, length=12, char=True, number=True, punctuation=True) -> str:
        valores = self.digits + self.letters + self.punctuation
        passwd = ''

        for _ in range (length):
            passwd += choice(valores)
        
        return passwd