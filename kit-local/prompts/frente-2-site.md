# Frente 2: Site

Abra o Claude Code na pasta `frentes/2-site` (ela tem `line-vet/` e `marketing-studio/`) e cole o texto abaixo como primeira mensagem.

```
Você é o agente da frente 2 (Site) do projeto de marketing da Dra. Aline França. Você está na pasta desta frente, que tem duas cópias de trabalho: line-vet/ (código do site) e marketing-studio/ (plano e conteúdo).

Antes de qualquer coisa, entenda o contexto. Em marketing-studio/ leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 2"), clientes/aline-franca/plano.md (seções 1, 2, 3 e 5 inteiras), clientes/aline-franca/perfil.md, clientes/aline-franca/site/briefing.md e a pasta clientes/aline-franca/andamento/. Em line-vet/ (você está numa branch própria desta frente, criada a partir de ccr-ddd55fa2-btz5yk), leia o README.md e o index.html inteiro, e veja o git log.

Descubra em que fase você está:
- Se assets/site.css ainda não existe: faça a fase 1 (PT-S1 e PT-S6). Não mude o visual: compare capturas de tela em 390 px e 1440 px antes e depois, e escreva testes com Playwright para a calculadora (1 animal 1 visita = R$ 50; 2 animais = R$ 75/dia; 1 animal 2 visitas = R$ 80; 2 gaiolas 2 visitas = R$ 200; 5 dias multiplica o total; data final antes da inicial bloqueia o envio). Mantenha o funcionamento sem JavaScript.
- Se a fase 1 está feita e o perfil.md já diz "Fonte: entrevista de ...": faça a fase 2 (PT-S2 a S5, S7, S8), com textos escritos pela skill copy-chief (leia marketing-studio/.claude/skills/copy-chief/SKILL.md e siga-o; canal site) a partir do perfil. Se a entrevista ainda não foi feita, pare ao fim da fase 1 e me avise.
- Fase 3 (PT-S9 a S11) só com as fotos recebidas (briefing-fotos.md).

Regras: visual editorial e acolhedor já existente (creme, Fraunces, primeira pessoa), sem cara de SaaS; nada com [CONFIRMAR] vai ao ar; siga metodo/regras-cfmv.md. Me mostre capturas de cada página pronta. Commit e push ao fim de cada PT, e registre o andamento em clientes/aline-franca/andamento/site.md no marketing-studio (git pull --rebase antes do push). Não edite perfil.md, a skill nem arquivos de outras frentes.

Como trabalhamos localmente: cada frente tem a sua pasta e a sua branch (frente/...). Para publicar o que fez no marketing-studio, rode em marketing-studio/: git pull --rebase origin main && git push origin HEAD:main. No line-vet (só a frente 2), publique com: git pull --rebase origin ccr-ddd55fa2-btz5yk && git push origin HEAD:ccr-ddd55fa2-btz5yk. Nunca use push --force. Se o push for recusado por conflito, resolva só os arquivos da sua frente; se o conflito for em arquivo de outra frente, pare e me avise.
```
