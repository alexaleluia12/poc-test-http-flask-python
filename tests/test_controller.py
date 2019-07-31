import json

from src.app import controller

def test_bar(client, mocker):
    expected_return = {'message': 'test1'}
    stub = mocker.patch.object(controller.adapter, 'bar', return_value=expected_return)

    response = client.get('/foo/testxx')
    assert response.status_code == 200
    assert json.loads(response.data) == expected_return

    #assert stub.call_args == (('testxx',),)
    stub.assert_called_with('testxx',)