import unittest
import diskspace


class TestDiskSpace(unittest.TestCase):

    def test_bytes_to_readable_for_B(self):
        blocksB = 1
        expected_exit = '512.00B'
        self.assertEqual(diskspace.bytes_to_readable(blocksB), expected_exit)

    def test_bytes_to_readable_for_Kb(self):
        blocksKb = 256
        expected_exit = '128.00Kb'
        self.assertEqual(diskspace.bytes_to_readable(blocksKb), expected_exit)

    def test_bytes_to_readable_for_Mb(self):
        blocksMb = 524288
        expected_exit = '256.00Mb'
        self.assertEqual(diskspace.bytes_to_readable(blocksMb), expected_exit)

    def test_bytes_to_readable_for_Gb(self):
        blocksGb = 1073741824
        expected_exit = '512.00Gb'
        self.assertEqual(diskspace.bytes_to_readable(blocksGb), expected_exit)


if __name__ == '__main__':
    unittest.main()
