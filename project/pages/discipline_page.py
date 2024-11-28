from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DisciplinePage(BasePage):
    def create_discipline(self, discipline_name, course_id):
        """Cria uma disciplina vinculada a um curso."""
        self.type((By.ID, "discipline-nome"), discipline_name)
        self.type((By.ID, "course-discipline-id"), course_id)
        self.click((By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn"))

    def enroll_student_in_discipline(self, student_id, discipline_id):
        """Inscreve um aluno em uma disciplina."""
        self.type((By.ID, "subscribe-student-id"), student_id)
        self.type((By.ID, "subscribe-discipline-id"), discipline_id)
        self.click((By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn"))

