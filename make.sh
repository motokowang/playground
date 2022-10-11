#!/bin/bash
yes y | docker system prune && python3 -m pip freeze > requirements.txt && cp requirements.txt ./thing1 && cp requirements.txt ./thing2 && docker-compose -p playground up --build
# yes y | docker system prune && python3 -m pip freeze > requirements.txt && docker build . -f Dockerfile -t motoko && docker run -dp 7777:7777 motoko