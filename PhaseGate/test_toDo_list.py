import movieRating_func
from unittest import TestCase

class MovieManager(TestCase):
    
    def test_can_add_movie(self):
        movieRating_func.movies.append()
        expected = ['write a code', 'water the plants', 'get some groceries', 'Get a bike', 'sleep', 'buy a goat']
        self.assertEqual(toDo_list_func.toDo_list, expected)

    def test_only_strings_allowed(self):
        initial_list = toDo_list_func.toDo_list.copy()
        movieRating_func.toDo_list.append(12)
        movieRating_func.toDo_list.append(27)
        self.assertEqual(toDo_list_func.toDo_list, initial_list, "List should not change if non-strings are added")

    def test_can_view_tasks(self):
        expected = ['Koto Aye', '', 'get some groceries', 'Get a bike', 'sleep']
        self.assertEqual(toDo_list_func.toDo_list, expected)

    def test_can_delete_task(self):
        popped_task = toDo_list_func.toDo_list.pop()
        expected = ['write a code', 'water the plants', 'get some groceries', 'Get a bike']
        self.assertEqual(toDo_list_func.toDo_list, expected)
        self.assertEqual(popped_task, 'sleep')