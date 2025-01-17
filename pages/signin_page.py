from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_INPUT = (By.ID, 'ap_email')

    def verify_signin_opened(self):
        actual_text = self.driver.find_element(*self.SIGNIN_HEADER).text
        assert actual_text == 'Sign in', f'Expected Sign in but got {actual_text}'
        # Verify email field present
        self.driver.find_element(*self.EMAIL_INPUT)