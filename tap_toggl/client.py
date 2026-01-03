"""REST client handling, including TogglStream base class."""

from __future__ import annotations

from typing import Any, override

from requests.auth import HTTPBasicAuth
from singer_sdk import RESTStream


class TogglStream(RESTStream[Any]):
    """Toggl stream class."""

    url_base = "https://api.track.toggl.com/api/v9"
    records_jsonpath = "$[*]"
    next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @override
    @property
    def authenticator(self) -> HTTPBasicAuth:
        """Get an authenticator for the Toggl API."""
        if api_token := self.config.get("api_token"):
            return HTTPBasicAuth(api_token, "api_token")
        if username := self.config.get("username"):
            password = self.config.get("password")
            return HTTPBasicAuth(username, password)  # type: ignore[arg-type]

        msg = "Invalid auth configuration"
        raise ValueError(msg)
