# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project overview

Paws a Moment and Rescue is intended to be a lightweight Django-based rescue CMS and public website for managing adoptable pets, news, success stories, and donations (from `README.md`).

The repository now contains a concrete Django project and four main apps:

- Project package: `paws_rescue/` with `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`.
- Apps:
  - `core` – shared base templates and the public home page.
  - `adoptions` – adoptable animals and adoption applications.
  - `stories` – news and success stories, optionally linked to animals.
  - `donations` – simple donation records and a basic donation form flow.

## Tech stack and layout

- **Framework**: Django (Python).
- **Entry points**:
  - `manage.py`: command-line entry for running the server, tests, and management commands.
  - `paws_rescue/settings.py`: global configuration, installed apps, database configuration.
  - `paws_rescue/urls.py`: top-level URL routing; includes URLs from each app.

Prefer following the existing app boundaries (core/adoptions/stories/donations) when adding new features.

## Commands

Use these commands as a starting point; prefer any project-specific scripts or Makefile/poetry/tox commands if they are later added to the repo.

### Environment setup

```bash path=null start=null
python -m venv .venv
# Activate the virtualenv (platform/shell specific)
#   Unix (bash/zsh): source .venv/bin/activate
#   Windows (PowerShell): .venv\\Scripts\\Activate.ps1

# Install dependencies once they are defined
# (adjust to the actual dependency file used by the project)
python -m pip install --upgrade pip
if exist requirements.txt python -m pip install -r requirements.txt
```

If the project later adopts `pyproject.toml`/Poetry, `pipenv`, or another tool, use the corresponding standard install commands instead (e.g., `poetry install`).

### Running the development server

Once `manage.py` exists at the repo root (or in the documented location):

```bash path=null start=null
python manage.py runserver
```

If the project uses per-environment settings (e.g., `DJANGO_SETTINGS_MODULE`), ensure the correct settings module is set via environment variable or `--settings`.

### Database migrations

Standard Django migration workflow (adjust for any custom scripts that may be added):

```bash path=null start=null
python manage.py makemigrations
python manage.py migrate
```

### Tests

Default Django test commands (prefer any project-specific `pytest`/tox/Makefile wrappers if present):

- **Run all tests**:

  ```bash path=null start=null
  python manage.py test
  ```

- **Run tests for a single app** (e.g., `adoptions`):

  ```bash path=null start=null
  python manage.py test adoptions
  ```

- **Run a single test case or method**:

  ```bash path=null start=null
  python manage.py test adoptions.tests.TestAdoptionViews.test_detail_view
  ```

If the project adopts `pytest`, use `pytest` (and its `-k`/`::` selectors) instead of `manage.py test` and respect any config in `pytest.ini`/`pyproject.toml`.

### Linting and formatting

As of this file, there are no lint/format configs or scripts in the repo. When they are added (e.g., Ruff, Flake8, Black, isort), prefer running them via any provided scripts (e.g., `make lint`, `poetry run ruff check .`) and keep new code consistent with existing configuration.

## Expected high-level architecture (once implemented)

When the Django project and apps are present, use this mental model to navigate and modify the codebase:

- **Core concepts**
  - **Adoptable pets**: models for animals, their statuses, and related metadata; views/DRF viewsets and templates or APIs to browse and apply for adoption.
  - **News & success stories**: models representing posts or stories; likely share a common "content" abstraction for public-facing pages.
  - **Donations**: models or integrations (Stripe, PayPal, etc.) handling donation records; likely includes webhooks or callbacks if payment providers are used.
  - **CMS vs. public site**: admin/staff-facing CRUD interfaces vs. public read-only browsing pages.

- **Django apps**
  - Expect separate apps for each major domain (e.g., `adoptions`, `stories`, `donations`, maybe a `core`/`public` app for shared templates and generic pages).
  - Try to keep cross-app dependencies flowing from more generic apps (e.g., `core`) out to more domain-specific apps, not the reverse.

- **URLs and views**
  - Global URL patterns in `<project_name>/urls.py` should include per-app `urls.py` files.
  - For new endpoints, extend the appropriate app-level `urls.py` rather than bloating the project-level routing.

- **Templates and static files**
  - Expect per-app `templates/<app_name>/...` directories and possibly a shared templates directory for site-wide layout.
  - Place app-specific static assets under `static/<app_name>/...` to avoid namespace collisions.

When adding new features, first identify the app that owns the relevant domain concept; extend that app's models/views/templates instead of creating unrelated utility modules.

## How future agents should orient themselves

When more code is present, future Warp agents should:

1. Locate `manage.py` and the Django project package (directory containing `settings.py`).
2. List Django apps via `INSTALLED_APPS` in `settings.py` to understand domain boundaries.
3. Inspect `models.py`, `urls.py`, and key views/serializers in each app to understand how pets, stories, and donations are wired together.
4. Check for any custom `management/commands`, DRF viewsets, or payment/webhook integrations that may affect behaviour when editing donation-related code.

Always prefer aligning with the existing app/module structure and patterns over introducing new architectural concepts unless there is a clear benefit and minimal churn.
