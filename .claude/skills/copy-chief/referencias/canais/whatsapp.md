# Canal: WhatsApp (WhatsApp Business)

É onde o pedido vira atendimento. O texto aqui é conversa: curto, direto, na primeira pessoa, como o cliente escreveria do próprio celular. O que medir: tempo até a primeira resposta, conversas que viram atendimento, avaliações recebidas depois do pedido.

Limites e recursos conferidos em novembro de 2026 no app WhatsApp Business (fontes no fim). O app muda com frequência: confira no próprio aparelho.

## Regras do canal
- Mensagem para uma pessoa por vez. Mensagem em massa só para quem salvou o número do cliente e pediu para receber (lista de transmissão). Nunca escreva texto pensado para disparo a desconhecidos.
- Mensagem automática não pode parecer robô fingindo ser gente. Se é automática, pode dizer que é ("Recebi sua mensagem e respondo assim que sair do atendimento").
- Nada de dado de outra pessoa na mensagem (nome de outro cliente, endereço, caso).
- O texto respeita as mesmas regras do setor que o post: nada de promessa, preço fora do permitido ou título não confirmado só porque a conversa é privada.
- Formatação do WhatsApp: `*negrito*` e `_itálico_` funcionam; use só para destacar uma informação (dia, horário). Sem lista enorme.
- No máximo um emoji por mensagem; nenhum em mensagem sobre problema ou reclamação.

## Saudação (mensagem automática para quem escreve pela primeira vez)
- O app manda a saudação no primeiro contato ou depois de um tempo sem conversa (guias citam 14 dias).
- 2 a 4 linhas, até ~300 caracteres para caber na tela sem rolar.
- Estrutura: cumprimento com o nome do cliente · o que ele faz em uma linha · o que a pessoa deve mandar para adiantar · quando ele responde (só se o perfil confirmar o horário; senão `[CONFIRMAR: horário de resposta]`).
- Ex. de estrutura (outro ramo): "Oi! Aqui é a Ana, eletricista em Sorocaba. Me conta o que precisa e, se puder, manda uma foto do problema. Respondo entre 8h e 18h."

## Ausência (fora do horário)
- 1 a 3 linhas. Diz que recebeu, quando volta a responder e, se o perfil disser que o cliente não atende urgência, para onde a pessoa deve ir nesse caso (sem citar concorrente pelo nome se o perfil não indicar parceiro).
- O app permite: sempre, horário personalizado ou fora do horário comercial (precisa do horário cadastrado no perfil).

## Respostas rápidas
- Até 50 respostas salvas; chamadas digitando `/` e o atalho na conversa.
- Atalho curto, em minúscula, sem acento: `/preco`, `/regiao`, `/como-funciona`, `/avaliacao`.
- Cada resposta responde uma pergunta só, em até ~400 caracteres, e termina com a próxima ação ("Me manda o seu bairro que eu vejo o dia").
- Sempre que o fato não estiver no perfil, a resposta vem com `[CONFIRMAR: ...]` e não pode ser salva no app antes de confirmar.
- Entregue em tabela: atalho · quando usar · texto.
- Conjunto mínimo sugerido: como funciona, região atendida, valores (ou como é feito o orçamento), horários, o que preparar antes da visita, pagamento, pedido de avaliação.

## Pedido de avaliação no Google
- Mandar depois de cada atendimento concluído, a todos os clientes, do mesmo jeito. Nunca só para quem gostou.
- 2 a 4 linhas: agradece pelo atendimento (sem citar detalhe sensível) · diz que a avaliação ajuda outras pessoas a encontrar o serviço · link curto do perfil · "leva 1 minuto".
- Proibido: desconto, brinde, sorteio, "avalia com 5 estrelas", pedir para apagar ou mudar avaliação ruim.
- Se o link ainda não existe, use `[CONFIRMAR: link de avaliação do perfil no Google]`.
- Entregue duas versões: logo depois do atendimento e lembrete único dias depois (sem insistir mais que isso).

## Lembrete de retorno (revisão, manutenção, reforço, renovação)
- Mensagem para um cliente que já foi atendido e tem algo a refazer numa data. Só para quem é cliente e conversa com o número.
- 3 a 5 linhas: nome da pessoa e do que é o lembrete (ex.: "a revisão do aquecedor") · quando vence (mês, não data inventada; a data vem do registro do cliente, no texto use o campo `[data]`) · por que vale não deixar passar, em uma frase, sem assustar · convite para marcar.
- Campos variáveis entre colchetes: `[nome]`, `[item]`, `[data]`. Diga na entrega que são campos a preencher, não `[CONFIRMAR]`.
- Sem promessa ("evita qualquer problema"), sem tom de cobrança, sem urgência falsa ("últimas vagas").
- Para lista de transmissão, uma mensagem que sirva para todos, sem nome.

## Pedido de autorização de uso de imagem ou depoimento
- Pedido para usar foto, vídeo ou fala de um cliente (ou de algo que pertence a ele) em post, site ou perfil.
- Deve dizer, em linguagem simples: o que será usado (qual foto ou trecho) · onde vai aparecer (Instagram, site, Google) · se aparece nome, rosto ou endereço (o padrão é não aparecer) · que a pessoa pode dizer não sem problema nenhum · que pode pedir para tirar depois.
- Termina com uma pergunta que a pessoa responde por escrito ("Posso usar? Se sim, me responde 'autorizo'."). A resposta por escrito é o registro.
- Lembre na entrega: registrar a autorização no arquivo de autorizações do cliente (`clientes/<cliente>/autorizacoes.md`) com data, o que foi autorizado e onde, antes de publicar.
- Nada de oferecer vantagem em troca da autorização.

## Formato de entrega por tipo
- Saudação e ausência: bloco de código, com contagem de caracteres.
- Respostas rápidas: tabela atalho · quando usar · texto.
- Pedidos e lembretes: as versões em bloco de código, com os campos variáveis indicados.

## Fontes
- Respostas rápidas (até 50, atalho com `/`, mídia não funciona no Web e no Desktop): [WhatsApp, Como usar respostas rápidas](https://faq.whatsapp.com/1791149784551042/?cms_platform=android).
- Mensagem de ausência (agendamento e destinatários): [WhatsApp, Como usar mensagens de ausência](https://faq.whatsapp.com/2565868990219715/?cms_platform=android).
- Transmissão para clientes: [WhatsApp, Como criar e enviar uma transmissão](https://faq.whatsapp.com/1711086883148106/?cms_platform=web).
- Saudação após 14 dias sem conversa e tamanho recomendado de ~300 caracteres: guias de terceiros ([Getkanal](https://getkanal.com/blog/whatsapp-automated-message-guide.md), [Lilach Bullock](https://www.lilachbullock.com/whatsapp-business-auto-reply-message/)); o limite máximo da saudação diverge entre fontes (1.024 a 4.096) e não foi confirmado no FAQ oficial.
- Pedido de avaliação sem vantagem e sem pedido seletivo: [Google, Dicas para receber mais avaliações](https://support.google.com/business/answer/3474122).
