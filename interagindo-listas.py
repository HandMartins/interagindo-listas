from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class CursoAutomacao:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe',options=chrome_options)
        
        
    def Iniciar(self):    
        self.driver.get("https://cursoautomacao.netlify.app/desafios.html")
        #self.driver.find_element_by_css_selector('a[href*="/desafios.html"]').click()

        lista_botoes_motos = self.driver.find_elements_by_css_selector('input[name="motos"]')

        for contador in range(0, len(lista_botoes_motos)):
            if (contador == 1 or contador == 3 or contador >= 4):
                self.driver.execute_script('arguments[0].click()', lista_botoes_motos[contador])

        self.preencheCity()        
        self.clicaBotoes()
        self.driver.close()        



    def preencheCity(self):
        lista_campo_cidade = self.driver.find_elements_by_css_selector('input[class="form-control cidadesinput"]')
        for index in lista_campo_cidade:
            index.send_keys('Brasília')

            
    def clicaBotoes(self):
        lista_sec = self.driver.find_elements_by_xpath('//button[contains(@onclick,"display:none")]')
        for elementos in lista_sec:
            self.driver.execute_script('arguments[0].click()', elementos)

    print("Fechando programa")
               

curso = CursoAutomacao()
curso.Iniciar()     




