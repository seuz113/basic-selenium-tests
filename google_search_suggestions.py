import time
from termcolor import colored
from helper.common_operations import *
import unittest
import allure

class GoogleSearchSuggestions(unittest.TestCase):

    def setUp(self):
        self.driver = set_up_chrome(google_url)

    #Test Case #GS-001
    @allure.step("Validate suggestion list is displayed")
    def test_suggestion_list_displayed(self):
        type_text = write_on_element(self.driver, "CSS", main_input, "The name of the w")

        suggestion_list = wait_for_element(self.driver, "CSS", all_suggestion_list_element)

        if suggestion_list:
            assert True
        else:
            assert False, "The suggestion menu was not displyaed"



    #Test Case #GS-002
    @allure.step("Get Result page after click on suggestion list")
    def test_select_option_from_suggestion(self):
        type_text = write_on_element(self.driver, "CSS", main_input, "The name of the w")

        element = wait_for_element(self.driver, "CSS", all_suggestion_list_element)
        click_element(element,  "CSS", first_option_suggestion)

        result_page = wait_for_element(self.driver, "CSS", result_page_google)
        print(result_page)

        if result_page:
            assert True 
        else:
            assert False, colored("Result page wasn't displyaed", "red")


    #Test Case #GS-003
    @allure.step("Open first page found using suggestion")
    def test_go_the_books_page(self):
        type_text = write_on_element(self.driver, "CSS", main_input, "The name of the w")
        element = wait_for_element(self.driver, "CSS", all_suggestion_list_element)
        click_element(element,  "CSS", first_option_suggestion)

        first_result_page_element = wait_for_element(self.driver, "CSS", link_first_result_page)
        click_element(first_result_page_element)

        find_content_page_id = wait_for_element(self.driver, "ID", title_page_first_link)
        text_element = find_content_page_id.text
        print(text_element)

        assert (text_element == "Patrick Rothfuss - The Books"), colored("First Page found isn't Patrick Rothfuss - The Books", "red")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
