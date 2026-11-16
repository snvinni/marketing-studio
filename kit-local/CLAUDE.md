# Coordenação do projeto Aline (pasta raiz)

Esta pasta junta os repositórios e as frentes de trabalho do marketing da Dra. Aline França. Um agente aberto aqui é o **coordenador**: ele não executa frentes, acompanha.

- Repositórios: `repos/marketing-studio` (branch `main`) e `repos/line-vet` (branch `ccr-ddd55fa2-btz5yk`).
- Frentes: `frentes/<frente>/`, cada uma com a sua cópia de trabalho e a sua branch. Não edite arquivos dentro de `frentes/`: há um agente trabalhando em cada uma.
- Regras e dependências: `repos/marketing-studio/clientes/aline-franca/frentes.md`.

## O que o coordenador faz
1. `git -C repos/marketing-studio pull --ff-only origin main` e `git -C repos/line-vet pull --ff-only origin ccr-ddd55fa2-btz5yk`.
2. Lê `repos/marketing-studio/clientes/aline-franca/andamento/` e o `git log` dos dois repositórios.
3. Diz ao Vinícius, em português e de forma curta:
   - o que cada frente já entregou;
   - o que está travado e por quê (dependência, ação de uma pessoa, conflito);
   - os pedidos de uma frente para outra;
   - qual é o próximo passo de cada uma.
4. Se pedirem, consolida a tabela de andamento da seção 11 de `clientes/aline-franca/plano.md` a partir dos arquivos de andamento, trabalhando em `repos/marketing-studio` na `main`.
