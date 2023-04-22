import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from decorators import social_login_required
import config


def create_fake_user():
    faker = Faker()
    data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password(length=8),
            }

    return data


class SocialNetworkScraper:

    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    REGISTER_URL = f"{BASE_URL}/auth/register"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self, driver=None, fake: bool = False, delay: int = 0):
        self.driver = driver or self.create_driver()
        self.delay = delay
        self.is_logged_in = False
        self.is_registered = False
        if fake:
            self.data = create_fake_user()
        else:
            self.data = {
                "username": config.SOCIAL_NETWORK_LOGIN,
                "email": config.SOCIAL_NETWORK_EMAIL,
                "password": config.SOCIAL_NETWORK_PASSWORD,
            }

    def create_driver(self):
        """
        Create chrome driver instance
        """
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            self.driver.maximize_window()
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_register(self):
        self.driver.get(self.REGISTER_URL)
        time.sleep(self.delay)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(self.data.get("username"))
        time.sleep(self.delay)

        email_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        email_elem.send_keys(self.data.get("email"))
        time.sleep(self.delay)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(self.data.get("password"))
        time.sleep(self.delay)

        confirm_password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='confirm_password']")
        confirm_password_elem.send_keys(self.data.get("password"))
        time.sleep(self.delay)

        password_elem.send_keys(keys.Keys.ENTER)
        time.sleep(self.delay)
        self.is_registered = True

    def social_network_login(self):
        """
        Log in to social-network
        """

        # navigate to login page
        self.driver.get(self.LOGIN_URL)
        time.sleep(self.delay)

        # set username
        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(self.data.get("username"))
        time.sleep(self.delay)

        # set password
        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(self.data.get("password"))
        time.sleep(self.delay)

        # log-in by pressing Enter
        password_elem.send_keys(keys.Keys.ENTER)
        time.sleep(self.delay)
        self.is_logged_in = True

    @social_login_required
    def social_network_add_post(self, title, content, fake=False):
        if fake:
            faker = Faker()
            title, content = faker.sentence(), faker.paragraph()

        # Create automated post on social-network
        self.driver.get(self.BLOG_URL)
        time.sleep(self.delay)

        # set title

        title_elem = self.driver.find_element(By.ID, "title")
        title_elem.send_keys(title)
        time.sleep(self.delay)

        # set content
        content_elem = self.driver.find_element(By.ID, "content")
        content_elem.send_keys(content)
        time.sleep(self.delay)

        # click Create post button
        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(self.delay)
        # like new post
        like_elem = self.driver.find_elements(By.XPATH, "//a[@class='btn btn-sm btn-outline-primary']")[0]
        like_elem.click()
        time.sleep(self.delay)
        # logout
        logout_elem = self.driver.find_element(By.XPATH, "//a[@href='/auth/logout']")

        logout_elem.click()
        time.sleep(self.delay)
        return self.driver
