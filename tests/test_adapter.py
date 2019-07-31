from src.app import adapter

def test_bar():
    result = adapter.bar('test')
    assert result == {'message': 'hello test'}