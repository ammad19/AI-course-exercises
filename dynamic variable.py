card = """
PIAIC Student Card
Roll No: 1
Name: Qasim
Father's Name: Muhammad Aslam
Course: A.I
"""
database = [[1, "Qasim", "Aslam", "A.I"],
            [2, "Mansoor", "Hussain", "CNC"],
            [3, "Ali", "Hamza", "Block Chain"]]
for r in database:
    card = """
PIAIC Student Card
Roll No: {0}
Name: {1}
Father's Name: {2}
Course: {3}
""".format(r[0],r[1],r[2],r[3])
    print(card)
    print()
