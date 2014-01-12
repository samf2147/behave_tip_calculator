@when(u'I go to the google home page')
def step_impl(context):
    '''have selenium navigate to google's home page'''
    context.browser.get('http://www.google.com')

@then(u'I should see that the title is "Google"')
def step_impl(context):
    '''check that title of most recently visited page is Google'''
    assert context.browser.title == "Google"