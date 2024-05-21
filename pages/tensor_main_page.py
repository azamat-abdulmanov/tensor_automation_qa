from base.base_page import BasePage
from config.links import Links
from locators.tensor_page_locators import MainPageLocators
import allure


class TensorMainPage(BasePage):
    locators = MainPageLocators
    PAGE_URL = Links.HOST_TENSOR

    @allure.step("Check exist strength in people block ")
    def check_exist_strength_in_people_block(self):
        strength_in_people_text = self.element_is_present(self.locators.STRENGTH_IN_PEOPLE_BLOCK).text
        assert "Сила в людях" == strength_in_people_text

    @allure.step("Click detail strength in people block")
    def click_detail_strength_in_people_block(self):
        self.element_is_clickable(self.locators.DETAIL_STRENGTH_IN_PEOPLE_BLOCK).click()
