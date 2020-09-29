# coding: utf-8
# Your code here!

class Task:
    def __init__(self, priority, require, start_day, end_days):
        self.priority = priority
        self.require = require
        self.start_day = start_day
        self.end_days = end_days


def main():
    number_of_task = int(input())
    task_list = []
    for priority in range(number_of_task):
        task_list.append(Task(priority, *list(map(int, input().split()))))
    
    start_day = min([item.start_day for item in task_list])
    
    candidate_tasks = [item for item in task_list if item.start_day == start_day]
    first_priority = min([item.priority for item in candidate_tasks])
    current_task = [item for item in candidate_tasks if item.priority == first_priority][0]
    print(current_task.require, current_task.start_day, current_task.end_days)
    
    
    current_time = 0
    while True:
        current_time += 1
        priority_list = [item for item in task_list if item.start_day <= current_time if not item.require == 0]
        if priority_list:
            if current_task.priority > min([item.priority for item in priority_list]):
                current_task = [item for item in task_list if item.priority == min([item.priority for item in priority_list])][0]
        
        current_task.require -= 1
    
        
        






if __name__ == "__main__":
    main()
    

# coding: utf-8
# Your code here!

class Task:
    def __init__(self, priority, require, start_day, end_days):
        self.priority = priority
        self.require = require
        self.start_day = start_day
        self.end_days = end_days


def main():
    number_of_task = int(input())
    task_list = []
    for priority in range(number_of_task):
        task_list.append(Task(priority, *list(map(int, input().split()))))
    
    start_day = min([item.start_day for item in task_list])
    
    candidate_tasks = [item for item in task_list if item.start_day == start_day]
    first_priority = min([item.priority for item in candidate_tasks])
    current_task = [item for item in candidate_tasks if item.priority == first_priority][0]
    print(current_task.require, current_task.start_day, current_task.end_days)
    
    
    current_time = 1
    while True:
        print("============")
        print("current_time", current_time, ":", current_task.priority)
        print("before", current_task.priority, current_task.require, current_task.start_day, current_task.end_days)
        if not current_task.require == 0:
            current_task.require -= 1
        
        if current_task.require == 0:
            priority_list = [item for item in task_list if current_time >= item.start_day if not item.require == 0]
            if priority_list:
                if min([item.priority for item in priority_list]) < current_task.priority:
                    print()
                    print("change_task")
                    print(current_task.priority)
                    current_task = [item for item in task_list if item.priority == min([item.priority for item in priority_list])][0]
                    print(current_task.priority)
            priority_list = []
                
        
        if current_time == current_task.end_days:
            if current_task.require > 0:
                break
        
        
        print("after", current_task.priority, current_task.require, current_task.start_day, current_task.end_days)
        
        current_time += 1
        
        
        
        priority_list = [item for item in task_list if current_time >= item.start_day if not item.require == 0]
        
        if priority_list:
            if min([item.priority for item in priority_list]) < current_task.priority:
                print()
                print("change_task")
                print(current_task.priority)
                current_task = [item for item in task_list if item.priority == min([item.priority for item in priority_list])][0]
                print(current_task.priority)
                
        
        if current_time == 20:
            break
    
        
        






if __name__ == "__main__":
    main()
    
