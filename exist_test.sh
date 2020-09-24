#!/bin/bash

dir="/Users/nakamuraaoi/Desktop/test_script/dockerfiles-master/"
file=result.json
cd $dir
        touch result.json
        for filepath in *; do
            echo $filepath
            if [ -d $dir$filepath ]; then
                echo "path is directory"
                cd $dir$filepath
                    ls
                    docker run -i --rm hadolint/hadolint hadolint - --format json < Dockerfile | jq . >> $dir$file
                cd ..
            else
                echo "path is not a directory"
            fi
        done
    
cd ..



