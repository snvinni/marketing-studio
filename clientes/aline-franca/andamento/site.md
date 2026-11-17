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

## 17/11/2026: material por condomínio (pedido c da frente 6)

- Feito (`line-vet`, commit `70d8eed`, pasta `materiais/`, fora do deploy):
  - **Modelo** `materiais/modelo-condominio.html`, com o texto do Petra e as mudanças de `operacao/parcerias.md`, seção 4:
    - **Desconto:** sem "50% de desconto"; agora "Cada animal a mais · da mesma casa, com valor reduzido", com os mesmos valores em reais (R$ 25 e R$ 40).
    - **Veterinária em casa:** seção nova, em azul, logo depois da abertura, com o texto da 4.2 e o botão "Falar com a Aline".
    - **Título:** "Veterinária em casa e pet sitter para os moradores do {condomínio}".
    - **CRMV:** passa a constar no rodapé.
    - **Deslocamento:** nada escrito, como pede a 4.1.
  - **Gerador** `materiais/gerar.mjs`. Rode `node materiais/gerar.mjs "Nome do Condomínio"` (com `--da` se o nome pedir "da" e "na"). Ele faz três coisas:
    - troca o nome do condomínio e monta os links de WhatsApp com "Oi, Aline! Moro no condomínio {nome}." (seção 6 de `whatsapp-business.md`);
    - embute o CSS do site, as fontes e a foto. O arquivo tem 226 KB e abre sem internet: conferi que não faz nenhum pedido fora do arquivo;
    - mantém a faixa amarela "Rascunho, não enviar" enquanto sobrar `[CONFIRMAR]`.

    Instruções em `materiais/README.md`.
  - **Petra Flamboyant:** não tem mais arquivo próprio, a pedido do Vinícius (commit `8a2a13a`). Ele é um condomínio como os outros: `node materiais/gerar.mjs "Petra Flamboyant"`. As versões geradas não ficam no Git (`materiais/.gitignore`). O arquivo antigo `Pet-Sitter-Dra-Aline-Franca-Petra-Flamboyant.html`, que tinha o "50% de desconto", saiu da pasta e continua no histórico do Git.
  - **Mensagem do orçamento:** começa com a frase do condomínio, e o bloco e o apartamento vêm numa linha à parte. A conta continua a mesma: 2 animais, 1 visita, 2 dias dão R$ 150.
  - **Conferido:** capturas em 390 e 1440 px, com e sem JavaScript, na aparência do site, e sem rolagem lateral no celular.
- Pendências (todas da Aline):
  - O material **não pode ser enviado** enquanto tiver `[CONFIRMAR]`. Faltam dois pontos:
    - o número do CRMV-SP (pergunta 1);
    - o que mostrar dos valores de consulta e vacina (perguntas 19 e 39).
  - Gerado para o Petra, o material também sai como rascunho, porque a seção de veterinária e o CRMV são novos. Se precisar reenviar ao Petra antes da entrevista, a versão antiga está no histórico do Git, mas tem o "50% de desconto".
- Pedidos para outras frentes:
  - **Frente 6:** o pedido (c) está atendido. O arquivo do Petra citado em `operacao/parcerias.md`, seção 4, não existe mais. O modelo agora é `line-vet/materiais/modelo-condominio.html`, e a versão de cada condomínio, inclusive a do Petra, sai do gerador. Atualize a referência.
  - **Frente 6:** em `whatsapp-business.md`, a seção 6 usa a etiqueta Condomínio. Nos links, a frase do botão da veterinária termina com "Queria saber sobre consulta e vacina em casa.", e a do orçamento continua com "Gostaria de um orçamento de pet sitter.". A primeira frase é sempre a mesma.

## 17/11/2026: site sem residencial e prévia do site inteiro

Pedido do Vinícius: "eu nao quero nada relacionado a residentcial / Vamos deixar a pagina agnostica / e como ficaria o site como um todo ? a versao com vet a domiciolo e pet sitter".

