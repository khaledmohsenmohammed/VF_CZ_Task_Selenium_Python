from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
import time

class TestBasket:
    driver = None

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.vodafone.cz/")
        yield
        # Teardown
        self.driver.quit()

    @allure.description("Test to verify adding an iPhone to the basket.")
    @allure.feature("Shopping Cart")
    @allure.story("User should be able to add an iPhone to the cart.")
    def test_add_to_basket(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Wait for the cookies popup and click "Accept Cookies"
        cookies_pop_up = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='homepage']/div[8]/div/p[2]/button[1]")))
        cookies_pop_up.click()

        # Wait for "Obchod" (Shop) menu and hover over it
        obchod = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Obchod']")))
        actions = ActionChains(driver)
        actions.move_to_element(obchod).perform()

        # Wait for the iPhone link and click it
        iphone = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='vf-header']/div[3]/div/div[1]/div[2]/div/nav/ul/li[4]/ul/li[2]/ul/li[1]/a")))
        actions.click(iphone).perform()

        # Wait for the first iPhone product link and click it
        first_iphone = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='product_apple-iphone-16-128-gb:iphone16128b']/div/div[2]/div/p[1]/a")))
        first_iphone.click()

        # Validate page title contains "iPhone"
        try:
            page_title = driver.title
            assert "iPhone" in page_title, "The page title does not contain 'iPhone'."
            print("Assertion passed. The page title contains 'iPhone'.")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

        # Wait for "Add to Cart" button and click it
        add_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='add_to_cart_button button smallTypo' and contains(@href, 'cart=add')]")))
        add_button.click()
        time.sleep(2)

        # Validate header confirming the item was added to the cart
        try:
            header_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/h1")))
            actual_text = header_element.text
            assert actual_text == "Do košíku jste vložili novou položku", "The header text does not match."
            print("Assertion passed. The header contains the expected text.")
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
            raise RuntimeError("Test failed due to an unexpected error.") from e
