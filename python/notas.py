def validador(text):
    while(True):
        nota = float(input(text))
        if nota < 10:
            return nota

 
nota1 = validador("nota 1: ")
nota2 = validador("nota 2: ")

print("nota 1 {}\nnota 2 {} \n\n\n\nmedia {}".format(nota1,nota2,((nota1+nota2)/2)))
