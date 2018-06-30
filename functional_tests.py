from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):


    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_use_functions(self):
        
        # Paul known a online quiz app.
        self.browser.get('http://localhost:8000/quiz/1/')
        # Paul notices the page title and header mention 'quiz'
        self.assertIn('quiz', self.browser.title)
        # Paul see question '50 Dollas more values than 10 Dollas?'
        question = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('50 Dollas more values than 10 Dollas?', question)
        
        # Paul knew the answer then clicked on the choice 'True'
        time.sleep(1)
        choice = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='1']").click()
        time.sleep(1) 
        
        # Paul accepted the answer 'True' by clicking the "Submit" button
        submit = self.browser.find_element_by_xpath(".//input[@type='submit' and @value='Vote']").click()
        time.sleep(3)



                
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
