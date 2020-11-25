import argparse
import logging
import requests
import functions
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
        for i in range(batch_size):
            q = 'Silicon Valley'
            offset =i  #increment by 1 for the next set of batch
            url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
            url_params = {'q': self.args.query.replace(' ', '+'),'api-key': self.args.api_key,'page': offset}
            r = requests.get(url,  params=url_params).json()

            #start by checking call was successful
            if r['status'] != 'OK':
                log.error("Error during API call")
                return None

            # TODO: implement - this dummy implementation returns one batch of data
            list_of_art = []
            for art in r['response']['docs']:
                list_of_art.append(functions.flatten_json(art))
            yield list_of_art

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
        "query": "Silicon Valley",
    }
    source = NYTimesSource()

    # This looks like an argparse dependency - but the Namespace class is just
    # a simple way to create an object holding attributes.
    source.args = argparse.Namespace(**config)

    for idx, batch in enumerate(source.getDataBatch(10)):
        print(f"{idx} Batch of {len(batch)} items")
        for item in batch:
            print(f"  - {item['_id']} - {item['headline.main']}")