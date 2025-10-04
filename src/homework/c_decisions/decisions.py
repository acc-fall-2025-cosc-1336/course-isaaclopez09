#convert from number to letter

def get_letter_grade(numerical_grade):

    letter_grade = ""

    if (numerical_grade > 100 and numerical_grade < 0):
        return ("Grade must be between 0 and 100")
    
    elif (numerical_grade >= 90 and numerical_grade <=100):
        letter_grade = "A"
    
    elif(numerical_grade >= 80 and numerical_grade <=89):
        letter_grade = "B"
    
    elif (numerical_grade >= 70 and numerical_grade <=79):
        letter_grade = "C"
    
    elif (numerical_grade >= 60 and numerical_grade <=69):
        letter_grade = "D"
    
    else:
        letter_grade = "F"
        
    return letter_grade
