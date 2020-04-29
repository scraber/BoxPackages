from unittest import TestCase

from boxes import packaging
from tests.expected_results import EXPECTED_RESULTS


class TestPackaging(TestCase):
    def test_packaging_success(self):
        # Auxiliary test to check if correctly copied all results from pdf file
        self.assertEqual(len(EXPECTED_RESULTS), 36)

        for order_size, expected in enumerate(EXPECTED_RESULTS, start=1):
            self.assertDictEqual(packaging.summary_order_boxes(order_size), expected)

    def test_packaging_fails_order_less_than_1(self):
        self.assertRaises(ValueError, packaging.summary_order_boxes, 0)
        self.assertRaises(ValueError, packaging.summary_order_boxes, -5)

    def test_packaging_fails_order_over_100(self):
        self.assertRaises(ValueError, packaging.summary_order_boxes, 101)
        self.assertRaises(ValueError, packaging.summary_order_boxes, 1024)
