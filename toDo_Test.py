import toDo_list_func
from unittest import TestCase

class TestToDo(unittest.TestCase):
	def test_that_can_add_task(self):
		actual = toDo_list.append('buy a goat')
		expected = ['write a code', 'water the plants', 'get some groceries', 'Get a bike', 'sleep' 'buy a goat']		
	
	def test_that_toDo_list_func_work_for_String(Self):
		self.assertRaises(ValueError, toDo_list_func.toDo_list, 12)
		self.assertRaises(ValueError, toDo_list_func.toDo_list, 27)

	def test_that_can_view_task(self):
		self.assertEqual(toDo_list)

	def test_that_can_delete_task(self):
		actual = toDo_list.pop()
		expected = ['write a code', 'water the plants', 'get some groceries', 'Get a bike', 'sleep']
	
		
		
		
		

	
