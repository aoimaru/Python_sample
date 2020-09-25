import sys
import requests
import json

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def cal(number,result):
    if number == 0:
        return 1
    elif number == 2:
        return 2
    else:
        if number % 2 == 0:
            return cal(number-1,result) + cal(number-2,result) + cal(number-3,result) + cal(number-4,result)
        else:
            return result

def main(argv):
    
    if not is_integer(argv[1]):
        print("error!")
    else:
        url = "http://challenge-server.code-check.io/api/recursive/ask?n={}&seed={}".format(argv[1],argv[0])
        headers = {"content-type": "application/json"}
        r = requests.get(url, headers=headers)
        data = r.json()
        print(data)

        ans = cal(data["n"],data["result"])
        
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])

