from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CoursePage(BasePage):
    def create_course(self, course_name):
        """Cria um curso com o nome especificado."""
        self.type((By.ID, "course-nome"), course_name)
        self.click((By.ID, "course-btn"))
    
    def enroll_student_in_course(self, student_id, course_id):
        """Inscreve um aluno em um curso."""
        self.type((By.ID, "student-id"), student_id)
        self.type((By.ID, "course-id"), course_id)
        self.click((By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn"))


