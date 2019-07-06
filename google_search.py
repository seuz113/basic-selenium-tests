import time
from termcolor import colored
from helper.common_operations import *
import unittest
import allure

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = set_up_chrome(google_url)

    #Test Case #GS-001
    @allure.step("Validate that site is launched")
    def test_validate_home_page_field_button(self):
        self.type_text = write_on_element(self.driver, "CSS", main_input, "testing")
        self.button_search = self.driver.find_element_by_css_selector(search_button)

        if self.type_text and self.button_search:
            assert(True)
        else:
            assert(False)

    #Test Case #GS-002
    @allure.step("Search Information Using search button")
    def test_search_information_using_button(self):
        self.type_text = write_on_element(self.driver, "CSS", main_input, "The name of the wind")
        self.element = wait_for_element(self.driver, "CSS", all_suggestion_list_element)
        click_element(self.element, "CSS", search_button_from_suggestion)

        self.first_result_page_element =wait_for_element(self.driver, "CSS", link_first_result_page)
        self.text_element = self.first_result_page_element.text
        print(self.text_element)

        assert (self.text_element == "The Name of the Wind - Patrick Rothfuss"), colored("First Result page link doesn't contain name The Name of the Wind - Patrick Rothfuss", "red")

    #Test Case #GS-003
    @allure.step("Open first result page found")
    def test_go_first_result_page(self):
        self.type_text = write_on_element(self.driver, "CSS", main_input, "The name of the wind")
        self.element = wait_for_element(self.driver, "CSS", all_suggestion_list_element)
        click_element(self.element, "CSS", search_button_from_suggestion)

        self.first_result_page_element = wait_for_element(self.driver, "CSS", link_first_result_page)
        click_element(self.first_result_page_element)

        self.find_content_page_id = wait_for_element(self.driver, "ID", title_page_first_link)
        self.text_element = self.find_content_page_id.text
        print(self.text_element)

        assert (self.text_element == "Patrick Rothfuss - The Books"),  colored("First Result page opened is not Patrick Rothfuss - The Books", "red")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





