# Frente 5: Instagram

Abra o Claude Code na pasta `frentes/5-instagram/marketing-studio` e cole o texto abaixo como primeira mensagem.

```
Você é o agente da frente 5 (Instagram) do projeto de marketing da Dra. Aline França. Você está dentro do repositório marketing-studio, numa cópia de trabalho só desta frente.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 5"), clientes/aline-franca/plano.md (seções 1, 3 e 7), metodo/pesquisa.md, metodo/regras-cfmv.md, clientes/aline-franca/perfil.md, clientes/aline-franca/entrevista.md, modelos/calendario-instagram.md, a skill em .claude/skills/copy-chief/ e a pasta clientes/aline-franca/andamento/. Veja o git log.

Confira primeiro se perfil.md diz "Fonte: entrevista de ...". Se a entrevista ainda não foi feita, pare e me avise: esta frente depende dela.

Com a entrevista feita, entregue em clientes/aline-franca/instagram/:
1. diagnostico.md: estado atual do perfil dela. Você não tem acesso ao Instagram; me peça capturas de tela do perfil e dos números dos últimos posts e trabalhe a partir delas.
2. perfil.md: nome do perfil, três opções de bio, destaques e o que cada um contém.
3. linha-editorial.md: os quatro pilares (em casa, gatos, orientação, prova), com 5 ideias de post por pilar tiradas das dúvidas e medos reais da entrevista.
4. calendario.md: 8 posts para o primeiro mês, dois por semana, alternando Reels e carrossel, cada um com roteiro ou telas, legenda, chamada e o material que a Aline precisa gravar.

Todo texto é escrito pela skill copy-chief no modo escrever e conferido no modo revisar. Nada de promessa de resultado, "especialista em felinos" ou foto de paciente sem autorização. Anote em andamento/instagram.md o que a skill errou ou deixou a desejar, como pedido para a frente 3. Commit e push ao fim de cada arquivo (git pull --rebase antes). Não edite perfil.md do cliente, a skill nem arquivos de outras frentes.

Como trabalhamos localmente: cada frente tem a sua pasta e a sua branch (frente/...); as outras frentes estão em pastas vizinhas, não mexa nelas. Para publicar o que fez, rode aqui: git pull --rebase origin main && git push origin HEAD:main. Nunca use push --force. Se o push for recusado por conflito, resolva só os arquivos da sua frente; se o conflito for em arquivo de outra frente, pare e me avise.
```
