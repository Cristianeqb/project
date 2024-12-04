import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.student_page import StudentPage
from pages.course_page import CoursePage
from pages.discipline_page import DisciplinePage


@pytest.fixture
def driver():
    """Configuração do WebDriver."""
    driver = webdriver.Chrome()
    driver.get("https://tdd-detroid.onrender.com/")
    driver.maximize_window()

    # Sincronizador para aguardar a tela carregar completamente
    driver.set_window_size(970, 555)
    elements = driver.find_elements(By.CSS_SELECTOR, ".smooth")
    while len(elements) > 0:
        elements = driver.find_elements(By.CSS_SELECTOR, ".smooth")
        sleep(1)

    yield driver
    driver.quit()


def test_complete_flow(driver):
    # Instanciando as páginas
    student_page = StudentPage(driver)
    course_page = CoursePage(driver)
    discipline_page = DisciplinePage(driver)

    # Passo 1: Criar aluno
    student_page.create_student("Cristiane")
    # Validação
    assert (
        "INFO Added student id: 1, Name: Cristiane"
        in driver.find_element(By.CSS_SELECTOR, ".py-p").text
    )

    # Passo 2: Criar três cursos
    course_page.create_course("Relações Públicas")
    course_page.create_course("Geografia")
    course_page.create_course("Medicina")
    # Validação
    assert "Relações Públicas" in driver.page_source
    assert "Geografia" in driver.page_source
    assert "Medicina" in driver.page_source

    # Passo 3: Inscrever aluno no curso de ID 1 (Relações Públicas)
    course_page.enroll_student_in_course(student_id="1", course_id="1")
    # Validação
    print(driver.page_source)  # Ajuda na depuração, remova após confirmar o texto correto
    assert "INFO Student id 1 subscribed to course id 1" in driver.page_source

    # Passo 4: Criar três matérias no curso de ID 1
    discipline_page.create_discipline("Fotografia", course_id="1")
    discipline_page.create_discipline("Sociologia", course_id="1")
    discipline_page.create_discipline("Matemática", course_id="1")
    # Validação
    assert "Fotografia" in driver.page_source
    assert "Sociologia" in driver.page_source
    assert "Matemática" in driver.page_source

    # Passo 5: Inscrever aluno nas três matérias
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="1")
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="2")
    discipline_page.enroll_student_in_discipline(student_id="1", discipline_id="3")
    # Validação
    assert "INFO Enrolled student id: 1 in discipline id: 1" in driver.page_source
    assert "INFO Enrolled student id: 1 in discipline id: 2" in driver.page_source
    assert "INFO Enrolled student id: 1 in discipline id: 3" in driver.page_source
