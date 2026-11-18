import pytest
from test_data.products import PRODUCTS

PRODUCT_TEST_CASES = pytest.mark.parametrize(
    "product",
    PRODUCTS,
    ids=lambda product: product["name"]
)