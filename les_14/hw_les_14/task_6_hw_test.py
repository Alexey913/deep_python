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
    with pytest.raises(Ex.ErrorAcsess):
        data.enter('Иван', "Дурак")

def test_add_user(data):
    data.enter('Sam', '114')
    data.add_user('Иван', 105, 7)
    new_user = User('Иван', 105, 7)
    assert new_user in data.users


if __name__ == '__main__':
    pytest.main(['-v'])