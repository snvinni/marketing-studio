# Marketing Studio

Estúdio de marketing digital para profissionais locais, começando por médicos-veterinários que atendem a domicílio. Aqui ficam o método, as skills dos agentes, os modelos de documento e uma pasta por cliente.

O código dos sites **não** fica aqui: cada site tem o seu repositório (o da Dra. Aline França é `snvinni/line-vet`).

## Como está organizado

| Pasta | O que tem |
|---|---|
| `metodo/` | O plano-base em trilhas, a pesquisa que o sustenta e as regras do CFMV. Vale para qualquer cliente. |
| `modelos/` | Documentos em branco: entrevista, pedido de fotos, autorizações, perfil do cliente, calendário. |
| `clientes/<cliente>/` | Tudo de um cliente: perfil, entrevista respondida, plano com andamento, textos por canal. |
| `.claude/skills/copy-chief/` | Skill de chefe de redação: escreve e revisa textos para qualquer cliente e canal. |

## Clientes

| Cliente | Pasta | Site | Situação |
|---|---|---|---|
| Dra. Aline França (vet a domicílio e pet sitter, Campinas) | `clientes/aline-franca/` | `snvinni/line-vet` | Descoberta: entrevista e fotos pendentes |

## Como começar um cliente novo

1. Copie `modelos/` para `clientes/<nome-do-cliente>/` (nome em minúsculas, com hífen).
2. Aplique a entrevista (`entrevista.md`) e preencha `perfil.md` com as respostas. Sem perfil preenchido, a skill copy-chief não escreve.
3. Copie `metodo/plano-base.md` para `clientes/<nome>/plano.md` e ajuste as trilhas ao cliente.
4. Se o cliente for de outro ramo, crie `.claude/skills/copy-chief/referencias/setores/<ramo>.md` usando o de veterinária como modelo.

## Como pegar uma tarefa

Cada cliente tem um `plano.md` dividido em pacotes de trabalho (PT). Cada PT diz do que depende, o que entregar e quando está pronto. Um agente pode pegar um PT lendo só este README, o `CLAUDE.md` e o `plano.md` do cliente. Ao terminar, marque o PT como feito na tabela de andamento do `plano.md`.

## Usando a skill copy-chief

Em uma sessão do Claude Code aberta neste repositório, peça por exemplo:

- "Usa o copy-chief para escrever a bio do Instagram da aline-franca."
- "Revisa com o copy-chief esta legenda: ..."

A skill lê `clientes/<cliente>/perfil.md`, carrega as regras do setor e do canal, e entrega o texto com as pendências marcadas `[CONFIRMAR]`.
