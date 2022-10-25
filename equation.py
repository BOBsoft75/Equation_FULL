from random import randint as rI

def createCoef(): # Создает словарь с максимальным заданой степнью многочлена
    coef = {}
    degree = int(input("Введите максимальную степень: "))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20,20)
    return coef


def createEquation(coefEquation: dict): # Создает строку уравнение
    equation = ''
    first = True

    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'


def parseEquation(equation: str): # Разрезает готовое уравнение на словарик
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])

    return dictEquation


equation1 = createEquation(createCoef())
equation2 = createEquation(createCoef())

parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)

def summ_equation(parEq1: dict, parEq2: dict): # Сложение двух словарей уравнений
    resultEquation ={}
    for i in range(max(len(parEq1), len(parEq2)), -1, -1):
        first = parEq1.get(i)
        second = parEq2.get(i)
        if first != None or second != None:
            resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)
    return resultEquation

resultEquation = summ_equation(parEq1, parEq2)

def printEquation(equation: str):
    print(equation.replace("x^0", '').replace(" 1x", "x").replace("x^1 ", 'x '))

printEquation(f'Первый многочлен {createEquation(parEq1)}')
printEquation(f'Второй многочлен {createEquation(parEq2)}')
printEquation(f'Сумма двух многочленов {createEquation(resultEquation)}')