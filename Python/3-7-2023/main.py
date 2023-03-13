class Artificial_Input:

    def __init__(self):

        self.Holding = [];
        self.Reading = 0;

        self.Production = False;

    def add_input(self, new_input, split_lines=True):

        Appending = None;

        if type(new_input) is str and split_lines:

            Appending = new_input.split("\n");

        elif type(new_input) is list:

            Appending = new_input;

        else:

            raise Exception("Given value is not a string or list!")

        self.Holding += Appending;

    def read(self):

        if not self.Production:

            Returning = self.Holding[self.Reading];
            self.Reading += 1;

            return Returning;
        
        else:

            return input();

Custom_Input = Artificial_Input();

Custom_Input.Production = True;

Custom_Input.add_input('''Klasa 1A
Pawel Nowak 5,5,5
Albert Blaziak 4,4,4,4,4,4,4,4,4,4,4
Klasa 1B
Jakub Leszcz 3,3,3,6
Mateusz Kozlowski 6,5,2,4,3
koniec''')

Raw_Info = [];

while True:

    Read = Custom_Input.read()

    if Read == 'koniec': break

    Raw_Info.append(Read)

Processed = {}
Current_Class = None;

for v in Raw_Info:

    if 'Klasa' in v:

        Processed[v] = {}
        Current_Class = v

    else:

        Split = v.split(' ')

        Full_Name, Raw_Grades = f"{Split[0]} {Split[1]}", Split[2]
        Grades = [];

        for Grade in Raw_Grades.split(','):

            Grades.append(int(Grade))

        Total = 0

        for v in Grades:

            Total += v

        Avg_Grade = Total/len(Grades)

        Processed.get(Current_Class)[Full_Name] = Avg_Grade

for Class in Processed:

    print(Class)

    Students = Processed.get(Class)
    Total = 0

    Largest = None

    for Student in Students:

        Avg_Grade = Students.get(Student)
        Total += Avg_Grade

        print(Student, Avg_Grade)

        if not Largest:

            Largest = [Avg_Grade, Student]
            continue

        if Avg_Grade > Largest[0]:

            Largest = [Avg_Grade, Student]

    Avg_Class = Total/len(Students)
    
    print(f"Srednia Klasy: {Avg_Class}")
    print(f"Najlepszy uczen: {Largest[1]}")