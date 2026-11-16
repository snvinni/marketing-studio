# Regras para agentes neste repositório

## Idioma e tom
- Tudo em português do Brasil: documentos, textos para clientes, mensagens de commit.
- Escreva como uma pessoa escreve para outra. Frases curtas, palavras comuns, sem jargão de marketing.

## Onde gravar
- Material de um cliente: só dentro de `clientes/<cliente>/`.
- Melhoria do método que vale para todos: `metodo/` ou `modelos/`.
- Mudança na skill: `.claude/skills/copy-chief/`. Toda mudança na skill precisa continuar passando nos casos de `evals/`.
- Fotos e vídeos originais não entram no Git. Ficam no Drive do cliente; anote o link em `clientes/<cliente>/briefing-fotos.md`.
- Código de site fica no repositório do site do cliente, nunca aqui.

## Fatos e confirmação
- Nunca invente fato sobre o cliente: formação, título, preço, horário, bairro atendido, número de clientes, depoimento.
- O que ainda não foi confirmado pelo cliente fica marcado `[CONFIRMAR]`. Nada com `[CONFIRMAR]` vai para o ar.
- A fonte de verdade é `clientes/<cliente>/perfil.md`, preenchido a partir da entrevista. Se perfil e outro documento divergirem, vale o perfil; aponte a divergência.

## Regras de setor
- Clientes veterinários: siga `metodo/regras-cfmv.md`. Na dúvida sobre um ponto ainda não confirmado com o CRMV, trate como proibido.
- Nunca publicar: promessa de resultado, imagem de animal em sofrimento, título de especialista que o cliente não tem registrado, foto de paciente sem autorização registrada em `autorizacoes.md`.

## Andamento
- Vários agentes trabalham em paralelo. Leia `clientes/<cliente>/frentes.md`, mexa só nos arquivos da sua frente e registre o que fez em `clientes/<cliente>/andamento/<frente>.md`. Não edite a tabela de andamento do `plano.md`.
- Faça `git pull --rebase` antes de cada push.
- Ações que dependem de uma pessoa (criar conta, pagar, gravar vídeo) ficam com o responsável indicado no PT; o agente prepara o material e deixa o passo a passo.
