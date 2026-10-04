$extensionSource = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$extensionsFolder = Join-Path $env:USERPROFILE ".vscode\extensions"
$extensionLink = Join-Path $extensionsFolder "local.python-learning-hints-ru-0.1.0"

New-Item -ItemType Directory -Path $extensionsFolder -Force | Out-Null

if (Test-Path -LiteralPath $extensionLink) {
    Write-Host "Расширение уже подключено:" $extensionLink
    exit 0
}

New-Item -ItemType Junction -Path $extensionLink -Target $extensionSource | Out-Null
Write-Host "Расширение подключено:" $extensionLink
Write-Host "В VS Code выполните команду: Developer: Reload Window"
