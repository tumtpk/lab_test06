import pytest
from function import mongodb_backup

collections = ["students","todos_app"]

@pytest.fixture(scope='module')
def db():
    # print('----------setup----------------')
    mongodb_backup.dump(collections)
    yield db
    # print('----------teardown----------------')
    mongodb_backup.restore()