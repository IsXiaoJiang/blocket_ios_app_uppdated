from model.common_fun import Common
from model.loginView import LoginView
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
from time import sleep
from selenium.webdriver.common.by import By



class SparadeTest(Common):

    def sparade_action(self):
        print("--------------------Click on the sparade-----------------------------------------------")
        Sparade = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND name='Sparade' ")
        self.execute_tap(Sparade)
        sleep(2)
        loggain_button = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND name='Logga in & kom igång!' ")
        self.execute_tap(loggain_button)
        sleep(2)
        print("--------------------Log in--------------------------------------------------------")
        hi = LoginView(self.driver)
        hi.login_action('760800543@qq.com')
        sleep(2)
        self.assert_if_element_exist("Du har inga bevakningar")
        sleep(1)
        print("--------------------Click on Annonser--------------------------------------------")
        annonser = self.driver.find_element_by_accessibility_id("Annonser")
        self.execute_tap(annonser)
        sleep(1)
        filter = self.driver.find_element_by_accessibility_id("Filtrera")
        self.execute_tap(filter)
        print("--------------------Click on rensa------------------------------------")
        sleep(1)
        rensa = self.driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="Rensa (1)"]')
        self.execute_tap(rensa)
        print("--------------------Click on Visa x träffar----------------------------------------")
        self.driver.implicitly_wait(2)
        result = self.driver.find_element_by_accessibility_id("Visa Resultat")
        self.execute_tap(result)
        print("--------------------Click on hjärta för att spara bevakningar----------------------")
        adwatch_heart = self.find_element(By.XPATH,
                                          "//XCUIElementTypeButton[@name='Säljes i hela Sverige']/following-sibling::XCUIElementTypeButton")
        self.execute_tap(adwatch_heart)
        sleep(3)
        print("--------------------if there is ja,Click on ja ------------------------------------")
        try:
            ja = self.driver.find_element_by_accessibility_id("Ja")
        except NoSuchElementException:
            print('ej ja')
        else:
            self.execute_tap(ja)
        print("--------------------Click on the searchbar-----------------------------------------------")
        sleep(3)
        searchbar =self.driver.find_element_by_accessibility_id("search_textfield_contentView")
        self.execute_tap(searchbar)
        sleep(3)
        print("--------------------clear text-----------------------------------------------")
        clear_text = self.driver.find_element_by_accessibility_id("Rensa text")
        self.execute_tap(clear_text)
        search = self.driver.find_element_by_accessibility_id("Search")
        self.execute_tap(search)
        print("--------------------Click on hjärta för att spara bevakningar----------------------")
        adwatch_heart = self.find_element(By.XPATH,
                                          "//XCUIElementTypeButton[@name='Säljes i hela Sverige']/following-sibling::XCUIElementTypeButton")
        self.execute_tap(adwatch_heart)
        sleep(2)
        print("--------------------if there is ja,Click on ja ------------------------------------")
        try:
            ja = self.driver.find_element_by_accessibility_id("Ja")
        except NoSuchElementException:
            print('ej ja')
        else:
            self.execute_tap(ja)
        print("--------------------Click on the sparade-----------------------------------------------")
        Sparade = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND name='Sparade' ")
        self.execute_tap(Sparade)
        sleep(2)
        bevakningar=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND name='Bevakningar' ")
        self.execute_tap(bevakningar)
        sleep(2)
        print("--------------------click on Pushnotiser ------------------------------------")
        Pushnotiser = self.driver.find_element_by_accessibility_id("Pushnotiser")
        self.execute_tap(Pushnotiser)
        switch = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeSwitch' AND name='Alla kategorier, Hela Sverige' ")
        self.execute_tap(switch)
        sleep(1)
        self.driver.back()
        print("--------------------click on Alla ------------------------------------")
        Alla = self.driver.find_element_by_accessibility_id("Alla")
        self.execute_tap(Alla)
        sleep(1)
        bevakningar = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND name='Bevakningar' ")
        self.execute_tap(bevakningar)
        print("--------------------click on Ändra------------------------------------")
        alter= self.driver.find_element_by_accessibility_id("Ändra")
        self.execute_tap(alter)
        print("--------------------ta bort en av bevakningar ------------------------------------")
        delete= self.driver.find_element_by_accessibility_id("Radera Alla kategorier, Hela Sverige")
        self.execute_tap(delete)
        sleep(1)
        radera = self.driver.find_element_by_accessibility_id("Radera")
        self.execute_tap(radera)
        sleep(1)
        klar = self.driver.find_element_by_accessibility_id("Klar")
        self.execute_tap(klar)
        self.assert_if_element_exist("Bilar inte till salu 2st, Alla kategorier, Hela Sverige")
        sleep(1)
        bevakningar = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeStaticText' AND name='Bevakningar' ")
        self.execute_tap(bevakningar)
        print("--------------------click on Ändra------------------------------------")
        alter = self.driver.find_element_by_accessibility_id("Ändra")
        self.execute_tap(alter)
        print("--------------------ta bort bevakningar ------------------------------------")
        delete = self.driver.find_element_by_accessibility_id("Radera Bilar inte till salu 2st, Alla kategorier, Hela Sverige")
        self.execute_tap(delete)
        sleep(1)
        radera = self.driver.find_element_by_accessibility_id("Radera")
        self.execute_tap(radera)
        sleep(1)
        self.assert_if_element_exist("Du har inga bevakningar")

















