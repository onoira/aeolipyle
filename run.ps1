$SCRIPT = "scripts\download_workshop_items.steamcmd"
$steamcmd = Get-Content settings\steamcmd.location
& "$steamcmd\steamcmd.exe" +runscript $(Get-ChildItem "$SCRIPT").FullName