- Feito:
  - **Sem residencial** (line-vet `6f2529e`, na `ccr-ddd55fa2-btz5yk`).
    - O material por condomínio virou uma apresentação única, `materiais/modelo.html`, para mandar a qualquer contato ou parceiro. Não cita condomínio nem lugar; o campo de "bloco e apartamento" voltou a ser "bairro e cidade".
    - O gerador não pede mais nome e grava `materiais/Dra-Aline-Franca.html`, com a frase "Oi, Aline! Vi sua apresentação."
    - READMEs sem Petra Flamboyant. Nenhuma menção a condomínio ou residencial sobrou no line-vet.
    - A página do Petra já tinha saído do Git no `8a2a13a` e só existe no histórico; não havia o que apagar. Apaguei só uma cópia gerada de teste ("Residencial Exemplo"), que não estava no Git.
    - As entradas anteriores deste arquivo sobre o material por condomínio ficam como histórico.
  - **Prévia do site inteiro** (line-vet `2e7a26e`, branch `previa/site-completo`, **não** publicada na `ccr-ddd55fa2-btz5yk`).
    - Nove páginas: início, veterinária a domicílio, vacinas em casa, gatos, pet sitter, sobre, atendimento, dúvidas e privacidade.
    - Textos provisórios, escritos com as regras da skill copy-chief (canal site, setor veterinária) e só com fatos do perfil. O resto está marcado `[CONFIRMAR]`.
    - Toda página tem a faixa "Prévia, rascunho" e `noindex`.
    - Em 390 px, o botão de WhatsApp aparece sem rolar em todas as páginas.
  - **Testes:** 91 passam. A conferência de publicação (`PUBLICAR=1`) barra as nove páginas enquanto houver `[CONFIRMAR]`, faixa de rascunho, `noindex` ou CRMV sem número.
- Pendências:
  - **Ok do Vinícius** para levar a prévia à `ccr-ddd55fa2-btz5yk`. Mesmo com o ok, nada vai ao ar com `[CONFIRMAR]`.
  - **Entrevista:** os textos finais saem pela copy-chief a partir do perfil.
  - **Fotos:** gatos e sobre têm espaço reservado para elas.
- Pedidos para outras frentes (o coordenador trata com o Vinícius):
  - `plano.md`, `perfil.md` e os arquivos das frentes 4 e 6 ainda falam em condomínio; não editei.
  - **Frente 6:** a frase da apresentação é "Oi, Aline! Vi sua apresentação." Se for usar etiqueta para ela no WhatsApp Business, é essa a frase.

## 17/11/2026: material de parceria com o conteúdo da frente 6

- Feito (line-vet, na `ccr-ddd55fa2-btz5yk`; o material fica fora do deploy):
  - `materiais/modelo.html` segue `operacao/parcerias.md`, seção 4.
    - **Veterinária em casa primeiro:** consulta e vacina; cirurgia, anestesia geral e internação ficam na clínica, com encaminhamento; valores "sob consulta".
    - **Depois o pet sitter:** "valor reduzido" para cada animal a mais, sem 50%.
    - CRMV no rodapé. Nada sobre deslocamento.
  - **Gerador:** `node materiais/gerar.mjs "Nome do parceiro"` (use `--na` quando o nome pede "na").
    - Os botões saem com "Oi, Aline! Peguei seu cartão no {parceiro}." (seção 5.3). O nome do parceiro aparece só na mensagem, não na página.
    - Sem nome, sai a versão geral: "Oi, Aline! Peguei seu cartão."
  - **Correção:** a calculadora do material estava quebrada desde a versão agnóstica (`6f2529e`). O teste novo (`tests/materiais.spec.js`) achou o erro; está corrigido.
- Pendências: o material sai como rascunho enquanto houver 4 pontos `[CONFIRMAR]` (perguntas 10, 16, 19 e 39, e o número do CRMV).

## 17/11/2026: prévia levada à branch principal

- Feito: com o ok do Vinícius ("Levar agora"), as nove páginas da prévia estão na `ccr-ddd55fa2-btz5yk` do line-vet (`f69f477`, README em `bd4466d`), por cima do material de parceria.
  - Continuam: a faixa "Prévia, rascunho", o `noindex` e os pontos `[CONFIRMAR]`.
  - A conferência `PUBLICAR=1 npx playwright test publicacao` barra as nove páginas até a entrevista.
  - Antes do push conferi que a branch não publica sozinha: o repositório é privado e não tem deploys no GitHub, nem status ou checagens nos commits, nem webhooks, nem GitHub Pages. A Vercel ainda não está ligada.
  - 95 testes passam.
