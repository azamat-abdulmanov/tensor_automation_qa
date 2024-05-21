from selenium.webdriver.common.by import By


class MainPageLocators:
    CONTACTS_HEADER = (By.XPATH, "(//a[@href='/contacts'])[1]")
    CLOSE_COOCIE_AGREEMENT_BUTTON = (By.XPATH, '//div[contains(@class, "sbis_ru-CookieAgreement__close")]')
    LOCAL_VERSIONS = (By.LINK_TEXT, "Скачать локальные версии")


class ContactsPageLocators:
    TENSOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")
    REGION_CHOOSER_BUTTON = (By.XPATH, "(//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')])[1]")
    PARTNERS = (
        By.XPATH,
        "//div[contains(@class, 'sbisru-Contacts-City__item-name sbisru-link pr-4 pr-xm-8 sbisru-text-main')]")


class DownloadLocators:
    PLUGIN_BUTTON = (By.XPATH, "//div[@data-id='plugin']")
    WINDOWS_BUTTON = (By.ID, "ws-2pw9upz1ria1715942210274")
    WEB_INSTALLER_DOWNLOAD = (By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")