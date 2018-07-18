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
        header1 = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Welcome to Quiz App', header1)
        # Paul see 'Add your Question'
        header2 = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Add your Question', header2)

        time.sleep(1)
        # Paul add the question 'Is this a Quiz App?' to inputbox        
        inputbox = self.browser.find_element_by_id('new_question')
        inputbox.send_keys('Is this a Quiz App?')
        time.sleep(1)
        # Paul enter 'Add' button
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Paul see 'Question List' below
        header3 = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Question list', header3)

        # Paul see his question that's he made 'Is this a Quiz App?' and clicked it
        question_of_Paul = self.browser.find_element_by_link_text('Is this a Quiz App?').click()
        time.sleep(2)
        
        # Paul notices the page title and header mention 'quiz'
        self.assertIn('quiz', self.browser.title)
        # Paul see question 'Is this a Quiz App?'
        question = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Is this a Quiz App?', question)

        # Paul see header 'Add your Choice'
        add_choice_header = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Add your Choice', add_choice_header)

        # Paul see link 'Instant add True and False'
        # Paul want to make True/False choices then Paul clicked it
        make_True_False = self.browser.find_element_by_link_text('Instant add True and False').click()
        time.sleep(2)
        
        # Paul want to make another choices with inputbox
        # Paul add the 3rd choice 'This is not a Quiz App' to inputbox
        input_choice1 = self.browser.find_element_by_id('new_choice')
        input_choice1.send_keys('This is not a Quiz App')
        time.sleep(1)
        # Paul enter 'Add' button
        input_choice1.send_keys(Keys.ENTER)
        time.sleep(3)

        # Paul add the 4th choice 'No' to inputbox
        input_choice2 = self.browser.find_element_by_id('new_choice')
        input_choice2.send_keys('No')
        time.sleep(1)
        # Paul enter 'Add' button
        input_choice2.send_keys(Keys.ENTER)

        # Paul knew the answer then clicked on the choice 'True'
        time.sleep(1)
        choice = self.browser.find_element_by_xpath(".//input[@type='radio' and @id='choice1']").click()
        time.sleep(1) 
        
        # Paul accepted the answer 'True' by clicking the "Submit" button
        submit = self.browser.find_element_by_xpath(".//input[@type='submit' and @value='Vote']").click()
        time.sleep(1)

        # Paul notices the page title and header mention 'result'
        self.assertIn('result', self.browser.title)
        # Paul see question 'Is this a Quiz App?'
        question = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Is this a Quiz App?', question)

        # Paul see result of 'True' 
        true = self.browser.find_element_by_id('1').text
        self.assertIn('True', true)

        # Paul see result of 'False'
        false = self.browser.find_element_by_id('2').text
        self.assertIn('False', false)
        time.sleep(1)    

        # Paul see result of 'This is not a Quiz App'
        not_a_quiz = self.browser.find_element_by_id('3').text
        self.assertIn('This is not a Quiz App', not_a_quiz)
        time.sleep(1)    

        # Paul see result of 'No'
        no = self.browser.find_element_by_id('4').text
        self.assertIn('No', no)
        time.sleep(1)    
    
        # Paul done the quiz but he wants to delete his question 'Is this a Quiz App?'
        # so he came back to detail page by clicking 'Vote again?' below
        vote_again = self.browser.find_element_by_link_text('Vote again?').click()
        time.sleep(1)

        # at the bottom there is a 'delete this question'
        # Paul clicked it to delete 'Is this a Quiz App'
        del_q = self.browser.find_element_by_link_text('delete this question').click()
        time.sleep(1)        
        
        # browser bring Paul back to home page
        # Paul do not want to do the question anymore then Paul close the browser
        self.browser.quit()

                
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
