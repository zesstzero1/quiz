from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):


    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_calculator_and_use_functions(self):
        
        # Paul known a online quiz app.
        self.browser.get('http://localhost:8000/calapp/')
        # Paul notices the page title and header mention 'QUIZ'
        self.assertIn('QUIZ', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('QUIZ', header_text)
        
         
        
                
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
