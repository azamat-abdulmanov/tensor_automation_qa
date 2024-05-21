from base.base_page import BasePage
from config.links import Links
from locators.sbis_page_locators import ContactsPageLocators
from data.locations import region
import allure


class SbisContactsPage(BasePage):
    locators = ContactsPageLocators()
    PAGE_URL = Links.CONTACT_SBIS_PAGE

    @allure.step("Click Tensor banner")
    def click_tensor_banner(self):
        self.element_is_clickable(self.locators.TENSOR_BANNER).click()

    @allure.step("Switch to Tensor tab")
    def switch_to_tensor_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    @allure.step("Check current location with expected")
    def check_location(self, expected_region):
        """"Check current location with expected
        :arg
        - expected_region - takes in data.locations.region
        """
        current_partners = []
        current_title = self.driver.title
        current_url = self.driver.current_url
        current_chooser = self.element_is_present(self.locators.REGION_CHOOSER_BUTTON).text
        partners = self.elements_are_present(self.locators.PARTNERS)
        for partner in partners:
            current_partners.append(partner.text)

        expected_partners = region[expected_region]["partners"]
        expected_title = region[expected_region]["title"]
        expected_url = region[expected_region]["url"]
        expected_chooser = region[expected_region]["chooser"]

        assert expected_partners == current_partners, f"Expected {expected_partners} partners"
        assert expected_title == current_title, f"Expected {expected_title} title"
        assert expected_url == current_url, f"Expected {expected_url} url"
        assert expected_chooser == current_chooser, f"Expected {expected_chooser} chooser"

    @allure.step("Change location")
    def change_location(self, new_region: str):
        self.element_is_clickable(self.locators.REGION_CHOOSER_BUTTON).click()
        self.element_is_clickable(("xpath", f"//span[@title='{new_region}']")).click()
        self.title_contains(new_region)
