# twitterwipe
0) use pip to install the stuff you need from requirements.txt.

1) Authorization - Pt. I  
get your consumer keys from twitter. copy keys.example.json to keys.json, and put your consumer keys into the json.
if you have app_key & app_secret, put those in now and skip to step (3).

2) Authorization - Pt. II  
run auth.py. it will print your app_key and secret to console. put those into your keys.json.

3) Configure  
put in the number of days worth of past data (starting from runtime) you want to preserve into config.yaml.

4) run the program with python:  
python twitterwipe.py

5) logs will be written to logs.logs, which is registered in the .gitignore.
