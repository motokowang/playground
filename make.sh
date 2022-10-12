#!/bin/bash
yes y | docker system prune && python3 -m pip freeze > requirements.txt && cp requirements.txt ./thing1 && cp requirements.txt ./thing2 && docker-compose -p playground up --build