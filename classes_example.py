class Train():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def open_seats(self):
        return self.capacity - len(self.passengers)
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

hogwarts = Train(3)
students = ["Harry", "Ron", "Hermione", "Draco"]
for student in students:
    if hogwarts.add_passengers(student):
        print(f"Welcome aboard, {student}")
    else:
        print(f"You did not make it, Sorry {student}")






    

