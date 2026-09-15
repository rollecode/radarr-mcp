<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Radarr MCP server

<img style="justify-content:center;text-align: center;width: 140px; height: auto;" alt="Radarr" src="public/logo.png" />

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Radarr](https://img.shields.io/badge/Radarr-FFC230?style=for-the-badge&logo=radarr&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-237%2F237-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Run Radarr from Claude.ai and Claude Code. All 237 operations of the v3 API are tools, generated from Radarr's own OpenAPI document. Not a curated subset: every endpoint Radarr's web interface can reach, this can reach.

<hr>

## Why not the other options

Measured against `Radarr.Api.V3/openapi.json`, which has 164 paths and 237 non-HEAD operations:

| Server | Radarr tools | Coverage |
| --- | --- | --- |
| `davidgibbons/mcp-arr` | 18 | 8 % |
| `niavasha/plex-mcp-server` | 8 | 3 % |
| `bardesss/arr-mcp` | unified verbs across 10 services | partial |
| This one | **237** | **100 %** |

The others hand-write a tool per endpoint they happened to need, so they cover movies, queue and calendar and stop there. Nothing else exposes `customformat`, `delayprofile`, `autotagging`, `exclusions`, `alternativetitle`, `extrafile`, `manualimport`, `seasonpass`, `remotepathmapping` or `qualitydefinition` at all.

## How it stays complete

`src/radarr_mcp/tools.py` is generated, not written:

```bash
curl -o openapi.json https://raw.githubusercontent.com/Radarr/Radarr/develop/src/Radarr.Api.V3/openapi.json
python scripts/generate_tools.py openapi.json src/radarr_mcp/tools.py
```

A test compares every generated call against every operation in the spec, in both directions. An endpoint Radarr adds and this misses fails the build; so does a tool pointing at an endpoint the spec does not define.

## Tool names

Verb first, derived from the method and path, so the name says what it does:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_movie`, `list_queue` |
| `get_*_by_id` | Read one record | `get_movie_by_id` |
| `create_*` | POST | `create_movie`, `create_command` |
| `update_*` | PUT | `update_qualityprofile_by_id` |
| `delete_*` | DELETE | `delete_moviefile_by_id` |

237 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## What is covered

Every resource group: `movie`, `moviefile`, `collection`, `credit`, `queue`, `history`, `blocklist`, `calendar`, `wanted`, `command`, `release`, `manualimport`, `rename`, `parse`, `indexer`, `indexerflag`, `downloadclient`, `importlist`, `exclusions`, `alternativetitle`, `extrafile`, `qualityprofile`, `qualitydefinition`, `customformat`, `customfilter`, `delayprofile`, `autotagging`, `notification`, `metadata`, `tag`, `rootfolder`, `remotepathmapping`, `language`, `localization`, `mediacover`, `filesystem`, `diskspace`, `health`, `log`, `update`, `backup`, `system` and the config endpoints.

## Setup

```bash
git clone https://github.com/rollecode/radarr-mcp.git
cd radarr-mcp
uv venv && uv pip install -e .
```

```bash
export RADARR_URL=http://127.0.0.1:7878
export RADARR_API_KEY=...   # Settings, General, Security
```

### Claude Code

```bash
claude mcp add radarr -- /path/to/radarr-mcp/.venv/bin/radarr-mcp
```

## Writing records

Radarr replaces a record on PUT rather than merging, so read it first, change the fields you want and send the whole object back as `body`. For a new resource, `list_*_schema` returns the shape it expects.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

## Licence

MIT
