from abc import ABC
from pages.web_page import WebPage
from pages.main_page import MainBankPage
from playwright.sync_api import Page, expect
from hooks.generator_random_data import GenerateRandomData
from time import sleep


class ApplicationFormCard:
    def __init__(self, page: Page):
        self.page = page
        self.fio = GenerateRandomData.get_random_fio()
        self.mobile = GenerateRandomData.get_random_mobile()
        self.email = GenerateRandomData.get_random_email()
        self.gender = GenerateRandomData.get_random_gender()

    def fill_in_app_form(self):
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').scroll_into_view_if_needed()
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').click()
        self.page.keyboard.insert_text(self.fio)

        self.page.locator('//input[@data-test-id= "phoneInput"]').click()
        self.page.locator('//input[@data-test-id= "phoneInput"]').scroll_into_view_if_needed()
        self.page.keyboard.insert_text(self.mobile)

        self.page.locator('//input[@data-test-id= "email-input"]').click()
        self.page.keyboard.insert_text(self.email)

        self.page.locator(f'//button[@data-test-id="sex-{self.gender}"]').click()

        self.page.locator('(//div[@class="e1jwl"])[2]').set_checked(checked=True)


class CreditCardsPage(MainBankPage, WebPage, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/get-money/credit-cards/'
        self.app_form = ApplicationFormCard(page)

    def get_100_days_card(self):
        self.page.locator('//button[@data-test-id="button" and @text = "Получить карту"]').click()

        if "#anketa" not in self.page.url:
            raise Exception('Button of get credit card was not clicked!', self.page.url)
        self.app_form.fill_in_app_form()
        sleep(4)





