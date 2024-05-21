from base.base_page import BasePage
from config.links import Links
from locators.tensor_page_locators import AboutPageLocators
import allure


class TensorAboutPage(BasePage):
    locators = AboutPageLocators
    PAGE_URL = Links.ABOUT_TENSOR_PAGE

    @allure.step("Check exist working block")
    def check_exist_working_block(self):
        working_block_text = self.element_is_present(self.locators.WORKING_BLOCK).text
        assert working_block_text == "Работаем", "Block 'Работаем' should be exist"

    @allure.step("Check size of images in working block are equal")
    def check_equality_sizes_images_working_block(self):
        width = set()
        height = set()
        images_working_block = self.elements_are_present(self.locators.IMAGES_WORKING_BLOCK)
        for img in images_working_block:
            width.add(img.get_attribute("width"))
            height.add(img.get_attribute("height"))

        assert len(width) == 1, "Widths of images not equal"
        assert len(height) == 1, "Heights of images not equal"
