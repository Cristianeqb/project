import pytest
from selenium import webdriver
from pages.student_page import StudentPage
from pages.course_page import CoursePage
from pages.discipline_page import DisciplinePage

@pytest.fixture
def driver():
    """Configuração do WebDriver."""
    driver = webdriver.Chrome()
    driver.get("https://tdd-detroid.onrender.com//")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_complete_flow(driver):
    # Instanciando as páginas
    student_page = StudentPage(driver)
    course_page = CoursePage(driver)
    discipline_page = DisciplinePage(driver)

    # Passo 1: Criar aluno
    student_page.create_student("Cristiane")

    # Passo 2: Criar três cursos
    course_page.create_course("Relações Públicas")
    course_page.create_course("Geografia")
    course_page.create_course("Medicina")

    # Passo 3: Inscrever aluno no curso de ID 1 (Relações Públicas)
    course_page.enroll_student_in_course(student_id="1", course_id="1")

    # Passo 4: Criar três matérias no curso de ID 1
    discipline_page.create_discipline("Fotografia", course_id="1")
    discipline_page.create_discipline("Sociologia", course_id="1")
    discipline_page.create_discipline("Matemática", course_id="1")

    # Passo 5: Inscrever aluno nas três matérias
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="1")
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="2")
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="3")



