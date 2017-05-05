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
ex_oparation()

def ex_flor_division():
    """ 整除除算 flor division \n
        '//'
    """
    floar_div_value_pos = 3//2
    floar_dov_value_neg = -3//2
    print("floar_div(3//2):{0}, floar_div(-3//2):{1}".format(
        floar_div_value_pos, floar_dov_value_neg
    ))
ex_flor_division()

def ex_modulo():
    """ 剰余演算子 modulo \n
        '%'
    """
    mod_value = 5 % 2
    print("mod(5%2):{0}".format(mod_value))
ex_modulo()

def ex_exponetiation():
    """ 指数演算子 Exponetiation \n
        '**'
    """
    exp_value = 2**10
    print("exp(2**10):{0}".format(exp_value))
ex_exponetiation()

def ex_type():
    """ 型判定 type \n
        type()
    """
    int_type = type(3)
    type_type = type(type(3))
    print("Integer(3) is {0}, type() is {1}".format(int_type, type_type))
ex_type()

def ex_fraction():
    """ 分数 Franction \n
        from fractions import Fraction
    """
    from fractions import Fraction
    fract_value = Fraction(3, 4)
    print("Fraction(3,4):{0}".format(fract_value))
ex_fraction()

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
ex_complex()

def try_except_input():
    """ 例外処理と入力 \n
        catch ValueError
    """
    try:
        input_value = input()
    except expression as identifier:
        pass



