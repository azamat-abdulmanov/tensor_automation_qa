import pytest
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_download_page import SbisDownloadPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

class BaseTest:
    sbis_main_page: SbisMainPage
    sbis_contacts_page: SbisContactsPage
    sbis_download_page: SbisDownloadPage
    tensor_main_page: TensorMainPage
    tensor_about_page: TensorAboutPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.sbis_main_page = SbisMainPage(driver)
        request.cls.sbis_contacts_page = SbisContactsPage(driver)
        request.cls.sbis_download_page = SbisDownloadPage(driver)
        request.cls.tensor_main_page = TensorMainPage(driver)
        request.cls.tensor_about_page = TensorAboutPage(driver)
