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
        self.browser.get('http://localhost:8000')
        # Paul notices the page title and header mention 'Quiz App'
        self.assertIn('Quiz App', self.browser.title)
        # Paul see 'Welcome to Quiz App'
        question = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Welcome to Quiz App', question)
        # Paul see Link 'Click here to do the Question' and clicked it
        h_link = self.browser.find_element_by_link_text('Click here to do the Question').click()
        time.sleep(1)

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
        time.sleep(2)

        # Paul notices the page title and header mention 'result'
        self.assertIn('result', self.browser.title)
        # Paul see question '50 Dollas more values than 10 Dollas?'
        question = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('50 Dollas more values than 10 Dollas?', question)

        # Paul see result of 'True' 
        true = self.browser.find_element_by_id('1').text
        self.assertIn('True', true)

        # Paul see result of 'False'
        false = self.browser.find_element_by_id('2').text
        self.assertIn('False', false)
        
        # Paul do not want to do the question anymore then Paul close the browser
        self.browser.quit()

                
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
