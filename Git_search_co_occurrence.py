from github import Github
import itertools
import dockerfile
import collections

def main():

    token = "Access token"

    g = Github(token)
    codes = g.search_code(query=
                          "nginx ln filename:Dockerfile size:<200"
                          )
    run_instructions = []
    
    for number, code in enumerate(codes):
        if number > 30:
            break

        string = code.decoded_content
        try:
            items = dockerfile.parse_string(string.decode('unicode-escape'))
            for item in items:
                if item.cmd == "run":
                    [run_instructions.append(string.split()) for string in item.value[0].split("&&")]
        except:
            passs

    sentence_combinations = [list(itertools.combinations(run_instruction, 2)) for run_instruction in run_instructions]

    target_combinations = []
    for sentence in sentence_combinations:
        target_combinations.extend(sentence)

    ct = collections.Counter(target_combinations)
    for counter in ct.most_common():
        print(counter)
    
if __name__ == "__main__":
    main()
