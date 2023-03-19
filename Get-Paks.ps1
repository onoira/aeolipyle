$OUT = 'out'
if (!(Test-Path -Path "$OUT")) {
     New-Item -ItemType Directory -Path "$OUT"
}

$INVALID_CHARS = [IO.Path]::GetInvalidFileNameChars() -Join ''
$RegExpInvalidChars = "[{0}]" -f [RegEx]::Escape($INVALID_CHARS)

$steamcmd = Get-Content settings\steamcmd.location
$appid = Get-Content -First 1 settings\app.id
Get-ChildItem -Directory "$steamcmd\steamapps\workshop\content\$appid" | ForEach-Object {

    $fid = $_.Name
    $title = $(curl -L "https://steamcommunity.com/sharedfiles/filedetails/?id=$fid" | Select-String -Pattern "<title>(.*)</title>").Matches.Groups[1].Value

    $title = $title -Replace ".+::",""              # Strip scope
    $title = $title -Replace "</?title>",""         # Strip tags
    $title = $title -Replace $RegExpInvalidChars    # Remove invalid characters
    $title = $title -Replace "^\s+|\s+$",""         # Trim whitespace
    $title = $title -Replace "\s","_"               # Underscore inner ws
    $title = $title -Replace [RegEx]::Escape($RegExpInvalidChars)

    $pakPath = [IO.Path]::Combine($_.FullName, 'contents.pak')
    $outPath = [IO.Path]::Combine("$OUT", "$title.pak")

    Copy-Item -Verbose "$pakPath" "$outPath"
    Start-Sleep -Seconds 2  # Don't assault Steam
}
