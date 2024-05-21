import re
import os
import allure
from base.base_page import BasePage
from config.links import Links
from locators.sbis_page_locators import DownloadLocators


class SbisDownloadPage(BasePage):
    locators = DownloadLocators()
    PAGE_URL = Links.DOWNLOAD_SBIS_PAGE

    @allure.step("Click plugin selector")
    def click_plugin(self):
        self.element_is_clickable(self.locators.PLUGIN_BUTTON).click()

    @allure.step("Click windows selector")
    def click_windows(self):
        self.element_is_clickable(self.locators.WINDOWS_BUTTON).click()

    @allure.step("Download web installer")
    def download_web_installer(self):
        return self.download_file(self.locators.WEB_INSTALLER_DOWNLOAD)

    @allure.step("Getting file size from web page text")
    def get_size_web_text(self, locator):
        link_name = self.element_is_present(locator).text
        size = float((re.findall(r"\d+.\d+", link_name))[0])
        return size

    @allure.step("Getting file size in downloaded file")
    def get_size_download_file(self, file_path, ):
        file_size = round((os.path.getsize(file_path)) / (1024 * 1024), 2)
        return file_size
