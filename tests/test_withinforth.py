from withinforth import withinforth
import unittest   # The test framework

class CreateMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.machine = withinforth.Interpreter()

    def test_empty_command(self):
        self.assertEqual(self.machine.run(""), "ok")

if __name__ == '__main__':
    unittest.main()
