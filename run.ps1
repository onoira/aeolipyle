$SCRIPT = "scripts\download_workshop_items.steamcmd"
$appid = Get-Content -First 1 settings\app.id
$steamcmd = Get-Content settings\steamcmd.location
& "$steamcmd\steamcmd.exe" +runscript $(Get-ChildItem "$SCRIPT").FullName