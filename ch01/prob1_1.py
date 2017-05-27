""" Chapter1 Programming Charenge """

def prob_1_1():
    """ 1-1 奇数偶数自動判定プログラム
            1.入力された数が奇数か偶数か判定する。
            2.入力された数と、その後に9つの奇数か偶数を続けて表示する
        ・is_integer()メソッドを使って、入力が小数点の数値がある、
        　整数でない時、エラーメッセージを表示すること
    """
    input_value = input("Input Integer Num!")
    try:
        value = float(input_value)
        if value.is_integer():
            odd_or_even = "even" if value % 2 == 0 else "odd"
            print("Your input {0} is {1}".format(input_value, odd_or_even))

            for i in range(1, 10):
                print("{0} : \t{1}".format(i, value))
                value = value + 2
        else:
            print("Please Input Integer!")
    except ValueError:
        print("Please Input Value of Number!")

def main():
    """ def main """
    prob_1_1()

if __name__ == '__main__':
    main()
