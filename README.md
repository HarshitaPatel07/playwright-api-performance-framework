# playwright-api-performance-framework
Scalable test automation framework covering UI (Playwright), API (Pytest), and performance testing (Locust) with CI/CD integration using GitHub Actions.

## Performance Testing with Locust

From the `api-tests` folder, install dependencies and run Locust against the configured base URL:

```bash
cd api-tests
python -m pip install -r requirements.txt
locust -f tests/performance-tests/locust-test.py
```

Locust will use `api-tests/config.py` and `.env` for `BASE_URL` by default. For headless execution:

```bash
locust -f tests/performance-tests/locust-test.py --headless -u 50 -r 10 -t 2m
```
