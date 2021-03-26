$appid = Get-Content -First 1 settings\app.id
$steamcmd = Get-Content settings\steamcmd.location
$steamapps = Get-Content settings\steamapps.location
& "$steamcmd\steamcmd.exe" +runscript $(Get-ChildItem "scripts\download_workshop_items.txt").FullName