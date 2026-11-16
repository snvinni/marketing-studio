# Kit para trabalhar localmente

Monta, no seu computador, uma pasta com os dois repositórios e uma pasta de trabalho por frente (um agente do Claude Code em cada).

## Montar do zero
```
mkdir projeto-aline && cd projeto-aline
git clone https://github.com/snvinni/marketing-studio.git repos/marketing-studio
git clone -b ccr-ddd55fa2-btz5yk https://github.com/snvinni/line-vet.git repos/line-vet
cp -r repos/marketing-studio/kit-local/* .
./criar-frentes.sh        # Windows: .\criar-frentes.ps1
```

Depois, em cada frente, abra o Claude Code na pasta indicada em `frentes/<frente>/PROMPT.md` e cole o prompt.

O `CLAUDE.md` daqui vai para a raiz da pasta `projeto-aline` e orienta um agente coordenador. As regras entre frentes estão em `clientes/aline-franca/frentes.md`.
