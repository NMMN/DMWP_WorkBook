""" Chapter1 Programming Charenge """

def prob1_3():
    """ 1-3 距離、質量、温度変換プログラム
            1.ユーザの入力したモード、値で単位変換を行う。
    """
    print_menu()
    mode = input('Select Convertion mode ...: ')

    if mode == '1':
        km_to_mile()
    elif mode == '2':
        mile_to_km()
    elif mode == '3':
        kg_to_pond()
    elif mode == '4':
        pond_to_kg()
    elif mode == '5':
        c_to_f()
    elif mode == '6':
        f_to_c()
    else:
        print('Your Input is Not Valid Number')

def print_menu():
    """ Displaing Manu """
    print("1. km to mile")
    print("2. mile to km")
    print("3. kg to pond")
    print("4. pond to kg")
    print("5. C to F")
    print("6. F to C")

def km_to_mile():
    """ kilometre to mile """
    km_value = float(input('Input Distance of Kilometre :'))
    mile = km_value / 1.609
    print("Distance in Miles :{0}".format(mile))

def mile_to_km():
    """ mile to kilometre """
    mile_value = float(input('Input Distance of Mile :'))
    kilometre = mile_value * 1.609
    print("Distance in Miles :{0}".format(kilometre))

def kg_to_pond():
    """ kg to pond """
    kg_value = float(input('Input Wight of kilogram :'))
    pond = kg_value / 0.453
    print("Wight in Ponds :{0}".format(pond))

def pond_to_kg():
    """ pond to kg """
    pond_value = float(input('Input Wight of pond :'))
    kilogram = pond_value * 0.453
    print("Wight in Kilogram :{0}".format(kilogram))

def c_to_f():
    """ Celsius to Fahrenheit """
    c_value = float(input('Input Temperature of C :'))
    feh_deg = (c_value / (5 / 9)) + 32
    print("Temperature in Fahrenheit :{0}".format(feh_deg))

def f_to_c():
    """ Fahrenheit to Celsius """
    f_value = float(input('Input Temperature of F :'))
    cel_deg = (f_value - 32) * (5 / 9)
    print("Temperature in Celsius :{0}".format(cel_deg))

def main():
    """ def main """
    prob1_3()

if __name__ == '__main__':
    main()
