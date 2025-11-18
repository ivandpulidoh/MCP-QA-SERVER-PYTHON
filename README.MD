# Selenium MCP Server - Test Automation with BDD and Page Object Model

## Project Description

This project uses a **Selenium MCP Server** to create test automations using **Behavior-Driven Development (BDD)**, **Python**, and the **Page Object Model (POM)** pattern. The system is capable of building a complete automation using only the steps described in a feature file, and has the ability to automatically repair broken scenarios.

### Main Features

- 🤖 **Intelligent Automation**: Generates automation code from natural language descriptions (Gherkin)
- 🔧 **Auto-repair**: Ability to detect and automatically repair failed test scenarios
- 📋 **BDD with Behave**: Test implementation using the Behave framework for Python
- 🏗️ **Page Object Model**: Test architecture following the POM pattern for better maintainability
- 🔌 **MCP Integration**: Uses the Selenium MCP Server to interact with browsers through MCP tools

### Video Demo

You can see a practical example of how this project works in the following video:

[![Video Demo](https://img.youtube.com/vi/3d_phRen8Hk/0.jpg)](https://youtu.be/3d_phRen8Hk)

**Direct link**: [Watch video on YouTube](https://youtu.be/3d_phRen8Hk)

The video shows a brief example of how the Selenium MCP Server is used to create automations with BDD and the Page Object Model pattern.

## Project Architecture

```
mcp-qa-server-python/
├── features/                    # BDD feature files (Gherkin)
│   ├── sign_in.feature         # Example feature for registration on utest.com
│   └── steps/                  # Step definitions
├── pages/                       # Page Objects following the POM pattern
│   └── base_page.py            # Base class for all page objects
├── selenium_mcp_server/        # MCP server references
├── requirements.txt            # Project dependencies
├── behave.ini                  # Behave configuration
└── README.MD                   # This file
```

## Technologies Used

- **Python**: Main programming language
- **Selenium**: Web automation framework
- **Behave**: BDD framework for Python
- **WebDriver Manager**: Automatic browser driver management
- **MCP (Model Context Protocol)**: Protocol for communication with the Selenium server

## Installation and Configuration

### Prerequisites

- Python 3.7 or higher
- Chrome browser installed
- Internet access to download drivers

### Installation Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd mcp-qa-server-python
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

The project requires the following dependencies (see `requirements.txt`):

- `behave==1.2.6`: BDD framework for Python
- `selenium==4.15.2`: Web automation framework
- `webdriver-manager==4.0.1`: Automatic driver management

## How It Works

### Workflow

The automation process follows these steps:

1. **Scenario Definition**: A `.feature` file is created with test scenarios in Gherkin language
   
2. **Execution with MCP Server**: The MCP LLM client (Cursor, Visual Studio Code, etc.) uses the Selenium_MCP_Server tools to:
   - Open a browser
   - Navigate to URLs
   - Interact with elements (click, type, select)
   - Validate page states

3. **Code Generation**: The LLM retrieves the selectors used and generates:
   - **Page Objects**: Classes that represent web pages following the POM pattern
   - **Step Definitions**: Implementations of the steps defined in the feature files

4. **Execution and Validation**: The test is executed with the command:
   ```bash
   behave features/sign_in.feature
   ```

5. **Auto-repair**: If the test fails, the system attempts to automatically repair the scenario until it works correctly

### Usage Example

#### Feature File (Gherkin)

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

#### Prompt for the LLM

```
Execute the steps described in the sign_in.feature file in Chrome using selenium-mcp-server and create the step definitions using the selectors you use to follow them; create the necessary page objects following the Page Object Model pattern.

After creating the step definitions and page models, run the command behave features/sign_in.feature to test the correct operation of the created code. If it fails, repair the test.
```


## Page Objects Structure

The project uses the Page Object Model pattern to organize the code:

### BasePage

The `BasePage` class provides common functionality for all page objects:

- `wait_for_url()`: Waits for the URL to match the expected one
- `wait_for_element()`: Waits for an element to be present
- `wait_for_element_clickable()`: Waits for an element to be clickable

All page objects inherit from `BasePage` to maintain consistency and code reusability.

## Test Execution

### Run a Specific Feature

```bash
behave features/sign_in.feature
```


## Integration with Selenium MCP Server

This project uses the [Selenium MCP Server](https://github.com/KiranMote/Selenium_MCP_Server) which provides MCP tools for:

- Starting and controlling browsers
- Navigating to URLs
- Interacting with page elements
- Capturing screenshots
- Validating element presence
- And many other web automation operations

## Advantages of This Approach

1. **Maintainability**: Code is organized following established patterns (POM)
2. **Readability**: Tests are written in natural language (Gherkin)
3. **Reusability**: Page objects can be reused across multiple tests
4. **Intelligent Automation**: The LLM can generate and repair code automatically
5. **Scalability**: Easy to add new features and scenarios

## References

- [Selenium MCP Server](https://github.com/KiranMote/Selenium_MCP_Server)
- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
