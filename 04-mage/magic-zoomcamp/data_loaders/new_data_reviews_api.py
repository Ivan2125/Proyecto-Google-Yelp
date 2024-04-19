import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.apify.com/v2/datasets/4Ol0pNnpvM3glzH3b/items?clean=true&format=json&view=reviews'
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()

    # Create a new DataFrame
    new_data = pd.DataFrame(data=data)
    
    return new_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
