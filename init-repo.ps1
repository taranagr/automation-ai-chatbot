$root="C:\automation-ai-chatbot"

$folders=@(
"frontend",
"frontend\app",
"frontend\components\ui",
"frontend\lib",
"backend",
"backend\app\routes",
"backend\app\services",
"mcp-server\app",
"infra"
)

foreach ($f in $folders){
 New-Item -ItemType Directory -Force -Path "$root\$f" | Out-Null
}

Write-Host "Folders created $root"