import secrets
from datetime import UTC, datetime, timedelta

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class ShareRequest(BaseModel):
    filename: str = Field(min_length=1, max_length=255)
    ttl_seconds: int = Field(default=3600, ge=60, le=604800)


class ShareLink(BaseModel):
    token: str
    filename: str
    expires_at: datetime


def create_app() -> FastAPI:
    app = FastAPI(title="SecureShare", version="0.1.0")
    links: dict[str, ShareLink] = {}

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "secure-share"}

    @app.post("/api/v1/shares", response_model=ShareLink)
    async def create_share(request: ShareRequest) -> ShareLink:
        token = secrets.token_urlsafe(24)
        link = ShareLink(
            token=token,
            filename=request.filename,
            expires_at=datetime.now(UTC) + timedelta(seconds=request.ttl_seconds),
        )
        links[token] = link
        return link

    @app.get("/api/v1/shares/{token}", response_model=ShareLink)
    async def resolve_share(token: str) -> ShareLink:
        link = links.get(token)
        if not link:
            raise HTTPException(status_code=404, detail="Share link not found")
        if link.expires_at <= datetime.now(UTC):
            raise HTTPException(status_code=410, detail="Share link expired")
        return link

    return app


app = create_app()
