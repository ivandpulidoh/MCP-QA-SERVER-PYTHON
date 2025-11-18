# Selenium MCP Server - Test Automation con BDD y Page Object Model

## Descripción del Proyecto

Este proyecto utiliza un **Selenium MCP Server** para crear automatizaciones de pruebas utilizando **Behavior-Driven Development (BDD)**, **Python** y el patrón **Page Object Model (POM)**. El sistema es capaz de construir una automatización completa utilizando únicamente los pasos descritos en un archivo de características (feature), y cuenta con la capacidad de reparar automáticamente escenarios rotos.

### Características Principales

- 🤖 **Automatización Inteligente**: Genera código de automatización a partir de descripciones en lenguaje natural (Gherkin)
- 🔧 **Auto-reparación**: Capacidad de detectar y reparar escenarios de prueba fallidos automáticamente
- 📋 **BDD con Behave**: Implementación de pruebas usando el framework Behave para Python
- 🏗️ **Page Object Model**: Arquitectura de pruebas siguiendo el patrón POM para mejor mantenibilidad
- 🔌 **Integración MCP**: Utiliza el Selenium MCP Server para interactuar con navegadores mediante herramientas MCP

## Arquitectura del Proyecto

```
mcp-qa-server-python/
├── features/                    # Archivos de características BDD (Gherkin)
│   ├── sign_in.feature         # Ejemplo de feature para registro en utest.com
│   └── steps/                  # Definiciones de pasos (step definitions)
├── pages/                       # Page Objects siguiendo el patrón POM
│   └── base_page.py            # Clase base para todos los page objects
├── selenium_mcp_server/        # Referencias al servidor MCP
├── requirements.txt            # Dependencias del proyecto
├── behave.ini                  # Configuración de Behave
└── README.MD                   # Este archivo
```

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Selenium**: Framework de automatización web
- **Behave**: Framework BDD para Python
- **WebDriver Manager**: Gestión automática de drivers de navegador
- **MCP (Model Context Protocol)**: Protocolo para comunicación con el servidor Selenium

## Instalación y Configuración

### Requisitos Previos

- Python 3.7 o superior
- Navegador Chrome instalado
- Acceso a internet para descargar drivers

### Pasos de Instalación

1. **Clonar el repositorio** (si aplica):
   ```bash
   git clone <url-del-repositorio>
   cd mcp-qa-server-python
   ```

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencias

El proyecto requiere las siguientes dependencias (ver `requirements.txt`):

- `behave==1.2.6`: Framework BDD para Python
- `selenium==4.15.2`: Framework de automatización web
- `webdriver-manager==4.0.1`: Gestión automática de drivers

## Cómo Funciona

### Flujo de Trabajo

El proceso de automatización sigue estos pasos:

1. **Definición de Escenarios**: Se crea un archivo `.feature` con los escenarios de prueba en lenguaje Gherkin
   
2. **Ejecución con MCP Server**: El cliente MCP LLM (Cursor, Visual Studio Code, etc.) utiliza las herramientas del Selenium_MCP_Server para:
   - Abrir un navegador
   - Navegar a URLs
   - Interactuar con elementos (clic, escritura, selección)
   - Validar estados de la página

3. **Generación de Código**: El LLM recupera los selectores utilizados y genera:
   - **Page Objects**: Clases que representan las páginas web siguiendo el patrón POM
   - **Step Definitions**: Implementaciones de los pasos definidos en los archivos feature

4. **Ejecución y Validación**: Se ejecuta el test con el comando:
   ```bash
   behave features/sign_in.feature
   ```

5. **Auto-reparación**: Si el test falla, el sistema intenta reparar automáticamente el escenario hasta que funcione correctamente

### Ejemplo de Uso

#### Archivo Feature (Gherkin)

```gherkin
Feature: Register on the utest.com website

    @TC-01
    Scenario: Fill in all the required fields for step 1
        Given I open de browser
        When  I navigate to "utest.com"
        And I click on the "Join Now" button
        Then I wait for the page "https://utest.com/signup/personal" to load
        When I fill the fields of the form
            | type   | field_name     | value              |
            | input  | First name:    | Ruben              |
            | input  | Last name:     | Smith              |
            | input  | Email address: | rsmith@example.com |
            | select | Month          | February           |
            | select | Day            | 5                  | 
            | select | Year           | 2000               |
        Then I valid that all fields have been filled correctly
        When I click on the "Next: Location" button
        Then I wait for the page "https://utest.com/signup/address" to load
```

#### Prompt para el LLM

```
Execute the steps described in the sign_in.feature file in Chrome using selenium-mcp-server and create the step definitions using the selectors you use to follow them; create the necessary page objects following the Page Object Model pattern.

After creating the step definitions and page models, run the command behave features/sign_in.feature to test the correct operation of the created code. If it fails, repair the test.
```

## Estructura de Page Objects

El proyecto utiliza el patrón Page Object Model para organizar el código:

### BasePage

La clase `BasePage` proporciona funcionalidades comunes para todos los page objects:

- `wait_for_url()`: Espera a que la URL coincida con la esperada
- `wait_for_element()`: Espera a que un elemento esté presente
- `wait_for_element_clickable()`: Espera a que un elemento sea clickeable

Todos los page objects heredan de `BasePage` para mantener consistencia y reutilización de código.

## Ejecución de Pruebas

### Ejecutar un Feature Específico

```bash
behave features/sign_in.feature
```


## Integración con Selenium MCP Server

Este proyecto utiliza el [Selenium MCP Server](https://github.com/KiranMote/Selenium_MCP_Server) que proporciona herramientas MCP para:

- Iniciar y controlar navegadores
- Navegar a URLs
- Interactuar con elementos de la página
- Capturar screenshots
- Validar presencia de elementos
- Y muchas otras operaciones de automatización web

## Ventajas del Enfoque

1. **Mantenibilidad**: El código está organizado siguiendo patrones establecidos (POM)
2. **Legibilidad**: Los tests se escriben en lenguaje natural (Gherkin)
3. **Reutilización**: Los page objects pueden ser reutilizados en múltiples tests
4. **Automatización Inteligente**: El LLM puede generar y reparar código automáticamente
5. **Escalabilidad**: Fácil agregar nuevos features y escenarios

## Referencias

- [Selenium MCP Server](https://github.com/KiranMote/Selenium_MCP_Server)
- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
