'''
    one-dimensional, deterministic context-free Lindenmayer-System (D0L-System)
    Prajakta Bhujbal - 3302943
    '''

variable1= 'C'
variable2 = 'A'
axiom = 'C'
C = 'A'
A = 'CA'
iter = 10
final_string = ''
substitute = ''

for i in range(iter):
    if i == 0:
        final_string = axiom
        print(final_string)
    output = ''
    for j in range(len(final_string)):
        temp = final_string[j]
        if (temp == 'C'):
            substitute = C
        else:
            substitute = A
        output = output + substitute
    final_string = ''
    final_string = final_string + output
    print(final_string)
