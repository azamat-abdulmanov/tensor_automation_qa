import allure
import time
import wget
import os

from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 10, poll_frequency=1)
        self.EC = EC

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)  # PAGE_URL подтягивается из дочернего класса

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def url_contains(self, char):
        return self.wait.until(EC.url_contains(char))

    def title_contains(self, char):
        return self.wait.until(EC.title_contains(char))

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_scripte("argument[0].scrollIntoView();", element)

    @allure.step("Download file")
    def download_file(self, locator):
        link = self.wait.until(EC.presence_of_element_located(locator)).get_attribute("href")
        file_name = link.split("/")[-1]
        file_path = f"downloads/{file_name}"
        if os.path.exists(file_path):
            os.remove(file_path)
            wget.download(link, file_path)
        else:
            wget.download(link, file_path)
        return file_path

    @allure.step("Check to file is downloaded")
    def file_is_downloaded(self, file_path, time_out=10, poll_frequency=1):
        while time_out:
            time_out -= poll_frequency
            if os.path.exists(file_path):
                return True
            time.sleep(poll_frequency)
        return False

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
