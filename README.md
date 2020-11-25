# Overview
- This project sets up a pipeline that utilizes the NYTimes Article Search API
- The results are flattened in preperation for insertion into a hypothetical database
- In this example, we simple print each batch call and the `_id` and `headline.main` for each article

## Setup
- First you will need to register for an [NY Times API key](https://developer.nytimes.com/get-started)
    - Make sure to enable the Article search API
- Fork this repo then clone to your local computer
 
```pip install -r requirements.txt
bash exe.sh
```
## startup
        pip install -r requirements.txt
        echo "api_key='_YOUR_API_KEY_'" > conf.py
        python test.py
        