- Pendências:
  - Entrevista: textos finais pela copy-chief, e depois tirar a faixa e o `noindex`.
  - Fotos.
  - Ao ligar a Vercel (PT-S12): a branch de produção vai mostrar a prévia. Só ligar depois que a conferência de publicação passar.

## 17/11/2026: fotos da Aline no Sobre

Pedido do Vinícius: "podemos ter uma parte no sobre, com um carrosel de fotos. A maioria vai ser fotos com animais. [...] Pesquise sobre e vamos adequar isso na pagina."

- Feito:
  - **Pesquisa** no adendo de `site/pesquisa-design.md`, com fontes.
    - Carrossel que passa sozinho é ignorado e fere a WCAG 2.2.2.
    - No celular, as pessoas arrastam com o dedo.
    - Fotos reais criam vínculo.
  - **Galeria no Sobre** (line-vet `82ded72`, na `ccr-ddd55fa2-btz5yk`): seção "Eu e os bichos", logo depois da abertura.
    - No celular, uma faixa que se arrasta, com a próxima foto aparecendo na borda.
    - No computador, um mosaico de 3 colunas com a primeira foto em destaque.
    - Nada passa sozinho, funciona sem JavaScript e rola pelo teclado.
    - Seis espaços reservados, com legendas `[CONFIRMAR]`.
  - 99 testes passam, incluindo a acessibilidade do Sobre.
- Pendências: as fotos. Ao chegarem, vão para `assets/fotos/` em 480 e 960 px (PT-S9), e cada foto de paciente precisa de linha em `autorizacoes.md`.
- Pedidos para outras frentes:
  - **Frente 1 (pedido de fotos à Aline):** a galeria pede fotos que o `briefing-fotos.md` ainda não cobre bem. Não editei o briefing.
    1. **De 3 a 5 fotos espontâneas da Aline com os próprios animais**, sem pose, em casa: carinho, colo, brincando. O item 13 hoje pede só "os próprios animais"; para criar afeto, ela precisa aparecer junto. Não precisam de autorização de terceiros.
    2. **Uma foto forte para o destaque:** a Aline com um gato no colo, olhando para ele, em casa, na vertical e na horizontal, com espaço em volta para recorte. Pode ser o item 2, com essa orientação.
    3. **De 2 a 3 fotos com pacientes em momento calmo**, como o exame no sofá (item 9) ou a mão fazendo carinho (desejável "mãos"). Precisam de autorização escrita do tutor, com a finalidade "site", e sem rosto do tutor, criança, endereço ou fachada (LGPD).
    4. **Uma foto de pet sitter com afeto** (item 12): brincando ou servindo ração.
    5. **Formato:** foto vertical também, porque a galeria usa recorte de retrato (4:5), e luz natural. Para a galeria, de 6 a 9 fotos no total.

## 17/11/2026: prévia na Vercel, paletas e uma foto por página

- Feito:
  - **Prévia no ar:** https://line-vet.vercel.app (produção da `ccr-ddd55fa2-btz5yk`).
    - Abre sem login; os endereços de cada deploy e de outras branches pedem login da Vercel.
    - Testei as nove páginas nesse endereço, em 390 e 1440 px: status 200, imagens, fontes, links internos e WhatsApp certos, sem erro no console e sem rolagem lateral.
    - Testes, guia de estilo, scripts e material de parceria dão 404.
    - A faixa de rascunho e o `noindex` continuam. A conferência `PUBLICAR=1` é só para o site final, não para a prévia.
    - O plano Hobby da Vercel é para uso não comercial; para o site final com domínio, decidir no PT-S12 (Vercel Pro ou Cloudflare Pages).
  - **GitHub Pages abandonado:** o script `scripts/gerar-pages.mjs` e a branch `gh-pages` ficaram sem uso. Dá para apagar os dois com o ok do Vinícius.
  - **Paletas (discovery, nada aplicado no site):** três opções com o azul principal, na branch `previa/paletas`.
    - Prévia (com login da Vercel): https://line-vet-git-previa-paletas-vinisnascimento00-6369s-projects.vercel.app/paletas
    - Qualquer página abre em `?paleta=a|b|c`.
    - Pesquisa, tabela de cores e contrastes no adendo de `site/pesquisa-design.md`. Recomendo a **B · Azul profundo**.
    - O botão do WhatsApp continua verde.
  - **Uma foto por página** (line-vet `b04c125` e `63dcede`): cada abertura tem um arco vertical 4:5 com a descrição da foto que vai ali.
    - A foto atual da Aline continua no bloco "Oi, eu sou a Aline" do início.
    - O arco é o formato combinado para as fotos novas.
  - 101 testes passam.
