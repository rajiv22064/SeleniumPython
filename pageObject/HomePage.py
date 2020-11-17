from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    Search = (By.XPATH, "//*[@type='search']")
    AddToCart = (By.XPATH, "//button[text()='ADD TO CART']")
    Cart_Icon = (By.XPATH, "//*[@class='cart-icon']/img")
    Proceed_ToCheckOut = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")


    def SearchBar(self):
        return self.driver.find_element(*HomePage.Search)

    def AddToCartItem(self):
        return self.driver.find_elements(*HomePage.AddToCart)

    def CartIcon(self):
        return self.driver.find_element(*HomePage.Cart_Icon)

    def ProceedToCheckOut(self):
        return self.driver.find_element(*HomePage.Proceed_ToCheckOut)









