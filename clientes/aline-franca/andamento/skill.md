# Andamento: frente 3 (Skill copy-chief)

## 16/11/2026, item 1: canais novos
- Feito:
  - `.claude/skills/copy-chief/referencias/canais/google-perfil.md`: descrição (até 750), serviços (até 300 por descrição), publicações (até 1.500), resposta a avaliação boa e ruim, regras do Google sobre pedido de avaliação.
  - `canais/whatsapp.md`: saudação, ausência, respostas rápidas (até 50, atalho `/`), pedido de avaliação, lembrete de retorno, pedido de autorização de imagem.
  - `canais/site.md`: título (~60), descrição (~120 a 155), abertura, página de serviço, "Sobre", perguntas frequentes.
  - `canais/anuncios-google.md`: títulos até 30, descrições até 90, caminho até 15, sitelinks e frases de destaque; sem promessa nem preço.
  - Cada canal cita as fontes dos limites (Central de Ajuda do Google, FAQ do WhatsApp, Google Ads, Search Central). Onde o número vem só de terceiros, está dito.
  - `setores/veterinaria-br.md`: nova seção "Por canal" com o que é próprio de veterinário em cada canal (CRMV, nada de diagnóstico pelo WhatsApp, lembrete de vacina sem garantia, autorização ao tutor, sem preço no anúncio).
  - Núcleo agnóstico: tirei os exemplos de veterinária de `principios.md`, `revisao.md` e `canais/instagram.md`.
  - `SKILL.md`: tabela de qual pedido vai para qual canal e a regra de contar caracteres de verdade.
- Pendências: nenhuma de pessoa.
- Pedidos para outras frentes: as frentes 2 (site), 4 (Google) e 6 (WhatsApp, anúncios) já podem pedir esses textos à skill.

## 16/11/2026, item 2: casos de teste dos canais novos
- Feito: quatro casos em `.claude/skills/copy-chief/evals/`, no formato dos existentes:
  - `google-descricao-avaliacao`: descrição do Google (pede bairros não confirmados) e resposta a avaliação de 1 estrela.
  - `whatsapp-lembrete-autorizacao`: lembrete de reforço de vacina e pedido de autorização de foto.
  - `site-pagina-vacinas`: página "Vacinação em casa" com título, descrição e perguntas frequentes.
  - `anuncio-google-consulta`: anúncio de pesquisa (pede desconto de 10%, que deve ficar de fora).
- Pendências: nenhuma.
- Pedidos para outras frentes: nenhum.

## 17/11/2026, item 3: segunda rodada de testes
- Feito: os 10 casos rodaram com e sem a skill, pela skill-creator. Com a skill, 48 de 49 critérios; sem a skill, 40 de 49. Nos quatro canais novos, 21 de 21 com a skill e 18 de 21 sem ela. Relatório em `relatorios/copy-chief-iteracao-2.md` e `.html`.
- Correções na skill (`SKILL.md`, `referencias/revisao.md`): cada versão corrigida sai com chamada e identificação; `[CONFIRMAR]` vai dentro do texto pronto, não só nas pendências. Reteste dos dois casos afetados com a skill corrigida: 5 de 5 e 6 de 6.
- Critérios ajustados para a próxima rodada: `revisar-titulo-felinos/05`, `reels-bastidor-gato/05`, `anuncio-google-consulta/03`.
- Pendências: bio-instagram, revisar-promessa e site-pagina-vacinas passam com e sem a skill; vale incluir neles uma armadilha na próxima rodada. Nada depende de pessoa.
- Pedidos para outras frentes: a skill está pronta para os canais Google, WhatsApp, site e anúncio. As frentes 2, 4, 5 e 6 podem anotar no próprio andamento o que a skill errar, como pedido para esta frente.
