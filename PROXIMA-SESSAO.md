# Prompt para continuar em uma nova sessão

Cole o texto abaixo como primeira mensagem de uma sessão nova do Claude Code (Opus 5.5), com os repositórios `snvinni/marketing-studio` e `snvinni/line-vet` selecionados.

````
Vamos continuar o projeto de marketing digital da Dra. Aline França, médica-veterinária que atende a domicílio em Campinas (cães e gatos, com carinho especial por gatos) e faz pet sitter. Eu sou o Vinícius e cuido do marketing dela.

## Onde está tudo
- `snvinni/line-vet` (branch `ccr-ddd55fa2-btz5yk`): código do site. Hoje é uma página só de pet sitter, com calculadora de orçamento que envia o pedido pelo WhatsApp. Sem deploy e sem domínio (domínio escolhido: draalinefranca.com.br).
- `snvinni/marketing-studio` (branch `main`): repositório do estúdio, com método, modelos, a pasta da Aline e a skill de redação `copy-chief`.

## Passo 1: situar-se
Se algum dos dois repositórios não estiver nesta sessão, conecte com o add_repo. Leia, nesta ordem: `README.md`, `CLAUDE.md`, `clientes/aline-franca/plano.md` (plano aprovado, com a tabela de andamento na seção 11) e `clientes/aline-franca/perfil.md`.

## Passo 2: fazer a entrevista com a Aline (PT-A1)
A entrevista ainda não começou. Eu vou passar as respostas da Aline aqui na conversa.
- Use as 42 perguntas de `clientes/aline-franca/entrevista.md`, na ordem dos blocos 1, 2, 4, 5, 3 e 6.
- Faça as perguntas pela ferramenta de perguntas com opções (AskUserQuestion), em grupos de até 4 do mesmo bloco, sempre com opções úteis. Eu escrevo detalhes no campo "Outro". Pergunta aberta demais (história, frase, exemplo) pode ir em texto normal.
- Quando a resposta for genérica, peça um exemplo concreto. Guarde as frases boas da Aline palavra por palavra: elas viram texto do site.
- No fim de cada bloco: resuma em 3 a 5 linhas, peça minha confirmação e grave as respostas em `clientes/aline-franca/entrevista.md` (respostas abaixo de cada pergunta; o que faltar fica [PENDENTE]). Faça commit por bloco.
- No bloco 6, pergunta 39, registre o que já foi confirmado com o CRMV-SP sobre preços, desconto, fotos de pacientes, depoimentos e títulos. O que não foi confirmado continua proibido (ver `metodo/regras-cfmv.md`).
- Ao terminar: reescreva `clientes/aline-franca/perfil.md` a partir da entrevista (seguindo `modelos/perfil-cliente.md`), marque o PT-A1 como feito na tabela de andamento do `plano.md`, faça commit e push.

## Passo 3: próximos pacotes
Depois da entrevista, me proponha a ordem dos próximos pacotes do `plano.md` e comece pelo que eu escolher. Os prováveis:
- PT-A2: mandar o pedido de fotos (`clientes/aline-franca/briefing-fotos.md`, mensagem já pronta).
- PT-S1 e PT-S6 no `line-vet`: separar CSS e JS do `index.html` e mover o pet sitter para `pet-sitter.html` sem mudar o visual; os 6 testes da calculadora precisam continuar passando (1 animal 1 visita = R$ 50; 2 animais = R$ 75/dia; 1 animal 2 visitas = R$ 80; 2 gaiolas 2 visitas = R$ 200; 5 dias multiplica; data final antes da inicial bloqueia o envio).
- PT-S2 a S5: páginas de veterinária a domicílio, vacinas e gatos, com textos escritos ou revisados pela skill `copy-chief`.
- PT-K3: primeiro calendário de Instagram com a skill.

## Regras
- Tudo em português do Brasil.
- Nunca invente fato sobre a Aline: o que não está confirmado fica [CONFIRMAR].
- Texto de divulgação passa pela skill `copy-chief` (`.claude/skills/copy-chief/` no marketing-studio).
- O visual do site é editorial e acolhedor (creme, serifa Fraunces, primeira pessoa), sem cara de SaaS.
- Commit e push ao fim de cada etapa, na branch da sessão no `line-vet` e na `main` do `marketing-studio`.
````
