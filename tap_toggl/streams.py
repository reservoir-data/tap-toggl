"""Stream type classes for tap-toggl."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_toggl.client import TogglStream


class TimeEntries(TogglStream):
    """Entries stream."""

    name = "time_entries"
    path = "/me/time_entries"
    primary_keys = ("id",)
    replication_key = "at"

    schema = th.PropertiesList(
        th.Property(
            "at",
            th.DateTimeType,
            description="When was last updated",
        ),
        th.Property(
            "billable",
            th.BooleanType,
            description="Whether the time entry is marked as billable",
        ),
        th.Property(
            "description",
            th.StringType,
            description=(
                "Time Entry description, null if not provided at creation/update"
            ),
        ),
        th.Property(
            "duration",
            th.IntegerType,
            description="Time entry duration. For running entries should be negative, preferable -1",  # noqa: E501
        ),
        th.Property(
            "duronly",
            th.BooleanType,
            description=(
                "Used to create a TE with a duration but without a stop time, this field is deprecated for GET endpoints where the value will always be true."  # noqa: E501
            ),
        ),
        th.Property(
            "id",
            th.IntegerType,
            description="Time Entry ID",
        ),
        th.Property(
            "pid",
            th.IntegerType,
            description="Project ID, legacy field",
        ),
        th.Property(
            "project_id",
            th.IntegerType,
            description="Project ID. Can be null if project was not provided or project was later deleted",  # noqa: E501
        ),
        th.Property(
            "server_deleted_at",
            th.DateTimeType,
            description="When was deleted, null if not deleted",
        ),
        th.Property(
            "start",
            th.DateTimeType,
            description="Start time in UTC",
        ),
        th.Property(
            "stop",
            th.DateTimeType,
            description="Stop time in UTC, can be null if it's still running or created with 'duration' and 'duronly' fields",  # noqa: E501
        ),
        th.Property(
            "tag_ids",
            th.ArrayType(th.IntegerType),
            description="Tag IDs, null if tags were not provided or were later deleted",
        ),
        th.Property(
            "tags",
            th.ArrayType(th.StringType),
            description="Tag names, null if tags were not provided or were later deleted",  # noqa: E501
        ),
        th.Property(
            "task_id",
            th.IntegerType,
            description="Task ID. Can be null if task was not provided or project was later deleted",  # noqa: E501
        ),
        th.Property(
            "uid",
            th.IntegerType,
            description="Time Entry creator ID, legacy field",
        ),
        th.Property(
            "user_id",
            th.IntegerType,
            description="Time Entry creator ID",
        ),
        th.Property(
            "workspace_id",
            th.IntegerType,
            description="Workspace ID",
        ),
    ).to_dict()


class Organizations(TogglStream):
    """Organizations stream."""

    name = "organizations"
    path = "/me/organizations"
    primary_keys = ("id",)
    replication_key = "at"

    schema = th.PropertiesList(
        th.Property(
            "admin",
            th.BooleanType,
            description="Whether the requester is an admin of the organization",
        ),
        th.Property(
            "at",
            th.DateTimeType,
            description="Organization's last modification date",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="Organization's creation date",
        ),
        th.Property(
            "id",
            th.IntegerType,
            description="Organization ID",
        ),
        th.Property(
            "is_multi_workspace_enabled",
            th.BooleanType,
            description="Is true when the organization option is_multi_workspace_enabled is set",  # noqa: E501
        ),
        th.Property(
            "is_unified",
            th.BooleanType,
            description="",
        ),
        th.Property(
            "max_data_retention_days",
            th.IntegerType,
            description="How far back free workspaces in this org can access data.",
        ),
        th.Property(
            "max_workspaces",
            th.IntegerType,
            description="Maximum number of workspaces allowed for the organization",
        ),
        th.Property(
            "name",
            th.StringType,
            description="Organization Name",
        ),
        th.Property(
            "owner",
            th.BooleanType,
            description="Whether the requester is a the owner of the organization",
        ),
        th.Property(
            "payment_methods",
            th.StringType,
            description="Organization's subscription payment methods. Omitted if empty.",  # noqa: E501
        ),
        th.Property(
            "permissions",
            th.StringType,
            description="",
        ),
        th.Property(
            "pricing_plan_id",
            th.IntegerType,
            description="Organization plan ID",
        ),
        th.Property(
            "server_deleted_at",
            th.DateTimeType,
            description="Organization's delete date",
        ),
        th.Property(
            "suspended_at",
            th.StringType,
            description="Whether the organization is currently suspended",
        ),
        th.Property(
            "trial_info",
            th.ObjectType(
                th.Property(
                    "last_pricing_plan_id",
                    th.IntegerType,
                    description="What was the previous plan before the trial",
                ),
                th.Property(
                    "next_payment_date",
                    th.StringType,
                    description="When the trial payment is due",
                ),
                th.Property(
                    "trial",
                    th.BooleanType,
                    description="Whether the organization's subscription is currently on trial",  # noqa: E501
                ),
                th.Property(
                    "trial_available",
                    th.BooleanType,
                    description="When a trial is available for this organization",
                ),
                th.Property(
                    "trial_end_date",
                    th.StringType,
                    description="When the trial ends",
                ),
            ),
        ),
        th.Property(
            "user_count",
            th.IntegerType,
            description="Number of organization users",
        ),
    ).to_dict()
