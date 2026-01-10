# Contributing to Ultravox MCP

Thank you for considering contributing to Ultravox MCP! Here's how you can help.

## Code of Conduct

Be respectful and professional. We welcome all backgrounds and experience levels.

## Getting Started

### 1. Fork & Clone

```bash
# Fork on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ultravox-mcp-unofficial.git
cd ultravox-mcp-unofficial

# Add upstream
git remote add upstream https://github.com/mak3it-org/ultravox-mcp-unofficial.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix-name
```

### 3. Setup Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy
```

### 4. Make Changes

Write clean, well-documented code:

```python
def my_function(param1: str, param2: int) -> dict:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        dict: Description of return value
    
    Raises:
        ValueError: When this error occurs
    """
    pass
```

### 5. Test Your Changes

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Format code
black src/ tests/

# Check code style
flake8 src/

# Type checking
mypy src/
```

### 6. Commit with Message

```bash
# Use clear, descriptive commit messages
git commit -m "feat: add new tool for managing webhooks"
git commit -m "fix: resolve 404 error in get_call_recording"
git commit -m "docs: update installation guide"

# Commit message format:
# feat:  new feature
# fix:   bug fix
# docs:  documentation
# test:  tests
# refactor: code refactoring
# chore: maintenance tasks
```

### 7. Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:
- Clear title
- Description of changes
- Related issues (#123)
- Screenshots (if applicable)

## Types of Contributions

### 🐛 Bug Reports

Create an issue with:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error logs/tracebacks

```
Title: [BUG] Server crashes when API key is missing

Environment:
- Python 3.11
- Windows 11
- Ultravox MCP v1.0.0

Steps to reproduce:
1. Remove ULTRAVOX_API_KEY from .env
2. Run python src/server.py
3. Try to call list_agents

Expected: Graceful error message
Actual: Server crashes with traceback

Error:
[traceback here]
```

### ✨ Feature Requests

Create an issue with:
- Use case/motivation
- Proposed solution
- Alternative approaches
- Any additional context

```
Title: [FEATURE] Add call analytics tool

Use case:
Users want to analyze call statistics and patterns

Proposed solution:
Add a new tool: get_call_analytics(call_id) that returns:
- Duration
- Sentiment analysis
- Topics discussed
- User satisfaction

This would help users understand call quality.
```

### 📚 Documentation

Improve docs:
- Fix typos
- Add examples
- Clarify instructions
- Translate to new languages
- Update API documentation

### 💡 Code Improvements

- Refactor for readability
- Add unit tests
- Optimize performance
- Add type hints
- Improve error handling

## Code Standards

### Python Style

```python
# ✅ Good
def calculate_total_price(items: list[dict], tax_rate: float) -> float:
    """Calculate total price including tax."""
    subtotal = sum(item['price'] for item in items)
    return subtotal * (1 + tax_rate)

# ❌ Bad
def calc_total(items, tax):
    total = 0
    for i in items:
        total += i['price']
    return total * (1 + tax)
```

### Comments & Docstrings

```python
# ✅ Good
def get_agent(agent_id: str) -> dict:
    """
    Retrieve agent details by ID.
    
    Args:
        agent_id: UUID of the agent
    
    Returns:
        dict: Agent configuration and metadata
    
    Raises:
        ValueError: If agent_id is invalid
        HTTPError: If agent not found (404)
    """

# ❌ Bad
def get_agent(agent_id):
    # get the agent
    return make_request(f"/agents/{agent_id}")
```

### Error Handling

```python
# ✅ Good
try:
    response = api.get_call(call_id)
    return response
except HTTPError as e:
    if e.response.status_code == 404:
        raise ValueError(f"Call {call_id} not found")
    raise

# ❌ Bad
try:
    return api.get_call(call_id)
except:
    return None
```

## Testing

### Write Tests

```python
# tests/test_calls.py
import pytest
from src.server import call_list_agents

def test_list_agents_success():
    """Test successful agents listing."""
    result = call_list_agents(limit=10)
    assert 'agents' in result
    assert len(result['agents']) <= 10

def test_list_agents_invalid_limit():
    """Test with invalid limit parameter."""
    with pytest.raises(ValueError):
        call_list_agents(limit=-1)

@pytest.mark.integration
def test_list_agents_api_key_invalid():
    """Test with invalid API key."""
    # Requires actual API call
    pass
```

### Test Coverage

Aim for >80% coverage:
```bash
pytest --cov=src --cov-report=term-missing
```

## Security

### Reporting Security Issues

Please do NOT create a public issue. Email: security@mak3it.org

Include:
- Vulnerability description
- Affected versions
- Suggested fix (optional)

We'll respond within 48 hours.

### Security Checklist

Before submitting:
- [ ] No hardcoded secrets/keys
- [ ] No SQL injection risks
- [ ] Proper input validation
- [ ] API key handling is secure
- [ ] Dependencies are up-to-date
- [ ] No debug info in logs

## Commit Workflow

```
1. Create branch
2. Make changes
3. Write/update tests
4. Format code (black)
5. Lint (flake8)
6. Type check (mypy)
7. Commit with clear message
8. Push to your fork
9. Create Pull Request
10. Respond to code review
11. Merge when approved
```

## Review Process

### Before Merging

- [ ] Tests pass (100%)
- [ ] Code coverage maintained
- [ ] Documentation updated
- [ ] No security issues
- [ ] At least 1 approval
- [ ] Changelog updated

### Code Review Guidelines

Be constructive:
```
# ✅ Good feedback
"Consider using a list comprehension here for better readability:
result = [item['id'] for item in items if item['active']]"

# ❌ Poor feedback
"This code is bad"
```

## Documentation Contributions

### Update Docs

```markdown
1. Add to docs/ folder
2. Update README.md if needed
3. Include English AND French
4. Add examples where applicable
5. Link from main docs index
```

### Translation

Help translate to:
- Spanish
- German
- Japanese
- Chinese
- Portuguese
- Other languages?

## Questions?

- 📖 Read the [docs](./docs/)
- 💬 Create a discussion issue
- 📧 Email: hello@mak3it.org

## Thank You! 🙏

Your contributions help make Ultravox MCP better for everyone!

---

**Happy coding!** 🚀
