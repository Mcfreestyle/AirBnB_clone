#!/usr/bin/python3
'''
    Contains the TestStateDocs classes
'''
import os
from datetime import datetime
import inspect
import models
from models import state
from models.base_model import BaseModel
import pep8
import unittest
State = state.State
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestStateDocs(unittest.TestCase):
    '''
        Tests to check the documentation and style of State class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Set up for the doc tests
        '''
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        '''
            Test that models/state.py conforms to PEP8
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        '''
            Test that tests/test_models/test_state.py conforms to PEP8
        '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        '''
            Test for the state.py module docstring
        '''
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        '''
            Test for the State class docstring
        '''
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")


class TestState(unittest.TestCase):
    '''
        Test the State class
    '''
    def test_is_subclass(self):
        '''
            Test that State is a subclass of BaseModel
        '''
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        '''
            Test that State has attribute name, and it's as an empty string
        '''
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if storage_t == "db":
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, None)

    def test_to_dict_creates_dict(self):
        '''
            Test to_dict method creates a dictionary with proper attrs
        '''
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        '''
            Test that values in dict returned from to_dict are correct
        '''
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        '''
            Test that the str method has the correct output
        '''
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))