# Automação College Manager

Este projeto tem como objetivo automatizar o fluxo de criação de alunos, cursos, disciplinas e inscrições em um sistema acadêmico simulado. A automação é realizada utilizando o Selenium WebDriver para interação com a interface web e Pytest para execução e gerenciamento dos testes.

## Tecnologias Utilizadas
- **Selenium**: Ferramenta de automação para interação com o navegador.
- **Pytest**: Framework para testes automatizados.
- **Python 3.10+**: Linguagem utilizada para desenvolver a automação.
- **Google Chrome**: Navegador utilizado nos testes.
- **ChromeDriver**: Driver utilizado para interação com o navegador Google Chrome.

## Pré-requisitos
Antes de rodar os testes, é necessário garantir que o ambiente esteja configurado corretamente:

1. **Instalar o Python 3.10 ou superior**  
   Certifique-se de ter o Python 3.10 ou superior instalado na sua máquina. Você pode verificar sua versão do Python com o comando:
   ```bash
   python --version
Configuração do Ambiente
Clone este repositório: Clone o projeto para sua máquina local:

bash
Copiar código
git clone https://github.com/SeuUsuario/CollegeManagerAutomation.git
Instale as dependências: Navegue até a pasta do projeto e instale as dependências listadas no arquivo requirements.txt:

bash
Copiar código
cd CollegeManagerAutomation
pip install -r requirements.txt
Estrutura do Projeto
A estrutura do projeto segue o padrão para automação com Selenium e Pytest. Abaixo está a estrutura de pastas:

bash
Copiar código
CollegeManagerAutomation/
├── pages/                 # Páginas da aplicação para interação com o Selenium
│   ├── student_page.py    # Funções relacionadas à página de estudantes
│   ├── course_page.py     # Funções relacionadas à página de cursos
│   └── discipline_page.py # Funções relacionadas à página de disciplinas
├── tests/                 # Testes automatizados
│   └── test_college_manager.py  # Testes principais de criação de aluno, curso, etc.
├── utils/                 # Funções utilitárias
│   └── validation_utils.py    # Funções de validação para os testes
├── requirements.txt       # Arquivo com as dependências do projeto
└── README.md              # Documentação do projeto
Como Rodar os Testes
Para rodar os testes automatizados com Pytest, siga os seguintes passos:

Verifique se o ChromeDriver está configurado corretamente.

Execute os testes: Para rodar os testes automatizados, execute o seguinte comando:

bash
Copiar código
pytest tests/
Os testes irão automaticamente abrir o navegador e executar as ações para criação de aluno, cursos, disciplinas e inscrições.

Fluxo de Testes
O fluxo automatizado abrange as seguintes etapas:

Criar um aluno: O teste cria um aluno na plataforma.
Criar um curso: O curso é criado e vinculado ao aluno.
Criar uma disciplina: A disciplina é criada e associada ao curso.
Inscrição do aluno: O aluno é inscrito nas disciplinas.
Personalização
Caso deseje adaptar o projeto para outro sistema ou modificar as páginas da aplicação, você pode alterar os arquivos na pasta pages/, ajustando os seletores do Selenium de acordo com o novo sistema ou interface.

