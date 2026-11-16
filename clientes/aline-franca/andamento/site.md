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
