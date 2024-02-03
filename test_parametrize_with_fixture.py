from pytest import fixture


@fixture(params=["apple","orange","grapes"])
def fruit(request):
    return request.param

# I am passing the fixture fruit as a parameter to this test function
def test_fruit(fruit):
    print(f"I am {fruit}")