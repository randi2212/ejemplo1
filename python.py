print("1 para sueldo, 2 para division")
x = int(input())

if x==1:
    print("codigo")
    c= input()
    print("nombre")
    n= input()
    print("apellido")
    a= input()
    print("sueldo base")
    sb= float(input())
    print("bonificacion")
    b= float(input())
    print("horas extra")
    h= float(input())
    print("descuentos")
    d= float(input())
    igss= sb * 0.0483
    hx = sb/30/8 * h
    ti= sb + b +hx
    td= d + igss
    sl= ti-td
    print("///")
    print("///")
    print("codigo: ", c)
    print("nombre completo :", n,a)
    print("///")
    print("total ingresos Q",ti)
    print("total descuentos Q",td)
    print("total liquido Q",sl)
elif x==2:
    print("en proceso")
   
