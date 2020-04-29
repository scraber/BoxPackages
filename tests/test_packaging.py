from unittest import TestCase

from boxes import packaging
from tests.expected_results import EXPECTED_RESULTS


class TestPackaging(TestCase):
    def test_collective_box(self):
        self.assertEqual(packaging.compute_collective_box(1), 0)
        self.assertEqual(packaging.compute_collective_box(2), 1)
        self.assertEqual(packaging.compute_collective_box(3), 1)
        self.assertEqual(packaging.compute_collective_box(4), 2)
        self.assertEqual(packaging.compute_collective_box(6), 2)
        self.assertEqual(packaging.compute_collective_box(7), 3)

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
