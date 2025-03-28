# Contributing to Pipedrive API v2 Python Client

Thank you for considering contributing to this project! We welcome improvements, bug fixes, and feature suggestions.

## Getting Started

### Prerequisites

*   Python 3.7+
*   `pip` and `venv` (or your preferred virtual environment tool)

### Setting Up the Environment

1.  **Fork the repository:** Click the "Fork" button on the top right of the GitHub repository page.
2.  **Clone your fork:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/pipedrive-v2-python.git
    cd pipedrive-v2-python
    ```
3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install dependencies:** Install the required packages, including development tools (like `pytest`, `flake8`, `black` if added later).
    ```bash
    pip install -r requirements.txt
    # Potentially: pip install -r requirements-dev.txt (if created)
    ```
5.  **Set up Pipedrive Credentials:** For running integration tests (Phase 1 of Roadmap), you'll need Pipedrive API credentials.
    *   Create a `.env` file in the project root directory.
    *   Add your API token and company domain:
        ```dotenv
        # .env
        PD_API_TOKEN="YOUR_PIPEDRIVE_API_TOKEN"
        PD_COMPANY_DOMAIN="yourcompanydomain" # e.g., 'mycompany' for mycompany.pipedrive.com
        ```
    *   **Important:** Never commit your `.env` file to Git. The `.gitignore` file should already include `.env`.

## Running Tests

*(This section will be updated once the testing framework is implemented in Phase 1)*

Integration tests will likely involve making live calls to the Pipedrive API using the credentials in your `.env` file. It's highly recommended to use a dedicated Pipedrive developer sandbox or a test account to avoid interfering with production data.

```bash
# Example command (once tests are available)
pytest tests/
```

Ensure all tests pass before submitting a pull request.

## Coding Style

*   Follow **PEP 8** guidelines.
*   Use **Black** for code formatting (if adopted). Run `black .` before committing.
*   Use **Flake8** for linting (if adopted). Run `flake8 .` to check for style issues.
*   Write clear and concise docstrings for modules, classes, and functions.

## Submitting Issues

If you encounter a bug, have a feature request, or a question:

1.  **Search existing issues:** Check if a similar issue has already been reported or discussed.
2.  **Open a new issue:** If not, create a new issue, providing as much detail as possible:
    *   **Bug Reports:** Describe the issue, steps to reproduce, expected behavior, actual behavior, library version, Python version, and any relevant error messages or tracebacks.
    *   **Feature Requests:** Explain the desired functionality and its use case.
    *   Use appropriate labels (e.g., `bug`, `enhancement`, `documentation`, `testing`).

## Submitting Pull Requests (PRs)

1.  **Create a feature branch:** Branch off the `main` (or `develop` if used) branch.
    ```bash
    git checkout -b your-feature-name
    ```
2.  **Make your changes:** Implement your feature or bug fix.
3.  **Add tests:** Include tests for any new functionality or bug fixes.
4.  **Ensure tests pass:** Run the test suite locally.
5.  **Format and lint:** Ensure your code adheres to the coding style guidelines.
6.  **Commit your changes:** Write clear and descriptive commit messages.
    ```bash
    git add .
    git commit -m "feat: Add helper function for searching persons by email"
    # Or: git commit -m "fix: Correctly handle pagination cursor in list_deals"
    ```
    *(Consider adopting Conventional Commits standard)*
7.  **Push your branch:**
    ```bash
    git push origin your-feature-name
    ```
8.  **Open a Pull Request:** Go to the original repository on GitHub and open a PR from your feature branch to the `main` branch.
    *   Provide a clear title and description for your PR, referencing any related issues (e.g., "Closes #123").
    *   Be prepared to discuss your changes and make adjustments based on code review feedback.

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. (If a CODE_OF_CONDUCT.md file exists, link to it here. Otherwise, consider adding one based on common templates like the Contributor Covenant).

Thank you for contributing!