# TITAN SonarQube Sandbox (synthetic, not deployed)

A real but deliberately small Python repository for Lab 8 tool familiarization.

## Includes

- Package under `src/quality_sandbox/`
- Parameterized `pytest` tests and meaningful assertions
- `pytest-cov` with statement and branch coverage; 80% minimum
- GitHub Actions CI with reports and optional SonarQube Cloud scanner + Quality Gate wait
- Two deliberate static-analysis probes: unused local variable and `eval()` (NEVER EXECUTED)

## Local validation

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 -m pip install -e .
python3 -m pytest -q --cov=quality_sandbox --cov-branch --cov-fail-under=80 --cov-report=term-missing --cov-report=xml:coverage.xml --junitxml=test-results.xml
```

## SonarQube Cloud connection

1. Import this repository into **SonarQube Cloud** and choose **GitHub Actions** (CI-based analysis). If offered automatic analysis, disable it for this project so there is one analysis path.
2. Obtain the exact **organization key** and **project key** from the newly created SonarQube project.
3. In the GitHub repository, add Actions **secret** `SONAR_TOKEN` (token value, never commit it).
4. Add Actions **variables** `SONAR_ORGANIZATION` and `SONAR_PROJECT_KEY` using those exact keys.
5. Push another commit or run **Actions > Python Quality and SonarQube > Run workflow**. The Sonar step is skipped until all three settings exist. A passing QA job before this setup is NOT evidence of a successful SonarQube scan.
6. Inspect the Issues, Measures and Quality Gate screens. Fix the two intentional source findings, then re-run and compare results. Detection depends on active rules; findings are not guaranteed for every Quality Profile.

If the action fails to resolve the Cloud endpoint, check the setup instructions presented by your SonarQube Cloud project and update the host setting accordingly.

### Safety and scope

- Public repository contains intentionally unsafe **synthetic code only**. No app is deployed or exposed as a service.
- Do not execute `unsafe_expression` or add it to the test suite.
- Public repository pull requests from forks do not receive `SONAR_TOKEN` in this workflow.
- This script does not configure GitHub branch protection; that requires separate verification in Lab 8.
- This is one controlled familiarization sandbox, not a new mandatory TITAN lab.
