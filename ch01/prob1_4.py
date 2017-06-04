""" Chapter1 Programming Charenge """

from fractions import Fraction

def prob1_4():
    """ 1-4 分数電卓  Fractional calculator
            1.２つの分数と、行いたい演算をユーザが入力する
            2.割り算を行う時、最初の分数を二つ目の分数で割ったのか、
              或いはその逆なのか、わかるように出力する。
    """
    try:
        flact_a = Fraction(input('Enter First Fraction'))
        flact_b = Fraction(input('Enter Second Fraction'))
        op_mode = input('Oparation to perform - Add, Subtract, Divide, Multiply :')

        if op_mode == 'Add':
            add(flact_a, flact_b)
        elif op_mode == 'Subtract':
            subtract(flact_a, flact_b)
        elif op_mode == 'Divide':
            divide(flact_a, flact_b)
        elif op_mode == 'Multiply':
            multiply(flact_a, flact_b)
        else:
            print('Invalid Input...')
    except BaseException:
        print('Error: {0}'.format(BaseException))

def add(flact_a, flact_b):
    """ Add Fraction A + B """
    print('Result Of Addition: {0} + {1} = {2}'.format(flact_a, flact_b, flact_a + flact_b))

def subtract(flact_a, flact_b):
    """ Subtract Fraction A + B """
    print('Result Of Subtract: {0} + {1} = {2}'.format(flact_a, flact_b, flact_a - flact_b))

def divide(flact_a, flact_b):
    """ Divide Fraction A + B """
    print('Result Of Divide: {0} + {1} = {2}'.format(flact_a, flact_b, flact_a / flact_b))

def multiply(flact_a, flact_b):
    """ Multiply Fraction A + B """
    print('Result Of Multiply: {0} + {1} = {2}'.format(flact_a, flact_b, flact_a * flact_b))

def main():
    """ def main """
    prob1_4()

if __name__ == '__main__':
    main()
