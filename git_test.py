from github import Github
import base64
import sys

def main():
    token = "accesss token"

    g = Github(token)

    repository = "seapy/dockerfiles"
    file_path = "elasticsearch/Dockerfile"

    repo = g.get_repo(repository)
    contents = repo.get_contents(file_path)
    content = base64.b64decode(contents.content)

    print(content)

    codes = g.search_code(query=
                          "RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log filename:Dockerfile"
                          )
    for number,code in enumerate(codes):
        if number > 10:
            break
        print(code.path)
        print(code.repository.full_name)

        repository = g.get_repo(code.repository.full_name)
        contents = repository.get_contents(code.path)
        content = base64.b64decode(contents.content)

        print(content)





        # with open("./Dockerfile", mode="wb") as f:
        #     f.write(content)
    print("****************************************")
    codes = g.search_code(query=
                          "COPY nginx.conf /etc/nginx/nginx.conf filename:Dockerfile"
                          )
    for number, code in enumerate(codes):
        if number > 10:
            break
        print(code.path)
        print(code.repository.full_name)

        repository = g.get_repo(code.repository.full_name)
        contents = repository.get_contents(code.path)
        content = base64.b64decode(contents.content)

        print(content)
    print("****************************************")
    codes = g.search_code(query=
                          "filename:Dockefile nginx"
                          )
    for number, code in enumerate(codes):
        if number > 10:
            break
        print(code.path)
        print(code.repository.full_name)

        repository = g.get_repo(code.repository.full_name)
        contents = repository.get_contents(code.path)
        content = base64.b64decode(contents.content)

        print(content)


if __name__ == "__main__":
    main()

