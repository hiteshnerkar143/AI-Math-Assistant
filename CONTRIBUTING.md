# Contributing Guidelines

Thank you for your interest in contributing to the AI Math Assistant project!

## How to Contribute

### 1. Report Bugs

Found a bug? Please report it by:

1. **Check existing issues** to avoid duplicates
2. **Create new issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - System info (OS, Python version)
3. **Example**:
```
Title: Graph plotting fails with exponential functions
Description: 
- When plotting "exp(x)", the graph window opens but no line appears
- Expected: Exponential curve visible
- OS: Windows 10, Python 3.11
```

### 2. Suggest Features

Have an idea? Please suggest it by:

1. **Describe the feature** clearly
2. **Explain the use case**
3. **Provide examples** if possible
4. **Example**:
```
Feature: Matrix operations
Use Case: Students need to multiply and add matrices
Example: "multiply [[1,2],[3,4]] by [[5,6],[7,8]]"
```

### 3. Submit Code

#### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/ai-math-assistant.git
cd ai-math-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

#### Code Style Guidelines

- **PEP 8**: Follow Python style guide
- **Type Hints**: Add type annotations
- **Docstrings**: Document all functions
- **Comments**: Explain complex logic
- **Naming**: Use clear, descriptive names

#### Example Code

```python
def calculate_distance(point1: Tuple[float, float], 
                       point2: Tuple[float, float]) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Args:
        point1: First point as (x, y) tuple
        point2: Second point as (x, y) tuple
        
    Returns:
        Distance between points
        
    Raises:
        TypeError: If points are not tuples
    """
    if not isinstance(point1, tuple) or not isinstance(point2, tuple):
        raise TypeError("Points must be tuples")
    
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

#### Before Submitting

1. **Format code**:
```bash
black .
```

2. **Check style**:
```bash
flake8 . --max-line-length=100
```

3. **Write tests**:
```bash
# Create tests/test_calculator.py
pytest tests/
```

4. **Update documentation**:
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md

#### Pull Request Process

1. **Create feature branch**:
```bash
git checkout -b feature/amazing-feature
```

2. **Make changes** with atomic commits:
```bash
git add .
git commit -m "Add amazing feature"
```

3. **Push to fork**:
```bash
git push origin feature/amazing-feature
```

4. **Create Pull Request** with:
   - Clear title and description
   - Reference to related issues
   - List of changes
   - Any breaking changes
   - Screenshots if UI changes

5. **Example PR**:
```
Title: Add matrix multiplication support

Description:
- Implements matrix multiplication using NumPy
- Adds validation for matrix dimensions
- Includes 10 test cases
- Updates documentation

Fixes: #42
Related: #38

Changes:
- Added MatrixCalculator class in utils/matrix_calc.py
- Added matrix operation examples to README
- Includes full test coverage

Breaking Changes: None
```

### 4. Documentation

Help improve documentation:

1. **Fix typos**: Correct spelling/grammar
2. **Clarify**: Make confusing parts clearer
3. **Add examples**: Include usage examples
4. **Update**: Keep docs in sync with code

#### Documentation Style

```markdown
## Feature Name

Brief description of the feature.

### Usage

Clear, step-by-step usage instructions.

### Examples

```python
# Code examples with output
result = feature()  # Expected output: ...
```

### Related

Links to related features or documentation.
```

## Development Workflow

### Project Structure

```
AI_Math_Assistant/
├── utils/              # Core utilities
├── models/             # ML models
├── gui/                # User interface
├── tests/              # Unit tests (to be added)
├── docs/               # Documentation
└── examples/           # Usage examples
```

### Adding a New Feature

1. **Create module** in appropriate directory:
```python
# utils/new_feature.py
def new_feature():
    """Docstring"""
    pass
```

2. **Add to __init__.py**:
```python
from .new_feature import new_feature
__all__ = ['new_feature']
```

3. **Add tests**:
```python
# tests/test_new_feature.py
def test_new_feature():
    assert new_feature() == expected
```

4. **Update README.md**:
   - Add to features section
   - Add usage example
   - Update table of contents

5. **Test thoroughly**:
```bash
pytest tests/test_new_feature.py -v
```

### Code Review Checklist

Before submitting:

- [ ] Code follows PEP 8 style
- [ ] Type hints added
- [ ] Docstrings complete
- [ ] No console.log/print statements
- [ ] Tests added and passing
- [ ] No breaking changes
- [ ] Documentation updated
- [ ] Commit messages clear
- [ ] No duplicate code
- [ ] Performance acceptable

## Testing

### Writing Tests

```python
# tests/test_calculator.py
import unittest
from utils.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(5, 6)
        self.assertEqual(result, 11)
    
    def test_add_negative(self):
        result = self.calc.add(-5, 3)
        self.assertEqual(result, -2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_calculator.py

# Run with coverage
pytest --cov=utils tests/

# Run with verbose output
pytest -v
```

## Commit Guidelines

### Commit Message Format

```
[TYPE] Brief description

Longer description explaining the what and why, not how.

Fixes: #123
Related: #456
```

### Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation change
- **style**: Code style change
- **refactor**: Code refactoring
- **perf**: Performance improvement
- **test**: Test addition/modification
- **chore**: Build, dependency, or tool change

### Examples

```
feat: Add matrix multiplication support
fix: Resolve graph plotting for exponential functions
docs: Update installation guide for Linux
refactor: Simplify calculator module
test: Add test cases for equation solver
```

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Report inappropriate behavior

## Questions?

Feel free to ask questions in:
- GitHub Issues
- Pull Request comments
- Discussion boards

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project credits

---

**Thank you for contributing!** 🎉

Together we're building an amazing math assistant!
