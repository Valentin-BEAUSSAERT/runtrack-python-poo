class Operation:

    def __init__(self):
        self.number1 = 12
        self.number2 = 3
    
    def afficher(self):
        print(f"Le nombre 1 est {self.number1}")
        print(f"le nombre 2 est {self.number2}")

        
operation = Operation()
operation.afficher()
