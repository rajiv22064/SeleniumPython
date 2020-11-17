from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)

        itemList1 = []
        itemList2 = []

        homePage.SearchBar().send_keys("ber")
        time.sleep(3)

        ItemsFound = homePage.AddToCartItem()
        print(len(ItemsFound))

        for item in ItemsFound:
            # ItemName = item.find_element_by_xpath("parent::div/parent::div/h4").text
            ItemName = item.find_element_by_xpath("../../h4").text
            itemList1.append(ItemName)
            item.click()

        print(itemList1)

        # Add to cart
        homePage.CartIcon().click()
        homePage.ProceedToCheckOut().click()

        self.PresenseOfElement("//*[@class='promoBtn']")

        CartItem = self.driver.find_elements_by_xpath("//*[@class='product-name']")
        print(len(CartItem))

        for cartI in CartItem:
            CItem = cartI.text
            print(CItem)
            itemList2.append(CItem)

        print(itemList2)
        assert itemList1 == itemList2