- Pendências:
  - O Vinícius escolhe a paleta; só então ela é aplicada no site.
  - O Vinícius manda a mensagem de validação à Aline (texto abaixo).
- **Mensagem para a Aline** (o Vinícius manda):
  > Oi, Aline! Montei um rascunho do seu site para você dar uma olhada: https://line-vet.vercel.app
  > É só um rascunho: não está no Google e só você tem o link. Os quadros tracejados são espaços para as suas fotos, e o que está em amarelo [CONFIRMAR] é o que preciso que você me confirme.
  > Quando puder, me diz:
  > 1. Os textos parecem você? Tem frase que você não diria?
  > 2. Os serviços estão certos? O que você faz em casa e o que não faz.
  > 3. Os preços do pet sitter estão certos? E consulta e vacina: posso mostrar o valor ou deixo "sob consulta"?
  > 4. Em quais bairros e horários você atende?
  > 5. O que está errado ou faltando?
  > Pode responder por áudio ou mandar print da parte que quer mudar. Obrigado!
- Pedidos para outras frentes:
  - **Frente 1: fotos de abertura, uma por página.** Para incluir no pedido de fotos à Aline; não editei o `briefing-fotos.md`.
    - **Regras para todas,** para formarem uma identidade: luz natural de janela, sem flash; casas de verdade, sem estúdio; vertical 4:5; a Aline olhando para o animal (menos no Sobre); jaleco nas de atendimento.
    - **Paciente** só com autorização escrita do tutor (`autorizacoes.md`, finalidade "site").
    - **LGPD:** sem rosto do tutor ou de criança, sem endereço, placa, número da casa ou fachada.

    | Página | Foto | Detalhes |
    |---|---|---|
    | Início | A Aline com um gato no colo | De jaleco, sorrindo para a câmera; sentada no chão ou no sofá; meio corpo. De preferência um gato dela. |
    | Veterinária em casa | Consulta na sala, na altura dele | Ajoelhada, examinando um cão deitado no tapete com o estetoscópio; maleta aberta ao lado; corpo inteiro, de lado. Tutor fora do quadro ou só as mãos. |
    | Vacinas | A vacina na mão, a carteira ao lado | Detalhe fechado, de cima: as mãos dela aplicando a vacina num gato ou cão calmo no sofá; caixa térmica e carteira de vacinação à vista. |
    | Gatos | O gato chega no tempo dele | Agachada, com a mão estendida sem tocar; um gato se aproximando; câmera baixa, perto de arranhador ou janela. |
    | Pet sitter | Uma visita enquanto o tutor viaja | Brincando com varinha ou servindo a ração; tigelas à vista; cozinha ou área de serviço, casa sem ninguém; luz da tarde. |
    | Sobre | Retrato com os gatos dela | Sem jaleco, olhando para a câmera, na casa dela; meio corpo. Os animais são dela, então não precisa de autorização. |
    | Atendimento | A caminho do atendimento | Saindo do carro com a maleta e a caixa térmica, numa rua arborizada; corpo inteiro, de lado ou de costas. Sem placa, número de casa nem fachada. |
    | Dúvidas | Conversa antes de examinar | Sentada, anotando ou explicando, com um cão tranquilo deitado ao lado; tutor fora do quadro ou de costas; três quartos. |

## 17/11/2026: variante com o fundo azul e cor própria para o pet sitter

Pedido do Vinícius, depois de ver as paletas: "da para o fundo ser azulzinho ? e o do pet sitter outra cor ?"

