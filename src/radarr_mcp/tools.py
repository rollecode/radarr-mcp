"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/radarr_mcp/tools.py

One tool per operation, 237 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_autotagging(body: dict) -> str:
    """Create AutoTagging.

    POST /api/v3/autotagging

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/autotagging", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_command(body: dict) -> str:
    """Create Command.

    POST /api/v3/command

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/command", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_customfilter(body: dict) -> str:
    """Create CustomFilter.

    POST /api/v3/customfilter

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/customfilter", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_customformat(body: dict) -> str:
    """Create CustomFormat.

    POST /api/v3/customformat

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/customformat", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_delayprofile(body: dict) -> str:
    """Create DelayProfile.

    POST /api/v3/delayprofile

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/delayprofile", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_downloadclient(body: dict, force_save: bool | None = None) -> str:
    """Create DownloadClient.

    POST /api/v3/downloadclient

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v3/downloadclient", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_action_by_name(name: str, body: dict) -> str:
    """Create DownloadClient.

    POST /api/v3/downloadclient/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v3/downloadclient/action/{name}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_test(body: dict, force_test: bool | None = None) -> str:
    """Create DownloadClient.

    POST /api/v3/downloadclient/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v3/downloadclient/test", query={"forceTest": force_test}, body=body)


@mcp.tool(annotations=_WRITE)
def create_downloadclient_testall() -> str:
    """Create DownloadClient.

    POST /api/v3/downloadclient/testall
    """
    return call("POST", "/api/v3/downloadclient/testall", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_exclusions(body: dict) -> str:
    """Create ImportListExclusion.

    POST /api/v3/exclusions

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/exclusions", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_exclusions_bulk(body: dict) -> str:
    """Create ImportListExclusion.

    POST /api/v3/exclusions/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/exclusions/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_history_failed_by_id(id_: int) -> str:
    """Create History.

    POST /api/v3/history/failed/{id}

    Args:
        id_: Path parameter.
    """
    return call("POST", f"/api/v3/history/failed/{id_}", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_importlist(body: dict, force_save: bool | None = None) -> str:
    """Create ImportList.

    POST /api/v3/importlist

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v3/importlist", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def create_importlist_action_by_name(name: str, body: dict) -> str:
    """Create ImportList.

    POST /api/v3/importlist/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v3/importlist/action/{name}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_importlist_movie(body: dict) -> str:
    """Create ImportListMovies.

    POST /api/v3/importlist/movie

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/importlist/movie", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_importlist_test(body: dict, force_test: bool | None = None) -> str:
    """Create ImportList.

    POST /api/v3/importlist/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v3/importlist/test", query={"forceTest": force_test}, body=body)


@mcp.tool(annotations=_WRITE)
def create_importlist_testall() -> str:
    """Create ImportList.

    POST /api/v3/importlist/testall
    """
    return call("POST", "/api/v3/importlist/testall", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_indexer(body: dict, force_save: bool | None = None) -> str:
    """Create Indexer.

    POST /api/v3/indexer

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v3/indexer", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def create_indexer_action_by_name(name: str, body: dict) -> str:
    """Create Indexer.

    POST /api/v3/indexer/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v3/indexer/action/{name}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_indexer_test(body: dict, force_test: bool | None = None) -> str:
    """Create Indexer.

    POST /api/v3/indexer/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v3/indexer/test", query={"forceTest": force_test}, body=body)


@mcp.tool(annotations=_WRITE)
def create_indexer_testall() -> str:
    """Create Indexer.

    POST /api/v3/indexer/testall
    """
    return call("POST", "/api/v3/indexer/testall", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_login(body: dict, return_url: str | None = None) -> str:
    """Create Authentication.

    POST /login

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        return_url: Query parameter.
    """
    return call("POST", "/login", query={"returnUrl": return_url}, body=body)


@mcp.tool(annotations=_WRITE)
def create_manualimport(body: dict) -> str:
    """Create ManualImport.

    POST /api/v3/manualimport

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/manualimport", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_metadata(body: dict, force_save: bool | None = None) -> str:
    """Create Metadata.

    POST /api/v3/metadata

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v3/metadata", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def create_metadata_action_by_name(name: str, body: dict) -> str:
    """Create Metadata.

    POST /api/v3/metadata/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v3/metadata/action/{name}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_metadata_test(body: dict, force_test: bool | None = None) -> str:
    """Create Metadata.

    POST /api/v3/metadata/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v3/metadata/test", query={"forceTest": force_test}, body=body)


@mcp.tool(annotations=_WRITE)
def create_metadata_testall() -> str:
    """Create Metadata.

    POST /api/v3/metadata/testall
    """
    return call("POST", "/api/v3/metadata/testall", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_movie(body: dict) -> str:
    """Create Movie.

    POST /api/v3/movie

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/movie", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_movie_import(body: dict) -> str:
    """Create MovieImport.

    POST /api/v3/movie/import

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/movie/import", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_notification(body: dict, force_save: bool | None = None) -> str:
    """Create Notification.

    POST /api/v3/notification

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("POST", "/api/v3/notification", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def create_notification_action_by_name(name: str, body: dict) -> str:
    """Create Notification.

    POST /api/v3/notification/action/{name}

    Args:
        name: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v3/notification/action/{name}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_notification_test(body: dict, force_test: bool | None = None) -> str:
    """Create Notification.

    POST /api/v3/notification/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_test: Query parameter.
    """
    return call("POST", "/api/v3/notification/test", query={"forceTest": force_test}, body=body)


@mcp.tool(annotations=_WRITE)
def create_notification_testall() -> str:
    """Create Notification.

    POST /api/v3/notification/testall
    """
    return call("POST", "/api/v3/notification/testall", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_qualityprofile(body: dict) -> str:
    """Create QualityProfile.

    POST /api/v3/qualityprofile

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/qualityprofile", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_queue_grab_bulk(body: dict) -> str:
    """Create QueueAction.

    POST /api/v3/queue/grab/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/queue/grab/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_queue_grab_by_id(id_: int) -> str:
    """Create QueueAction.

    POST /api/v3/queue/grab/{id}

    Args:
        id_: Path parameter.
    """
    return call("POST", f"/api/v3/queue/grab/{id_}", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_release(body: dict) -> str:
    """Create Release.

    POST /api/v3/release

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/release", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_release_push(body: dict) -> str:
    """Create ReleasePush.

    POST /api/v3/release/push

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/release/push", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_releaseprofile(body: dict) -> str:
    """Create ReleaseProfile.

    POST /api/v3/releaseprofile

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/releaseprofile", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_remotepathmapping(body: dict) -> str:
    """Create RemotePathMapping.

    POST /api/v3/remotepathmapping

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/remotepathmapping", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_rootfolder(body: dict) -> str:
    """Create RootFolder.

    POST /api/v3/rootfolder

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/rootfolder", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_system_backup_restore_by_id(id_: int) -> str:
    """Create Backup.

    POST /api/v3/system/backup/restore/{id}

    Args:
        id_: Path parameter.
    """
    return call("POST", f"/api/v3/system/backup/restore/{id_}", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_system_backup_restore_upload() -> str:
    """Create Backup.

    POST /api/v3/system/backup/restore/upload
    """
    return call("POST", "/api/v3/system/backup/restore/upload", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_system_restart() -> str:
    """Create System.

    POST /api/v3/system/restart
    """
    return call("POST", "/api/v3/system/restart", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_system_shutdown() -> str:
    """Create System.

    POST /api/v3/system/shutdown
    """
    return call("POST", "/api/v3/system/shutdown", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_tag(body: dict) -> str:
    """Create Tag.

    POST /api/v3/tag

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v3/tag", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_autotagging_by_id(id_: int) -> str:
    """Delete AutoTagging.

    DELETE /api/v3/autotagging/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/autotagging/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_blocklist_bulk(body: dict) -> str:
    """Delete Blocklist.

    DELETE /api/v3/blocklist/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/blocklist/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_blocklist_by_id(id_: int) -> str:
    """Delete Blocklist.

    DELETE /api/v3/blocklist/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/blocklist/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_command_by_id(id_: int) -> str:
    """Delete Command.

    DELETE /api/v3/command/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/command/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_customfilter_by_id(id_: int) -> str:
    """Delete CustomFilter.

    DELETE /api/v3/customfilter/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/customfilter/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_customformat_bulk(body: dict) -> str:
    """Delete CustomFormat.

    DELETE /api/v3/customformat/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/customformat/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_customformat_by_id(id_: int) -> str:
    """Delete CustomFormat.

    DELETE /api/v3/customformat/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/customformat/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_delayprofile_by_id(id_: int) -> str:
    """Delete DelayProfile.

    DELETE /api/v3/delayprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/delayprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_downloadclient_bulk(body: dict) -> str:
    """Delete DownloadClient.

    DELETE /api/v3/downloadclient/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/downloadclient/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_downloadclient_by_id(id_: int) -> str:
    """Delete DownloadClient.

    DELETE /api/v3/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/downloadclient/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_exclusions_bulk(body: dict) -> str:
    """Delete ImportListExclusion.

    DELETE /api/v3/exclusions/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/exclusions/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_exclusions_by_id(id_: int) -> str:
    """Delete ImportListExclusion.

    DELETE /api/v3/exclusions/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/exclusions/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_importlist_bulk(body: dict) -> str:
    """Delete ImportList.

    DELETE /api/v3/importlist/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/importlist/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_importlist_by_id(id_: int) -> str:
    """Delete ImportList.

    DELETE /api/v3/importlist/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/importlist/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_indexer_bulk(body: dict) -> str:
    """Delete Indexer.

    DELETE /api/v3/indexer/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/indexer/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_indexer_by_id(id_: int) -> str:
    """Delete Indexer.

    DELETE /api/v3/indexer/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/indexer/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_metadata_by_id(id_: int) -> str:
    """Delete Metadata.

    DELETE /api/v3/metadata/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/metadata/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_movie_by_id(id_: int, delete_files: bool | None = None, add_import_exclusion: bool | None = None) -> str:
    """Delete Movie.

    DELETE /api/v3/movie/{id}

    Args:
        id_: Path parameter.
        delete_files: Query parameter.
        add_import_exclusion: Query parameter.
    """
    return call("DELETE", f"/api/v3/movie/{id_}", query={"deleteFiles": delete_files, "addImportExclusion": add_import_exclusion}, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_movie_editor(body: dict) -> str:
    """Delete MovieEditor.

    DELETE /api/v3/movie/editor

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/movie/editor", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_moviefile_bulk(body: dict) -> str:
    """Delete MovieFile.

    DELETE /api/v3/moviefile/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", "/api/v3/moviefile/bulk", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_moviefile_by_id(id_: int) -> str:
    """Delete MovieFile.

    DELETE /api/v3/moviefile/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/moviefile/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_notification_by_id(id_: int) -> str:
    """Delete Notification.

    DELETE /api/v3/notification/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/notification/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_qualityprofile_by_id(id_: int) -> str:
    """Delete QualityProfile.

    DELETE /api/v3/qualityprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/qualityprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_queue_bulk(body: dict, remove_from_client: bool | None = None, blocklist: bool | None = None, skip_redownload: bool | None = None, change_category: bool | None = None) -> str:
    """Delete Queue.

    DELETE /api/v3/queue/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        remove_from_client: Query parameter.
        blocklist: Query parameter.
        skip_redownload: Query parameter.
        change_category: Query parameter.
    """
    return call("DELETE", "/api/v3/queue/bulk", query={"removeFromClient": remove_from_client, "blocklist": blocklist, "skipRedownload": skip_redownload, "changeCategory": change_category}, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_queue_by_id(id_: int, remove_from_client: bool | None = None, blocklist: bool | None = None, skip_redownload: bool | None = None, change_category: bool | None = None) -> str:
    """Delete Queue.

    DELETE /api/v3/queue/{id}

    Args:
        id_: Path parameter.
        remove_from_client: Query parameter.
        blocklist: Query parameter.
        skip_redownload: Query parameter.
        change_category: Query parameter.
    """
    return call("DELETE", f"/api/v3/queue/{id_}", query={"removeFromClient": remove_from_client, "blocklist": blocklist, "skipRedownload": skip_redownload, "changeCategory": change_category}, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_releaseprofile_by_id(id_: int) -> str:
    """Delete ReleaseProfile.

    DELETE /api/v3/releaseprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/releaseprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_remotepathmapping_by_id(id_: int) -> str:
    """Delete RemotePathMapping.

    DELETE /api/v3/remotepathmapping/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/remotepathmapping/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_rootfolder_by_id(id_: int) -> str:
    """Delete RootFolder.

    DELETE /api/v3/rootfolder/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/rootfolder/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_system_backup_by_id(id_: int) -> str:
    """Delete Backup.

    DELETE /api/v3/system/backup/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/system/backup/{id_}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_tag_by_id(id_: int) -> str:
    """Delete Tag.

    DELETE /api/v3/tag/{id}

    Args:
        id_: Path parameter.
    """
    return call("DELETE", f"/api/v3/tag/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_alttitle_by_id(id_: int) -> str:
    """Read AlternativeTitle.

    GET /api/v3/alttitle/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/alttitle/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_autotagging_by_id(id_: int) -> str:
    """Read AutoTagging.

    GET /api/v3/autotagging/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/autotagging/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_by_path(path: str) -> str:
    """Read StaticResource.

    GET /{path}

    Args:
        path: Path parameter.
    """
    return call("GET", f"/{path}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_collection_by_id(id_: int) -> str:
    """Read Collection.

    GET /api/v3/collection/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/collection/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_command_by_id(id_: int) -> str:
    """Read Command.

    GET /api/v3/command/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/command/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_downloadclient_by_id(id_: int) -> str:
    """Read DownloadClientConfig.

    GET /api/v3/config/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/downloadclient/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_host_by_id(id_: int) -> str:
    """Read HostConfig.

    GET /api/v3/config/host/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/host/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_importlist_by_id(id_: int) -> str:
    """Read ImportListConfig.

    GET /api/v3/config/importlist/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/importlist/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_indexer_by_id(id_: int) -> str:
    """Read IndexerConfig.

    GET /api/v3/config/indexer/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/indexer/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_mediamanagement_by_id(id_: int) -> str:
    """Read MediaManagementConfig.

    GET /api/v3/config/mediamanagement/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/mediamanagement/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_metadata_by_id(id_: int) -> str:
    """Read MetadataConfig.

    GET /api/v3/config/metadata/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/metadata/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_naming_by_id(id_: int) -> str:
    """Read NamingConfig.

    GET /api/v3/config/naming/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/naming/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_config_ui_by_id(id_: int) -> str:
    """Read UiConfig.

    GET /api/v3/config/ui/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/config/ui/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_content_by_path(path: str) -> str:
    """Read StaticResource.

    GET /content/{path}

    Args:
        path: Path parameter.
    """
    return call("GET", f"/content/{path}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_credit_by_id(id_: int) -> str:
    """Read Credit.

    GET /api/v3/credit/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/credit/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_customfilter_by_id(id_: int) -> str:
    """Read CustomFilter.

    GET /api/v3/customfilter/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/customfilter/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_customformat_by_id(id_: int) -> str:
    """Read CustomFormat.

    GET /api/v3/customformat/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/customformat/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_delayprofile_by_id(id_: int) -> str:
    """Read DelayProfile.

    GET /api/v3/delayprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/delayprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_downloadclient_by_id(id_: int) -> str:
    """Read DownloadClient.

    GET /api/v3/downloadclient/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/downloadclient/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_exclusions_by_id(id_: int) -> str:
    """Read ImportListExclusion.

    GET /api/v3/exclusions/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/exclusions/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_importlist_by_id(id_: int) -> str:
    """Read ImportList.

    GET /api/v3/importlist/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/importlist/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_indexer_by_id(id_: int) -> str:
    """Read Indexer.

    GET /api/v3/indexer/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/indexer/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_language_by_id(id_: int) -> str:
    """Read Language.

    GET /api/v3/language/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/language/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_log_file_by_filename(filename: str) -> str:
    """Read LogFile.

    GET /api/v3/log/file/{filename}

    Args:
        filename: Path parameter.
    """
    return call("GET", f"/api/v3/log/file/{filename}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_log_file_update_by_filename(filename: str) -> str:
    """Read UpdateLogFile.

    GET /api/v3/log/file/update/{filename}

    Args:
        filename: Path parameter.
    """
    return call("GET", f"/api/v3/log/file/update/{filename}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_mediacover_by_movie_id_by_filename(movie_id: int, filename: str) -> str:
    """Read MediaCover.

    GET /api/v3/mediacover/{movieId}/{filename}

    Args:
        movie_id: Path parameter.
        filename: Path parameter.
    """
    return call("GET", f"/api/v3/mediacover/{movie_id}/{filename}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_metadata_by_id(id_: int) -> str:
    """Read Metadata.

    GET /api/v3/metadata/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/metadata/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_id(id_: int) -> str:
    """Read Movie.

    GET /api/v3/movie/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/movie/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_id_folder(id_: int) -> str:
    """Read MovieFolder.

    GET /api/v3/movie/{id}/folder

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/movie/{id_}/folder", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_moviefile_by_id(id_: int) -> str:
    """Read MovieFile.

    GET /api/v3/moviefile/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/moviefile/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_notification_by_id(id_: int) -> str:
    """Read Notification.

    GET /api/v3/notification/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/notification/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_qualitydefinition_by_id(id_: int) -> str:
    """Read QualityDefinition.

    GET /api/v3/qualitydefinition/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/qualitydefinition/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_qualityprofile_by_id(id_: int) -> str:
    """Read QualityProfile.

    GET /api/v3/qualityprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/qualityprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_releaseprofile_by_id(id_: int) -> str:
    """Read ReleaseProfile.

    GET /api/v3/releaseprofile/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/releaseprofile/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_remotepathmapping_by_id(id_: int) -> str:
    """Read RemotePathMapping.

    GET /api/v3/remotepathmapping/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/remotepathmapping/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_rootfolder_by_id(id_: int) -> str:
    """Read RootFolder.

    GET /api/v3/rootfolder/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/rootfolder/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_system_task_by_id(id_: int) -> str:
    """Read Task.

    GET /api/v3/system/task/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/system/task/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_tag_by_id(id_: int) -> str:
    """Read Tag.

    GET /api/v3/tag/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/tag/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_tag_detail_by_id(id_: int) -> str:
    """Read TagDetails.

    GET /api/v3/tag/detail/{id}

    Args:
        id_: Path parameter.
    """
    return call("GET", f"/api/v3/tag/detail/{id_}", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_alttitle(movie_id: int | None = None, movie_metadata_id: int | None = None) -> str:
    """Read AlternativeTitle.

    GET /api/v3/alttitle

    Args:
        movie_id: Query parameter.
        movie_metadata_id: Query parameter.
    """
    return call("GET", "/api/v3/alttitle", query={"movieId": movie_id, "movieMetadataId": movie_metadata_id}, body=None)


@mcp.tool(annotations=_READ)
def list_api() -> str:
    """Read ApiInfo.

    GET /api
    """
    return call("GET", "/api", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_autotagging() -> str:
    """Read AutoTagging.

    GET /api/v3/autotagging
    """
    return call("GET", "/api/v3/autotagging", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_autotagging_schema() -> str:
    """Read AutoTagging.

    GET /api/v3/autotagging/schema
    """
    return call("GET", "/api/v3/autotagging/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_blocklist(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, movie_ids: list | None = None, protocols: list | None = None) -> str:
    """Read Blocklist.

    GET /api/v3/blocklist

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        movie_ids: Query parameter.
        protocols: Query parameter.
    """
    return call("GET", "/api/v3/blocklist", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "movieIds": movie_ids, "protocols": protocols}, body=None)


@mcp.tool(annotations=_READ)
def list_blocklist_movie(movie_id: int | None = None) -> str:
    """Read Blocklist.

    GET /api/v3/blocklist/movie

    Args:
        movie_id: Query parameter.
    """
    return call("GET", "/api/v3/blocklist/movie", query={"movieId": movie_id}, body=None)


@mcp.tool(annotations=_READ)
def list_calendar(start: str | None = None, end: str | None = None, unmonitored: bool | None = None, tags: str | None = None) -> str:
    """Read Calendar.

    GET /api/v3/calendar

    Args:
        start: Query parameter.
        end: Query parameter.
        unmonitored: Query parameter.
        tags: Query parameter.
    """
    return call("GET", "/api/v3/calendar", query={"start": start, "end": end, "unmonitored": unmonitored, "tags": tags}, body=None)


@mcp.tool(annotations=_READ)
def list_collection(tmdb_id: int | None = None) -> str:
    """Read Collection.

    GET /api/v3/collection

    Args:
        tmdb_id: Query parameter.
    """
    return call("GET", "/api/v3/collection", query={"tmdbId": tmdb_id}, body=None)


@mcp.tool(annotations=_READ)
def list_command() -> str:
    """Read Command.

    GET /api/v3/command
    """
    return call("GET", "/api/v3/command", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_downloadclient() -> str:
    """Read DownloadClientConfig.

    GET /api/v3/config/downloadclient
    """
    return call("GET", "/api/v3/config/downloadclient", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_host() -> str:
    """Read HostConfig.

    GET /api/v3/config/host
    """
    return call("GET", "/api/v3/config/host", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_importlist() -> str:
    """Read ImportListConfig.

    GET /api/v3/config/importlist
    """
    return call("GET", "/api/v3/config/importlist", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_indexer() -> str:
    """Read IndexerConfig.

    GET /api/v3/config/indexer
    """
    return call("GET", "/api/v3/config/indexer", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_mediamanagement() -> str:
    """Read MediaManagementConfig.

    GET /api/v3/config/mediamanagement
    """
    return call("GET", "/api/v3/config/mediamanagement", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_metadata() -> str:
    """Read MetadataConfig.

    GET /api/v3/config/metadata
    """
    return call("GET", "/api/v3/config/metadata", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_naming() -> str:
    """Read NamingConfig.

    GET /api/v3/config/naming
    """
    return call("GET", "/api/v3/config/naming", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_config_naming_examples(rename_movies: bool | None = None, replace_illegal_characters: bool | None = None, colon_replacement_format: dict | None = None, standard_movie_format: str | None = None, movie_folder_format: str | None = None, id_: int | None = None, resource_name: str | None = None) -> str:
    """Read NamingConfig.

    GET /api/v3/config/naming/examples

    Args:
        rename_movies: Query parameter.
        replace_illegal_characters: Query parameter.
        colon_replacement_format: Query parameter.
        standard_movie_format: Query parameter.
        movie_folder_format: Query parameter.
        id_: Query parameter.
        resource_name: Query parameter.
    """
    return call("GET", "/api/v3/config/naming/examples", query={"renameMovies": rename_movies, "replaceIllegalCharacters": replace_illegal_characters, "colonReplacementFormat": colon_replacement_format, "standardMovieFormat": standard_movie_format, "movieFolderFormat": movie_folder_format, "id": id_, "resourceName": resource_name}, body=None)


@mcp.tool(annotations=_READ)
def list_config_ui() -> str:
    """Read UiConfig.

    GET /api/v3/config/ui
    """
    return call("GET", "/api/v3/config/ui", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_credit(movie_id: int | None = None, movie_metadata_id: int | None = None) -> str:
    """Read Credit.

    GET /api/v3/credit

    Args:
        movie_id: Query parameter.
        movie_metadata_id: Query parameter.
    """
    return call("GET", "/api/v3/credit", query={"movieId": movie_id, "movieMetadataId": movie_metadata_id}, body=None)


@mcp.tool(annotations=_READ)
def list_customfilter() -> str:
    """Read CustomFilter.

    GET /api/v3/customfilter
    """
    return call("GET", "/api/v3/customfilter", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_customformat() -> str:
    """Read CustomFormat.

    GET /api/v3/customformat
    """
    return call("GET", "/api/v3/customformat", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_customformat_schema() -> str:
    """Read CustomFormat.

    GET /api/v3/customformat/schema
    """
    return call("GET", "/api/v3/customformat/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_delayprofile() -> str:
    """Read DelayProfile.

    GET /api/v3/delayprofile
    """
    return call("GET", "/api/v3/delayprofile", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_diskspace() -> str:
    """Read DiskSpace.

    GET /api/v3/diskspace
    """
    return call("GET", "/api/v3/diskspace", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_downloadclient() -> str:
    """Read DownloadClient.

    GET /api/v3/downloadclient
    """
    return call("GET", "/api/v3/downloadclient", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_downloadclient_schema() -> str:
    """Read DownloadClient.

    GET /api/v3/downloadclient/schema
    """
    return call("GET", "/api/v3/downloadclient/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_exclusions() -> str:
    """Read ImportListExclusion.

    GET /api/v3/exclusions
    """
    return call("GET", "/api/v3/exclusions", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_exclusions_paged(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None) -> str:
    """Read ImportListExclusion.

    GET /api/v3/exclusions/paged

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
    """
    return call("GET", "/api/v3/exclusions/paged", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction}, body=None)


@mcp.tool(annotations=_READ)
def list_extrafile(movie_id: int | None = None) -> str:
    """Read ExtraFile.

    GET /api/v3/extrafile

    Args:
        movie_id: Query parameter.
    """
    return call("GET", "/api/v3/extrafile", query={"movieId": movie_id}, body=None)


@mcp.tool(annotations=_READ)
def list_feed_v3_calendar_radarr_ics(past_days: int | None = None, future_days: int | None = None, tags: str | None = None, unmonitored: bool | None = None, release_types: list | None = None) -> str:
    """Read CalendarFeed.

    GET /feed/v3/calendar/radarr.ics

    Args:
        past_days: Query parameter.
        future_days: Query parameter.
        tags: Query parameter.
        unmonitored: Query parameter.
        release_types: Query parameter.
    """
    return call("GET", "/feed/v3/calendar/radarr.ics", query={"pastDays": past_days, "futureDays": future_days, "tags": tags, "unmonitored": unmonitored, "releaseTypes": release_types}, body=None)


@mcp.tool(annotations=_READ)
def list_filesystem(path: str | None = None, include_files: bool | None = None, allow_folders_without_trailing_slashes: bool | None = None) -> str:
    """Read FileSystem.

    GET /api/v3/filesystem

    Args:
        path: Query parameter.
        include_files: Query parameter.
        allow_folders_without_trailing_slashes: Query parameter.
    """
    return call("GET", "/api/v3/filesystem", query={"path": path, "includeFiles": include_files, "allowFoldersWithoutTrailingSlashes": allow_folders_without_trailing_slashes}, body=None)


@mcp.tool(annotations=_READ)
def list_filesystem_mediafiles(path: str | None = None) -> str:
    """Read FileSystem.

    GET /api/v3/filesystem/mediafiles

    Args:
        path: Query parameter.
    """
    return call("GET", "/api/v3/filesystem/mediafiles", query={"path": path}, body=None)


@mcp.tool(annotations=_READ)
def list_filesystem_type(path: str | None = None) -> str:
    """Read FileSystem.

    GET /api/v3/filesystem/type

    Args:
        path: Query parameter.
    """
    return call("GET", "/api/v3/filesystem/type", query={"path": path}, body=None)


@mcp.tool(annotations=_READ)
def list_health() -> str:
    """Read Health.

    GET /api/v3/health
    """
    return call("GET", "/api/v3/health", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_history(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, include_movie: bool | None = None, event_type: list | None = None, download_id: str | None = None, movie_ids: list | None = None, languages: list | None = None, quality: list | None = None) -> str:
    """Read History.

    GET /api/v3/history

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        include_movie: Query parameter.
        event_type: Query parameter.
        download_id: Query parameter.
        movie_ids: Query parameter.
        languages: Query parameter.
        quality: Query parameter.
    """
    return call("GET", "/api/v3/history", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "includeMovie": include_movie, "eventType": event_type, "downloadId": download_id, "movieIds": movie_ids, "languages": languages, "quality": quality}, body=None)


@mcp.tool(annotations=_READ)
def list_history_movie(movie_id: int | None = None, event_type: dict | None = None, include_movie: bool | None = None) -> str:
    """Read History.

    GET /api/v3/history/movie

    Args:
        movie_id: Query parameter.
        event_type: Query parameter.
        include_movie: Query parameter.
    """
    return call("GET", "/api/v3/history/movie", query={"movieId": movie_id, "eventType": event_type, "includeMovie": include_movie}, body=None)


@mcp.tool(annotations=_READ)
def list_history_since(date: str | None = None, event_type: dict | None = None, include_movie: bool | None = None) -> str:
    """Read History.

    GET /api/v3/history/since

    Args:
        date: Query parameter.
        event_type: Query parameter.
        include_movie: Query parameter.
    """
    return call("GET", "/api/v3/history/since", query={"date": date, "eventType": event_type, "includeMovie": include_movie}, body=None)


@mcp.tool(annotations=_READ)
def list_importlist() -> str:
    """Read ImportList.

    GET /api/v3/importlist
    """
    return call("GET", "/api/v3/importlist", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_importlist_movie(include_recommendations: bool | None = None, include_trending: bool | None = None, include_popular: bool | None = None) -> str:
    """Read ImportListMovies.

    GET /api/v3/importlist/movie

    Args:
        include_recommendations: Query parameter.
        include_trending: Query parameter.
        include_popular: Query parameter.
    """
    return call("GET", "/api/v3/importlist/movie", query={"includeRecommendations": include_recommendations, "includeTrending": include_trending, "includePopular": include_popular}, body=None)


@mcp.tool(annotations=_READ)
def list_importlist_schema() -> str:
    """Read ImportList.

    GET /api/v3/importlist/schema
    """
    return call("GET", "/api/v3/importlist/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_indexer() -> str:
    """Read Indexer.

    GET /api/v3/indexer
    """
    return call("GET", "/api/v3/indexer", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_indexer_schema() -> str:
    """Read Indexer.

    GET /api/v3/indexer/schema
    """
    return call("GET", "/api/v3/indexer/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_indexerflag() -> str:
    """Read IndexerFlag.

    GET /api/v3/indexerflag
    """
    return call("GET", "/api/v3/indexerflag", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_language() -> str:
    """Read Language.

    GET /api/v3/language
    """
    return call("GET", "/api/v3/language", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_localization() -> str:
    """Read Localization.

    GET /api/v3/localization
    """
    return call("GET", "/api/v3/localization", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_localization_language() -> str:
    """Read Localization.

    GET /api/v3/localization/language
    """
    return call("GET", "/api/v3/localization/language", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_log(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, level: str | None = None) -> str:
    """Read Log.

    GET /api/v3/log

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        level: Query parameter.
    """
    return call("GET", "/api/v3/log", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "level": level}, body=None)


@mcp.tool(annotations=_READ)
def list_log_file() -> str:
    """Read LogFile.

    GET /api/v3/log/file
    """
    return call("GET", "/api/v3/log/file", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_log_file_update() -> str:
    """Read UpdateLogFile.

    GET /api/v3/log/file/update
    """
    return call("GET", "/api/v3/log/file/update", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_login() -> str:
    """Read StaticResource.

    GET /login
    """
    return call("GET", "/login", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_logout() -> str:
    """Read Authentication.

    GET /logout
    """
    return call("GET", "/logout", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_manualimport(folder: str | None = None, download_id: str | None = None, movie_id: int | None = None, filter_existing_files: bool | None = None) -> str:
    """Read ManualImport.

    GET /api/v3/manualimport

    Args:
        folder: Query parameter.
        download_id: Query parameter.
        movie_id: Query parameter.
        filter_existing_files: Query parameter.
    """
    return call("GET", "/api/v3/manualimport", query={"folder": folder, "downloadId": download_id, "movieId": movie_id, "filterExistingFiles": filter_existing_files}, body=None)


@mcp.tool(annotations=_READ)
def list_metadata() -> str:
    """Read Metadata.

    GET /api/v3/metadata
    """
    return call("GET", "/api/v3/metadata", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_metadata_schema() -> str:
    """Read Metadata.

    GET /api/v3/metadata/schema
    """
    return call("GET", "/api/v3/metadata/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_movie(tmdb_id: int | None = None, exclude_local_covers: bool | None = None, language_id: int | None = None) -> str:
    """Read Movie.

    GET /api/v3/movie

    Args:
        tmdb_id: Query parameter.
        exclude_local_covers: Query parameter.
        language_id: Query parameter.
    """
    return call("GET", "/api/v3/movie", query={"tmdbId": tmdb_id, "excludeLocalCovers": exclude_local_covers, "languageId": language_id}, body=None)


@mcp.tool(annotations=_READ)
def list_movie_lookup(term: str | None = None) -> str:
    """Read MovieLookup.

    GET /api/v3/movie/lookup

    Args:
        term: Query parameter.
    """
    return call("GET", "/api/v3/movie/lookup", query={"term": term}, body=None)


@mcp.tool(annotations=_READ)
def list_movie_lookup_imdb(imdb_id: str | None = None) -> str:
    """Read MovieLookup.

    GET /api/v3/movie/lookup/imdb

    Args:
        imdb_id: Query parameter.
    """
    return call("GET", "/api/v3/movie/lookup/imdb", query={"imdbId": imdb_id}, body=None)


@mcp.tool(annotations=_READ)
def list_movie_lookup_tmdb(tmdb_id: int | None = None) -> str:
    """Read MovieLookup.

    GET /api/v3/movie/lookup/tmdb

    Args:
        tmdb_id: Query parameter.
    """
    return call("GET", "/api/v3/movie/lookup/tmdb", query={"tmdbId": tmdb_id}, body=None)


@mcp.tool(annotations=_READ)
def list_moviefile(movie_id: list | None = None, movie_file_ids: list | None = None) -> str:
    """Read MovieFile.

    GET /api/v3/moviefile

    Args:
        movie_id: Query parameter.
        movie_file_ids: Query parameter.
    """
    return call("GET", "/api/v3/moviefile", query={"movieId": movie_id, "movieFileIds": movie_file_ids}, body=None)


@mcp.tool(annotations=_READ)
def list_notification() -> str:
    """Read Notification.

    GET /api/v3/notification
    """
    return call("GET", "/api/v3/notification", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_notification_schema() -> str:
    """Read Notification.

    GET /api/v3/notification/schema
    """
    return call("GET", "/api/v3/notification/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_parse(title: str | None = None) -> str:
    """Read Parse.

    GET /api/v3/parse

    Args:
        title: Query parameter.
    """
    return call("GET", "/api/v3/parse", query={"title": title}, body=None)


@mcp.tool(annotations=_READ)
def list_ping() -> str:
    """Read Ping.

    GET /ping
    """
    return call("GET", "/ping", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_qualitydefinition() -> str:
    """Read QualityDefinition.

    GET /api/v3/qualitydefinition
    """
    return call("GET", "/api/v3/qualitydefinition", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_qualitydefinition_limits() -> str:
    """Read QualityDefinition.

    GET /api/v3/qualitydefinition/limits
    """
    return call("GET", "/api/v3/qualitydefinition/limits", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_qualityprofile() -> str:
    """Read QualityProfile.

    GET /api/v3/qualityprofile
    """
    return call("GET", "/api/v3/qualityprofile", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_qualityprofile_schema() -> str:
    """Read QualityProfileSchema.

    GET /api/v3/qualityprofile/schema
    """
    return call("GET", "/api/v3/qualityprofile/schema", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_queue(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, include_unknown_movie_items: bool | None = None, include_movie: bool | None = None, movie_ids: list | None = None, protocol: dict | None = None, languages: list | None = None, quality: list | None = None, status: list | None = None) -> str:
    """Read Queue.

    GET /api/v3/queue

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        include_unknown_movie_items: Query parameter.
        include_movie: Query parameter.
        movie_ids: Query parameter.
        protocol: Query parameter.
        languages: Query parameter.
        quality: Query parameter.
        status: Query parameter.
    """
    return call("GET", "/api/v3/queue", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "includeUnknownMovieItems": include_unknown_movie_items, "includeMovie": include_movie, "movieIds": movie_ids, "protocol": protocol, "languages": languages, "quality": quality, "status": status}, body=None)


@mcp.tool(annotations=_READ)
def list_queue_details(movie_id: int | None = None, include_movie: bool | None = None) -> str:
    """Read QueueDetails.

    GET /api/v3/queue/details

    Args:
        movie_id: Query parameter.
        include_movie: Query parameter.
    """
    return call("GET", "/api/v3/queue/details", query={"movieId": movie_id, "includeMovie": include_movie}, body=None)


@mcp.tool(annotations=_READ)
def list_queue_status() -> str:
    """Read QueueStatus.

    GET /api/v3/queue/status
    """
    return call("GET", "/api/v3/queue/status", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_release(movie_id: int | None = None) -> str:
    """Read Release.

    GET /api/v3/release

    Args:
        movie_id: Query parameter.
    """
    return call("GET", "/api/v3/release", query={"movieId": movie_id}, body=None)


@mcp.tool(annotations=_READ)
def list_releaseprofile() -> str:
    """Read ReleaseProfile.

    GET /api/v3/releaseprofile
    """
    return call("GET", "/api/v3/releaseprofile", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_remotepathmapping() -> str:
    """Read RemotePathMapping.

    GET /api/v3/remotepathmapping
    """
    return call("GET", "/api/v3/remotepathmapping", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_rename(movie_id: list | None = None) -> str:
    """Read RenameMovie.

    GET /api/v3/rename

    Args:
        movie_id: Query parameter.
    """
    return call("GET", "/api/v3/rename", query={"movieId": movie_id}, body=None)


@mcp.tool(annotations=_READ)
def list_root(path: str) -> str:
    """Read StaticResource.

    GET /

    Args:
        path: Path parameter.
    """
    return call("GET", "/", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_rootfolder() -> str:
    """Read RootFolder.

    GET /api/v3/rootfolder
    """
    return call("GET", "/api/v3/rootfolder", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_system_backup() -> str:
    """Read Backup.

    GET /api/v3/system/backup
    """
    return call("GET", "/api/v3/system/backup", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_system_routes() -> str:
    """Read System.

    GET /api/v3/system/routes
    """
    return call("GET", "/api/v3/system/routes", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_system_routes_duplicate() -> str:
    """Read System.

    GET /api/v3/system/routes/duplicate
    """
    return call("GET", "/api/v3/system/routes/duplicate", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_system_status() -> str:
    """Read System.

    GET /api/v3/system/status
    """
    return call("GET", "/api/v3/system/status", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_system_task() -> str:
    """Read Task.

    GET /api/v3/system/task
    """
    return call("GET", "/api/v3/system/task", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_tag() -> str:
    """Read Tag.

    GET /api/v3/tag
    """
    return call("GET", "/api/v3/tag", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_tag_detail() -> str:
    """Read TagDetails.

    GET /api/v3/tag/detail
    """
    return call("GET", "/api/v3/tag/detail", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_update() -> str:
    """Read Update.

    GET /api/v3/update
    """
    return call("GET", "/api/v3/update", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_wanted_cutoff(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, monitored: bool | None = None) -> str:
    """Read Cutoff.

    GET /api/v3/wanted/cutoff

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        monitored: Query parameter.
    """
    return call("GET", "/api/v3/wanted/cutoff", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "monitored": monitored}, body=None)


@mcp.tool(annotations=_READ)
def list_wanted_missing(page: int | None = None, page_size: int | None = None, sort_key: str | None = None, sort_direction: dict | None = None, monitored: bool | None = None) -> str:
    """Read Missing.

    GET /api/v3/wanted/missing

    Args:
        page: Query parameter.
        page_size: Query parameter.
        sort_key: Query parameter.
        sort_direction: Query parameter.
        monitored: Query parameter.
    """
    return call("GET", "/api/v3/wanted/missing", query={"page": page, "pageSize": page_size, "sortKey": sort_key, "sortDirection": sort_direction, "monitored": monitored}, body=None)


@mcp.tool(annotations=_WRITE)
def update_autotagging_by_id(id_: str, body: dict) -> str:
    """Update AutoTagging.

    PUT /api/v3/autotagging/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/autotagging/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_collection(body: dict) -> str:
    """Update Collection.

    PUT /api/v3/collection

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/collection", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_collection_by_id(id_: str, body: dict) -> str:
    """Update Collection.

    PUT /api/v3/collection/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/collection/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_downloadclient_by_id(id_: str, body: dict) -> str:
    """Update DownloadClientConfig.

    PUT /api/v3/config/downloadclient/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/downloadclient/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_host_by_id(id_: str, body: dict) -> str:
    """Update HostConfig.

    PUT /api/v3/config/host/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/host/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_importlist_by_id(id_: str, body: dict) -> str:
    """Update ImportListConfig.

    PUT /api/v3/config/importlist/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/importlist/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_indexer_by_id(id_: str, body: dict) -> str:
    """Update IndexerConfig.

    PUT /api/v3/config/indexer/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/indexer/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_mediamanagement_by_id(id_: str, body: dict) -> str:
    """Update MediaManagementConfig.

    PUT /api/v3/config/mediamanagement/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/mediamanagement/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_metadata_by_id(id_: str, body: dict) -> str:
    """Update MetadataConfig.

    PUT /api/v3/config/metadata/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/metadata/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_naming_by_id(id_: str, body: dict) -> str:
    """Update NamingConfig.

    PUT /api/v3/config/naming/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/naming/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_config_ui_by_id(id_: str, body: dict) -> str:
    """Update UiConfig.

    PUT /api/v3/config/ui/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/config/ui/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_customfilter_by_id(id_: str, body: dict) -> str:
    """Update CustomFilter.

    PUT /api/v3/customfilter/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/customfilter/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_customformat_bulk(body: dict) -> str:
    """Update CustomFormat.

    PUT /api/v3/customformat/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/customformat/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_customformat_by_id(id_: str, body: dict) -> str:
    """Update CustomFormat.

    PUT /api/v3/customformat/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/customformat/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_delayprofile_by_id(id_: str, body: dict) -> str:
    """Update DelayProfile.

    PUT /api/v3/delayprofile/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/delayprofile/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_delayprofile_reorder_by_id(id_: int, after: int | None = None) -> str:
    """Update DelayProfile.

    PUT /api/v3/delayprofile/reorder/{id}

    Args:
        id_: Path parameter.
        after: Query parameter.
    """
    return call("PUT", f"/api/v3/delayprofile/reorder/{id_}", query={"after": after}, body=None)


@mcp.tool(annotations=_WRITE)
def update_downloadclient_bulk(body: dict) -> str:
    """Update DownloadClient.

    PUT /api/v3/downloadclient/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/downloadclient/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_downloadclient_by_id(id_: int, body: dict, force_save: bool | None = None) -> str:
    """Update DownloadClient.

    PUT /api/v3/downloadclient/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v3/downloadclient/{id_}", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def update_exclusions_by_id(id_: str, body: dict) -> str:
    """Update ImportListExclusion.

    PUT /api/v3/exclusions/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/exclusions/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_importlist_bulk(body: dict) -> str:
    """Update ImportList.

    PUT /api/v3/importlist/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/importlist/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_importlist_by_id(id_: int, body: dict, force_save: bool | None = None) -> str:
    """Update ImportList.

    PUT /api/v3/importlist/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v3/importlist/{id_}", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def update_indexer_bulk(body: dict) -> str:
    """Update Indexer.

    PUT /api/v3/indexer/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/indexer/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_indexer_by_id(id_: int, body: dict, force_save: bool | None = None) -> str:
    """Update Indexer.

    PUT /api/v3/indexer/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v3/indexer/{id_}", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def update_metadata_by_id(id_: int, body: dict, force_save: bool | None = None) -> str:
    """Update Metadata.

    PUT /api/v3/metadata/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v3/metadata/{id_}", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def update_movie_by_id(id_: str, body: dict, move_files: bool | None = None) -> str:
    """Update Movie.

    PUT /api/v3/movie/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        move_files: Query parameter.
    """
    return call("PUT", f"/api/v3/movie/{id_}", query={"moveFiles": move_files}, body=body)


@mcp.tool(annotations=_WRITE)
def update_movie_editor(body: dict) -> str:
    """Update MovieEditor.

    PUT /api/v3/movie/editor

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/movie/editor", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_moviefile_bulk(body: dict) -> str:
    """Update MovieFile.

    PUT /api/v3/moviefile/bulk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/moviefile/bulk", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_moviefile_by_id(id_: str, body: dict) -> str:
    """Update MovieFile.

    PUT /api/v3/moviefile/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/moviefile/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_moviefile_editor(body: dict) -> str:
    """Update MovieFile.

    PUT /api/v3/moviefile/editor

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/moviefile/editor", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_notification_by_id(id_: int, body: dict, force_save: bool | None = None) -> str:
    """Update Notification.

    PUT /api/v3/notification/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        force_save: Query parameter.
    """
    return call("PUT", f"/api/v3/notification/{id_}", query={"forceSave": force_save}, body=body)


@mcp.tool(annotations=_WRITE)
def update_qualitydefinition_by_id(id_: str, body: dict) -> str:
    """Update QualityDefinition.

    PUT /api/v3/qualitydefinition/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/qualitydefinition/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_qualitydefinition_update(body: dict) -> str:
    """Update QualityDefinition.

    PUT /api/v3/qualitydefinition/update

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v3/qualitydefinition/update", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_qualityprofile_by_id(id_: str, body: dict) -> str:
    """Update QualityProfile.

    PUT /api/v3/qualityprofile/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/qualityprofile/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_releaseprofile_by_id(id_: str, body: dict) -> str:
    """Update ReleaseProfile.

    PUT /api/v3/releaseprofile/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/releaseprofile/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_remotepathmapping_by_id(id_: str, body: dict) -> str:
    """Update RemotePathMapping.

    PUT /api/v3/remotepathmapping/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/remotepathmapping/{id_}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_tag_by_id(id_: str, body: dict) -> str:
    """Update Tag.

    PUT /api/v3/tag/{id}

    Args:
        id_: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v3/tag/{id_}", query=None, body=body)
