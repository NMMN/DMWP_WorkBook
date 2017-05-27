""" Chapter1 note """

def ex_oparation():
    """ 基本数学演算 oparation \n
        '+' '-' '*' '/'
    """
    add_value = 2 + 3
    sub_value = 2 - 3
    mult_value = 2 * 3
    div_value = 6 / 3
    print('add(2+3):{0}, sub(2-3):{1}, mult(2*3):{2}, div(6/3):{3}'.format(
        add_value, sub_value, mult_value, div_value))

def ex_flor_division():
    """ 整除除算 flor division \n
        '//'
    """
    floar_div_value_pos = 3//2
    floar_dov_value_neg = -3//2
    print("floar_div(3//2):{0}, floar_div(-3//2):{1}".format(
        floar_div_value_pos, floar_dov_value_neg
    ))

def ex_modulo():
    """ 剰余演算子 modulo \n
        '%'
    """
    mod_value = 5 % 2
    print("mod(5%2):{0}".format(mod_value))

def ex_exponetiation():
    """ 指数演算子 Exponetiation \n
        '**'
    """
    exp_value = 2**10
    print("exp(2**10):{0}".format(exp_value))

def ex_type():
    """ 型判定 type \n
        type()
    """
    int_type = type(3)
    type_type = type(type(3))
    print("Integer(3) is {0}, type() is {1}".format(int_type, type_type))

def ex_fraction():
    """ 分数 Franction \n
        from fractions import Fraction
    """
    from fractions import Fraction
    fract_value = Fraction(3, 4)
    print("Fraction(3,4):{0}".format(fract_value))

def ex_complex():
    """ 複素数 complex number \n
        use 'j' in Python
    """
    cpm_value = 2 + 3j
    cpm_real = cpm_value.real
    cpm_img = cpm_value.imag
    print("cpm:{0}, real:{1}, img:{2}".format(cpm_value, cpm_real, cpm_img))

    cpm_con = cpm_value.conjugate()
    cpm_abs = abs(cpm_value)
    print("cpm.con:{0}, abs(cpm):{1}".format(cpm_con, cpm_abs))

def ex_try_except():
    """ 例外処理 \n
        catch ValueError
    """
    try:
        input_value = float('3/4')
        print("a is Collct Number:{0}".format(input_value))
    except ValueError:
        print("Catch ValueError!")

def ex_input():
    """ 入力 \n
        input
    """
    #実行するといちいち入力を求められてしまうので、コメントアウト
    # input_value = input('input an Integer!')
    # print(input_value)
ex_input()

def ex_is_integer():
    """ 整数判定 \n
        float is Integer?
    """
    float_value = 1.1
    print("1.1 is Integer?:{0}".format(float_value.is_integer()))

def ex_for_in_range():
    """ loop \n
        for i in range(1, 10, 2)
    """
    print("for_in_range 1 to 10 add 2")
    for i in range(1, 10, 2):
        print("\t:{0}".format(i))
    print("loop end!")

""" 単位変換Tips
    1 mile = 1.609 km
    1 pond = 0.453 kg
    C = (F - 32) * ( 5 / 9)
"""


def main():
    """ def main"""
    ex_oparation()
    ex_flor_division()
    ex_modulo()
    ex_exponetiation()
    ex_type()
    ex_fraction()
    ex_complex()
    ex_try_except()
    ex_is_integer()
    ex_for_in_range()

if __name__ == '__main__':
    main()
