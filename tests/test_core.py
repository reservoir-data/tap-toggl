"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from typing import Any

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_toggl.tap import TapToggl

SAMPLE_CONFIG: dict[str, Any] = {}

TestTapToggl = get_tap_test_class(
    TapToggl,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        max_records_limit=10,
        ignore_no_records_for_streams=["time_entries"],
    ),
)
