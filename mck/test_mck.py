from unittest import TestCase, main
from unittest.mock import Mock, MagicMock
from mck import Foo

class TestMck(TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_foo(self):
		foo = Foo()
		foo.bar = MagicMock()
		foo.bar.return_value = 1
		res = foo.yaa()
		foo.bar.assert_called_with()
		self.assertEqual(res, 1)

	def test_abc(self):
		foo = Foo()
		mock = MagicMock(name='bleh')
		foo.abc(mock)
		mock.something.assert_called_with(mock)

if __name__ == '__main__':
    main()
