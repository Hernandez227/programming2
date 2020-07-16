

'''Es para checar si el alumno aprobo o reprobo'''
def grade(score):

    if score < 5:
        return 'Reprobado'
    elif score < 7:
        return 'Suficiente'
    elif score < 9:
        return 'Dominado'
    elif score < 10:
        return 'Sobresaliente'
    else:
        return 'Excelente'

def passed_subject(subject):
    '''
    Función que recibe una tupla con una asignatura y su nota y devuelve True si la asignatura está aprobada o False si está suspensa.abs
    Parámetros:
       '''
    return (subject[1] >= 5)


def apply_grade(scores):

    passed = dict(filter(passed_subject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade, passed.values())
    return dict(zip(subjects, grades))


print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))