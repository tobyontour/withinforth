from withinforth import withinforth
import unittest   # The test framework

class CreateMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.machine = withinforth.Interpreter()

    def test_empty_command(self):
        self.assertEqual(self.machine.run(""), "ok")

    def test_retrieve_emtpy_stack(self):
        self.assertEqual(self.machine.run("."), ":1: Stack underflow")

if __name__ == '__main__':
    unittest.main()
