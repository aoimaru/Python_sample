# coding: utf-8
# Your code here!

class Prioy:
    def __init__(self, priority, require_days, start_day, end_days):
        self.priority = priority
        self.require_days = require_days
        self.start_day = start_day
        self.end_days = end_days
    
    def rest_days(self, done_days):
        print(self.rest_days)

def main():
    number_of_task = int(input())
    informations = []
    for priority in range(number_of_task):
        informations.append(Prioy(priority, *list(map(int, input().split()))))
    
    for information in informations:
        print(information.priority, information.require_days, information.start_day, information.end_days)
    
    
    start_days = sorted([item.start_day for item in informations])
    print(start_days)
    
    current_day = 0
    while True:
        current_day += 1
        if current_day in start_days:
            
            
            
            break
        


if __name__ == "__main__":
    main()
    

