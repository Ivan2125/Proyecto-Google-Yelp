import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform_reviews_google(data, *args, **kwargs):
    
    # drop google_site_merged
    data.dropna(subset=['user_id'], inplace=True)

    # Drop unnecessary columns
    data.drop(['name','latitude','longitude','category','state','city','state_us','horario','avg_rating','num_of_reviews','state','state_us','horario','business_name','State_review'],axis=1,inplace=True)
    
    # Rename columns to export
    data.rename(columns={'resp': 'business_reply', 'State_review': 'state_review'}, inplace=True)

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
