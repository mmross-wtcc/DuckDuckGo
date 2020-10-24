import requests
import pytest

# get the json data from the url
url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'
response = requests.get(url)
json_data = response.json()

# create list of text from the json data
text_list = []
for text in json_data['RelatedTopics']:
    text_list.append(text['Text'])
    print((text['Text']))
    
# ----------------------------------------------------------------------
# PyTests for DuckDucGo API Query
# Tests to ensure all presidents are in the RelatedTopics Text fields
# ----------------------------------------------------------------------

def test_heading():
    assert "Presidents of the United States" in json_data["Heading"]
   
   
def test_url():
    assert 'presidents+of+the+united+states' in url


@pytest.mark.parametrize('president', ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson',
                                        'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce',
                                        'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
                                        'Cleveland', 'Harrison', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 
                                        'Harding', 'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 
                                        'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama',
                                        'Trump'])
def test_each_president(president):
    found = False
    for line in text_list:
        if president in line:
            found = True
    
    assert found == True



