# Codecademy py lists project - Gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
#gradebook = [subjects, grades]

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][-1]=98    #change grade in gradebook

gradebook[2].remove(gradebook[2][1])
gradebook[2].append("Pass")

full_gradebook = (last_semester_gradebook + gradebook)
print(full_gradebook,sep="\n")
