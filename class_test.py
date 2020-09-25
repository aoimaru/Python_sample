import sys

class Node:
    def __init__(self,number,comp,value):
        self.number = number
        self.comp = comp
        self.value = value

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    Tree = []
    
    for i, v in enumerate(lines):
        if i == 0:
            number_of_village, number_of_question = map(int,v.split())
            print(number_of_village, number_of_question)

            number_list = [0] * number_of_village
        else:
            person_1, person_2, value = map(int, v.split())
            Tree.append(Node(person_2, person_1 , value))
    
    for num,group in enumerate(number_list):
        for tree in Tree:
            if not num == tree.number:
                number_list[group] = -1
            else:
                comp_value = tree.comp
                break_flag = 0
                while True:
                    if break_flag == 1:
                        break
                    for tree_2 in Tree:
                        if not comp_value == tree_2.number:
                            break_flag = 1
                        else:
                            comp_value = tree_2.number
                print(comp_value)
            

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)



import sys

class Node:
    def __init__(self,number,comp,value):
        self.number = number
        self.comp = comp
        self.value = value

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    Tree = []
    
    for i, v in enumerate(lines):
        if i == 0:
            number_of_village, number_of_question = map(int,v.split())
            # print(number_of_village, number_of_question)

            number_list = [0] * number_of_village
        else:
            person_1, person_2, value = map(int, v.split())
            Tree.append(Node(person_2, person_1 , value))
    
    for num,group in enumerate(number_list):
        not_flag = 0
        for tree in Tree:
            if not num == tree.number:
                number_list[group] = -1
                break
            else:
                comp_name = tree.comp
                comp_value = tree.comp
                break_flag = 0
                while True:
                    if break_flag == 1:
                        break
                    for tree_2 in Tree:
                        if not comp_value == tree_2.number:
                            break_flag = 1
                        else:
                            if not tree_2.number == comp_name:
                                comp_value = tree_2.number
                            else:
                                not_flag = 1
                                break_flag = 1
                                break
                # print(comp_value)
    
                if not_flag == 1:
                    print(-1)
                    break
                else:
                    number_list[num] = comp_value - 1
                    print(number_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


import sys

class Node:
    def __init__(self,number,comp,value):
        self.number = number
        self.comp = comp
        self.value = value

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    Tree = []
    
    for i, v in enumerate(lines):
        if i == 0:
            number_of_village, number_of_question = map(int,v.split())
            # print(number_of_village, number_of_question)

            number_list = [0] * number_of_village
        else:
            person_1, person_2, value = map(int, v.split())
            Tree.append(Node(person_2, person_1 , value))
    
    for num,group in enumerate(number_list):
        not_flag = 0
        for tree in Tree:
            if not num == tree.number:
                number_list[group] = -1
                break
            else:
                comp_name = tree.comp
                comp_value = tree.comp
                value = 0
                break_flag = 0
                while True:
                    if break_flag == 1:
                        break
                    for tree_2 in Tree:
                        if not comp_value == tree_2.number:
                            break_flag = 1
                        else:
                            if not tree_2.number == comp_name:
                                comp_value = tree_2.number
                                value -= comp_value
                                print(value)
                            else:
                                not_flag = 1
                                break_flag = 1
                                break
                # print(comp_value)
    
                if not_flag == 1:
                    print(-1)
                    break
                else:
                    number_list[num] = value
                    print(number_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
