# coding: utf-8
# Your code here!


def main():
    number_of_people, nubmer_of_interview = map(int, input().split())
    
    age_list = [-1 for _ in range(number_of_people+1)]
    
    print(age_list)
    
    youngest = 0
    
    contradiction = 0
    
    for count in range(nubmer_of_interview):
        do, done, difference = map(int, input().split())
        if count == 0:
            if difference > 0:
                age_list[do] = youngest
                age_list[done] = youngest + difference
            elif difference == 0:
                age_list[do] = youngest
                age_list[done] = youngest
            else:
                age_list[do] = youngest
                age_list[done] = youngest
        
        else:
            if not age_list[do] == -1:
                if difference > 0:
                    if age_list[done] == -1:
                        age_list[done] = age_list[do] + difference
                    else:
                        if do > done:
                            contradiction = 1
                            break
                elif difference == 0:
                    if age_list[done] == -1:
                        comp = age_list[do]
                        age_list[done] = comp
                    
                    else:
                        if not do == done:
                            contradiction = 1
                            break
                else:
                    if age_list[done] == -1:
                        comp_age = age_list[do] + difference
                        if comp_age < 0:
                            youngest = 0
                            age_list[done] = 0
                            age_list = [item - comp_age for number, item in enumerate(age_list) if not item == -1 if not number == done]
                        else:
                            if comp_age >= youngest:
                                age_list[done] = age_list[do] + difference
                            else:
                                youngest = comp_age
                                age_list[done] = comp_age
                     
                    
                    
                    comp_age = age_list[do] + difference
                    if comp_age < 0:
                        youngest = 0
                        age_list = [item-comp_age for item in age_list if not item == -1]
                    else:
                        if comp_age >= youngest:
                            age_list[done] = age_list[do] + difference
                        else:
                            youngest = comp_age
                            age_list[done] = comp_age
            else:
                # if difference > 0:
                #     if do < done:
                #         contradiction = 1
                #         break
                #     else:
                        
                        
                        
                        
                        
                        
                        
                # elif difference == 0:
                #     if not do == done:
                #         contradiction = 1
                # else:
                #     if do > done:
                #         contradiction = 1
                        
        
        print(age_list)
                            




if __name__ == "__main__":
    main()



# coding: utf-8
# Your code here!


def main():
    number_of_people, nubmer_of_interview = map(int, input().split())
    
    age_list = [-1 for _ in range(number_of_people+1)]
    
    
    youngest = 0
    
    contradiction = 0
    
    for count in range(nubmer_of_interview):
        do, done, difference = map(int, input().split())
        if count == 0:
            if difference > 0:
                age_list[do] = youngest
                age_list[done] = youngest + difference
            elif difference == 0:
                age_list[do] = youngest
                age_list[done] = youngest
            else:
                age_list[do] = youngest
                age_list[done] = youngest
        
        else:
            if not age_list[do] == -1:
                if difference > 0:
                    if age_list[done] == -1:
                        age_list[done] = age_list[do] + difference
                    else:
                        if do > done:
                            contradiction = 1
                            break
                elif difference == 0:
                    if age_list[done] == -1:
                        comp = age_list[do]
                        age_list[done] = comp
                    
                    else:
                        if not do == done:
                            contradiction = 1
                            break
                else:
                    if age_list[done] == -1:
                        comp_age = age_list[do] + difference
                        if comp_age < 0:
                            youngest = 0
                            age_list[done] = 0
                            age_list = [item - comp_age for number, item in enumerate(age_list) if not item == -1 if not number == done]
                        else:
                            if comp_age >= youngest:
                                age_list[done] = age_list[do] + difference
                            else:
                                youngest = comp_age
                                age_list[done] = comp_age
                                age_list = [item - comp_age for number, item in enumerate(age_list) if not item == -1 if not number == done]
                     
            else:
                if age_list[done] == -1:
                    if difference >= 0:
                        age_list[do] = 0
                        age_list[done] = difference
                    else:
                        age_list[do] = - difference
                        age_list[done] = 0
                        
                else:
                    comp = age_list[done]
                    if difference >= 0:
                        age_list[do] = comp - difference
                    else:
                        age_list[do] = comp + difference
        
        if max(age_list) > 100:
            contradiction = 1
        
                        
    if contradiction == 1:
        print(-1)
    else:
        [age_list.pop(number) for number, item in enumerate(age_list) if item == -1]
        print(max(age_list) - min(age_list))
                            




if __name__ == "__main__":
    main()

