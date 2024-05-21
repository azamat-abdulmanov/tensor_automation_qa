from selenium.webdriver.common.by import By


class MainPageLocators:
    STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']/p")
    DETAIL_STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, "//a[@href='/about']")


class AboutPageLocators:
    WORKING_BLOCK = (By.XPATH, "//h2[contains(text(), 'Работаем')]")
    IMAGES_WORKING_BLOCK = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper' ]/img")
