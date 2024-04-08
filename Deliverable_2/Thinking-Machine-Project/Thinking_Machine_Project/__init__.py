from dagster import Definitions, load_assets_from_modules, IOManager, FilesystemIOManager

from .assets import daily_checkins

daily_checkins_assets = load_assets_from_modules([daily_checkins])

defs = Definitions(
    assets=[*daily_checkins_assets],
    resources={
        "io_manager": FilesystemIOManager(base_dir="data/outputs"),
    }
)
