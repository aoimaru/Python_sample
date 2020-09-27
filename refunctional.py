# coding: utf-8
# Your code here!

def judge(check_id,comment_dict):
    answear = [value[1] for key,value in comment_dict.items() if key == check_id]
    answear = sum(answear)
    check_list = []
    for key,value in comment_dict.items():
        if value[0] == check_id:
            check_list.append(key)
    
    if not check_list:
        return answear
    else:
        return answear + sum([judge(check_in,comment_dict) for check_in in check_list])

def main():
    comment_views = int(input())
    comment_dict = {}
    for comment_view in range(comment_views):
        comment = input().split()
        comment_do_id = int(comment[0])
        if comment[1] == "None":
            comment_done_id = 0
        else:
            comment_done_id = int(comment[1])
        comment_heart = int(comment[2])
        comment_list = []
        comment_list.append(comment_done_id)
        comment_list.append(comment_heart)
        comment_dict[comment_do_id] = comment_list
    
    answear_dict = {}
    for key,value in comment_dict.items():
        init_check_id = key
        answear = judge(init_check_id,comment_dict)
        answear_dict[key] = answear
    max_value = max(answear_dict.values())
    answear_list = [key for key,value in answear_dict.items() if value == max_value]
    print(min(answear_list))
    
if __name__ == "__main__":
    main()


