import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.drop(['review_id','useful', 'funny','cool'], axis=1,inplace=True)
    data.rename(columns={'business_id':'gmap_id', 'stars':'rating', 'date':'time'}, inplace= True)
    data['business_reply'] = None
    new_order = ['gmap_id', 'user_id', 'time', 'rating', 'text', 'business_reply']
    data = data[new_order]
    data.columns

    # Convert user_id dtype to string
    data['user_id'] = data['user_id'].apply(str)
    data['gmap_id'] = data['gmap_id'].apply(str)
    data['rating'] = data['rating'].apply(int)
    data['text'] = data['text'].apply(str)
    
    # Convert timestamps to datetime objects
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')

    # Format timestamps to 'dd/mm/yy hh:mm' without microseconds
    data['time'] = data['time'].dt.strftime('%d/%m/%y %H:%M')
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