- Feito (branch `previa/paletas`, `3fb9148`; nada na `ccr-ddd55fa2-btz5yk`): três variantes a partir da B, com o fundo do site em azul claro, texto em azul-tinta `#1B2B38` e cartões, faixas e espaço das fotos em creme quente `#F7F1E6`. O pet sitter ganha cor própria na abertura, nos itálicos, nos botões e na calculadora.
  - **D:** fundo `#EEF4F8`, pet sitter salmão (abertura `#F9E4D8`, texto e botão `#8A3B28`).
  - **E:** fundo `#E6EFF5`, pet sitter amarelo-manteiga (abertura `#F7EBC4`, texto e botão `#6B4E10`).
  - **F (recomendada):** fundo da E com o pet sitter salmão.
  - **Contrastes** (WCAG AA, conferidos à mão e com axe nas nove páginas, em 390 e 1440 px; 113 testes passam):
    - Texto sobre o fundo azul: 12,4 a 13,1:1.
    - Azul principal: 5,9 a 6,2:1; branco no botão azul: 6,9:1.
    - Texto do pet sitter: 6,6 a 6,9:1; branco no botão do pet sitter: 7,7:1.
    - Borda de campo sobre o fundo: 3,0 a 3,2:1.
    - WhatsApp: branco 5,4:1.
  - **Verde-sálvia descartado:** fica quase igual ao verde do WhatsApp (1,14:1 entre os dois), e um botão de orçamento verde ao lado do botão verde do WhatsApp confunde.
  - **Prévia** (com login da Vercel): https://line-vet-git-previa-paletas-vinisnascimento00-6369s-projects.vercel.app/paletas, ou qualquer página com `?paleta=d`, `e` ou `f`.
- **Avaliação franca:** o fundo azul funciona, desde que cartões e faixas fiquem em creme quente; sem isso, fica com cara de clínica.
  - O ganho é a identidade: o site fica "azul" de verdade, e o pet sitter se separa bem da veterinária.
  - A perda é um pouco do calor de papel que o creme dá.
  - O tom `#EEF4F8` (D) parece quase branco em muitas telas; `#E6EFF5` (E e F) se lê como azul.
  - Se o Vinícius preferir mais acolhimento, a B (creme com faixas azuis) continua uma boa escolha.
- Pendências: o Vinícius escolher entre B, D, E e F. Só então a paleta vai para a `ccr-ddd55fa2-btz5yk`.

## 17/11/2026: fundo contínuo (paletas G e H)

O Vinícius não gostou dos cortes de cor da página de vacinas ("eu nao gostei dessa transicao de cores"): cabeçalho creme, abertura em faixa azul, creme de novo, com uma linha fina em cada corte.

- Feito (branch `previa/paletas`; nada na `ccr-ddd55fa2-btz5yk`): duas variantes com um fundo só na página inteira, cabeçalho incluído. Sem faixas de ponta a ponta, sem linhas finas entre seções (separação por espaço), cor só em elementos contidos e uma única mudança de cor, no rodapé. Passam na acessibilidade nas nove páginas (117 testes).
  - **G (recomendada):** azul claro contínuo `#E6EFF5`; rodapé um tom mais fundo `#D3E1EB` (mudança suave); pet sitter salmão no arco da foto, nos itálicos, nos botões e nos cartões.
  - **H:** creme contínuo, azul no arco da foto, nos cartões, no bilhete e nos botões; rodapé azul escuro `#173F57` (mudança intencional); pet sitter ruivo, também nos botões.
  - Prévia (com login da Vercel): https://line-vet-git-previa-paletas-vinisnascimento00-6369s-projects.vercel.app/vacinas-em-casa?paleta=g (ou `?paleta=h`).
- O que o Vinícius viu e não é defeito do site atual:
  - **Arco da foto vazio à direita:** a captura era de uma versão anterior da prévia das paletas, montada antes das fotos por página. Desde `3fb9148` o arco aparece em 1440 px; conferi na prévia e no endereço da Aline.
  - **Botão redondo escuro na borda direita:** não é do site, que não tem nenhum elemento fixo no computador. É, muito provavelmente, a barra de ferramentas da Vercel, que aparece nas prévias para quem está logado. A Aline não vê. Dá para esconder pelo próprio botão ou em Settings → General → Vercel Toolbar.
- Pendências: o Vinícius escolher entre G e H (ou outra). Só então a paleta vai para a `ccr-ddd55fa2-btz5yk`.

