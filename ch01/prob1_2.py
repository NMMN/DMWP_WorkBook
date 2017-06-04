""" Chapter1 Programming Charenge """

def prob1_2():
    """ 1-2 乗算表生成器  Multiplication Table Priniter
            1.ユーザの入力した数の乗算した値を出力する。
            2.表示する数もユーザの入力により決定すること
        例えば、'9'の定数を'15'個表示したい。
        memo: 数値に対する例外処理を入れてみても良いかもしれない。
              課題に含まれていないが、メモとして残しておく。
    """
    input_multi = int(input("Input Multiplication Num :"))
    input_count = int(input("How many times multiple? :"))

    for i in range(1, input_count):
        print("{0} * {1} = {2}".format(input_multi, i, input_multi*i))

def main():
    """ def main """
    prob1_2()

if __name__ == '__main__':
    main()
