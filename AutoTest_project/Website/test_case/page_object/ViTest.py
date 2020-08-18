from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from model.common_fun import Common
from model.loginView import LoginView
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
from time import sleep



class Vi(Common):


    def vi_action(self,username, password):
        '''
        filter = self.driver.find_element_by_accessibility_id("Filtrera")
        self.execute_tap(filter)
        print("---------Click on plats----------------------------")
        plats_button = self.find_element(By.XPATH, "//XCUIElementTypeStaticText[@name='Plats']")
        self.execute_tap(plats_button)
        print("--------------Click on norrbotton-----------------------")
        norrbotton = self.find_element(By.XPATH, "(//XCUIElementTypeOther[@name='nedåt'])[2]")
        self.execute_tap(norrbotton)
        print("-----------välj arvidsjaur---------------")
        ostermalm = self.driver.find_element_by_accessibility_id("Arvidsjaur")
        self.execute_tap(ostermalm)
        klar = self.driver.find_element_by_accessibility_id("Klar")
        self.execute_tap(klar)
        print("--------------------Click on Visa x träffar----------------------------------------")
        result = self.driver.find_element_by_accessibility_id("Visa Resultat")
        self.execute_tap(result)
        sleep(2)
        '''
        searchbar = self.driver.find_element_by_accessibility_id("search_textfield_contentView")
        self.execute_tap(searchbar)
        sleep(1)
        clear = self.driver.find_element_by_accessibility_id("delete")
        for i in range(0, 10):
            self.execute_tap(clear)
        #searchbar.clear()
        print("-------------------Search with 'Bil röda super snygg'-------------------------")
        searchbar.set_value('Bil röda super snygg')
        print("-------------------Tap on 'search' on keyboard-------------------------")
        search = self.driver.find_element_by_accessibility_id("Search")
        self.execute_tap(search)
        print("-------------------Tap on the ad -----------------------------------")
        myAd = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND name='Bil röda super snygg' ")
        self.execute_tap(myAd)
        sleep(2)
        print("------------tryck på hjärta för att spara ad--------------------------")
        try:
            heart=self.find_elements(By.XPATH,"//XCUIElementTypeNavigationBar[@name='Blocket.PreviousNextViewAdContainer']/XCUIElementTypeButton[2]")
        except NoSuchElementException:
            print("it is old vi")
        else:
            self.execute_tap(heart)
        try:
            heart_oldVi=self.find_elements(By.XPATH,"//XCUIElementTypeNavigationBar[@name='BLPreviousNextContainer']/XCUIElementTypeButton[2]")
        except NoSuchElementException:
            print("it is new vi")
        else:
            self.execute_tap(heart_oldVi)
        print("------------logga in---------------------------------------------------")
        hi = LoginView(self.driver)
        hi.login_action("760800543@qq.com")
        sleep(2)
        print("------------tryck på sparade---------------------------------------------------")
        sparade = self.driver.find_element_by_accessibility_id("Sparade")
        self.execute_tap(sparade)
        print("------------sparade annonser-------------------------------------------")
        saveads=self.driver.find_element_by_accessibility_id("Sparade annonser")
        self.execute_tap(saveads)
        sleep(2)
        try:
            self.driver.find_element_by_accessibility_id("Ändra")
        except NoSuchAttributeException:
            print(" the function of save ad has prolem")
        sleep(2)
        Annonser=self.driver.find_element_by_accessibility_id("Annonser")
        self.execute_tap(Annonser)
        sleep(2)
        print("------------tryck på hjärta för att ta bort sparade ad----------------")
        try:
            heart=self.find_elements(By.XPATH,"//XCUIElementTypeNavigationBar[@name='Blocket.PreviousNextViewAdContainer']/XCUIElementTypeButton[2]")
        except NoSuchElementException:
            print("it is old vi")
        else:
            self.execute_tap(heart)
        try:
            heart_oldVi=self.find_elements(By.XPATH,"//XCUIElementTypeNavigationBar[@name='BLPreviousNextContainer']/XCUIElementTypeButton[2]")
        except NoSuchElementException:
            print("it is new vi")
        else:
            self.execute_tap(heart_oldVi)
        '''
        sparade = self.driver.find_element_by_accessibility_id("Sparade")
        self.execute_tap(sparade)
        try:
            self.driver.find_element_by_accessibility_id("Inga annonser sparade")
        except NoSuchAttributeException:
            print(" the function of save ad has prolem")
        '''
        print("------------tryck på share button--------------------------------------")
        share=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='action share' ")
        self.execute_tap(share)
        avbryt=self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(avbryt)
        try:
            place=self.driver.find_element_by_accessibility_id("Plats")
        except NoSuchElementException:
            print('no plats')
        else:
            self.execute_tap(place)
            sleep(1)
            tillbaka=self.driver.find_element_by_accessibility_id("Tillbaka")
            self.execute_tap(tillbaka)
        self.swipeUpLess()
        print("------------if there is Extrauppgifter-------------------------------")
        try:
            Extrauppgifter=self.driver.find_element_by_accessibility_id("Från Bytbil")
        except NoSuchElementException:
            print('no Extrauppgifter')
        else:
            self.execute_tap(Extrauppgifter)
            tillbaka=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='Tillbaka' ")
            self.execute_tap(tillbaka)
        print("------------if there is inför köpet-------------------------------")
        try:
            inforKopet = self.driver.find_element_by_accessibility_id("Låna upp till 600 000 kr")
        except NoSuchElementException:
            print('no inforKopet')
        else:
            self.execute_tap(inforKopet)
            sleep(2)
            url=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeOther' AND name='URL' ")
            self.execute_tap(url)
            rensa= self.driver.find_element_by_accessibility_id("Rensa text")
            self.execute_tap(rensa)
            #url.clear()
            url.set_value('blocket://')
            sleep(1)
            ok=self.driver.find_element_by_accessibility_id("Go")
            self.execute_tap(ok)
            open=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeStaticText' AND name='Öppna' ")
            self.execute_tap(open)
            sleep(3)
        self.swipeUpLess()
        print("------------if there is Visa telefonnummer-------------------------------")
        try:
            telefonnummer=self.driver.find_element_by_ios_predicate(
                "type=='XCUIElementTypeButton' AND label='Visa telefonnummer' ")
            sleep(2)
        except:
            print('no visa telefonnummer')
        else:
            self.execute_tap(telefonnummer)
            sleep(1)
            tel=self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='070-576 09 27' ")
            self.execute_tap(tel)
            avbryt = self.driver.find_element_by_accessibility_id("Avbryt")
            self.execute_tap(avbryt)

        print("------------if there is  Skicka meddelande---------------------------------------")
        sleep(5)
        try:
            meddelande = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='Skicka meddelande' ")
        except Exception:
            print('no skcika meddelande')
        else:
            actions = TouchAction(self.driver)
            self.execute_tap(meddelande)
            sleep(2)
            avbryt = self.driver.find_element_by_accessibility_id("Avbryt")
            self.execute_tap(avbryt)
            sleep(1)
            self.execute_tap(meddelande)
            keyboardH = self.driver.find_element_by_accessibility_id("H")
            actions.tap(keyboardH)
            actions.perform()
            keyboardE = self.driver.find_element_by_accessibility_id("e")
            actions.tap(keyboardE)
            actions.perform()
            keyboardJ = self.driver.find_element_by_accessibility_id("j")
            actions.tap(keyboardJ)
            actions.perform()
            skicka = self.driver.find_element_by_accessibility_id("Skicka")
            self.execute_tap(skicka)
            try:
                toast_loc = self.find_element(By.XPATH, ".//*[contains(@text,'Ditt meddelande har skickats!')]")
                sleep(2)
            except NoSuchElementException:
                print('no toast')
            try:
                ja = self.driver.find_element_by_accessibility_id("Ja")
            except NoSuchElementException:
                print('ej ja')
            else:
                self.execute_tap(ja)
                tack=self.driver.find_element_by_accessibility_id("Nej tack")
                self.execute_tap(tack)


        print("------------if there is skicka mejl---------------------------------------")
        try:
            mejl = self.driver.find_element_by_ios_predicate(
                "type=='XCUIElementTypeButton' AND label='Skicka mejl' ")
            sleep(2)
        except NoSuchElementException:
            print('no visa melj')
        else:
            self.execute_tap(mejl)
            sleep(2)
            avbryt = self.driver.find_element_by_accessibility_id("Avbryt")
            self.execute_tap(avbryt)
            Radera=self.driver.find_element_by_accessibility_id("Radera utkast")
            self.execute_tap(Radera)
        print("------------if there is ' Digitalt köpekontrakt '-------------------------------------")
        try:
            digital_contract = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND name='Digitalt köpekontrakt' ")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(digital_contract)
            sleep(1)
            close=self.driver.find_element_by_accessibility_id("Stäng")
            self.execute_tap(close)
        self.swipeUpLess()
        print("------------if there is 'Starta Blocketbetalning '-------------------------------------")
        try:
         Blocketbetalning = self.driver.find_element_by_ios_predicate(
                "type=='XCUIElementTypeButton' AND name='Starta Blocketbetalning' ")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(Blocketbetalning)
            sleep(1)
            close = self.driver.find_element_by_accessibility_id("Stäng")
            self.execute_tap(close)
        self.swipeUpLess()
        print("------------if there is '	Kolla ditt kreditutrymme. '-------------------------------------")
        try:
            kreditutrymme= self.driver.find_element_by_ios_predicate(
                "type=='XCUIElementTypeButton' AND name='Kolla ditt kreditutrymme.' ")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(kreditutrymme)
            sleep(1)
            close = self.driver.find_element_by_accessibility_id("Stäng")
            self.execute_tap(close)


        print("------------click on ' andra ha även tittat på' ------------------------------")
        try:
            other_ads=self.find_element(By.XPATH,'//XCUIElementTypeOther[@name="ANDRA HAR ÄVEN TITTAT PÅ"]/following-sibling::XCUIElementTypeCell[1]')
        except NoSuchElementException:
            print("no such element")
        else:
            print('det finns andra har även tittat på----')
            self.execute_tap(other_ads)
            #self.execute_tap(other_ads)
            tillbaka = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='Tillbaka' ")
            self.execute_tap(tillbaka)

        self.driver.execute_script("mobile: scroll", {"direction": 'down'})
        print("------------click on ' Alla objekt i butiken '------------------------------")
        try:

            objekt = self.driver.find_element_by_accessibility_id("Alla objekt i butiken")
        except NoSuchElementException:
            print("no Alla objekt i butiken")
        else:
            self.execute_tap(objekt)

        print("------------click on ' Ta bort, ändra, förnya'------------------------------")
        try:

            change=self.driver.find_element_by_accessibility_id("Ta bort, ändra, förnya")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(change)
            sleep(2)
            Ok=self.driver.find_element_by_accessibility_id("OK")
            self.execute_tap(Ok)

        print("------------click on  'Anmäl annons '----------------------------------------")
        try:

            report = self.driver.find_element_by_accessibility_id("Anmäl annons")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(report)
            close=self.driver.find_element_by_accessibility_id("Stäng")
            self.execute_tap(close)

        print("------------click on ' Kundservice '----------------------------------------")
        kundservice=self.driver.find_element_by_accessibility_id("Kundservice")
        self.execute_tap(kundservice)
        print("------------click on ' stäng '----------------------------------------")
        close = self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(close)
        print("------------click on ' Tips och Inspiration'----------------------------------------")
        kundservice = self.driver.find_element_by_accessibility_id("Tips och Inspiration")
        self.execute_tap(kundservice)
        print("------------click on ' stäng '----------------------------------------")
        close = self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(close)
        print("------------click on ' Kundsäkerhet'----------------------------------------")
        kundservice = self.driver.find_element_by_accessibility_id("Kundsäkerhet")
        self.execute_tap(kundservice)
        print("------------click on ' stäng '----------------------------------------")
        close = self.driver.find_element_by_accessibility_id("Stäng")
        self.execute_tap(close)
        hi = LoginView(self.driver)
        hi.logout_action("xiaoqq")
        sleep(2)
        annonser = self.driver.find_element(By.XPATH,"//XCUIElementTypeButton[@name='Annonser']")
        self.execute_tap(annonser)
        try:

            change=self.driver.find_element_by_accessibility_id("Ta bort, ändra, förnya")
        except NoSuchElementException:
            print("no such element")
        else:
            self.execute_tap(change)
            sleep(2)
            hi.login_action_sendkeys('xiao.jiang@schibsted.com', 'nevermore5202')
            sleep(1)
            close = self.driver.find_element_by_accessibility_id("Stäng")
            self.execute_tap(close)
            sleep(1)
            change = self.driver.find_element_by_accessibility_id("Ta bort, ändra, förnya")
            self.execute_tap(change)
            andra=self.driver.find_element_by_accessibility_id("Ändra")
            self.execute_tap(andra)
            moveon=self.driver.find_element_by_accessibility_id("Fortsätt")
            self.execute_tap(moveon)
            avbryt= self.driver.find_element_by_accessibility_id("Avbryt")
            self.execute_tap(avbryt)
            hi.logout_action("xiaoschib")
            self.assert_if_element_exist("Logga in")

        '''

        try:
            meddelande = self.driver.find_element_by_ios_predicate("type=='XCUIElementTypeButton' AND label='Skicka meddelande' ")
        except Exception:
            print('no skcika meddelande')
        else:
            print('tryck på skicka meddelande')
            self.execute_tap(meddelande)
            hi = LoginView(self.driver)
            hi.login_action_sendkeys('760800543@qq.com','125803636jx')
            hi.logout_action("xiaoqq")
        '''