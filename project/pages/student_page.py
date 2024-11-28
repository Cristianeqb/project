from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class StudentPage(BasePage):
    def create_student(self, name):
        """Cria um aluno com o nome especificado."""
        self.type((By.ID, "student-nome"), name)
        self.click((By.ID, "student-btn"))


