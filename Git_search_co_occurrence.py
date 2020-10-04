from github import Github
import base64
# import zlib
import itertools
import collections

instruction_list = [
        "FROM",
        "nMAINTAINER",
        "nRUN",
        "nCMD",
        "nENTRYPOINT",
        "nLABEL",
        "nEXPOSE",
        "nENV",
        "nADD",
        "nCOPY",
        "nVOLUME",
        "nUSER",
        "nWORKDIR",
        "nARG",
        "nONBUILD",
        "nSTOPSIGNAL",
        "nHEALTHCHECK",
        "nSHELL"
    ]


def main():

    cli_dict = {}

    token = "access token"

    g = Github(token)
    codes = g.search_code(query=
                          "nginx filename:Dockerfile size:<200"
                          )

    for number, code in enumerate(codes):
        if number > 30:
            break

        # repository = g.get_repo(code.repository.full_name)
        # contents = repository.get_contents(code.path)
        # content = base64.b64decode(contents.content)
        content = code.decoded_content

        strings = str(content)

        position_list = []

        for instruction in instruction_list:
            index = -1
            while True:
                index = strings.find(instruction, index + 1)
                if index == -1:
                    break
                position_list.append(index)

        position_list = sorted(position_list)

        for number,index in enumerate(position_list):
            if number == len(position_list)-1:
                cmd = strings[index:]
            else:
                cmd = strings[index:position_list[number+1]-1]

            # dock_cmd, file_cmd = cmd.split(" ", 1)[0], cmd.split(" ", 1)[1]
            dock_cmd,file_cmd  = cmd.split(" ",1)[0],cmd.split(" ",1)[1].split("#")[0]

            if dock_cmd == "FROM":
                if not "nginx" in file_cmd:
                    break

            if not dock_cmd in cli_dict:
                cli_dict[dock_cmd] = []
                cli_dict[dock_cmd].append(file_cmd)
            else:
                cli_dict[dock_cmd].append(file_cmd)

    instructed_list = []
    for dock,commands in cli_dict.items():
        if dock == "nRUN":
            for command in commands:
                # print(command)
                # [map(lambda x:command_list.append(x),item) for item in command.split("&&")]
                [instructed_list.append(item.split()) for item in command.split("&&")]

                # instructs = [[one for one in item.split() if not "\\" in one]for item in command.split("&&")]
                # [[instructed_list.append(one) for one in item.split() if not "\\" in one]for item in command.split("&&")]

    # for instruct in instructed_list:
    #     print(instruct)

    # for instruct in instructed_list:
    #     for suffix,item in enumerate(instruct):
    #
    #         if "\\" in item:
    #             instruct.pop(suffix)
    #         item.strip()

    for instruct in instructed_list:
        for suffix,item in enumerate(instruct):
            if "\\" in item:
                # print("before",item)
                instruct[suffix] = instruct[suffix].split("\\")[0]
                # print("after",instruct[suffix])
                if len(instruct[suffix]) == 0:
                    instruct.pop(suffix)

    print()

    for instruct in instructed_list:
        print(instruct)
    #     print(instruct)
    #     print(instruct)


    # instructed_combinations = [[list(itertools.combinations(instructed, 2)) for instructed in instructeds] for instructeds in instructed_list]
    # instructed_list = [[item for item in instruct] for instruct in instructed_list]
    sentence_combinations = [list(itertools.combinations(instructed, 2)) for instructed in instructed_list]
    sentence_combinations = [[tuple(sorted(words)) for words in sentence] for sentence in sentence_combinations]
    target_combinations = []
    for sentence in sentence_combinations:
        target_combinations.extend(sentence)
    #
    ct = collections.Counter(target_combinations)
    for counter in ct.most_common()[:20]:
        print(counter)



if __name__ == "__main__":
    main()

