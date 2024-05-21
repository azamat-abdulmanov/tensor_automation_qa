from base.base_page import BasePage
from config.links import Links
from locators.sbis_page_locators import MainPageLocators
import allure


class SbisMainPage(BasePage):
    locators = MainPageLocators()
    PAGE_URL = Links.HOST_SBIS

    @allure.step("Click contacts in header")
    def click_contacts_header(self):
        self.element_is_clickable(self.locators.CONTACTS_HEADER).click()
        self.url_contains("?")

    @allure.step("Click download local versions")
    def click_download_local_versions(self):
        self.element_is_clickable(self.locators.CLOSE_COOCIE_AGREEMENT_BUTTON).click()
        self.element_is_clickable(self.locators.LOCAL_VERSIONS).click()
        self.url_contains("?")
