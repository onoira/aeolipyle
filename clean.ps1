$VERBOSE=$false
Remove-Item -Verbose:$VERBOSE scripts/download_workshop_items.steamcmd -ErrorAction SilentlyContinue
if (!(Test-Path -Path fids)) {
    New-Item -Verbose:$VERBOSE -Path fids -ItemType File
} else {
    Clear-Content -Verbose:$VERBOSE -Path fids
}
if (!(Test-Path -Path urls)) {
    New-Item -Verbose:$VERBOSE -Path urls -ItemType File
} else {
    Clear-Content -Verbose:$VERBOSE -Path urls
}