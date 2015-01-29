# Example steps
from behave import given, when, then

# Given our subtractor is installed
@given('our subtractor is installed')
def step_impl(context):
    pass
# When I subtract 4 from 7
@when('I subtract {y} from {x}')
def step_impl(context,y,x):
    if '.' in x or '.' in y:
      x = float(x)
      y = float(y)
    else:
      x = int(x)
      y = int(y)
     
    context.result = x - y
# Then the result should be 3
@then('the result should be {result}')
def step_impl(context, result):
    if '.' in result:
      result = float(result)
    else:
      result = int(result)
    assert (context.result - result) <= 0.0001

@then('it should return {result} within {err} error')
def step_impl(context, result, err):
    if '.' in result:
      result = float(result)
    else:
      result = int(result)
    assert (context.result - result) <= float(err)

