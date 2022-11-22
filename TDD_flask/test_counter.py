"""
Test Case for Counter Web service 

 - RESTful API
 - endpoint : counters/
 - name of counter is spicified in path
 - if name already exist then 409 error is reruened
"""

from unittest import TestCase
from my_flask_app import app
import statuses
import nose

# for error of nosetests in windows:
import collections
collections.Callable = collections.abc.Callable


class CounterTest(TestCase):
    " testing counters API"
    
    def setUp(self):
        self.client = app.test_client()
        
        
    def test_create_counter(self):
        """It should create a counter"""
        result = self.client.post('/counters/foo')
        self.assertEqual(result.status_code, statuses.HTTP_201_CREATED)
    
    
    def test_duplicated_counter(self):
        """It should raise error for duplicated counters"""
        result = self.client.post('/counters/dup')
        self.assertEqual(result.status_code, statuses.HTTP_201_CREATED)
        result = self.client.post('/counters/dup')
        self.assertEqual(result.status_code, statuses.HTTP_409_CONFLICT)
        




if __name__ == "__main__":
    nose.main()    