# i_need_server
Community resources chat-bot server

# Run
1. ```docker-compose build```
2. ```docker-compose up```
Access at ```192.168.99.100:8000```, or whatever the docker-machine ip is.
If changes, may need to update ```settings.py```->ALLOWED_HOSTS with new IP.

#Run Tests
Change environments: 
1. List environments: ```conda env list```
2. Activate environment: ```activate nlp```
Run tests (be sure to use the double-quotes):
```python -m unittest discover ./ "*test.py"```