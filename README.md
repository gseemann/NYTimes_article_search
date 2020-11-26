# Overview
- This project sets up a pipeline that utilizes the NYTimes Article Search API
- The results are flattened in preperation for insertion into a hypothetical database
- In this example, we print each batch call and the `_id` and `headline.main` for each article. We then store the full results into a csv file in the `output` folder

## Setup
- First you will need to register for an [NY Times API key](https://developer.nytimes.com/get-started)
    - Make sure to enable the Article search API
- Fork this repo then clone to your local computer
- Next `cd` into the cloned folder and run the below commands (make sure to insert YOUR API key)

        pip install -r requirements.txt
        echo "api_key='_YOUR_API_KEY_'" > conf.py
- Though not necessary, if you want to change the search parameters this can be done in the params.py file
## Run
- Now you are ready to run the script

        python test.py
- While running, the current batch will be printed to the terminal along with the `_id` and `headline.main` for each article 
- The full output will be stored in `output/output_df.csv` 
- Note: Each time you run this, the output will be overwritten. To save multiple runs, go to params.py between runs and change the `file_out` variable to a new name
