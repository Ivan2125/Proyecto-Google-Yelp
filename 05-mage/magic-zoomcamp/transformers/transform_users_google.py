if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data.drop(['gmap_id','state_us','horario','category','latitude','longitude','category','num_of_reviews','state','city','state_us','horario','time','text','resp','business_name','State_review','avg_rating'],axis=1,inplace=True)
    data.drop_duplicates('user_id', inplace=True)
    data.rename(columns={'name':'user_name'}, inplace= True)
    desired_columns = ['user_id','user_name','rating']
    data = data[desired_columns]
    data.dropna(subset=['user_id'],inplace=True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
