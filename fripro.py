import pandas as pd

def user_input(no_ofstu):
    names = []
    scores = []

    for i in range(no_ofstu):
        print(f"\nStudent {i+1}")
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))

        names.append(name)
        scores.append(score)

    return names, scores


def score_class(scores):
    grades = []

    for item in scores:
        if 90 <= item <= 100:
            grades.append("O")
        elif 80 <= item < 90:
            grades.append("A")
        elif 70 <= item < 80:
            grades.append("B")
        elif 60 <= item < 70:
            grades.append("C")
        elif 50 <= item < 60:
            grades.append("D")
        elif 30 <= item < 50:
            grades.append("E")
        else:
            grades.append("F")

    return grades


n = int(input("Enter number of students: "))

names, scores = user_input(n)

grades = score_class(scores)

Data = {
    "Name": names,
    "Grade": grades,
    "Score": scores
}

df = pd.DataFrame(Data)

avg = df["Score"].mean()

print("\nStudent Data:\n", df)
print("\n\n\nAverage mark:", avg)

print("\nClass Toppers:\n", df[df["Score"] > avg])

df["Result"] = df["Score"].apply(lambda x: "Pass" if x >=30 else "Fail")
print("fass fail list \n", df["Result"])