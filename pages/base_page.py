from selenium.webdriver import Chrome, Firefox, Safari, Edge, ChromiumEdge, Ie

class BasePage():
    
    def __init__(self, browser: Chrome | Firefox | Safari | Edge | ChromiumEdge | Ie, url: str):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)