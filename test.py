import argparse
import logging
import requests
import pandas as pd 

#my python files
import functions
import params
import conf

"""
Skeleton for Squirro Delivery Hiring Coding Challenge
October 2020
"""


log = logging.getLogger(__name__)


class NYTimesSource(object):
    """
    A data loader plugin for the NY Times API.
    """

    def __init__(self):
        pass

    def connect(self, inc_column=None, max_inc_value=None):
        log.debug("Incremental Column: %r", inc_column)
        log.debug("Incremental Last Value: %r", max_inc_value)

    def disconnect(self):
        """Disconnect from the source."""
        # Nothing to do
        pass

    def getDataBatch(self, batch_size):
        """
        Generator - Get data from source on batches.

        :returns One list for each batch. Each of those is a list of
                 dictionaries with the defined rows.
        """
#         print(params.flag)
#         params.flag+=1
        for i in range(batch_size):
            q = 'Silicon Valley'
            params.offset = params.offset+i  #increment by 1 for the next set of batch
            url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
            url_params = {'q': self.args.query.replace(' ', '+'),'api-key': self.args.api_key,'page': params.offset}
            response = requests.get(url,  params=url_params)
            r = response.json()

            #start by checking call was successful
            if response.ok:
                if r['status'] != 'OK':
                    log.error("Error with API call, NYT status not ok")
                    return None

                # TODO: implement - this dummy implementation returns one batch of data
                list_of_art = []
                for art in r['response']['docs']:
                    list_of_art.append(functions.flatten_json(art))   #attach to list returned in call
                yield list_of_art
            else:
                log.error("Error during API call on request side")
                
    def getSchema(self):
        """
        Return the schema of the dataset
        :returns a List containing the names of the columns retrieved from the
        source
        """

        schema = [
            "title",
            "body",
            "created_at",
            "id",
            "summary",
            "abstract",
            "keywords",
        ]

        return schema


if __name__ == "__main__":
    config = {
        "api_key": conf.api_key,
        "query": params.search
    }
    source = NYTimesSource()
    #create headers in csv file to store data (*note this overwrites previous results)
    pd.DataFrame(columns = params.col_names).to_csv(params.file_out)

    # This looks like an argparse dependency - but the Namespace class is just
    # a simple way to create an object holding attributes.
    source.args = argparse.Namespace(**config)

    for idx, batch in enumerate(source.getDataBatch(params.batch)):
        df = pd.DataFrame(columns = params.col_names)
        print(f"{idx} Batch of {len(batch)} items")
        for item in batch:
            df = df.append(item, ignore_index=True)
            print(f"- {item['_id']} - {item['headline.main']}")
        #save current call values into df
        with open(params.file_out, 'a') as f:
            df.to_csv(params.file_out, mode='a', header=False, index=True)
            

    