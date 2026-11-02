# Blog Post

A multi-user **blogging platform** built with Django: users register, write posts, and manage their own content and profile.

## Features

- Create, read, update and delete posts. Only the author can edit or delete a post.
- Paginated home feed, plus a page for each author (`/user/<username>`)
- Register, log in and log out
- Profile page with a picture, created automatically by a signal when a user signs up
- Password reset by email
- Forms styled with django-crispy-forms

## Running

```bash
python -m venv venv && source venv/bin/activate
pip install "django==3.0.7" django-crispy-forms pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver        # http://localhost:8000
```

> `requirments.txt` (sic) is a full environment freeze, so installing the three packages above is enough.

## Routes

| Path | Description |
|---|---|
| `/` | All posts |
| `/post/new/` | New post |
| `/post/<id>/`, `/post/<id>/update/`, `/post/<id>/delete/` | View, edit or delete a post |
| `/user/<username>` | Posts by one user |
| `/register/`, `/login/`, `/logout/`, `/profile/` | Accounts |
| `/password-reset/` | Reset a forgotten password |
| `/about/` | About page |

## Tech

Python · Django 3.0 · django-crispy-forms · Bootstrap · SQLite

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |
| `EMAIL_HOST_PASSWORD` | SMTP password for Django email |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
