# Andamento: frente 2 (Site)

Código em `snvinni/line-vet`, branch `ccr-ddd55fa2-btz5yk`.

## 16/11/2026: fase 1 (PT-S1 e PT-S6)

- Feito:
  - **PT-S1** (commit `662be7a`): CSS e JS saíram do `index.html` para `assets/site.css` e `assets/site.js`, sem build. Uma função só monta os links de WhatsApp; a calculadora roda só na página que tem o formulário. Cabeçalho e rodapé marcados como blocos padrão. O menu (Veterinária em casa · Vacinas · Gatos · Pet sitter · Sobre · Falar no WhatsApp; recolhido no celular, aberto sem JavaScript) está pronto em `tests/exemplos/menu.html` e entra nas páginas na fase 2, quando elas existirem. Pôr agora criaria links para páginas que ainda não existem.
  - **PT-S6** (commit `8714daf`): `pet-sitter.html` com o conteúdo de pet sitter e a calculadora intacta, título e endereço próprios, no `sitemap.xml`. O `index.html` continua com o mesmo conteúdo até a página inicial nova (PT-S2).
  - **Origem nas mensagens** (commit `e7d87c6`): a última linha de cada mensagem de WhatsApp do site diz de onde a pessoa veio, com as frases das etiquetas da frente 6: "Vim pelo seu site (página Pet sitter).", "Te achei no Google (...)" com `?origem=google`, "Vi seu anúncio no Google (...)" com `?origem=anuncio`. A marca vale para as outras páginas da mesma visita.
  - **Visual:** capturas em 390 e 1440 px, com e sem JavaScript, antes e depois, comparadas pixel a pixel. Iguais. A única diferença foi de suavização de letra em algumas capturas, sem nada mudar de lugar; ela também aparece entre duas capturas do mesmo arquivo.
  - **Testes** (Playwright, `npm test` no `line-vet`, 44 passam em 390 e 1440 px): os 6 casos da calculadora em `/` e `/pet-sitter` (1 animal 1 visita R$ 50; 2 animais R$ 75/dia; 1 animal 2 visitas R$ 80; 2 gaiolas 2 visitas R$ 200; 5 dias multiplicam o total; data final antes da inicial bloqueia o envio), a página sem JavaScript, os links de WhatsApp com origem e o menu. Conferi que os testes falham se o preço ou o bloqueio de datas quebrarem.
  - `tests/`, `package.json` e afins ficam fora do deploy (`.vercelignore`). O README do `line-vet` explica como montar uma página nova e rodar os testes.
- Pendências:
  - **Fase 2 parada:** a entrevista ainda não foi feita (`perfil.md`). PT-S2 a S5, S7 e S8 começam quando a linha "Fonte" do perfil citar a entrevista. Quem destrava: Vinícius e Aline (frente 1).
  - Enquanto não houver a página inicial nova, `/` e `/pet-sitter` têm o mesmo conteúdo (cada uma com o seu `canonical`). Resolve no PT-S2. O site ainda não está no ar, então isso não pesa agora.
  - O site mostra "50% de desconto" no animal adicional. `metodo/regras-cfmv.md` pede "valor reduzido para o segundo animal" até a checagem no CRMV, mas o `perfil.md` diz para manter como está até essa checagem. Mantive. Trocar na fase 2, se a Aline não confirmar com o CRMV antes. Quem resolve: Aline.
  - Nome e número do CRMV no rodapé: PT-S11, depende do número (`perfil.md`: `[CONFIRMAR número]`).
- Pedidos para outras frentes:
  - **Frente 6:** o pedido de origem nos botões do site está atendido (ver acima). A frase vem na **última** linha da mensagem, não na primeira, porque a primeira é o pedido do cliente ("Olá, Aline! Gostaria de um orçamento..."). As palavras são as mesmas das etiquetas. A frase genérica "Oi, Aline! Vim pelo seu site." da tabela da seção 6 não é usada no site.
  - **Frente 4:** o link do site no perfil do Google deve ser `https://draalinefranca.com.br/?origem=google`, quando o site estiver no ar.

