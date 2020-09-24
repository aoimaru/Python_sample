# coding: utf-8
# Your code here!
import numpy as np

def main():
    days, holidays = map(int, input().split())
    strings = []
    work_list = []
    for num in range(days):
        if input() == "work":
            strings.append(0)
            work_list.append(num)
        else:
            strings.append(1)
    
    value_list = []
    for count in range(len(work_list) - (holidays-1)):
        check = np.array([item for num, item in enumerate(work_list) if not count <= num <= count + (holidays-1)])
        if len(check) == 1:
            values = max(work_list)
        else:
            values = max(np.diff(check, n= 1))
            if count == 0:
                if values < check[0]:
                    values = check[0]
            values -= 1

        value_list.append(values)
    
    print(max(value_list))        
        
if __name__ == "__main__":
    main()
    

