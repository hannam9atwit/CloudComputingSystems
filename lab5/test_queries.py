import unittest
from queries import (
    get_products_by_price,
    get_customers_full_name_m_to_z,
    get_midpriced_products_by_date,
    get_order_item_totals,
    get_product_categories,
    get_addresses_by_email,
    get_shipping_addresses
)

class TestLab5Queries(unittest.TestCase):
    def test_query_1(self):
        result = get_products_by_price()
        self.assertGreater(len(result), 0)

    def test_query_2(self):
        result = get_customers_full_name_m_to_z()
        self.assertTrue(all(row[1] >= 'M' for row in result))

    def test_query_3(self):
        result = get_midpriced_products_by_date()
        for row in result:
            self.assertGreater(row[1], 500)
            self.assertLess(row[1], 2000)

    def test_query_4(self):
        result = get_order_item_totals()
        for row in result:
            item_total = row[6]
            self.assertGreater(item_total, 500)

    def test_query_5(self):
        result = get_product_categories()
        self.assertGreater(len(result), 0)

    def test_query_6(self):
        result = get_addresses_by_email('allan.sherwood@yahoo.com')
        self.assertTrue(all('allan.sherwood@yahoo.com' in row for row in result))

    def test_query_7(self):
        result = get_shipping_addresses()
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
