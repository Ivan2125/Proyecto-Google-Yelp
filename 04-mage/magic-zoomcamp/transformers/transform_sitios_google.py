if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform_sitios_google(data, *args, **kwargs):
    data.drop({'state','state_us','horario','category','latitude','longitude','category','state','city','state_us','horario'},axis=1,inplace=True)
    data.rename(columns={'name':'business_name'},inplace= True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
