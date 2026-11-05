PRODUCTS = [
    {
        "name": "Sauce Labs Backpack",
        "price": 29.99,
    },
    {
        "name": "Sauce Labs Bike Light",
        "price": 9.99,
    },
    {
        "name": "Sauce Labs Bolt T-Shirt",
        "price": 15.99,
    },
    {
        "name": "Sauce Labs Fleece Jacket",
        "price": 49.99,
    },
    {
        "name": "Sauce Labs Onesie",
        "price": 7.99,
    },
    {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "price": 15.99,
    },
]

EXPECTED_PRODUCT_COUNT = len(PRODUCTS)


SORTING_TEST_DATA = [
    (
        "az",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ],
    ),
    (
        "za",
        [
            "Test.allTheThings() T-Shirt (Red)",
            "Sauce Labs Onesie",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Bike Light",
            "Sauce Labs Backpack",
        ],
    ),
    (
        "lohi",
        [
            "Sauce Labs Onesie",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Test.allTheThings() T-Shirt (Red)",
            "Sauce Labs Backpack",
            "Sauce Labs Fleece Jacket",
        ],
    ),
    (
        "hilo",
        [
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Test.allTheThings() T-Shirt (Red)",
            "Sauce Labs Bike Light",
            "Sauce Labs Onesie",
        ],
    ),
]