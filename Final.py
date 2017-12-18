prompt = '> '
import math


def input_classes():

    print "What are your classes?"
    classes = raw_input(prompt)
    classes = classes.rstrip().split(", ")
    return classes


def input_grade():

    print "What are your grades? Remember to keep them in the order you typed the original list."
    grades = raw_input(prompt)
    grades = grades.rstrip().split(", ")

    return grades


def input_percentages():

    print "What are the percentages of your finals out of your total grade? Remember to keep them in the order you typed the original list."
    percentages = raw_input(prompt)
    percentages = percentages.rstrip().split(", ")

    return percentages

def input_grade_wanted():
    print "What grade do you want to acheive in all of your classes?"
    grade_wanted = raw_input(prompt)
    return grade_wanted


def solve_algebra():
    classes = input_classes()
    grades = input_grade()
    percentages = input_percentages()
    grade_wanted = input_grade_wanted()


    if len(classes) != len(grades) or len(grades) != len(percentages):
        return "The lengths don't match up. Try again"
    
    
    Grades_in_percentages = []
    for i in range(len(grades)):
        grade = int(float(grades[i]))
        grade = grade * float(0.01)
        Grades_in_percentages.append(grade)

    percent_completed = []
    for p in range(len(percentages)):
        percentage = float(int(percentages[p]))
        percentage = percentage * float(0.01)
        percent_completed.append(float(1) - percentage)


    percent_of_final = []
    for f in range(len(percentages)):
        percentage = float(int(percentages[f]))
        percentage = percentage * float(0.01)
        percent_of_final.append(percentage)

    multiplied = []
    for p in range(len(percent_completed)):
        mutiply = (percent_completed[p] * Grades_in_percentages[p])
        multiplied.append(mutiply)

    grade_wanted = float(int(grade_wanted)) * float(0.01)
    
    multiplied_and_subtracted = []
    for f in range(len(multiplied)):
        subtract = grade_wanted - multiplied[f]
        multiplied_and_subtracted.append(subtract)


    done = []
    for d in range(len(multiplied_and_subtracted)):
        divide = multiplied_and_subtracted[d] / percent_of_final[d]
        done.append(divide)



print solve_algebra()