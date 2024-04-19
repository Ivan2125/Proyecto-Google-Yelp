if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform_business_yelp(data, *args, **kwargs):
    data.drop(['address', 'city', 'postal_code', 'latitude','longitude','is_open', 'attributes', 'categories', 'hours', 'state_name', 'state_code'],axis=1, inplace= True)
    data.rename(columns={'business_id':'gmap_id','name':'business_name','stars':'avg_rating','review_count':'num_of_reviews'},inplace=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
