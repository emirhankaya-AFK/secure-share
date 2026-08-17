# Secure Share

[English](README.md) | [Türkçe](README_TR.md)

API for creating expiring share links. Cryptographic tokens are generated with Python secrets and expiry is enforced on read.

POST /api/v1/shares creates a link; GET /api/v1/shares/{token} resolves an active link. The MVP stores metadata in memory and does not upload files. Production needs S3-compatible storage, signed downloads, authorization, malware scanning, audit logs and a database.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

