# aeolipyle

Automate text-based mod lists for Steam.

## Requirements

- Python 3.6 or higher
- Steam
- steamcmd
  - See the [developer's wiki](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD) for more information.

## Getting started

You must first build the installer. The following options are available:

### From a list of URLs

1. Create a `urls.txt` file containing a list of workshop links.
   These links must start with 'http'.
2. Run `utils/parse.py`.
   This will create a `fids` file.

### From a list of IDs

1. Create a `fids` file containing a list of `PublishedFileId`s.
2. Run `utils/make.py`.
   This will create a `scripts/download_workshop_items.txt` file.

### Running the installer

In PowerShell, simply run `./run.ps1`.

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
