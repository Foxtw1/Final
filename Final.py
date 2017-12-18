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
    
    
