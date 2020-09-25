# coding: utf-8
# Your code here!

def judge(number):
    def digit(check_num , number):
        if int(check_num) > number:
            return 0
        
        if all(check_num.count(digit_num) > 0 for digit_num in "753"):
            print("dp:",check_num)
            count = 1
        else:
            print("no_dp:",check_num)
            count = 0
        
        for add_num in "753":
            count = count + digit(check_num + add_num , number)
            print("conut:{},add_num:{}".format(count,add_num))
        return count
        
    print(digit("0",number))

def main():
    number = int(input())
    judge(number)
    
if __name__ == "__main__":
    main()

input
575

output    
no_dp: 0
no_dp: 07
no_dp: 077
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:7
no_dp: 075
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:5
no_dp: 073
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:3
conut:0,add_num:7
no_dp: 05
no_dp: 057
conut:0,add_num:7
no_dp: 0575
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:5
dp: 0573
conut:1,add_num:7
conut:1,add_num:5
conut:1,add_num:3
conut:1,add_num:3
conut:1,add_num:7
no_dp: 055
no_dp: 0557
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:7
no_dp: 0555
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:5
no_dp: 0553
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:3
conut:1,add_num:5
no_dp: 053
dp: 0537
conut:1,add_num:7
conut:1,add_num:5
conut:1,add_num:3
conut:1,add_num:7
no_dp: 0535
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:1,add_num:5
no_dp: 0533
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:1,add_num:3
conut:2,add_num:3
conut:2,add_num:5
no_dp: 03
no_dp: 037
no_dp: 0377
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:7
dp: 0375
conut:1,add_num:7
conut:1,add_num:5
conut:1,add_num:3
conut:1,add_num:5
no_dp: 0373
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:1,add_num:3
conut:1,add_num:7
no_dp: 035
dp: 0357
conut:1,add_num:7
conut:1,add_num:5
conut:1,add_num:3
conut:1,add_num:7
no_dp: 0355
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:1,add_num:5
no_dp: 0353
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:1,add_num:3
conut:2,add_num:5
no_dp: 033
no_dp: 0337
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:7
no_dp: 0335
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:5
no_dp: 0333
conut:0,add_num:7
conut:0,add_num:5
conut:0,add_num:3
conut:0,add_num:3
conut:2,add_num:3
conut:4,add_num:3
4
