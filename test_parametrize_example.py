from pytest import mark
@mark.parametrize("number",[1,0,100,-4])
def test_first(number):
    assert number > 0


@mark.parametrize("product_name,product_color",[("shoe","black"),("car","red"),("mobile","gloden"),("printer","white")])
def test_product(product_name,product_color):
    print(f"I am {product_name} with {product_color}")




