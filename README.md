# Playwright API Performance Framework

A comprehensive test automation framework covering UI (Playwright), API (Pytest), and performance testing with CI/CD integration.

## 🏗️ Architecture

```
playwright-api-performance-framework/
├── api-tests/                 # API test automation
│   ├── src/objects/          # Page Object Models for APIs
│   │   ├── base_api.py       # Base API class
│   │   └── users_object.py   # Users API object
│   ├── tests/                # Test files
│   │   ├── data/            # Test data & validation
│   │   └── test_*.py        # Individual test files
│   ├── utils/               # Utilities (logging, helpers)
│   ├── config.py            # Configuration
│   ├── conftest.py          # Pytest fixtures
│   └── .env                 # Environment variables
├── ui-tests/                # UI test automation (Playwright)
├── reports/                 # Test reports
├── logs/                   # Application logs
└── requirements.txt        # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+ (for UI tests)
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd playwright-api-performance-framework
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp api-tests/.env.example api-tests/.env
   # Edit .env with your API credentials
   ```

4. **Set up UI tests**
   ```bash
   cd ui-tests
   npm install
   npx playwright install
   cd ..
   ```

### Running Tests

**API Tests:**
```bash
# Run all API tests
pytest api-tests/tests/

# Run specific test file
pytest api-tests/tests/test_get_all_users.py -v

# Run with HTML report
pytest api-tests/tests/ --html=reports/api-report.html

# Run parallel tests
pytest api-tests/tests/ -n 4
```

**UI Tests:**
```bash
cd ui-tests
npm test
```

## 📊 Features

### API Testing
- ✅ REST API testing with requests
- ✅ Comprehensive logging
- ✅ Schema validation
- ✅ Test data management
- ✅ Parallel test execution
- ✅ HTML reporting
- ✅ CI/CD integration

### UI Testing
- ✅ Playwright-based testing
- ✅ Cross-browser support
- ✅ Visual regression testing
- ✅ CI/CD integration

### Performance Testing (Planned)
- 🔄 Locust integration
- 🔄 Load testing capabilities
- 🔄 Performance metrics collection

## 🛠️ Configuration

### Environment Variables (.env)
```bash
# API Configuration
BASE_URL=https://api.example.com/v2
ACCESS_TOKEN=your_api_token_here

# Logging
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Request Settings
REQUEST_TIMEOUT=10
```

### Pytest Configuration (pytest.ini)
- Test discovery patterns
- Reporting options
- Test markers (smoke, regression, api, ui, performance)
- Warning filters

## 📝 Test Structure

### API Tests
```python
import pytest
from src.objects.users_object import Users
from tests.data.test_data import get_test_user
from tests.data.validation import validate_user_response

class TestUsersAPI:
    @pytest.fixture
    def users_api(self):
        return Users()

    @pytest.mark.api
    def test_create_user(self, users_api):
        user_data = get_test_user("valid_user")
        response = users_api.create_user(user_data)

        assert response.status_code == 201
        data = response.json()
        validate_user_response(data)
```

### Test Data Management
- Centralized test data in `tests/data/test_data.py`
- Schema validation in `tests/data/validation.py`
- Environment-specific data support

## 🔍 Logging

- **Console logging**: Real-time test execution feedback
- **File logging**: Persistent logs with timestamps
- **Structured format**: Includes timestamps, log levels, and context
- **Dynamic file naming**: Based on test file names

Log files are stored in `api-tests/logs/` with format: `{test_name}_{timestamp}.log`

## 📈 Reporting

### HTML Reports
```bash
pytest api-tests/tests/ --html=reports/api-report.html
```

### Allure Reports (Planned)
```bash
pytest api-tests/tests/ --alluredir=allure-results
allure serve allure-results
```

## 🚀 CI/CD

GitHub Actions workflow includes:
- Automated test execution on push/PR
- Multi-job setup (API + UI tests)
- Artifact upload for test results
- Status checks and notifications

## 🏷️ Test Markers

```bash
# Run only smoke tests
pytest -m smoke

# Run API tests
pytest -m api

# Run regression tests
pytest -m regression
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📋 TODO

- [ ] Add performance testing with Locust
- [ ] Implement Allure reporting
- [ ] Add API contract testing
- [ ] Database testing integration
- [ ] Mobile testing support
- [ ] Docker containerization

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
