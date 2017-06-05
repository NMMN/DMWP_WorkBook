""" Chapter1 Programming Charenge """

from prob1_1 import prob1_1 as prob1
from prob1_2 import prob1_2 as prob2
from prob1_3 import prob1_3 as prob3
from prob1_4 import prob1_4 as prob4

def prob_1_5():
    """ 1-5 ユーザに脱出機能を与える
            今まで書いてきたプログラムに対して無限ループを加え、
            ユーザが望む限り、呼び出したプログラムを繰り返せるようにする。
            * 問題で今までのプログラムを書き換えるとなっているが、
            　せっかくなので、今までかいたプログラムを呼び出して繰り返すようにした。
    """
    while 1:
        print_menu()
        try:
            user_input = input()
            if user_input == "quit":
                print("Good Bye !!")
                break
            call_method(int(user_input))

        except ValueError:
            print("Please Input Value of Number!")

def print_menu():
    """ Displaing Manu """
    print("起動するプログラムを選んでください。")
    print("1. 奇数偶数自動判定プログラム")
    print("2. 乗算表生成器")
    print("3. 距離、質量、温度変換プログラム")
    print("4. 分数電卓")
    print("\t \"quit\" プログラムの終了 ")

def call_method(mode):
    """ モードで指定されるプログラムを無限ループする """
    while 1:
        if mode == 1:
            print("奇数偶数自動判定")
            prob1()
        elif mode == 2:
            print("乗算表生成器")
            prob2()
        elif mode == 3:
            print("距離、質量、温度変換")
            prob3()
        elif mode == 4:
            print("分数電卓")
            prob4()
        else:
            # 1-4でなければ脱出
            break
        exit_input = input("continue? y , n :")
        if exit_input == 'n':
            return True

def main():
    """ def main """
    prob_1_5()


if __name__ == '__main__':
    main()
