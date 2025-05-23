<div align="center">

# tap-toggl

<div>
  <a href="https://polar.sh/reservoir-data/tap-toggl">
    <img src="https://polar.sh/embed/seeks-funding-shield.svg?org=edgarrmondragon&repo=tap-toggl"/>
  </a>
  <a href="https://scientific-python.org/specs/spec-0000/">
    <img alt="SPEC 0 — Minimum Supported Dependencies" src="https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038"/>
  </a>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-toggl/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-toggl/main.svg"/>
  </a>
  <a href="https://github.com/reservoir-data/tap-toggl/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-toggl"/>
  </a>
</div>

Singer tap for [Toggl](https://toggl.com) Time Tracking.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| username            | False    | None    | Toggl username |
| password            | False    | None    | Toggl password |
| api_token           | False    | None    | Toggl API token |
| start_date          | False    | None    | Earliest datetime to get data from |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| faker_config        | False    | None    | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an addtional dependency (through the `singer-sdk` `faker` extra or directly). |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |
| batch_config        | False    | None    |             |

A full list of supported settings and capabilities is available by running: `tap-toggl --about`

## Supported Python Versions

* 3.11
* 3.12
* 3.13
* 3.14

### Source Authentication and Authorization

There are two ways to authenticate for `tap-toggl`:

1. Using your username and password
2. Using your API token

If `api_token` is provided, `tap-toggl` will use it to authenticate. Otherwise, it will try to use `username` and `password`. If neither is provided, `tap-toggl` will raise an error.

## Usage

You can easily run `tap-toggl` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-toggl --version
tap-toggl --help
tap-toggl --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
uv tool install --with tox-uv tox
```

### Create and Run Tests

Run all tests:

```bash
tox run-parallel
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Go ahead and [install Meltano](https://docs.meltano.com/getting-started/installation/) if you haven't already.

1. Install all plugins

   ```bash
   meltano install
   ```

1. Check that the extractor is working properly

   ```bash
   meltano invoke tap-toggl --version
   ```

1. Execute an ELT pipeline

   ```bash
   meltano run tap-toggl target-jsonl
   ```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
