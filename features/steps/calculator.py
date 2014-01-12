from flask import url_for

@when(u'I go to the tip calculator')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see the calculator form')
def step_impl(context):
    assert context.browser.title == 'Tip calculator'