# 🤝 Contributing to Ultravox MCP

First off, thank you for considering contributing to Ultravox MCP! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Report unacceptable behavior to the maintainers

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your Python version and operating system**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and the expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python/PEP 8 style guide
* Include appropriate test cases
* Update documentation as needed
* End all files with a newline

## Development Setup

### 1. Fork the Repository

Click the "Fork" button on the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/Ultravox-mcp.git
cd Ultravox-mcp
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black isort
```

### 5. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Making Changes

1. **Write your code** following PEP 8 style guide
2. **Write tests** for your changes
3. **Run tests locally**:
   ```bash
   pytest tests/
   ```
4. **Check code quality**:
   ```bash
   flake8 src/
   black src/ --check
   isort src/ --check-only
   ```

### Code Style

We follow PEP 8 and use `black` for code formatting:

```bash
# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Sort imports
isort src/ tests/
```

### Writing Tests

```python
import unittest
from src.server import UltravoxMCPServer

class TestUltravoxMCP(unittest.TestCase):
    def setUp(self):
        # Set up test fixtures
        pass
    
    def test_list_agents(self):
        # Test your feature
        server = UltravoxMCPServer()
        result = server.list_agents(limit=5)
        self.assertIsNotNone(result)
```

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Examples:
```
Add agent listing functionality
Fix: Handle missing API key gracefully
Docs: Update installation guide for Windows
Tests: Add coverage for call retrieval
```

## Submitting Changes

### 1. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 2. Submit a Pull Request

Go to the repository and click "Compare & pull request"

### 3. PR Description

Please include:
* A clear description of what your PR does
* Link to any related issues (e.g., "Closes #123")
* Any breaking changes
* Screenshots if applicable

### 4. Wait for Review

Maintainers will review your PR. Be prepared to make changes if requested.

## Pull Request Review Checklist

Your PR will be reviewed for:

- [ ] Code quality and style compliance
- [ ] Test coverage
- [ ] Documentation updates
- [ ] No breaking changes (unless justified)
- [ ] Proper error handling
- [ ] Follows project structure

## Project Structure

```
Ultravox-mcp/
├── src/
│   └── server.py           # Main MCP server
├── tests/
│   └── test_server.py      # Unit tests
├── docs/                   # Documentation
├── examples/               # Code examples
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
├── Dockerfile             # Docker configuration
├── LICENSE                # MIT License
└── README.md             # Main documentation
```

## Documentation

If you add a new feature:

1. Update the relevant documentation file in `docs/`
2. Update `README.md` if necessary
3. Add examples in `examples/`
4. Update `CHANGELOG.md`

## Need Help?

* Check existing issues and pull requests
* Read the main [README.md](./README.md)
* Look at [examples/](./examples/) for usage patterns
* Open a discussion for questions

## Recognize Contributions

Contributors are recognized in:
- Git commit history
- Project CHANGELOG
- Documentation

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

---

**Thank you for contributing to Ultravox MCP! 🎉**

---

**This project is maintained by [Mak3it.org](https://mak3it.org)**  
AI-Powered Legal Technology Solutions

---

## Contribuer au MCP Ultravox (Français)

Merci de considérer une contribution à Ultravox MCP!

### Comment Contribuer?

#### Signaler un Bug

Avant de créer un rapport de bug, consultez la liste des issues. Quand vous créez un rapport, incluez:

* Un titre clair et descriptif
* Les étapes exactes pour reproduire le problème
* Des exemples spécifiques
* Le comportement observé
* Le comportement attendu
* Votre version Python et système d'exploitation

#### Proposer une Amélioration

Les suggestions sont suivies comme des issues GitHub. Incluez:

* Un titre clair
* Une description étape par étape
* Des exemples spécifiques
* Pourquoi cette amélioration serait utile

#### Pull Requests

* Remplissez le modèle requis
* Suivez le style PEP 8
* Incluez les tests appropriés
* Mettez à jour la documentation

### Configuration du Développement

```bash
# 1. Fork le dépôt
# 2. Clonez votre fork
git clone https://github.com/YOUR_USERNAME/Ultravox-mcp.git

# 3. Créez un environnement virtuel
python -m venv venv
source venv/bin/activate

# 4. Installez les dépendances
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black isort

# 5. Créez une branche
git checkout -b feature/votre-fonctionnalite
```

### Style de Code

```bash
# Formatage
black src/ tests/

# Vérifier le style
flake8 src/ tests/

# Trier les imports
isort src/ tests/
```

### Messages de Commit

* Utilisez le présent ("Add feature" pas "Added feature")
* Limitez la première ligne à 72 caractères
* Référencez les issues

Exemples:
```
Add agent listing functionality
Fix: Handle missing API key gracefully
Docs: Update installation guide
Tests: Add coverage for calls
```

### Soumettre les Changements

1. Poussez vers votre fork
2. Soumettez une Pull Request
3. Attendez la révision
4. Apportez les changements demandés

---

**Merci de contribuer! 🎉**
