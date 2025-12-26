import pytest

class TestHuman():
    def test_fuck(self, predict):
        print(predict)
        login = predict[0]
        password = predict[1]
        assert login == "opaa", "Неправильный логин"