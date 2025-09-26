#convert from number to letter

def numerical_grade_to_letter(numerical_grade):

    if numerical_grade >= 90:
        return "A"
    elif numerical_grade >= 80:
        return "B"
    elif numerical_grade >= 70:
        return "C"
    elif numerical_grade >= 60:
        return "D"
    else:
        return "F"
