$VERBOSE=$false
Remove-Item -Verbose:$VERBOSE scripts/download_workshop_items.steamcmd -ErrorAction SilentlyContinue
if (Test-Path -Path fids) {
    Clear-Content -Verbose:$VERBOSE -Path fids
}
if (Test-Path -Path urls) {
    Clear-Content -Verbose:$VERBOSE -Path urls
}