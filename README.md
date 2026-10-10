# Secure Share

[English](#english) | [Türkçe](#türkçe) | [Deutsch](#deutsch)

## English

### Purpose
API for creating expiring share links. Cryptographic tokens are generated with Python secrets and expiry is enforced on read.

### Verified Features
- POST `/api/v1/shares` creates a share link.
- GET `/api/v1/shares/{token}` resolves an active link.
- Token generation using `secrets`.
- Expiry check on read.
- In‑memory metadata storage (MVP).
- Dockerfile and compose.yaml for containerised execution.
- Test suite executable with `pytest`.

### Stack
- Python (packaged via `pyproject.toml`).
- ASGI server (uvicorn) – inferred from `uvicorn app.main:app`.
- FastAPI‑style routing (implied by uvicorn command).
- Docker.
- pytest for testing.

### Setup / Usage
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
# or with Docker
docker compose up
```

### Testing
```bash
pytest -q
```

### Limitations
- Metadata is stored only in memory; data is lost on process restart.
- No file upload or storage; MVP does not persist shares.
- Missing production‑grade components: S3‑compatible storage, signed downloads, authorization, malware scanning, audit logs, and a database.

### License
See the `LICENSE` file.

## Türkçe

### Amaç
Python `secrets` ile kriptografik token üreten ve okuma sırasında süresi geçerliliğini zorunlu kılan, expiring share linkleri sağlayan bir API.

### Doğrulanmış Özellikler
- `/api/v1/shares` POST ile paylaşım linki oluşturulur.
- `/api/v1/shares/{token}` GET ile aktif link çözümlenir.
- Token üretimi `secrets` modülüyle yapılır.
- Okuma sırasında süre kontrolü yapılır.
- Metadata bellekte tutulur (MVP).
- Dockerfile ve compose.yaml ile konteynerli çalıştırma desteklenir.
- Testler `pytest` ile çalıştırılabilir.

### Yığın
- Python (pyproject.toml ile paketlenmiş).
- Uvicorn ASGI sunucusu (uvicorn app.main:app).
- FastAPI tarzı yönlendirme (uvicorn komutundan çıkarılabilir).
- Docker.
- pytest test framework’i.

### Kurulum / Kullanım
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
# Docker ile
docker compose up
```

### Test
```bash
pytest -q
```

### Sınırlamalar
- Metadata sadece bellekte saklanır; süreç yeniden başlatıldığında veri kaybolur.
- Dosya yükleme veya depolama yok; MVP paylaşımları kalıcı değildir.
- Üretim için gerekli olan S3‑uyumlu depolama, imzalı indirmeler, yetkilendirme, kötü amaçlı yazılım taraması, denetim günlükleri ve veritabanı eksiktir.

### Lisans
`LICENSE` dosyasına bakınız.

## Deutsch

### Zweck
Eine API zur Erstellung von teilbaren Links mit begrenzter Gültigkeitsdauer. Tokens werden mit Python‑`secrets` erzeugt und die Gültigkeit wird beim Lesen erzwungen.

### Verifizierte Funktionen
- `POST /api/v1/shares` erzeugt einen Share‑Link.
- `GET /api/v1/shares/{token}` löst einen aktiven Link auf.
- Token‑Erzeugung mittels `secrets`‑Modul.
- Ablaufprüfung beim Lesen.
- Metadaten werden im Speicher gehalten (MVP).
- Dockerfile und compose.yaml ermöglichen containerisierten Betrieb.
- Testsuite lässt sich mit `pytest` ausführen.

### Stack
- Python (verpackt über `pyproject.toml`).
- Uvicorn ASGI‑Server (aus `uvicorn app.main:app` ersichtlich).
- FastAPI‑ähnliches Routing (impliziert durch den Uvicorn‑Befehl).
- Docker.
- pytest für Tests.

### Einrichtung / Nutzung
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
# Oder mit Docker
docker compose up
```

### Tests
```bash
pytest -q
```

### Einschränkungen
- Metadaten existieren nur im Speicher; bei Neustart des Prozesses gehen sie verloren.
- Kein Dateiupload oder -speicher; die MVP speichert keine Dateien dauerhaft.
- Für den Produktivbetrieb fehlen: S3‑kompatibler Speicher, signierte Downloads, Autorisierung, Malware‑Scanning, Audit‑Logs und eine Datenbank.

### Lizenz
Siehe die Datei `LICENSE`.
