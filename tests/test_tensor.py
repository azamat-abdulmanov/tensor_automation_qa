from base.base_test import BaseTest
from locators.sbis_page_locators import DownloadLocators
import allure
import pytest


@allure.feature("Tensor test")
class TestTensor(BaseTest):

    @allure.story("Task one")
    @pytest.mark.smoke
    def test_task_one(self):
        self.sbis_main_page.open()
        self.sbis_main_page.click_contacts_header()
        self.sbis_contacts_page.click_tensor_banner()
        self.sbis_contacts_page.switch_to_tensor_tab()
        self.tensor_main_page.is_opened()
        self.tensor_main_page.check_exist_strength_in_people_block()
        self.tensor_main_page.click_detail_strength_in_people_block()
        self.tensor_about_page.is_opened()
        self.tensor_about_page.check_exist_working_block()
        self.tensor_about_page.check_equality_sizes_images_working_block()

    @allure.story("Task two")
    @pytest.mark.smoke
    def test_task_two(self):
        self.sbis_main_page.open()
        self.sbis_main_page.click_contacts_header()
        self.sbis_contacts_page.check_location("Республика Башкортостан")
        self.sbis_contacts_page.change_location("Камчатский край")
        self.sbis_contacts_page.check_location("Камчатский край")

    @allure.story("Task three")
    @pytest.mark.smoke
    def test_task_three(self):
        self.sbis_main_page.open()
        self.sbis_main_page.click_download_local_versions()
        self.sbis_download_page.click_plugin()
        size_web_installer = self.sbis_download_page.get_size_web_text(DownloadLocators.WEB_INSTALLER_DOWNLOAD)
        path_web_installer = self.sbis_download_page.download_web_installer()
        assert self.sbis_download_page.file_is_downloaded(path_web_installer), "File isn't downloaded"
        size_download_file = self.sbis_download_page.get_size_download_file(path_web_installer)
        assert size_web_installer == size_download_file, "The downloaded file size isn't equal to the website"
