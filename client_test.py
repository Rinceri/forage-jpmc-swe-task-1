import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        """
        Check output of getDataPoint
        """
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        """
        Check output of getDataPoint where top_bid price is greater than top_ask price
        """
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    """ ------------ Add more unit tests ------------ """
    def test_getRatio_calculateRatio(self):
        """
        Check output of getRatio where price_a is higher, then where price_b is higher
        """
        args = [(119.2, 120.48), (121.68, 117.87)]

        for arg in args:
            self.assertEqual(
                getRatio(*arg),
                arg[0]/arg[1]
            )

    def test_getRatio_calculateRatioAZero(self):
        """
        Check output of getRatio where price_a is zero
        """
        arg = (0, 119.2)

        self.assertEqual(
            getRatio(*arg),
            arg[0]/arg[1]
        )

    def test_getRatio_calculateRatioBZero(self):
        """
        Check output of getRatio where price_b is zero
        """
        arg = (119.2, 0)

        # division by zero returns None in this function
        self.assertIsNone(
            getRatio(*arg)
        )



if __name__ == '__main__':
    unittest.main()
