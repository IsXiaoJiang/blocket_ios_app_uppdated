from model.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By



class AiBilarTest(Common):

    def aiBilar_action(self):
        nyAnnons=self.driver.find_element_by_accessibility_id("Ny annons")
        self.execute_tap(nyAnnons)
        '''
        print("-------------------Tap on Omslagsbild-------------------------")
        Omslagsbild=self.driver.find_element_by_accessibility_id("Omslagsbild")
        actions.tap(Omslagsbild)
        actions.perform()
        try:
            OK=self.driver.find_element_by_accessibility_id("OK")
        except NoSuchAttributeException:
            print("Search function has problem")
        else:
            actions.tap(OK)
            actions.perform()
        '''
        valjKategori =self.driver.find_element_by_accessibility_id("Välj kategori")
        self.execute_tap(valjKategori)
        sleep(2)
        #Fordon = self.driver.find_element(By.XPATH,'//XCUIElementTypeStaticText[@name="Fordon"]')
        Fordon =self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND label='Fordon' ")
        self.execute_tap(Fordon)
        sleep(3)
        Bilar= self.driver.find_element_by_accessibility_id("Bilar")
        #Bilar = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND label='Bilar' ")
        self.execute_tap(Bilar)
        self.driver.implicitly_wait(2)
        saljes = self.driver.find_element_by_accessibility_id("Säljes")
        self.execute_tap(saljes)
        sleep(1)
        self.klar_button()
        self.swipeUpLess()
        print("--------------------Set value to postnummer---------------------------")
        postnummer = self.find_element(By.XPATH,"//XCUIElementTypeStaticText[@name='Postnummer']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(postnummer)
        postnummer.set_value('12333')
        self.klar_button
        self.assert_if_element_exist("type=='XCUIElementTypeTextField' AND value='12333' ")
        print("--------------------Set value to Reg.nr.---------------------------")
        regNr = self.find_element(By.XPATH,"//XCUIElementTypeStaticText[@name='Reg.nr.']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(regNr)
        regNr.set_value('abc123')
        self.klar_button()
        self.assert_if_element_exist("type=='XCUIElementTypeTextField' AND value='abc123' ")
        registreringsnummer=self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeSwitch' AND label='Svenskt registreringsnummer saknas' ")
        self.execute_tap(registreringsnummer)
        modelyear = self.driver.find_element_by_accessibility_id("Modellår")
        self.execute_tap(modelyear)
        sleep(2)
        picker = self.driver.find_element_by_xpath('//XCUIElementTypePickerWheel')
        picker.set_value('2019')
        self.klar_button()
        miltal = self.driver.find_element_by_accessibility_id("Miltal")
        self.execute_tap(miltal)
        picker = self.driver.find_element_by_xpath('//XCUIElementTypePickerWheel')
        picker.set_value('500 - 999')
        self.klar_button()
        Vaxellada = self.driver.find_element_by_accessibility_id("Växellåda")
        self.execute_tap(Vaxellada)
        picker = self.driver.find_element_by_xpath('//XCUIElementTypePickerWheel')
        picker.set_value('Automat')
        self.klar_button()
        #Bränsle =  self.driver.find_element_by_accessibility_id("Bränsle")
        Bränsle = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND label='Bränsle' ")
        self.execute_tap(Bränsle)
        picker = self.driver.find_element_by_xpath('//XCUIElementTypePickerWheel')
        picker.set_value('Diesel')
        self.klar_button()
        self.swipeup()
        Biltyp = self.driver.find_element_by_accessibility_id("Biltyp")
        self.execute_tap(Biltyp)
        picker = self.driver.find_element_by_xpath('//XCUIElementTypePickerWheel')
        picker.set_value('Kombi')
        self.klar_button()
        #self.swipeup()
        print("--------------------Set value to Rubrik---------------------------")
        Rubrik = self.find_element(By.XPATH,
                                  "//XCUIElementTypeStaticText[@name='Rubrik']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(Rubrik)
        Rubrik.set_value('xiao testar kategori bilar')
        self.klar_button()
        self.assert_if_element_exist("type=='XCUIElementTypeTextField' AND value='xiao testar kategori bilar' ")
        print("--------------------Set value to Beskrivning av varan---------------------------")
        Beskrivning = self.find_element(By.XPATH,
                                   "//XCUIElementTypeStaticText[@name='Beskrivning av varan']/following-sibling::XCUIElementTypeTextView")
        self.execute_tap(Beskrivning)
        Beskrivning.set_value('xiao testar kategori bilar')
        self.klar_button()
        self.assert_if_element_exist("type=='XCUIElementTypeTextField' AND value='xiao testar kategori bilar' ")
        print("--------------------Set value to Pris---------------------------")
        Pris = self.find_element(By.XPATH,
                                   "//XCUIElementTypeStaticText[@name='Pris']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(Pris)
        Pris.set_value('666')
        self.klar_button()
        self.assert_if_element_exist("type=='XCUIElementTypeTextField' AND value='666' ")
        valjPlats = self.driver.find_element_by_accessibility_id("Välj plats")
        self.execute_tap(valjPlats)
        Stockholm = self.driver.find_element_by_accessibility_id("Stockholm")
        self.execute_tap(Stockholm)
        print("---------Swipeup so i can see stockholm stad----------------------------")
        self.swipeup()
        stockholm_stad = self.driver.find_element_by_accessibility_id("Stockholms Stad")
        self.execute_tap(stockholm_stad)
        sleep(5)
        Bromma = self.driver.find_element_by_accessibility_id("Bromma")
        self.execute_tap(Bromma)
        self.driver.implicitly_wait(2)
        self.swipeUpLess()
        print("--------------------Set value to 'name'---------------------------------")
        Name = self.find_element(By.XPATH,
                                        "//XCUIElementTypeStaticText[@name='Namn']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(Name)
        Name.set_value('Xiao Jiang')
        self.driver.implicitly_wait(3)
        print("--------------------Set value to 'Mejladress'---------------------------------")
        Mail= self.find_element(By.XPATH,
                                 "//XCUIElementTypeStaticText[@name='Mejladress']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(Mail)
        Mail.set_value('xiaojiang@test.com')
        self.driver.implicitly_wait(2)
        print("--------------------Set value to 'Telefon'---------------------------------")
        Telefon = self.find_element(By.XPATH,
                                 "//XCUIElementTypeStaticText[@name='Telefon']/preceding-sibling::XCUIElementTypeTextField")
        self.execute_tap(Telefon)
        self.telephone_action()
        sleep(1)
        print("--------------------Turn on /off temporarily telephone nummer------------------")
        hideNummber= self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeSwitch' AND label='Tillfälligt telefonnummer (+10kr)' ")
        self.execute_tap(hideNummber)
        self.execute_tap(hideNummber)
        print("--------------------Turn on temporarily telephone nummer----------------------")
        hideNummber = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeSwitch' AND label='Dölj telefonnumret' ")
        self.execute_tap(hideNummber)
        print("--------------------Cick on 'Förhandsgranska annons'----------------------")
        Preview = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND label='Förhandsgranska annons' ")
        self.execute_tap(Preview)
        print("--------------------close view 'Förhandsgranska annons'----------------------")
        close = self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(close)
        print("--------------------press 'Fortsätt'---------------------------------------")
        Continue = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeStaticText' AND label='Fortsätt' ")
        self.execute_tap(Continue)
        '''
        print("--------------------Turn on /off extraTjänster------------------")
        extra= self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeSwitch' AND label='Fri vägassistans i 3 mån' ")
        self.execute_tap(extra)
        self.execute_tap(extra)
        print("--------------------press 'Fortsätt'---------------------------------------")
        Continue = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeStaticText' AND label='Fortsätt' ")
        self.execute_tap(Continue)
        '''
        print("--------------------Turn on /off veckoförnelse-----------------")
        veckofornelse = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeSwitch' AND label='Veckoförnyelse, Din annons hamnar högst upp i listan på Blocket varje vecka i max 7 veckor., Lägg till Veckoförnyelse (+290kr)' ")
        self.execute_tap(veckofornelse)
        self.execute_tap(veckofornelse)
        print("--------------------press 'Fortsätt'---------------------------------------")
        Continue = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeStaticText' AND label='Fortsätt' ")
        self.execute_tap(Continue)
        print("--------------------Set value to 'Lösenord'---------------------------------")
        password = self.find_element(By.XPATH,
                                 "//XCUIElementTypeStaticText[@name='Lösenord']/preceding-sibling::XCUIElementTypeSecureTextField")
        self.execute_tap(password)
        password.set_value('11111')
        print("--------------------Set value to 'Lösenord'---------------------------------")
        password = self.find_element(By.XPATH,
                                     "//XCUIElementTypeStaticText[@name='Upprepa lösenord']/preceding-sibling::XCUIElementTypeSecureTextField")
        self.execute_tap(password)
        password.set_value('11111')
        print("--------------------press 'Fortsätt'---------------------------------------")
        Continue = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeStaticText' AND label='Fortsätt' ")
        self.execute_tap(Continue)
        sleep(3)
        print("--------------------press 'Swish'---------------------------------------")
        Swish = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND name='Swish' ")
        self.execute_tap(Swish)
        sleep(3)
        print("--------------------press 'Tillbaka'---------------------------------------")
        Tillbaka = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND label='Tillbaka' ")
        self.execute_tap(Tillbaka)
        sleep(4)
        print("--------------------press 'Ok' again if needs--------------------------------------")
        try:
            Ok = self.driver.find_element(By.XPATH,'//XCUIElementTypeButton[@name="Ok"]')
        except NoSuchElementException:
            print('ej Ok')
        else:
            self.execute_tap(Ok)
        sleep(3)
        print("--------------------press 'Swish' again---------------------------------------")
        Swish = self.driver.find_element_by_accessibility_id("Swish")
        self.execute_tap(Swish)
        sleep(4)
        print("--------------------press 'Tillbaka' again---------------------------------------")
        Tillbaka = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND label='Tillbaka' ")
        self.execute_tap(Tillbaka)
        print("--------------------press 'Ok' again if needs--------------------------------------")
        sleep(4)
        try:
            Ok=self.driver.find_element_by_accessibility_id("Ok")
        except NoSuchElementException:
            print('ej Ok')
        else:
            self.execute_tap(Ok)
            sleep(3)
        print("--------------------press 'Kortbetalning'---------------------------------------")
        Kortbetalning= self.driver.find_element_by_accessibility_id("Kortbetalning")
        self.execute_tap(Kortbetalning)
        sleep(4)
        print("--------------------press 'Tillbaka'---------------------------------------")
        Tillbaka = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND label='Tillbaka' ")
        self.execute_tap(Tillbaka)
        sleep(4)
        print("--------------------press 'Ok' again if needs--------------------------------------")
        try:
            Ok=self.driver.find_element_by_accessibility_id("Ok")
        except NoSuchElementException:
            print('ej Ok')
        else:
            self.execute_tap(Ok)
        sleep(4)
        print("--------------------press 'Kortbetalning' again---------------------------------------")
        Kortbetalning = self.driver.find_element_by_accessibility_id("Kortbetalning")
        self.execute_tap(Kortbetalning)
        sleep(4)
        print("--------------------press 'tillbaka' again---------------------------------------")
        Tillbaka = self.driver.find_element_by_ios_predicate(
            "type=='XCUIElementTypeButton' AND label='Tillbaka' ")
        self.execute_tap(Tillbaka)
        sleep(3)
        try:
            Ok=self.driver.find_element_by_accessibility_id("Ok")
        except NoSuchElementException:
            print('ej Ok')
        else:
            self.execute_tap(Ok)
            sleep(3)
        print("--------------------press 'Telefonbetalning'---------------------------------------")
        Telefonbetalning = self.driver.find_element_by_accessibility_id("Telefonbetalning")
        self.execute_tap(Telefonbetalning)
        sleep(3)
        print("--------------------press 'stäng'---------------------------------------")
        close = self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(close)