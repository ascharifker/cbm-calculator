import unittest
from cbm_calculator import Box, Container, total_boxes_volume, containers_needed

class TestCBMCalculator(unittest.TestCase):
    def test_box_volume(self):
        box = Box(1, 1, 1)
        self.assertAlmostEqual(box.volume, 1.0)

    def test_total_volume(self):
        boxes = [Box(1, 1, 1, 2), Box(0.5, 0.5, 0.5, 4)]
        expected = 2 * 1 * 1 * 1 + 4 * 0.5 * 0.5 * 0.5
        self.assertAlmostEqual(total_boxes_volume(boxes), expected)

    def test_containers_needed(self):
        boxes = [Box(1, 1, 1, 10)]
        container = Container(2, 2, 2)
        self.assertEqual(containers_needed(boxes, container), 2)

if __name__ == '__main__':
    unittest.main()
