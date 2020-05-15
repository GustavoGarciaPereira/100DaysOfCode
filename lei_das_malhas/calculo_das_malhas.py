#calculos das malhas

#dado um conjunto com duas malhas.
#em termos simplis uma é para um programador, um conjunto de
# baterio ou qualquer finter de energia, para alimentação no sirquito

#e 


#consumo no sirquito, como eu resistencia, o que tira/gasta energia
#esses são esta pessas nosso jogo


#primeira malhas tenho
# 20v
# 4r
# 1r

#segunda malha
# 7v
# 1r
# 4r

#i1 = i2 + i3


#from sympy import linear_eq_to_matrix, symbols
#from sympy.solvers.solveset import linsolve
#x, y, z = symbols('x, y, z')



#[1x -1y -1z] = 0
#[-1x 20-4y 0z] = 0
#[7x -1-4-4y 0z] = 0


#re = linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z))
#re = linsolve([x-y-z,20-4*y+x,7+z-4*y], (x, y, z))
#print(re)



#
#         [3   2  -1  1]
#system = [2  -2   4 -2]
#         [2  -1   2  0]
#system=[3x+2y−z−1,2x−2y+4z+2,2x−y+2z]


#[1x -1y -1z] = 0
#[-1x 20-4y 0z] = 0
#[7x -1-4-4y 0z] = 0

#[x -y -z] = 0
#[-x -4y 0z] = -20
#[0x -4y z] = -7

#system=[x -y -z,-x -4y 0z -20,0x -4y z -7]


from sympy import Matrix, S, linsolve, symbols
x, y, z = symbols("x, y, z")
A = Matrix([[1,-1,-1],[-1,-4,0],[0,-4,1]])
b = Matrix([0, -20, -7])


re = linsolve((A, b), [x, y, z])
print(re)

