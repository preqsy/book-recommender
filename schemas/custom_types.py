from typing import Optional
from fastapi import Form


class OAuth2PasswordRequestFormLower:

    def __init__(
        self,
        grant_type: str = Form(None, regex="password"),
        username: str = Form(...),
        password: str = Form(...),
        client_id: Optional[str] = Form(None),
        client_secret: Optional[str] = Form(None),
    ):
        self.username = username.lower()
        self.password = password
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
