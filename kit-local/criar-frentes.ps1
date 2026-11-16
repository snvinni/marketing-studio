# Versão para Windows (PowerShell). Faz o mesmo que criar-frentes.sh.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$Raiz = (Get-Location).Path
$MS = Join-Path $Raiz "repos\marketing-studio"
$LV = Join-Path $Raiz "repos\line-vet"

Write-Host "Atualizando os repositórios..."
git -C $MS pull --ff-only origin main
git -C $LV pull --ff-only origin ccr-ddd55fa2-btz5yk

function Criar($repo, $destino, $branch, $base) {
  if (Test-Path $destino) { Write-Host "  já existe: $destino"; return }
  git -C $repo show-ref --verify --quiet "refs/heads/$branch"
  if ($LASTEXITCODE -eq 0) { git -C $repo worktree add -q $destino $branch }
  else { git -C $repo worktree add -q -b $branch $destino $base }
  Write-Host "  criado: $destino (branch $branch)"
}

New-Item -ItemType Directory -Force -Path "frentes" | Out-Null
foreach ($f in "1-entrevista","2-site","3-skill","4-google","5-instagram","6-operacao") {
  Write-Host "Frente $f"
  New-Item -ItemType Directory -Force -Path "frentes\$f" | Out-Null
  Criar $MS (Join-Path $Raiz "frentes\$f\marketing-studio") "frente/$f" "main"
  if ($f -eq "2-site") { Criar $LV (Join-Path $Raiz "frentes\$f\line-vet") "frente/$f" "ccr-ddd55fa2-btz5yk" }
  Copy-Item "prompts\frente-$f.md" "frentes\$f\PROMPT.md" -Force
}
Write-Host ""
Write-Host "Pronto. Para começar uma frente: cd frentes\1-entrevista\marketing-studio ; claude   (frente 2: cd frentes\2-site ; claude)"
