if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.drop(['title','textTranslated', 'publishAt','likesCount', 'reviewUrl','reviewerPhotoUrl', 'reviewerNumberOfReviews','isLocalGuide','responseFromOwnerDate', 'reviewImageUrls',
       'reviewContext', 'reviewDetailedRating', 'reviewerUrl'],axis=1,inplace=True)

    def map_response(response):
        if response is not None and isinstance(response, str):
            return 'yes'
        else:
            return 'no'

    # Apply the function to the 'response' column
    data['responseFromOwnerText'] = data['responseFromOwnerText'].apply(lambda x: map_response(x))
    
    data.drop(['name','rating'],axis=1,inplace=True)
    data.rename(columns={'reviewerId':'user_id','reviewId':'gmap_id','publishedAtDate':'time','reviewOrigin':'source','stars': 'rating', 'responseFromOwnerText':'business_reply'},inplace=True)
    new_order = ['gmap_id','user_id','time','rating','text','business_reply','source']
    data = data[new_order] 
        
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
