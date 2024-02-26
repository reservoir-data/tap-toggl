"""Toggl tap class."""

from __future__ import annotations

import typing as t

import requests
from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_toggl import streams

OPENAPI_URL = "https://api.planetscale.com/v1/openapi-spec"


class TapToggl(Tap):
    """Singer tap for Toggl."""

    name = "tap-toggl"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "username",
            th.StringType,
            description="Toggl username",
        ),
        th.Property(
            "password",
            th.StringType,
            description="Toggl password",
            secret=True,
        ),
        th.Property(
            "api_token",
            th.StringType,
            description="Toggl API token",
            secret=True,
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def get_openapi_schema(self) -> dict[t.Any, t.Any]:
        """Retrieve OpenAPI schema for this API.

        Returns:
            OpenAPI schema.
        """
        return requests.get(OPENAPI_URL, timeout=5).json()  # type: ignore[no-any-return]

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Toggl streams.
        """
        return [
            streams.TimeEntries(tap=self),
            streams.Organizations(tap=self),
        ]
