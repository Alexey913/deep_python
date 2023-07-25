# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
from Project import Project
from User import User
import Excep as Ex

@pytest.fixture
def data():
    return Project.load_users('users.json')

def test_enter(data):
    data.enter('Han', '105')
    assert data.admin.name == 'Han' and \
            data.admin.uid == '105'

def test_enter_error(data):
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-Дурак не существует!"):
        data.enter('Иван', "Дурак")

def test_add_user(data):
    data.enter('Sam', 114)
    new_user = User('Иван', '105', 7)
    data.add_user('Иван', '105', 7)
    assert new_user in data.users

def test_add_user_error_level(data):
    data.enter('Sam', '114')
    with pytest.raises(Ex.ErrorLevel, match="Операция для пользователя Иван не может быть выполнена, т.к. его уровень доступа (1) выше, чем уровень администратора (4)!"):
        data.add_user('Иван', '105', 1)

def test_add_user_error_user(data):
    data.enter('Sam', '114')
    with pytest.raises(Ex.ErrorUser, match="Пользователь Carl с ID-106 уже существует!"):
        data.add_user('Carl', '106', 6)

def test_del_user(data):
    data.enter('Sam', '114')
    new_user = User('Han', '105', 5)
    data.del_user('Han', '105')
    assert not new_user in data.users

def test_del_user_error_user(data):
    data.enter('Sam', '114')
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-105 не существует!"):
        data.del_user('Иван', '105')

def test_del_user_error_level(data):
    data.enter('Sam', '114')
    with pytest.raises(Ex.ErrorLevel, match="Операция для пользователя Lee не может быть выполнена, \
т.к. его уровень доступа (1) выше, чем уровень администратора (4)!"):
        data.del_user('Lee', '101')

if __name__ == '__main__':
    pytest.main(['-v'])