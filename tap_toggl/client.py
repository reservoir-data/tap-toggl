"""REST client handling, including TogglStream base class."""

from __future__ import annotations

import typing as t

from requests.auth import HTTPBasicAuth
from singer_sdk import RESTStream


class TogglStream(RESTStream[t.Any]):
    """Toggl stream class."""

    url_base = "https://api.track.toggl.com/api/v9"
    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @property
    def authenticator(self) -> HTTPBasicAuth:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        if api_token := self.config.get("api_token"):
            return HTTPBasicAuth(api_token, "api_token")
        if username := self.config.get("username"):
            password = self.config.get("password")
            return HTTPBasicAuth(username, password)

        msg = "Invalid auth configuration"
        raise ValueError(msg)

        # match self.config["auth"]:
        #     case {"username": username, "password": password}:
        #         return HTTPBasicAuth(username, password)
        #     case {"api_token": api_token}:
        #         return HTTPBasicAuth(api_token, "api_token")
        #     case _:
        #         msg = "Invalid auth configuration"
        #         raise ValueError(msg)

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}

    def get_url_params(
        self,
        context: dict[str, t.Any] | None,
        next_page_token: t.Any | None,  # noqa: ARG002, ANN401
    ) -> dict[str, t.Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        params: dict[str, t.Any] = {}
        if start_date := self.get_starting_timestamp(context):
            params["since"] = int(start_date.timestamp())

        return params
