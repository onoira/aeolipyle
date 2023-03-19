# aeolipyle

Automate text-based mod lists for Steam.

## Requirements

- Python 3.8 or higher
- Steam
- `steamcmd` — see the [developer's wiki](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD) for more information.

## Getting started

You must first build the installer. The following options are available:

### Building a list of URLs

1. Create a collection on the Steam Workshop.
2. On the collection page, open the Developer Tools (F12).
3. In the Developer Console, paste the contents of `utils/modlist.js`.
   - This will download a `urls` file to your configured downloads location.
   - Move or copy the `urls` file to the aeolipyle directory.

### From a list of URLs

1. Create a `urls` file containing a list of workshop links.
   Lines **not** starting in `http` are ignored.
2. Run `utils/parse.py`.
   This will create a `fids` file.

### From a list of IDs

1. Create a `fids` file containing a list of `PublishedFileId`s.
2. Run `utils/make.py`.
   This will create a `scripts/download_workshop_items.steamcmd` file.

### Running the installer

In PowerShell: run `./run.ps1`.

### Exporting mod paks

> ⚠ This has only been tested and designed with Starbound in mind.
>
> Known issues: _a few_ mods aren't named `contents.pak` — but I handled these by hand.

For distributing mod lists using `.pak` files: run `Get-Paks.ps1`.

All `.pak` files will be placed in an `out/` folder.

## Settings

`settings/app.id`
: The game ('app') ID. All lines after the first are ignored.

`settings/steamapps.location`
: The `steamapps/` library path.

`settings/steamcmd.location`
: The steamcmd install path.

`settings/user.name`
: The Steam account username to use. **Recommended to use your own**.

## Contributing

This repository is not open for contributions.

Please [create a new issue](https://github.com/onoira/aeolipyle/issues/new).

## License

[GNU AGPLv3](LICENSE)
