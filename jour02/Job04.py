

class Student:
    def __init__(self, nom, prenom, studentId, level):
        self.__nom = nom 
        self.__prenom = prenom 
        self.__studentId = studentId
        self.__credits = 0  
       

    def add_credits(self, credits):
        # Ajoute du crédtis si la valeur est positive
        if credits > 0:
            self.__credits += credits
            print(f"{credits} crédits ajoutés. Total des crédits: {self.__credits}.")
        else:
            print("Erreur : Le nombre de crédits à ajouter doit être supérieur à zéro.")
    
    def studentEval(self):
        # Evaluate the student based on the number of credits
        if self.__credits >= 90:
            return "Très bien"
        elif self.__credits >= 80:
            return "Bien"
        elif self.__credits >= 70:
            return "Passable"
        elif self.__credits >= 60:
            return "Suffisant"
        else:
            return "Insuffisant"

    def studentInfo(self):
        # Print infos étudiants et évaluation
        evaluation = self.studentEval()
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"ID = {self.__studentId}") 
        print(f"Niveau = {evaluation}")

# Instance
john_doe = Student("Doe", "John", 145, "Débutant")

#  Ajouter les crédtis et imprimer le total
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

john_doe.studentInfo()
