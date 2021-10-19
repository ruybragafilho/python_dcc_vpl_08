from functools import reduce


def delInitials(L):
    """Esta funcao recebe uma lista de strings L, e retorna uma string S.
    S contem os elementos de L que possuem mais de um caracter, sempre com a
    primeira letra maiuscula. Ex.:
    delInitials(['Fer', 'mag', 'Q', 'pereira']) = 'Fer, Mag, Pereira'
    """        
    AUX = [ s[0].upper() + s[1:] for s in L if len(s) > 1 ]   
    return  reduce( lambda acc, si: acc + ", " + si, AUX[1:], AUX[0] )
    
    

def everyOccurrence(S, Q):
    """Esta funcao retorna uma lista L formada pelos indices de caracteres na
    string S que existem tambem na string Q. Ex.:
    everyOccurrence('Fernando', 'abcde') == [1, 4, 6]
    everyOccurrence('xaxbxaxyza', 'abcde') == [1, 3, 5, 9]
    Para resolver esse exercicio, voce pode usar a funcao enumerate, ex.:
    [(a, b) for a, b in enumerate('abc')] == [(0, 'a'), (1, 'b'), (2, 'c')]
    Outra dica eh usar combinacoes de 'for' em compreencoes de lista, ex.:
    [(a, b) for a in 'xyz' for b in [1, 2]] ==
    [('x', 1), ('x', 2), ('y', 1), ('y', 2), ('z', 1), ('z', 2)]
    """
    #return [index for index, element in enumerate(S) if element in Q]
    LCHAR = [ c for c in S if c in Q ]
    LENUM = [ (a, b) for a, b in enumerate( S ) ]    
    return [ i[0] for i in LENUM if i[1] in LCHAR ]    
    

 
def factors(N):
    """Retorna uma lista com os divisores do numero N, exceto 1 e N.
    Exemplos:
    factors(6) == [2, 3]
    factors(10) == [2, 5]
    factors(12) == [2, 3, 4, 6]
    factors(28) == [2, 4, 7, 14]
    """    
    return [ d for d in range( 2, int(N/2) + 1 ) if N%d == 0 ] 


import operator
def isPerfect(N):
    """N eh perfeito se a soma de seus fatores (exceto ele mesmo) eh N.
    obs.: se for utilizar "factors" para resolver esse exercicio, lembre-se,
    que aquela funcao nao retorna o '1' como fator.
    Exemplos:
    isPerfect(6) == True
    isPerfect(10) == False
    isPerfect(12) == False
    isPerfect(28) == True
    """    
    return N == reduce( lambda acc, n: acc + n, factors(N), 1 )




print("\n\n")

L = ['Fer', 'mag', 'Q', 'pereira']
print( "delInitials: ", delInitials(L) )

print( "\neveryOccurrence: ", everyOccurrence('xaxbxaxyza', 'abcde') )
print( "everyOccurrence: ", everyOccurrence('Fernando', 'abcde') )

print( "\nFactors: ", factors(6) )
print( "Factors: ", factors(10) )
print( "Factors: ", factors(12) )
print( "Factors: ", factors(28) )

print( "\nisPerfect: ", isPerfect(6) )
print( "isPerfect: ", isPerfect(10) )
print( "isPerfect: ", isPerfect(12) )
print( "isPerfect: ", isPerfect(28) )



print("\n\n")