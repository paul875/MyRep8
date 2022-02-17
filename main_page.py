from selenium.webdriver.common.by import By


class mainPage:
    def __init__(self, driver, base):
        driver.get(base)
        self.link_pay = driver.find_element(By.CLASS_NAME, 'b-header-b-sec-menu-e-link')
        self.link_cert = driver.find_element(By.XPATH, '//li[2]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_rating = driver.find_element(By.XPATH, '//li[3]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_new = driver.find_element(By.XPATH, '//li[4]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_discount = driver.find_element(By.XPATH, '//li[5]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_contacts = driver.find_element(By.XPATH, '//li[9]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_support = driver.find_element(By.XPATH, '//li[10]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_map = driver.find_element(By.XPATH, '//li[11]/a[@class="b-header-b-sec-menu-e-link"]')
        self.link_basket = driver.find_element(By.CLASS_NAME, "b-header-b-personal-e-icon-count-m-cart")
        self.edit_search = driver.find_element(By.ID, 'search-field')
        self.search_submit = driver.find_element(By.CLASS_NAME, 'b-header-b-search-e-srch-icon')

    def link_pay_click(self):
        self.link_pay.click()

    def link_cert_click(self):
        self.link_cert.click()

    def link_rating_click(self):
        self.link_rating.click()

    def link_new_click(self):
        self.link_new.click()

    def link_discount_click(self):
        self.link_discount.click()

    def link_contacts_click(self):
        self.link_contacts.click()

    def link_support_click(self):
        self.link_support.click()

    def link_map_click(self):
        self.link_map.click()

    def get_basket_quan(self):
        return self.link_basket.text

    def set_search(self, str1):
        self.edit_search.send_keys(str1)

    def search_click(self):
        self.search_submit.click()
