# Passagem de Plantão

Sistema web desenvolvido em Django para registro e acompanhamento de passagens de plantão em centrais de monitoramento.

## Visão Geral

O projeto "Passagem de Plantão" é uma aplicação web robusta, construída com o framework Django, que visa otimizar e centralizar os registros de ocorrências e informações relevantes durante as trocas de turno em centrais de monitoramento. A plataforma oferece um formulário para operadores de monitoramento de veículos, além de um dashboard gerencial para visualização de dados e indicadores.

A aplicação utiliza múltiplos bancos de dados para segregar as informações, garantindo uma melhor organização e performance. Além disso, o sistema conta com um sistema de autenticação e autorização de usuários, restringindo o acesso às diferentes áreas da aplicação de acordo com o perfil de cada colaborador.

## Funcionalidades Principais

  * **Autenticação de Usuários:** Sistema de login seguro que direciona os usuários para suas respectivas áreas de trabalho com base em seus grupos de permissão.
  * **Formulário de Passagem de Plantão (Monitoramento):** Permite que os operadores de monitoramento de veículos registrem informações detalhadas sobre o plantão, incluindo:
      * Dados do operador e coordenador.
      * Controle de volumetria de veículos (em pernoite, viagem, manutenção, etc.).
      * Registro de ocorrências como desvios de rota, sinistros, paradas não autorizadas, entre outros.
      * Checklist de equipamentos (mouse pad, descanso de pé, carregador).
      * Campo de observações para informações adicionais.
  * **Dashboard Gerencial:** Uma área exclusiva para gerentes, que apresenta os dados consolidados das passagens de plantão em formato de gráficos e tabelas, permitindo uma análise rápida e eficiente das operações. O dashboard inclui:
      * Gráficos de pizza, barras e linhas com indicadores chave.
      * Tabela com as últimas passagens de plantão, com detalhes exibidos em um modal.
      * Contadores de sinistros e veículos em viagem.
  * **Banco de Dados Dedicado:** Utiliza um banco de dados secundário (`plantao_db`) para armazenar os registros de passagem de plantão, mantendo a organização e a performance do sistema.

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com as principais configurações e aplicações organizadas da seguinte forma:

```
passagem_plantao_django/
├── .github/workflows/         # Configuração de CI com GitHub Actions
├── .vscode/                   # Configurações do VS Code
├── config_projeto/            # Configurações globais do projeto (settings, urls, etc.)
├── login_app/                 # Aplicação principal do projeto
│   ├── migrations/            # Migrações do banco de dados
│   ├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/             # Templates HTML
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── db_router.py           # Roteador para múltiplos bancos de dados
│   ├── forms.py
│   ├── forms_plantao.py
│   ├── models.py
│   ├── models_plantao.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── plantao_db.sqlite3         # Banco de dados secundário para passagens de plantão
├── popular_banco.py           # Script para popular o banco de dados com dados de teste
├── requirements.txt
└── ...
```

## Tecnologias Utilizadas

  * **Backend:**
      * Python 3
      * Django 5.2.4
  * **Frontend:**
      * HTML5
      * CSS3
      * JavaScript
  * **Banco de Dados:**
      * SQLite (com suporte a múltiplos bancos)
  * **Visualização de Dados:**
      * Pandas
      * Plotly

## Como Executar o Projeto

Para executar o projeto em seu ambiente local, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/passagem_plantao_django.git
    cd passagem_plantao_django
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    python manage.py migrate --database=plantao_db
    ```

5.  **Crie um superusuário para acessar o painel de administração:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **(Opcional) Popule o banco de dados com dados de teste:**

    ```bash
    python popular_banco.py
    ```

7.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

Após iniciar o servidor, acesse `http://127.0.0.1:8000/` em seu navegador para visualizar a aplicação.

## Grupos de Usuários

O sistema possui diferentes grupos de usuários com permissões específicas:

  * **operadorescm:** Acesso ao formulário de passagem de plantão de monitoramento.
  * **gerentes:** Acesso ao dashboard gerencial.

## Contribuição

Contribuições são bem-vindas\! Se você tiver alguma sugestão de melhoria ou encontrar algum problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Autor

**Guilherme Reis**

  * GitHub: [guilhermereis120](https://www.google.com/search?q=https://github.com/guilhermereis120)