## 17/11/2026: design e núcleo do site (antes da entrevista)

- Feito (todos no `line-vet`, branch `ccr-ddd55fa2-btz5yk`):
  - **Pesquisa de mercado e boas práticas** guardada em `clientes/aline-franca/site/pesquisa-design.md` (com as fontes). Conclusões que guiaram o resto: CRMV visível em todas as páginas, contraste, fontes leves e sem Google, WhatsApp como ação principal sem bolha flutuante, uma página de Atendimento em vez de páginas de bairro, avaliações só com link para o Google, medição sem cookie.
  - **Contraste (WCAG 2.2 AA)** (commit `78e4560`). Três cores reprovavam e foram trocadas por tons um pouco mais escuros:
    - texto secundário (era 4,4:1);
    - subtítulos em terracota;
    - botão de WhatsApp (era 3,1:1).

    As bordas de campo também ficaram mais visíveis. Um teste automático com axe-core roda em todas as páginas.
  - **Cor por serviço** (`78e4560`): na veterinária e nas páginas gerais, azul na frente e terracota de apoio; no pet sitter (`class="svc-pet"`), o contrário. O bloco "olhar de médica-veterinária" continua azul.
  - **Fontes no próprio site** (`78e4560`), em `assets/fontes/`. Caíram de 215 KB para 109 KB e o visitante não é mais enviado ao Google. O desenho dos títulos e a altura das páginas não mudaram.
  - **Celular** (`5b30612`):
    - **Barra de WhatsApp:** aparece quando o botão do topo sai da tela e some na calculadora e no bilhete final.
    - **Cabeçalho-modelo:** os dois serviços ficam sempre à vista, com o ponto da cor de cada um.
  - **Medição pronta** (`5b30612`): cada botão de WhatsApp diz a página e a posição. A contagem só liga quando houver Umami na página (ver pendências).
  - **Guia de estilo** (`fabce74`), em `guia-de-estilo.html`, fora do deploy. Tem as peças das oito páginas, nas versões de veterinária e de pet sitter, e um formulário curto que vira mensagem de WhatsApp (para o PT-S3). Os textos são de exemplo; o que depende da entrevista está marcado `[CONFIRMAR]`.
  - `?origem=instagram` aceito (`f572d1c`), a pedido da frente 6.
  - 69 testes passam em 390 e 1440 px.
- Pendências:
  - Fase 2 continua esperando a entrevista.
  - **Medição:** o Vinícius precisa criar a conta no Umami (grátis até 100 mil eventos por mês, sem cookie) e me passar o código do site. A Vercel só conta cliques no plano pago; a Cloudflare não conta cliques.
  - **Preço de consulta e vacina:** o manual do CFMV de 2026 permite mostrar valor "em termos discretos". O "sob consulta" do projeto é mais rígido do que a norma exige. Decisão da Aline, de preferência depois da checagem no CRMV-SP.
  - **Cor por serviço na página inicial atual:** `/` está provisoriamente em terracota, porque mostra o conteúdo de pet sitter. Volta ao azul com a página inicial nova (PT-S2).
- Pedidos para outras frentes:
  - **Frente 6:** os pedidos (a) frase de origem e (b) `?origem=google`, `?origem=anuncio` e `?origem=instagram` estão atendidos. A frase vai na última linha da mensagem. O pedido (c), material por condomínio a partir do arquivo do Petra Flamboyant, ainda não foi feito: é trabalho à parte, aguardando o Vinícius dizer quando.
  - **Frente 1:** a pesquisa traz uma lista de fotos em ordem de prioridade (`site/pesquisa-design.md`, seção 3). Vale conferir se o `briefing-fotos.md` cobre: retrato em casa, a Aline no chão com um gato, mãos vacinando, a mala e a caixa térmica.
