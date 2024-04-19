if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.drop(['review_count', 'yelping_since', 'useful', 'funny','cool', 'elite', 'friends', 'fans', 'compliment_hot','compliment_more', 'compliment_profile', 'compliment_cute','compliment_list', 'compliment_note', 'compliment_plain','compliment_cool', 'compliment_funny', 'compliment_writer','compliment_photos'],axis=1,inplace=True)
    data.rename(columns={'average_stars':'rating', 'name':'user_name'},inplace=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
