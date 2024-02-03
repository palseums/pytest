from pytest import fixture

# we have four type of scope
# default is function
# function : will execute for each function
# module : module means file level run one time at the file level
# class: class level
# session : session level

@fixture(scope="module")
def connect_db():
    print("I need to connect to employee databases")
    yield
    print("I closed the connection")



def test_connect_to_database(connect_db):
    print("I got value from database_1")


def test_connect_to_database_2(connect_db):
    print("I got value from database_2")


