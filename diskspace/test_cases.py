import unittest
import diskspace
import subprocess
import StringIO
import sys


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

    def test_subprocess_check_output(self):
        command = 'ls'
        expected_exit = subprocess.check_output(command)
        self.assertEqual(diskspace.subprocess_check_output(command),
                         expected_exit)

    def test_print_tree(self):
        path = '/home/Downloads'
        total_size = 1

        file_tree_node = {
            'print_size': '100.00Kb',
            'children': [],
            'size': total_size
        }

        file_tree = {
            path: file_tree_node
        }

        largest_size = 2
        catched = StringIO.StringIO()
        sys.stdout = catched

        diskspace.print_tree(
            file_tree,
            file_tree_node,
            path,
            largest_size,
            total_size,
        )

        expected_exit = '100.00Kb  100%  {}\n'.format(path)
        sys.stdout = sys.__stdout__

        self.assertEqual(catched.getvalue(), expected_exit)


if __name__ == '__main__':
    unittest.main()