## 17/11/2026: "está tudo creme" (cache do CSS)

- **Causa:** o `vercel.json` guardava tudo de `/assets/` por 7 dias no navegador, inclusive `site.css`, `site.js` e `paletas.css`, que mudam sem trocar de endereço. O Vinícius abriu a prévia com o HTML novo e o CSS antigo: a paleta G não existia no CSS guardado, então ficou tudo creme. O espaço da foto também apareceu sem estilo (pata gigante e lista com bolinhas).
- **Correção** (line-vet `c01ef28` na `ccr-ddd55fa2-btz5yk`; `3534394` na `previa/paletas`):
  - Cache de 7 dias só para fontes e imagens; CSS e JS são conferidos a cada visita. Conferido no ar: `site.css` com `max-age=0, must-revalidate`.
  - Links com `?v=2`, para abandonar as cópias já guardadas.
  - Teste que barra cache longo em `site.css` e `site.js`.
- **Erro meu no caminho:** ao juntar a correção na `previa/paletas`, um conflito foi publicado com os marcadores no HTML (`aa0ec4a`). Corrigi em seguida, num commit novo (`3534394`), sem reescrever o histórico. Afetou só a prévia das paletas, protegida por login; a branch principal e o endereço da Aline não foram afetados.
- O botão redondo escuro à direita, que aparece na captura, é a barra de ferramentas da Vercel (só para quem está logado).

## 17/11/2026: seletor de cores na página e seis paletas novas

Pedido do Vinícius: "eu nao gostei do contraste no geral mesmo. Quero que veja mais opcoes de paleta de cores, e coloque para eu testar uma opcao de mudar diretamente na pagina. para eu conseguir validar com a aline".

- Feito (line-vet `0b1ce56` na `previa/paletas` e `fb03be0` na `ccr-ddd55fa2-btz5yk`, que é o endereço que a Aline abre sem login):
  - **Botão "Cores" na faixa amarela de rascunho**, em todas as páginas. Abre a lista de paletas e troca o visual na hora.
    - A escolha vale para as outras páginas e fica salva no aparelho.
    - `?paleta=nevoa` no endereço também escolhe, e "Copiar o link com esta paleta" gera o link para mandar.
    - A aparência padrão continua a **Atual**: quem abre o site só vê o botão a mais.
    - Funciona no teclado (Esc fecha) e no celular.
  - **Seis paletas novas**, em três níveis de contraste: Névoa e Lavanda (suave), Pêssego e Areia e sálvia (médio), Linho e marinho e Azul claro (forte). Tabela com as contas no adendo de `site/pesquisa-design.md`.
  - **O pet sitter agora fica numa família de cor só.** Antes o azul de apoio brigava com o ruivo do botão e dos títulos; é a causa mais provável do "contraste" que incomodou.
  - **Fundo contínuo, sem faixas e sem linhas entre seções**; só o rodapé muda de cor.
  - Testado **no endereço real**, em 390 e 1440 px: botão nas nove páginas, 7 opções, escolha guardada ao andar e ao recarregar, sem erro no console.
  - 146 testes passam: acessibilidade de cada paleta nas nove páginas, fundo contínuo, o seletor e a prévia sem JavaScript. Verifiquei os testes derrubando de propósito uma cor e uma faixa.
  - Sai `paletas.html` (as paletas A a H). `scripts/paletas.py` gera `assets/paletas.css` e a lista do botão e confere o contraste.
- **Decisão que tomei por conta própria:** levei o seletor à `ccr-ddd55fa2-btz5yk`, e não só à prévia com login, porque é a única que a Aline abre. O combinado era não levar paleta nenhuma ao site antes de o Vinícius escolher, e isso se mantém (o padrão é a Atual). Se ele preferir, dá para tirar com `git revert fb03be0`.
- **Antes de publicar o site final:** a conferência `PUBLICAR=1` barra o site se sobrar `paletas.css`, `previa.js` ou `data-paleta`. A paleta escolhida entra no `:root` de `assets/site.css` (passo a passo no README).
- Pendências: o Vinícius e a Aline escolherem a paleta; o Vinícius mandar a mensagem de validação à Aline, agora dizendo que ela pode trocar as cores no botão "Cores".
- Pedidos para outras frentes: nenhum.
