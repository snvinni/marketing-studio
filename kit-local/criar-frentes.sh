#!/usr/bin/env bash
# Cria uma pasta de trabalho para cada frente em frentes/, usando git worktree.
# Cada frente ganha a sua branch (frente/<nome>), então dois agentes nunca
# mexem nos mesmos arquivos ao mesmo tempo. Pode rodar de novo sem problema:
# o que já existe é mantido.
set -euo pipefail
cd "$(dirname "$0")"
RAIZ="$(pwd)"
MS="$RAIZ/repos/marketing-studio"
LV="$RAIZ/repos/line-vet"

echo "Atualizando os repositórios..."
git -C "$MS" pull --ff-only origin main || echo "  (não deu para atualizar o marketing-studio agora; seguindo com a cópia local)"
git -C "$LV" pull --ff-only origin ccr-ddd55fa2-btz5yk || echo "  (não deu para atualizar o line-vet agora; seguindo com a cópia local)"

criar() { # repo destino branch base
  local repo="$1" destino="$2" branch="$3" base="$4"
  if [ -e "$destino" ]; then echo "  já existe: ${destino#$RAIZ/}"; return; fi
  if git -C "$repo" show-ref --verify --quiet "refs/heads/$branch"; then
    git -C "$repo" worktree add -q "$destino" "$branch"
  else
    git -C "$repo" worktree add -q -b "$branch" "$destino" "$base"
  fi
  echo "  criado: ${destino#$RAIZ/} (branch $branch)"
}

mkdir -p frentes
for f in 1-entrevista 2-site 3-skill 4-google 5-instagram 6-operacao; do
  echo "Frente $f"
  mkdir -p "frentes/$f"
  criar "$MS" "$RAIZ/frentes/$f/marketing-studio" "frente/$f" main
  if [ "$f" = "2-site" ]; then
    criar "$LV" "$RAIZ/frentes/$f/line-vet" "frente/$f" ccr-ddd55fa2-btz5yk
  fi
  cp "prompts/frente-$f.md" "frentes/$f/PROMPT.md"
done

echo
echo "Pronto. Para começar uma frente:"
echo "  cd frentes/1-entrevista/marketing-studio && claude   (frente 2: cd frentes/2-site && claude)"
echo "e cole o texto de PROMPT.md como primeira mensagem."
