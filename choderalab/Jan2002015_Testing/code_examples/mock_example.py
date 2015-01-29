# mock_example.py
from mock import Mock

class Myclass(object):
  def closer(self, something):
      something.close()
      
mycase = Myclass()
mock = Mock()
mycase.closer(mock)
mock.close.assert_called_with() 
