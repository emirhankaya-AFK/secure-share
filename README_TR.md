# Secure Share

[English](README.md) | [Türkçe](README_TR.md)

Süreli paylaşım bağlantıları oluşturan API. Kriptografik token'lar Python secrets ile üretilir ve okuma sırasında süre kontrol edilir.

POST /api/v1/shares bağlantı oluşturur; GET /api/v1/shares/{token} aktif bağlantıyı çözer. MVP metadata'yı bellekte tutar ve dosya yüklemez. Üretimde S3, imzalı indirme, yetkilendirme, malware taraması, audit log ve veritabanı gerekir.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

