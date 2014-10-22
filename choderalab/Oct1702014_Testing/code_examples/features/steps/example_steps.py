# Example steps
from behave import given, when, then

# Given our subtractor is installed
@given('our subtractor is installed')
def step_impl(context):
    pass
# When I subtract 4 from 7
@when('I subtract {y} from {x}')
def step_impl(context,y,x):
    context.result = int(x) - int(y)
# Then the result should be 3
@then('the result should be {result}')
def step_impl(context, result):
    assert context.result == int(result)
