<!-- Pesquisa feita em 17/11/2026 por um agente da frente 2 (site). Fontes citadas em cada item. -->

# Pesquisa: site da Dra. Aline França (veterinária a domicílio, Campinas)

Data da pesquisa: 17/11/2026. Fontes lidas na web entre 2010 e 2026, com prioridade para 2024–2026.
Método: busca na web e leitura das páginas. Quando uma página não abriu, digo. Alguns números foram medidos por mim (tamanho das fontes no Google Fonts e contraste das cores do `assets/site.css` atual); isso está indicado.

---

## Resumo: 14 recomendações, em ordem de impacto

1. **Nome completo e número do CRMV-SP em lugar visível em todas as páginas** (cabeçalho ou rodapé, e na página Sobre). O Manual de Publicidade do CFMV (2026) põe isso como obrigatório e lista "omitir nome completo e número de inscrição no CRMV" entre o que não pode. É também o sinal de confiança mais barato que existe.
2. **Os primeiros segundos no celular respondem a quatro perguntas:** quem é (foto real da Aline + "médica-veterinária"), o que faz (consulta e vacinas em casa, cães e gatos), onde (Campinas + bairros) e como chamar (WhatsApp). Nada de slogan genérico no lugar disso.
3. **WhatsApp como ação principal, com mensagem pré-escrita diferente por página** (`wa.me/55…?text=…`). No celular, uma barra fixa no rodapé só depois que o botão do topo sai da tela, e que some quando o bilhete de fechamento aparece. Ela precisa deixar espaço (`scroll-padding-bottom`) para não esconder o foco do teclado (WCAG 2.4.11).
4. **Corrigir contraste antes de lançar.** Medi as cores atuais: o azul `#4F96B0` sobre o creme dá 2,95:1 (reprova até para título grande). O texto cinza `#7A6E66` dá 4,39:1 (reprova texto normal). O branco sobre o verde do WhatsApp `#1FA855` dá 3,09:1 (reprova). Há trocas prontas na seção 5.
5. **Dizer com clareza o que se faz em casa e o que não se faz.** A Resolução CFMV 1.690/2026 regulamentou o atendimento domiciliar. Ela permite vacina em casa, proíbe cirurgia e anestesia geral e obriga a informar os limites ao tutor. Uma página de Dúvidas honesta sobre isso passa mais confiança do que qualquer selo.
6. **Fotos reais, nunca banco de imagens.** A pesquisa de rastreamento ocular da NN/g mostra que as pessoas ignoram fotos genéricas e olham fotos de gente real que trabalha no lugar. Enquanto as fotos não chegam: um retrato bom da Aline e tipografia. Nada de ilustração de IA.
7. **Fontes: auto-hospedar e cortar peso.** Medi no Google Fonts: a Caveat só para a assinatura pesa 48,9 KB; recortada à frase da assinatura cai para 6,9 KB (ou vira SVG, 0 KB de fonte). A Fraunces com eixo `opsz` pesa 81,7 + 67,4 KB; sem o eixo, 36,6 + 22,9 KB. Auto-hospedar também evita mandar o IP do visitante ao Google, o que ajuda a dispensar banner de cookies.
8. **Uma página "Atendimento" forte, não dez páginas de bairro.** O Google trata páginas de cidade/bairro quase iguais como abuso de "doorway". Uma página com a lista real de bairros, horários e como funciona o deslocamento atende a busca local sem risco.
9. **Perfil da Empresa no Google como negócio de área de serviço:** endereço oculto, até 20 áreas, nome sem palavra-chave, link para o site com UTM. É ele que aparece no mapa para "veterinário a domicílio Campinas".
10. **Avaliações: link para o Google, não widget.** O CFMV trata repostagem de depoimento como publicação própria. O Google não dá estrelas a avaliações que o próprio negócio exibe sobre si. Melhor um link discreto "Ver avaliações no Google".
11. **Preço:** o manual do CFMV permite divulgar o valor de consulta e vacina "em termos discretos" e proíbe tabela de procedimentos que dependem de avaliação, "grátis" e promoção. A calculadora do pet sitter pode seguir; para atos veterinários, "sob consulta" ou "a partir de" é decisão do projeto. As duas opções estão dentro da regra.
12. **Dados estruturados mínimos e verdadeiros:** um bloco JSON-LD `VeterinaryCare` com `areaServed` e telefone, sem `aggregateRating`. O resultado rico de FAQ deixou de existir em 7/5/2026. Mantenha as perguntas na página, mas não conte com estrelas nem com "sanfona" no Google.
13. **Medir clique no WhatsApp por página sem cookies:** Umami (plano grátis, 100 mil eventos/mês, atributo `data-umami-event` direto no HTML) ou Plausible (pago, conta cliques em links externos e mostra a página de origem). O Vercel só tem eventos no plano Pro, e o Cloudflare Web Analytics não tem eventos.
14. **Página de privacidade curta e verdadeira:** quem é a responsável, que o site não guarda formulário (a conversa vai para o WhatsApp, da Meta), qual ferramenta de medição usa e por quê, canal para pedidos do titular e regra de uso de fotos de pacientes. Sem banner, se não houver cookie nem conteúdo de terceiros.

---

## 1. Boas práticas para site de serviço local de uma pessoa só

### O que o visitante procura primeiro
- A NN/g resume quatro fatores de confiança, estáveis há décadas: (1) qualidade do design, sem erro de digitação nem link quebrado; (2) transparência sobre custos e regras; (3) conteúdo completo, correto e atual; (4) ligação com o resto da web, como avaliações de terceiros. No estudo, todos os participantes disseram que leriam avaliações antes de contratar. [NN/g, 2016](https://www.nngroup.com/articles/trustworthy-design/)
- **Para este site:** no topo da página inicial, no celular, sem rolar:
  - retrato real da Aline (já existe `aline.jpg`);
  - "Oi, eu sou a Aline, médica-veterinária" + **CRMV-SP nº ____**;
  - uma frase do que faz: "Consulta e vacinas na sua casa, para cães e gatos, em Campinas";
  - um botão de WhatsApp;
  - logo abaixo, uma linha de bairros/regiões e horários (com link para Atendimento).

### Prova de confiança que cabe nas regras do CFMV
- Nome completo + CRMV (obrigatório, ver seção de regras abaixo).
- Formação descrita com exatidão. O manual permite "informar sobre a sua especialização" só "desde que comprovada". [Manual de Publicidade CFMV, 2026](https://www.cfmv.gov.br/wp-content/uploads/2026/02/Manual-de-Publicidade-reduzido.pdf)
- Mostrar o processo, não só o resultado. A NN/g cita fotos do processo de trabalho como sinal de competência. [NN/g](https://www.nngroup.com/articles/trustworthy-design/) **Aqui:** a mala de atendimento, a caixa térmica da vacina, a carteira de vacinação preenchida, a Aline sentada no chão com um gato (com autorização).
- Explicar limites. A Res. CFMV 1.690/2026 obriga a veterinária a "informar ao responsável todas as limitações" e a orientar o encaminhamento a uma clínica quando necessário (art. 4º). [Res. 1.690/2026 – LegisWeb](https://www.legisweb.com.br/legislacao/?id=489828) Uma seção "Quando eu indico ir à clínica" é honesta e reduz atrito.
- Avaliações: link para o Perfil no Google (ver seção 6).

### Chamada para ação e WhatsApp
- O formato oficial é `https://wa.me/<número com DDI, sem +, zeros, parênteses ou traços>?text=<mensagem codificada>`. [WhatsApp FAQ](https://faq.whatsapp.com/5913398998672934) O site já usa isso.
- O WhatsApp é o canal certo no Brasil: pesquisa Opinion Box de junho/2025 (1.126 usuários) aponta 97% de uso diário. Entre 79% e 82% já falaram com empresas pelo app; as fontes divergem. 59% não gostam de resposta automática. [Agendor resumindo Opinion Box](https://www.agendor.com.br/blog/?p=54534), [Consumidor Moderno](https://consumidormoderno.com.br/comunicacao-empresas-no-whatsapp-pesquisa/), [ABC da Comunicação](https://www.abcdacomunicacao.com.br/73-dos-consumidores-preferem-mensagens-e-64-ja-compram-pelo-whatsapp-aponta-pesquisa-da-plataforma/). Não abri o relatório original.
- **Mensagem pré-escrita por página** (curta, editável, em primeira pessoa do tutor):
  - Vacinas: "Oi, Aline! Quero vacinar meu/minha ___ em casa. Bairro: ___"
  - Gatos: "Oi, Aline! Tenho ___ gato(s) e queria uma consulta em casa. Bairro: ___"
  - Pet sitter: a mensagem já sai da calculadora com as datas e o valor estimado.
  - Deixe um espaço para o bairro: isso responde a primeira pergunta dela.
- **Botão fixo?** Não achei estudo forte (procurei NN/g sem sucesso). A orientação prática da UX Movement é usar barra fixa só em páginas longas, com mais de duas telas de rolagem, e evitar em páginas curtas porque tapa conteúdo sem ganho. [UX Movement](https://uxmovement.com/mobile/when-to-use-a-floating-call-to-action-button/) A NN/g, sobre cabeçalhos fixos: o menor possível, fundo opaco, pouca animação, e versão "aparece ao rolar para cima" no celular. [NN/g, 2021](https://www.nngroup.com/articles/sticky-headers/)
  - **Recomendação:** no celular, barra de rodapé fina (altura ≈ 56–64 px, texto "Chamar no WhatsApp" + ícone oficial), mostrada só quando o botão do topo sai da tela e escondida quando o bilhete final, que já tem botão, entra na tela. No computador, nada fixo: o botão no topo e no fim bastam, e o número fica escrito para quem quer salvar o contato.
  - Não use a bolha verde redonda flutuante no canto: é o clichê de template e cobre conteúdo.
- **Marca do WhatsApp:** a Meta pede que não se mude a cor nem o desenho do logo, e que ele não seja o elemento mais destacado da página. [Meta – WhatsApp Brand](https://www.meta.com/pt-br/brand/resources/whatsapp/whatsapp-brand/) Botão com fundo próprio do site + ícone oficial pequeno resolve.

### Formulários curtos
- O site não precisa de formulário. O "formulário" é a mensagem do WhatsApp. A calculadora do pet sitter é o único campo de entrada. Use `type="date"`/`type="number"`, rótulo visível acima do campo (não só placeholder) e nenhum campo de nome, telefone ou e-mail, porque o WhatsApp já identifica a pessoa. Assim o site não coleta dado pessoal (ajuda na LGPD, seção 7). Fontes secundárias sobre teclado numérico e rótulo acima: [Zuko](https://www.zuko.io/blog/optimizing-the-phone-number-field-on-forms). Não achei a página da NN/g sobre formulários móveis.

### Página por serviço e por área
- Uma página por serviço (domicílio, vacinas, gatos, pet sitter) é correto: cada uma responde a uma busca diferente ("vacina em casa gato") e tem conteúdo próprio.
- Área atendida: ver seção 6 (doorway).

### Regras do CFMV que mudam o design (lidas na fonte)
- **Res. CFMV 1.649/2025** (publicidade) e seu **Manual (2026)**:
  - Nome completo + CRMV "na página principal do perfil", "ou em um local de destaque no site". Omitir é vedado. [Manual CFMV 2026](https://www.cfmv.gov.br/wp-content/uploads/2026/02/Manual-de-Publicidade-reduzido.pdf)
  - Preço: vedado divulgar tabela de procedimentos que dependem de avaliação prévia (art. 6º, V). Já valores de "consultas, curativos, vacinas, exames" que não dependem de avaliação "podem ser divulgados", "em termos discretos", sem promoção, brinde ou "grátis". [Res. 1.649/2025 – LegisWeb](https://www.legisweb.com.br/legislacao/?id=479765), [Manual](https://www.cfmv.gov.br/wp-content/uploads/2026/02/Manual-de-Publicidade-reduzido.pdf)
  - Repostar depoimento de cliente conta como publicação própria (art. 5º).
  - Imagem de paciente: autorização "expressa, prévia e informada", por escrito, com a finalidade (art. 8º e manual, cap. VI).
  - Vedado prometer resultado e anunciar técnica sem comprovação (art. 6º, III e IV). Vedado atribuir a si "distinção que não obteve" (anexo, VII), o que cobre selos como "Cat Friendly" sem certificação.
  - Vedado comparar negativamente com colegas ou clínicas. Cuidado ao escrever "por que em casa é melhor": descreva o benefício para o gato sem atacar a clínica. A própria Res. 1.690/2026 chama o estabelecimento veterinário de "padrão-ouro".
- **Res. CFMV 1.690/2026** (atendimento domiciliar): só veterinário com inscrição ativa; vacinação ("administração de imunobiológicos") prevista; vedadas cirurgias (exceto sutura superficial, coleta e drenagem de abscesso), anestesia geral (exceto eutanásia), transfusão e outros; fluidoterapia só com a profissional presente; prontuário obrigatório. [LegisWeb](https://www.legisweb.com.br/legislacao/?id=489828)

---

## 2. Design autêntico vs. cara de SaaS/template

### O que faz um site parecer "feito por gente"
- **Informação específica, não decoração.** As imagens que as pessoas olham são as que carregam informação útil. As decorativas, de "sentir bem", são ignoradas. [NN/g](https://www.nngroup.com/articles/photos-as-web-content/)
- **Detalhe que só ela teria:** nomes de bairros reais, o que vai na mala, como ela chega (de carro? de app?), quanto tempo dura uma visita de vacina, o que fazer com o gato antes de ela chegar. O template não tem isso.
- **Voz em primeira pessoa e consistente.** O site já tem. Bom exemplo: a Dra. Jo Lewis escreve "eu" no The Cat Vet (seção Exemplos).
- **Tipografia como protagonista.** As tendências de 2025–2026 citadas por Webflow, Framer e Envato falam em "volta aos fundamentos" (tipografia, layout) e em toques feitos à mão (letra manuscrita, ilustração própria) contra a "mesmice algorítmica". [Webflow 2026](https://webflow.com/blog/web-design-trends-2026), [Framer](https://www.framer.com/blog/web-design-trends/), [Vistaprint](https://www.vistaprint.com/hub/web-design-trends)
- **Alerta:** a Fast Company argumentou em 2025/2026 que o "artesanal falso" virou ele mesmo um jeito de se misturar. Não consegui abrir a matéria (403); li só o trecho no buscador. [Fast Company](https://www.fastcompany.com/91584397/ai-fears-are-fueling-the-handmade-branding-trend-technology-ai-fear-handmade-design) Tradução prática: a assinatura Caveat e o recibo picotado funcionam porque têm função (assinar o bilhete, mostrar o orçamento). Não espalhe rabiscos, setas desenhadas e manchas de aquarela "para parecer humano".

### Padrões que denunciam template/IA (lista de um estúdio, 2026)
Inter como única fonte; gradiente roxo-azul no hero e nos botões; hero enorme com frase vaga; cartões todos com o mesmo canto arredondado de ~16 px; espaçamentos idênticos em tudo; foto de banco (gente sorrindo no notebook); ilustração 3D "de plástico"; o mesmo fade-in em todo bloco; e, no excesso oposto, parallax e cursor customizado em tudo. [925 Studios, 2026](https://www.925studios.co/blog/ai-slop-web-design-guide)

### O que manter e o que ajustar na identidade atual
- **Manter:** creme + Fraunces itálico + Figtree + assinatura + bilhete + recibo picotado. É uma combinação editorial coerente e rara em site de veterinária.
- **Ajustar:** os cartões de serviço não devem virar a grade de três colunas de ícone + título + texto. Prefira lista editorial: título em serifa, duas linhas, "o que inclui", "quanto tempo", link. Variar ritmo: uma seção em texto corrido, outra em lista, outra com foto grande.
- **Para gatos sem selo:** em vez de "Cat Friendly", descrever práticas concretas e verificáveis: "chego devagar", "deixo ele escolher o canto", "uso toalha", "marco no horário mais calmo da casa". Não é promessa de resultado, é descrição de conduta.

---

## 3. Fotografia e imagem

- **Por que real:** a NN/g mediu que as pessoas passaram ~10% mais tempo olhando retratos de funcionários do que lendo as biografias, que ocupavam 316% mais espaço. Fotos genéricas de modelos são ignoradas. [NN/g](https://www.nngroup.com/articles/photos-as-web-content/)
- **Lista de fotos para pedir (em ordem de prioridade):**
  1. Retrato da Aline de meio corpo, luz natural, fundo de casa (não de estúdio). Serve para o topo e o Sobre.
  2. A Aline de joelhos ou sentada no chão, examinando um gato no sofá ou na caminha dele.
  3. Mãos: aplicando vacina, segurando a carteirinha, abrindo a mala.
  4. Objetos: mala de atendimento, caixa térmica, estetoscópio sobre a mesa da sala.
  5. Pet sitter: tigela, caixa de areia limpa, um gato dormindo com a luz da tarde (foto que vai pelo WhatsApp ao tutor).
  6. Recortes de Campinas (rua arborizada, portão) só se forem dela e tiverem função na página Atendimento.
- **Autorização:** para qualquer foto de paciente ou de casa de cliente, termo escrito com a finalidade (site, Instagram), como pede o manual do CFMV (cap. VI). [Manual](https://www.cfmv.gov.br/wp-content/uploads/2026/02/Manual-de-Publicidade-reduzido.pdf) Evite placa, número da casa e rosto de criança ao fundo. Fotos dos próprios animais da Aline não precisam de termo de terceiros e são ótimas para começar.
- **Enquanto as fotos não chegam:**
  - Só tipografia + o retrato que já existe. Títulos grandes em Fraunces, muito respiro e o bilhete fazem o trabalho.
  - Se quiser algum desenho: poucos traços de linha simples (uma tigela, uma caixa de transporte), feitos à mão ou por ilustrador, numa cor só. Nunca ilustração de IA nem foto de banco. Ambas aparecem na lista de clichês acima e contradizem o "eu atendo pessoalmente".
  - Não colocar "foto ilustrativa" de gato de banco: o visitante tende a supor que é paciente.
- **Técnico:** cada foto em AVIF + WebP (fallback JPEG), com `srcset` de 2–3 larguras e `width`/`height` declarados para não haver salto de layout (seção 4).

---

## 4. Celular e desempenho

### Core Web Vitals (limites atuais)
- **LCP ≤ 2,5 s**, **INP ≤ 200 ms**, **CLS ≤ 0,1**, medidos no 75º percentil das visitas, separado por celular e computador. [web.dev – Web Vitals](https://web.dev/articles/vitals) Limites de "ruim": LCP > 4 s, INP > 500 ms, CLS > 0,25. [web.dev – thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds) Um post no DEV dizia que o Google "apertou" os limites em 2025; não há confirmação oficial e a web.dev contradiz.

### Peso de página
- Mediana da web em out/2024, celular: 2.311 KB por página; 900 KB de imagens e 111 KB de fontes na página inicial. [Web Almanac 2024](https://almanac.httparchive.org/en/2024/page-weight)
- O site atual (medi os arquivos): `index.html` 20 KB, `site.css` 19 KB, `site.js` 10 KB, `aline.jpg` 18 KB. Está muito abaixo da mediana. **Orçamento sugerido:** até ~300 KB por página no primeiro carregamento, incluindo fontes e a foto principal.

### Fontes (o maior ganho disponível)
Medi o arquivo latino (woff2) que o Google Fonts entrega hoje:

| Pedido | Tamanho |
|---|---|
| Fraunces com eixos `opsz` + `wght`, normal e itálico (como está hoje) | 81,7 KB + 67,4 KB |
| Fraunces só `wght`, normal (400/600) | 36,6 KB |
| Fraunces só `wght`, itálico 400 | 22,9 KB |
| Figtree variável (300–900) | 20,2 KB |
| Caveat 400, latino completo | 48,9 KB |
| Caveat recortada ao texto "Com carinho, Aline" (`&text=`) | 6,9 KB |

- **Recomendações:**
  - Tirar o eixo `opsz` da Fraunces (ou fixar um valor). Economia de ~90 KB.
  - Assinatura: virar SVG (traçado da assinatura real da Aline seria ainda mais autêntico) ou recortar a Caveat só às letras usadas.
  - Auto-hospedar os woff2 no próprio domínio, com `unicode-range` latino. A web.dev diz que o ganho de velocidade de auto-hospedar é "misto" na prática, mas mais provável com CDN e HTTP/2 (a Vercel tem). [web.dev – fontes](https://web.dev/articles/font-best-practices) O argumento mais forte aqui é privacidade (seção 7).
  - Só WOFF2. `preload` só da Fraunces normal (o título do topo). `font-display: swap` nos títulos; no corpo, `swap` com fallback ajustado por `size-adjust` para não haver salto, ou `optional`. [web.dev – fontes](https://web.dev/articles/font-best-practices)
  - Três famílias é o teto. Não adicionar mono nem uma quarta fonte.

### Imagens
- AVIF tem ~96,7% de suporte global (iOS Safari 16+). [caniuse](https://caniuse.com/avif) Use `<picture>` com AVIF → WebP → JPEG.
- A imagem do topo (provável LCP) **nunca** com `loading="lazy"`. Ela fica no HTML (não em CSS) e leva `fetchpriority="high"`. As demais vão com `loading="lazy"` e `decoding="async"`. [web.dev – LCP, 2025](https://web.dev/articles/optimize-lcp)
- Sempre `width` e `height` (ou `aspect-ratio`) para CLS ≈ 0.

### INP
- Site estático com pouco JS já tende a passar. Na calculadora do pet sitter, calcule no evento `input` sem reflows pesados e sem bibliotecas.

### Toque, cabeçalho e menu
- Alvo mínimo WCAG 2.2 AA: 24×24 px (ou espaço equivalente). [W3C 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) Para os botões principais, mire em 44–48 px de altura. A NN/g sugere ~1 cm × 1 cm em cabeçalho fixo. [NN/g](https://www.nngroup.com/articles/sticky-headers/)
- Menu: a NN/g achou que menu escondido (hambúrguer) foi usado em 57% dos casos contra 86% do menu combinado, e recomenda deixar visíveis até 4 links de topo. [NN/g](https://www.nngroup.com/articles/hamburger-menus/) **Proposta:** no celular, cabeçalho com nome + 2 links visíveis ("Serviços", "Atendimento") + "Menu" em texto (não só ícone) para as 8 páginas. No computador, 4–5 links visíveis.
- Cabeçalho fixo no celular só se for fino e do tipo "aparece ao rolar para cima". Com a barra de WhatsApp no rodapé, dois elementos fixos comem tela demais. Prefira o cabeçalho não fixo.

### Barra fixa de WhatsApp no rodapé (celular): prós e contras
- **Prós:** a ação está sempre a um toque; páginas longas (Dúvidas, Gatos) não obrigam a voltar ao topo.
- **Contras:** come ~10% da altura da tela; pode cobrir conteúdo e o foco do teclado (WCAG 2.4.11 reprova se cobrir totalmente); vira ruído se estiver em página curta; e, se ficar sempre visível, repete o botão do bilhete final.
- **Como fazer bem:** aparecer depois do primeiro botão sair da tela; esconder quando o bilhete final aparece; `padding-bottom` no `body` e `scroll-padding-bottom` iguais à altura da barra ([W3C técnica C43](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)); respeitar `env(safe-area-inset-bottom)` no iPhone; não animar além de um deslizar curto.

---

## 5. Acessibilidade (WCAG 2.2 AA + LBI)

### Contraste: cálculo feito com as cores do `site.css` atual
Fundo `--paper #F6F1E9`. Mínimos: 4,5:1 texto normal; 3:1 texto grande (≥ 24 px, ou ≥ 18,66 px em negrito) e bordas/ícones de controles (1.4.11).

| Cor | Uso provável | Contraste | Situação | Troca sugerida |
|---|---|---|---|---|
| `--ink #2B2420` | texto | 13,6 | ok | — |
| `--ink-2 #4A403A` | texto | 9,0 | ok | — |
| `--muted #7A6E66` | texto secundário | 4,39 | **reprova** texto normal | `#776B64` (4,59) |
| `--brand #4F96B0` | itálico azul dos títulos | 2,95 | **reprova** até título grande | `--brand-ink #2F6F87` (4,99) ou `#3E7589` (4,54) |
| `--brand-ink #2F6F87` | links | 4,99 | ok | — |
| `--terra #C0704A` | destaques | 3,30 | só título grande | `#A35B39` (4,54) para texto pequeno |
| branco sobre `--wa #1FA855` | botão WhatsApp | 3,09 | **reprova** | `#198845` ou mais escuro (4,52) |
| branco sobre `--wa-600 #178F47` | botão (hover?) | 4,15 | reprova texto normal | idem |
| `--line #E2D7C7` | bordas | 1,26 | reprova se for borda de campo | borda de campo ≥ 3:1 |

(Cálculo meu, fórmula de luminância relativa da WCAG.) Como o verde do botão não precisa ser o verde do logo, escurecer o fundo do botão não fere a marca do WhatsApp, desde que o ícone oficial fique intacto.

### Outros pontos que importam aqui
- **Foco visível** em todo link e botão: contorno de 2–3 px em `--brand-ink`, com `outline-offset`. Sem `outline: none`.
- **Foco não encoberto** (2.4.11, AA): ver barra fixa acima. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
- **Alvos de toque** 24×24 px mínimo (2.5.8, AA); links dentro de frase estão isentos. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- **Movimento:** envolver qualquer animação (barra deslizando, revelações) em `@media (prefers-reduced-motion: no-preference)`. Nada que se mova sozinho por mais de 5 s sem pausa (2.2.2).
- **Calculadora:** `<label>` ligado a cada campo; resultado num elemento com `aria-live="polite"` para leitor de tela anunciar o total; erros em texto, não só em cor.
- **Imagens:** `alt` descritivo nas fotos de atendimento ("Aline examina um gato cinza no sofá da tutora"); `alt=""` nas decorativas; a assinatura em SVG com `aria-label` ou texto oculto.
- **Idioma:** `<html lang="pt-BR">`.
- **Lei Brasileira de Inclusão, art. 63:** "É obrigatória a acessibilidade nos sítios da internet mantidos por empresas com sede ou representação comercial no País", conforme "as melhores práticas e diretrizes de acessibilidade adotadas internacionalmente" (na prática, WCAG). O §1º pede "símbolo de acessibilidade em destaque". [Lei 13.146/2015](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm) Ver seção de incertezas sobre profissional autônoma.

---

## 6. SEO local e dados estruturados

### Perfil da Empresa no Google (o que mais pesa para "veterinário a domicílio Campinas")
- Negócio que atende na casa do cliente deve **ocultar o endereço** e cadastrar área de cobertura: até 20 áreas (cidades, CEPs ou regiões), sem raio, até ~2 horas de carro. [Google – área de cobertura](https://support.google.com/business/answer/9157481?hl=pt-BR)
- Nome real do negócio, **sem palavra-chave** ("Dra. Aline França – Médica-Veterinária", não "Veterinária a Domicílio Campinas Vacinas Gatos"). Site informado deve ser do negócio, não rede social. [Diretrizes do Perfil](https://support.google.com/business/answer/3038177?hl=pt-BR)
- Link do site no Perfil com UTM (`?utm_source=google&utm_medium=perfil`) para separar essas visitas na medição (seção 8).
- As áreas do Perfil e a lista de bairros da página Atendimento devem bater.

### Páginas de área sem "doorway"
- O Google define doorway como páginas criadas para ranquear buscas parecidas e que levam a páginas intermediárias menos úteis. Um exemplo que ele dá: "páginas voltadas a regiões ou cidades específicas que afunilam o usuário para uma página". [Google – políticas de spam](https://developers.google.com/search/docs/essentials/spam-policies)
- **Para este site:** uma página **Atendimento** com:
  - lista real de bairros/regiões (agrupados: Cambuí e centro, Barão Geraldo, Sousas e Joaquim Egídio, Taquaral… conforme ela de fato atende);
  - dias e horários, antecedência para marcar, se cobra deslocamento e como;
  - o que acontece fora da área ("me chame e vemos");
  - um mapa? Só se for imagem estática feita por vocês. Mapa embutido do Google carrega cookies e scripts de terceiros (seção 7).
- Criar página de bairro **só** se houver conteúdo real e diferente (ex.: Barão Geraldo tem muita república de estudante com gato e horário diferente). Não criar dez páginas trocando só o nome.

### Título e descrição
- Título único por página, curto e descritivo, marca no fim com separador, sem repetir palavra-chave. [Google – title links](https://developers.google.com/search/docs/appearance/title-link) Ex.: "Vacina em casa para cães e gatos em Campinas | Dra. Aline França".
- Descrição única por página. O Google só a usa quando acha mais precisa que o texto da página. [Google – snippets](https://developers.google.com/search/docs/appearance/snippet) Ex.: "Vacino seu cão ou gato em casa, sem caixa de transporte. Atendo bairros de Campinas. Fale comigo pelo WhatsApp."

### schema.org
- `VeterinaryCare` existe em schema.org como subtipo de `MedicalOrganization` (não de `LocalBusiness`) e aceita `areaServed` (texto, `Place`, `AdministrativeArea`). [schema.org/VeterinaryCare](https://schema.org/VeterinaryCare)
- A documentação de LocalBusiness do Google exige `address` e `name`, recomenda `telephone`, `url`, `openingHoursSpecification`, `priceRange`, e manda usar o subtipo mais específico. Ela não fala de negócio sem endereço nem de `areaServed`. [Google – LocalBusiness](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- **Sugestão prática** (um bloco na página inicial, repetido de forma resumida no Atendimento):
  - `"@type": ["VeterinaryCare", "LocalBusiness"]`, `name`, `url`, `telephone`, `image` (retrato), `founder`/`employee` como `Person` com `name` e `hasCredential` (CRMV);
  - `address` só com `addressLocality: "Campinas"`, `addressRegion: "SP"`, `addressCountry: "BR"` (sem rua);
  - `areaServed`: lista de `Place`/`City` com os bairros e cidades reais;
  - `openingHoursSpecification` com os horários reais;
  - `sameAs`: Instagram e o link do Perfil no Google.
  - **Não** incluir `aggregateRating`/`review`: o Google diz que, quando o próprio negócio controla as avaliações sobre si (inclusive widgets do Google ou Facebook), a página não ganha estrelas. [Google – review snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- **FAQPage:** o Google publicou em 8/5/2026 a nota "Deprecating the FAQ rich result feature": o recurso não aparece mais na busca desde 7/5/2026, e a documentação saiu do ar em 15/6/2026. [Google – changelog / FAQPage](https://developers.google.com/search/docs/appearance/structured-data/faqpage) Já vinha restrito a sites de governo e saúde desde 2023. [Google, 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes) **Conclusão:** a página Dúvidas continua valendo pelo conteúdo. O markup FAQPage é opcional e não gera nada visível no Google.
- `Service` (um por página de serviço) não gera resultado rico no Google. Use só se quiser descrever bem para outros leitores de dados; não é prioridade.

---

## 7. Privacidade e LGPD

### Precisa de banner de cookies?
- O guia da ANPD (2022, atualizado em jan/2025) aceita legítimo interesse para cookies estritamente necessários e, possivelmente, para medição de audiência. Para cookies não necessários, como os de publicidade, ele indica consentimento. O guia também desaconselha caixas pré-marcadas e recomenda uma "Política de Cookies". [Felsberg resumindo o guia](https://www.felsberg.com.br/cookies-e-protecao-de-dados-pessoais-orientacoes-da-anpd/), [Machado Meyer](https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/anpd-divulga-novo-guia-com-orientacoes-sobre-cookies) Não consegui ler o PDF original da ANPD (a página só trouxe metadados).
- Ferramentas sem cookie:
  - **Plausible:** não usa cookie nem localStorage; conta visitante único por hash diário de IP + user-agent com sal trocado a cada 24 h; diz que não precisa de banner. [Plausible – data policy](https://plausible.io/data-policy)
  - **Vercel Web Analytics:** sem cookies de terceiros; visitante identificado por hash da requisição, descartado em 24 h. [Vercel – privacidade](https://vercel.com/docs/analytics/privacy-policy)
  - **Umami:** "não usa cookies". [Umami – preços/FAQ](https://umami.is/pricing)
  - **Cloudflare Web Analytics:** a doc oficial diz que não rastreia o usuário entre sites; fontes secundárias dizem que não usa cookie nem localStorage. [Cloudflare](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/), [ctrl.blog](https://www.ctrl.blog/entry/review-cloudflare-analytics/)
- **Conclusão para este site:** sem cookies próprios, com medição sem cookie, **fontes auto-hospedadas** e **sem embeds** (mapa do Google, post do Instagram, vídeo do YouTube, widget de avaliações), não há o que consentir num banner. Se algum embed entrar, use "clique para carregar" (imagem estática + link).
- **Por que as fontes contam:** em 20/1/2022 um tribunal de Munique (LG München I, 3 O 17493/20) condenou um site por carregar Google Fonts do servidor do Google sem consentimento, porque isso envia o IP do visitante. A saída apontada foi hospedar localmente. É decisão alemã de primeira instância, sob a GDPR, não a LGPD, mas mostra o risco. [The Register](https://www.theregister.com/2022/01/31/website_fine_google_fonts_gdpr/), [IHK](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176)

### O que a página de privacidade precisa ter (curta, em primeira pessoa)
1. Quem é a responsável: nome, CRMV, cidade, contato.
2. O que o site coleta: nenhum formulário guarda dados; a calculadora roda no navegador e não envia nada.
3. WhatsApp: ao tocar no botão, a conversa acontece no WhatsApp (Meta), com as regras dele; o que a Aline guarda das conversas e por quanto tempo.
4. Medição: nome da ferramenta, que não usa cookie, o que registra (página, origem, tipo de aparelho, país/cidade) e por quanto tempo.
5. Dados do atendimento: ficha/prontuário do animal e dados do tutor são guardados porque a Res. CFMV 1.690/2026 (art. 5º) e a Res. 1.321/2020 exigem prontuário. [LegisWeb](https://www.legisweb.com.br/legislacao/?id=489828)
6. Fotos: só publica foto de animal ou casa com autorização escrita, que pode ser retirada.
7. Direitos do titular (art. 18 da LGPD: acesso, correção, exclusão etc.) e o canal para pedir (WhatsApp ou e-mail).
8. Data da última atualização.
- **Encarregado (DPO):** a Res. CD/ANPD 2/2022 dispensa agentes de pequeno porte de indicar encarregado, desde que ofereçam um canal de comunicação com o titular (art. 11). [Machado Meyer](https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/empresas-de-pequeno-porte-podem-ser-dispensadas-de-ter-dpo), [texto da resolução](https://www.gov.br/palmares/pt-br/midias/arquivos-menu-acesso-a-informacao/legislacao/resolucao-cd-anpd-n2-2022.pdf) Ver incertezas sobre o enquadramento de pessoa física.

---

## 8. Medição de cliques no WhatsApp por página

| Ferramenta | Sem cookie | Evento de clique | Página de origem | Custo |
|---|---|---|---|---|
| **Umami** (nuvem) | sim | `data-umami-event="whatsapp"` + `data-umami-event-pagina="vacinas"` direto no `<a>` | sim, como propriedade | grátis: 100 mil eventos/mês, 1 site, 6 meses de histórico |
| **Plausible** | sim | automático para links externos ("Outbound Link: Click"), ou classe `plausible-event-name=WhatsApp` | sim ("top pages that drive the clicks") | a partir de US$ 9/mês (10 mil pageviews); 30 dias grátis |
| **Vercel Web Analytics** | sim | `va('event', {name:'WhatsApp', data:{pagina:'vacinas'}})` | sim, via `data` | **eventos só nos planos Pro e Enterprise** |
| **Cloudflare Web Analytics** | sim | não tem eventos | — | grátis |

Fontes: [Umami – eventos](https://docs.umami.is/docs/track-events), [Umami – preços](https://umami.is/pricing), [Plausible – outbound](https://plausible.io/docs/outbound-link-click-tracking), [Plausible – eventos](https://plausible.io/docs/custom-event-goals), [Plausible – preços](https://plausible.io/#pricing), [Vercel – eventos](https://vercel.com/docs/analytics/custom-events). Cloudflare sem eventos: fontes secundárias ([ctrl.blog](https://www.ctrl.blog/entry/review-cloudflare-analytics/)); a FAQ oficial não abriu.

**Recomendação:** Umami no plano grátis, se couber nos 100 mil eventos/mês (para um site local, deve sobrar). Senão, Plausible. Marcar cada link de WhatsApp com duas propriedades: `pagina` (inicio, domicilio, vacinas, gatos, pet-sitter, sobre, atendimento, duvidas) e `posicao` (topo, barra, bilhete, calculadora). Nunca enviar o texto da mensagem nem dados da calculadora que identifiquem a pessoa.

Complementos:
- UTM no link do Perfil no Google e na bio do Instagram (`?utm_source=instagram&utm_medium=bio`). Umami e Plausible leem UTM.
- Medida real de sucesso: pedir à Aline que anote, por um mês, quantas conversas começaram com a mensagem pré-escrita de cada página (o texto denuncia a origem). É grátis e confirma os números da ferramenta.

---

## Exemplos de sites

Li o texto das páginas. A ferramenta não mostra imagens, então quando digo "fotos reais" me baseio em nomes de arquivo e legendas, e aviso.

1. **The Cat Vet – Dra. Jo Lewis (Reino Unido, só gatos, domicílio)** – https://www.thecatvet.co.uk/
   Faz bem: escreve em primeira pessoa, com história pessoal e tom leve, e diz as cidades atendidas. Copiar: a voz "eu" e a especificidade da área. Não copiar: o selo "Cat Friendly Veterinarian" (ela tem certificação; a Aline não pode usar) e o excesso de ofertas (livro, cursos, loja, gorjeta) disputando a página.

2. **First Paw Mobile Vet (Melbourne, Austrália)** – https://firstpaw.com.au/
   Faz bem: "Como funciona" em 4 passos, tabela "em casa x clínica", lista de bairros em página própria, aviso claro de que não atende emergência, e fotos de pets em casa e do veterinário em visita (pelas legendas). Copiar: os passos, o aviso de limite e a página de bairros. Adaptar a tabela sem desmerecer clínica (regra do CFMV).

3. **Dr Taylah (Melbourne, domicílio, foco em fim de vida e idosos)** – https://drtaylah.com.au/ (lido em drtaylah.squarespace.com/services)
   Faz bem: preços "a partir de" com duração ("$229 (45 min)"), raio de atendimento explícito (~70 km), tom calmo e frase concreta sobre atendimento sem pressa, e indica colega para casos fora do foco. Copiar: preço com duração e indicar colega. Atenção: preço de procedimento no Brasil tem limite (seção 1).

4. **Pets' Request Mobile Veterinary Services (Davis, EUA)** – https://www.petsrequest.com/
   Faz bem: diz que mandar mensagem de texto é o jeito mais rápido (equivale ao WhatsApp), avisa de que só aceita novos pacientes em certas cidades e lista horários com exceções. Copiar: o aviso de disponibilidade ("este mês estou com agenda para…") e a honestidade sobre a área. Não copiar: o layout de plataforma (feito em PetDesk, sem nome de veterinário na página).

5. **DrBigodes (Grande Lisboa, domicílio)** – https://drbigodes.pt/
   Faz bem: horários claros e uma lista completa de localidades atrás de "Ver localidades". Exemplo do que evitar: formulário de captura no hero, grade de cartões de serviço, número de WhatsApp diferente entre topo e rodapé, e "sem custos extra" repetido sem mostrar valor algum.

6. **Vets 2 Your Pets (Reino Unido, rede de domicílio)** – https://vets2yourpets.co.uk/mobile-vet-services/
   Faz bem: explica a estrutura de preço ("taxa de visita + o que for feito; orçamento antes") e o limite físico ("só levamos o equipamento que conseguimos carregar"). Copiar: essas duas frases, adaptadas. Exemplo do que evitar: sobras de template na página ("{title}", "{vendor_count}"), erros de digitação e frases-clichê repetidas em todos os serviços.

7. **Veros – página Felinos (São Paulo)** – https://veros.vet/felinos-2
   Faz bem: dicas práticas para reduzir estresse (caixa de transporte coberta, levar objeto conhecido). Copiar: transformar isso em "Como preparar seu gato para a minha visita". Exemplo do que evitar: superlativos sem prova ("maior infraestrutura da América Latina", "melhor bloco cirúrgico do país").

8. **The Cat Practice (Nova York, só gatos)** – https://www.thecatpractice.com/
   Faz bem: conteúdo educativo em linguagem simples sobre gatos esconderem doença, e telefone com horários por serviço. Exemplo do que evitar: aviso de COVID ainda no topo em 2026. Conteúdo velho derruba a confiança; a NN/g põe "atual" entre os quatro fatores.

9. **Lap of Love (EUA, rede de domicílio para fim de vida)** – https://www.lapoflove.com/
   Faz bem: tom acolhedor ("Helping you and your pet is our passion") e perfis de veterinários com bio pessoal. Li só parte da página e não vi as fotos. Copiar: bio pessoal com rosto. Não copiar: o tamanho de rede (localizador, "Join our team").

10. **Matéria sobre cat sitters do ABC Paulista (jun/2025)** – https://www.abcdoabc.com.br/cat-sitter
    Não é site de cuidadora, mas mostra o que o tutor brasileiro espera: visita de ~1 h, fotos e relatos pelo WhatsApp, areia, água, brincadeira, remédio oral se prescrito. Copiar: listar isso na página Pet sitter e no recibo da calculadora ("inclui: …").

**Não encontrei** (com a busca disponível, que é dos EUA) site próprio de veterinária a domicílio independente em Campinas. Os resultados foram marketplaces (GetNinjas, Cronoshare) e o consultório móvel gratuito da prefeitura. Pode ser só limitação da busca, mas sugere pouca concorrência com site próprio. Também não achei site autoral de cat sitter brasileira para indicar.

---

## O que evitar

**Clichês de SaaS/template**
- Hero com gradiente, frase vaga ("Cuidado que transforma vidas") e botão "Comece agora" / "Agende já".
- Três cartões de preço lado a lado; "mais popular"; riscado de preço.
- Grade de ícones genéricos (patinha, coração, estetoscópio) com três linhas de texto cada.
- Contadores ("+500 pets atendidos", "98% de satisfação"), sobretudo inflados ou sem fonte.
- Selos e badges ("Cat Friendly", "Fear Free", "Top Vet") sem certificação, o que também é vedado pelo CFMV.
- Bolha verde redonda flutuante no canto, pop-up de "posso ajudar?", chat automático. 59% dos usuários não gostam de resposta automática no WhatsApp, segundo a Opinion Box citada acima.
- Inter/fonte do sistema como única fonte, cantos de 16 px em tudo, o mesmo fade-in em todo bloco, parallax, fonte mono.
- Carrossel de depoimentos com foto de banco.

**Erros comuns de site de vet/pet**
- Esconder o CRMV ou o nome completo.
- Foto de banco de gato "perfeito" ou de veterinário de jaleco em clínica que não é a dela.
- Foto de paciente sem autorização escrita; foto com placa ou número da casa do cliente.
- "Especialista em felinos" sem título registrado. Use "atendo muitos gatos", "gosto de gatos", "fiz curso de X" (com exatidão).
- Prometer resultado ("seu gato sem estresse", "vacinação sem dor").
- Comparar mal com clínicas ("na clínica seu gato sofre").
- Tabela de preço de procedimento; "consulta grátis"; "promoção de vacina".
- Mapa do Google embutido, feed do Instagram embutido, widget de avaliações. Pesam, carregam cookies e, no caso do widget, conflitam com o CFMV.
- Conteúdo velho (aviso de COVID, horário de férias passado, bairro que não atende mais).
- Número de WhatsApp inconsistente entre páginas.
- Site sem dizer o que **não** faz em casa (emergência, cirurgia), o que gera frustração e contradiz a Res. 1.690/2026.

---

## Pontos em que as fontes discordam ou que não consegui confirmar

1. **Preço de consulta e vacina.** A regra do projeto diz "de preferência sob consulta". O manual do CFMV (2026) permite divulgar valor de consulta e vacina "em termos discretos". As duas posições são compatíveis; publicar ou não é escolha, não obrigação.
2. **Exigência de CRMV no site de pessoa física.** O art. 4º, §3º, da Res. 1.649/2025 fala de "estabelecimentos". A exigência para o profissional (nome + CRMV em local de destaque) está no manual, que interpreta o artigo. Na prática, mostrar é o mais seguro.
3. **FAQPage.** O Google confirma o fim do resultado rico (maio/2026). Blogs dizem para manter o markup "por via das dúvidas", inclusive para IA. Não achei fonte oficial que diga que FAQPage ajuda em outro lugar.
4. **LocalBusiness sem endereço.** O Google exige `address` para LocalBusiness e não explica o caso de quem atende só em domicílio. Usar só cidade/estado é prática comum, mas não confirmei que o Google aceite. `VeterinaryCare` não é subtipo de `LocalBusiness` em schema.org; o tipo duplo `["VeterinaryCare","LocalBusiness"]` é solução minha, não orientação do Google.
5. **Cookies de medição e banner.** Os fornecedores (Plausible) dizem que não precisa de banner. O guia da ANPD trata de cookies, e as ferramentas sem cookie ainda processam o IP (em hash). Os advogados divergem sobre o peso do legítimo interesse para analytics. Recomendo mencionar a ferramenta na política, mesmo sem banner.
6. **Agente de pequeno porte.** Não confirmei se pessoa física autônoma (sem CNPJ) ou MEI entra no art. 2º da Res. CD/ANPD 2/2022. As fontes falam de ME, EPP, startups e entidades sem fins lucrativos.
7. **LBI art. 63** fala de "empresas com sede ou representação comercial no País". Não está claro se alcança profissional autônoma pessoa física. O símbolo de acessibilidade do §1º quase nunca é usado; não achei padrão oficial atual dele.
8. **Barra fixa de WhatsApp.** Não achei estudo independente (NN/g, Baymard) sobre botão flutuante de contato em site de serviço. Só há opinião prática e estudos de app (MDPI 2019/2024).
9. **Números do WhatsApp no Brasil.** Opinion Box: 79% ou 82% falam com empresas, conforme a matéria. Não li o relatório original.
10. **Auto-hospedar fontes é mais rápido?** A web.dev diz que o resultado real é "misto". O argumento firme é privacidade, não velocidade.
11. **Marca WhatsApp.** O resumo da página da Meta sugere não usar "WhatsApp" como verbo. Não consegui ver as regras completas de botão nem de tamanho mínimo.
12. **Páginas que não abri:** homevets.co.uk (erro SSL), vetstoyou.pt (domínio não resolve), petlove.com.br (403), Fast Company (403), Cats Only Veterinary House Calls (403), PDF do guia de cookies da ANPD (veio sem texto), manual de publicidade do CRMV-SP 2024 (404), página de "Contato" da NN/g (404), FAQ oficial do Cloudflare Web Analytics.
13. **Fotos dos exemplos.** Não vi as imagens dos sites citados, só textos e nomes de arquivo.

---

## Adendo (17/11/2026): fotos da Aline no Sobre (carrossel ou outra forma)

Pedido do Vinícius: uma parte no Sobre com fotos da Aline, a maioria com animais, com destaque, para criar afeto.

**Carrossel que passa sozinho, não.**
- Em teste da Nielsen Norman Group, as pessoas não viram uma informação que estava no slide mais visível de um carrossel automático. Carrossel lembra anúncio, e anúncio a gente aprende a ignorar. O artigo original não abriu; li resumos em [Yale Usability](https://usability.yale.edu/usability-best-practices/hero-imagescarousels), [ConversionXL](https://conversionxl.com/blog/dont-use-automatic-image-sliders-or-carousels) e [Smashing Magazine](https://uxdesign.smashingmagazine.com/2022/04/designing-better-carousel-ux).
- A WCAG 2.2.2 (nível A) exige poder pausar, parar ou esconder qualquer movimento que comece sozinho e dure mais de 5 segundos. A W3C pede botão de pausa em carrossel automático ([W3C WAI, tutorial de carrosséis](https://www.w3.org/WAI/tutorials/carousels/animations/)).

**O que as pessoas fazem com galerias.**
- No celular, quase todo mundo arrasta com o dedo; os pontinhos de navegação passam despercebidos. Mostrar as miniaturas evita que fotos fiquem escondidas ([Baymard: miniaturas](https://baymard.com/blog/always-use-thumbnails-additional-images), [Baymard: gestos no celular](https://baymard.com/blog/mobile-image-gestures)). A maior parte das diretrizes da Baymard é paga; li os resumos públicos.

**Fotos reais criam vínculo.**
- As pessoas olham fotos de gente real que trabalha ali e ignoram fotos genéricas. No "Sobre", o retrato ajuda a associar o serviço a uma pessoa ([NN/g, Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/)).

**Decisão.**
- Celular: uma faixa que se arrasta com o dedo, com a próxima foto aparecendo na borda.
- Computador: um mosaico com uma foto em destaque e todas à vista.
- Nada passa sozinho. É só CSS (`scroll-snap`, [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)), funciona sem JavaScript e dá para rolar pelo teclado.

**Desempenho.**
- Cada foto em 480 e 960 px, AVIF ou WebP com JPEG de reserva, `width` e `height` declarados e carregamento adiado (`loading="lazy"`), como na seção 4.
- Seis fotos de cerca de 40 KB no celular cabem no limite de 1 MB por página do PT-S9.

**Regras.**
- **CFMV:** foto de paciente só com autorização escrita do tutor, registrada em `autorizacoes.md`; nunca resultado de tratamento nem animal em sofrimento (`metodo/regras-cfmv.md`).
- **LGPD e Código Civil (art. 20):** a imagem de uma pessoa é dado pessoal, e o uso comercial pede autorização específica, com finalidade e prazo ([Migalhas](https://www.migalhas.com.br/depeso/394075/protecao-de-dados-pessoais-no-uso-de-imagem-e-voz), [Normas Legais, modelo de termo](https://www.normaslegais.com.br/guia/clientes/termo-de-autorizacao-para-uso-de-imagem-e-voz.htm)). Na prática: evitar rosto de tutor, de criança, endereço, número da casa e fachada. Se o tutor aparecer, a autorização dele é separada da autorização do pet. Fontes de divulgação jurídica, não da ANPD.
- **Os animais da própria Aline** não precisam de autorização de terceiros. São o melhor começo.

---

## Adendo (17/11/2026): paleta com o azul como cor principal

Pedido do Vinícius: "Quero uma paleta de cores que tenha o azulzinho como principal (quero que pesquise sobre qual paleta ficaria bom, veja as melhores de designers renomados)".

**Referências**
- **Sanzo Wada, *A Dictionary of Color Combinations*** (1933–34; seleção de 348 combinações publicada pela Seigensha em 2010). É uma referência clássica entre designers ([Wada Sanzo Colors](https://wada-sanzo-colors.com/about); versão digital em [sanzo-wada.dmbk.io](https://sanzo-wada.dmbk.io), dados abertos em [mattdesl/dictionary-of-colour-combinations](https://github.com/mattdesl/dictionary-of-colour-combinations)). Combinações com azul e um tom quente que serviram de base:
  - **nº 1:** English Red e Cerulean Blue.
  - **nº 99:** Pale Lemon Yellow e Cerulean Blue.
  - **nº 186:** Hay's Russet, Ochraceous Salmon e Blue.
- **Pentagram:**
  - [MedExpress](https://pentagram.com/work/medexpress): equilibrou os azuis clínicos com uma série de tons mais quentes.
  - [Roche](https://www.pentagram.com/work/roche): saiu de azul e cinza para uma gama "mais vibrante, humana e quente", com um azul mais rico no centro.
- **Koto, [Huma](https://www.designweek.co.uk/issues/14-19-april-2020/huma-rebrand):** cores frias e quentes inspiradas no tempo e no céu, para fugir da cara "fria e estéril" do setor.
- **Guia da PetDesk para clínicas veterinárias** ([PetDesk](https://petdesk.com/blog/the-psychology-of-color-in-veterinary-marketing)): uma cor forte, um destaque complementar e neutros.
- **Cautela:** que o azul "passa confiança" é uma regra prática de design, não um achado sólido de pesquisa ([99designs](https://99designs.com/logo-design/business-of-color/healthcare)).

**Resumo:** o azul fica na frente; um tom quente (terracota, salmão, ruivo) tira a cara de clínica; o fundo creme e a tipografia editorial evitam a cara de SaaS.

**Opções** (branch `previa/paletas` do line-vet; contrastes WCAG AA conferidos à mão e com axe nas nove páginas):

| | A · Azul e terracota | B · Azul profundo (Wada 186) | C · Azul e areia (Wada 99) |
|---|---|---|---|
| Fundo | creme #F6F1E9 | creme #F5F0E6 | areia #F7F2E1 |
| Texto | #2B2420 (13,6:1) | #1F2A33 (12,9:1) | #24302F (12,2:1) |
| Principal (botão, links, itálico) | #2F6F87 (5,0:1; branco 5,6:1) | #1D5F86 (6,1:1; branco 6,9:1) | #0E6E7E (5,3:1; branco 5,9:1) |
| Faixa | azul claro #E4EEF1 | azul claro #E2ECF3 na abertura; bilhete e rodapé em azul escuro #173F57 (creme 9,8:1) | água #DDEFF0 |
| Apoio | terracota só em enfeite | ruivo #7A3A2C (7,5:1) e salmão ocre #D8A37B | ocre #7A5A12 (5,7:1) e manteiga #E8C766 |
| Pet sitter | itálicos terracota, botões azuis | abertura salmão, itálicos ruivos, botões azuis | itálicos ocre, faixas manteiga, botões azuis |

**Recomendação: B.**
- É a que mais põe o azul na frente e a mais própria: faixa azul na abertura, bilhete e rodapé em azul escuro.
- Mantém um tom quente próximo da terracota de hoje, então a identidade continua reconhecível.
- Tem o maior contraste das três.
- A é a mais segura, mas muda pouco. C se afasta da identidade atual e o petróleo lembra spa ou clínica.

**Botão do WhatsApp: continua verde** (`#167A3E`, branco 5,4:1).
- O verde avisa na hora que o toque abre o WhatsApp.
- A Meta só protege o desenho e a cor do logotipo, não a cor do botão ([Meta](https://www.meta.com/pt-br/brand/resources/whatsapp/whatsapp-brand/)).
- Fica restrito aos botões de WhatsApp; o resto segue o azul.

---

## Adendo (17/11/2026): mais paletas e seletor na própria página

Feedback do Vinícius sobre a Azul claro (G): "eu nao gostei do contraste no geral mesmo". Ele não disse se era contraste demais ou de menos, então a resposta foi cobrir a faixa inteira: paletas **suaves** (texto e cores mais próximos do fundo, as duas famílias de cor vizinhas), **médias** e **fortes**, todas dentro do mínimo de acessibilidade (WCAG 2.2 AA).

**O que mudou na lógica das cores** (a causa mais provável da sensação de contraste):
- No pet sitter, o azul era a cor de apoio (subtítulo, números, patinhas, sublinhado) ao lado de um botão e títulos ruivos. Duas cores fortes brigando na mesma tela. Agora o pet sitter fica numa **família de cor só**.
- Nas páginas de veterinária, o apoio é do mesmo azul (Névoa e Lavanda) ou um tom quente discreto (as demais).
- Fundo contínuo, sem faixas e sem linhas entre seções; só o rodapé muda de cor.

**Referências usadas** (as combinações da Sanzo Wada, em `mattdesl/dictionary-of-colour-combinations`, escurecidas só o necessário para texto e botão passarem no contraste; não são os tons exatos do livro):
- nº 194 (Seashell Pink, Olympic Blue, Jasper Red): Pêssego.
- nº 135 e 294 (Sulpher Yellow, Salvia Blue): Areia e sálvia.
- nº 274 (Olympic Blue, Light Mauve): Lavanda.
- Névoa, Linho e marinho e Azul claro são do próprio projeto.

| Paleta | Contraste | Fundo | Texto | Principal (branco no botão) | Pet sitter | Rodapé |
|---|---|---|---|---|---|---|
| Névoa | suave | #EEF3F6 | 10,5:1 | #376E87 (5,0:1) | rosa-poeira #9A4F55 (5,2:1) | #DDE7EE |
| Lavanda | suave | #F5F4F8 | 12,1:1 | #3E6694 (5,4:1) | lavanda #7A5490 (5,5:1) | #E6E3EE |
| Pêssego | médio | #FBF5F0 | 11,6:1 | #3D6496 (5,6:1) | terracota #A2482A (5,6:1) | #F1E6DE |
| Areia e sálvia | médio | #F5F1E6 | 11,0:1 | #496B91 (4,9:1) | ocre #84621A (5,0:1) | #EAE3D2 |
| Linho e marinho | forte | #F2EEE7 | 11,6:1 | #2B4C6F (7,7:1) | terracota #9A5238 (5,0:1) | marinho #22384F (10,4:1) |
| Azul claro | forte | #E6EFF5 | 12,4:1 | #1D5F86 (5,9:1) | salmão #8A3B28 (6,6:1) | #D3E1EB |

Todos os pares de texto e fundo que o site usa (texto, texto suave, apagado; azul, pet sitter e apoio sobre fundo, cartão e faixas), a borda de campo (3:1) e o rodapé são conferidos por `scripts/paletas.py`; a checagem de acessibilidade (axe) roda em cada paleta, nas nove páginas, em 390 e 1440 px.

O botão do WhatsApp segue verde (`#167A3E`, branco 5,4:1).

---

## Adendo (17/11/2026): mais paletas, para veterinária e design moderno

Pedido do Vinícius: "procure mais opções de paletas; veja as que melhor combinam com vet e sites com designs modernos".

**O que a pesquisa mostrou** (fontes de marketing e agências; são opinião, não dado):
- **Veterinária:** o azul domina porque passa calma e confiança, mas pode parecer frio se usado sozinho. Balancear com neutros e um acento quente ([PetDesk, dez/2025](https://petdesk.com/blog/the-psychology-of-color-in-veterinary-marketing); [LifeLearn, ago/2025](https://www.lifelearn.com/2025/08/26/color-psychology-how-veterinary-practices-can-use-it-in-marketing-and-branding/)). Precedente de azul com tom quente: o rebrand da IVC Evidensia, com azul-petróleo, marinho e coral ([Made Good Designs](https://madegooddesigns.com/veterinary-branding/)); a busca trouxe a descrição de segunda mão, não o material oficial da marca.
- **Design de sites em 2026:** a fórmula que mais se repete é base calma e quente, mais **um acento só**, mais textura visível, e uma tendência "feita por gente" contra o site de modelo pronto ([Network Solutions](https://www.networksolutions.com/blog/website-design-trends/); [Cascade Web Dev, sobre o branco-nuvem em sites](https://cascadewebdev.com/blog/2025-12-12/why-pantones-cloud-dancer”-is-the-perfect-starting-point-for-website-design-in-2026.html)).
- **Cor de 2026 da Pantone: Cloud Dancer** (11-4201), um branco suave. A recepção entre designers foi **dividida**: uns o veem como calma e respiro, outros como seguro demais ([Print Monthly](https://www.printmonthly.co.uk/?p=13614); [Wallpaper](https://www.wallpaper.com/design-interiors/pantone-colour-of-the-year-2026-cloud-dancer-white)). Há quem peça mais saturação ([FM, "The Case for Bolder Color in 2026"](https://wpengine.fm.co/stills/cloud-dancer-bold-colors/)).
- **Cobalto contra ouro** aparece como combinação de contraste forte para pequenos negócios ([Small Business Expo](https://www.thesmallbusinessexpo.com/blog/design-trends-for-2025-in-web-design-and-graphic-design/)).
- **Não confirmado:** uma busca trouxe a combinação "azul-ardósia + canela + branco-nuvem + areia" com códigos de cor, mas não consegui achar a página de origem. Usei só a ideia; os tons da Nuvem são derivados por mim e conferidos no contraste.
- **Verde-musgo e sálvia** (PetDesk sugere azul com verde para clínicas de bem-estar) ficaram de fora: no pet sitter, um botão verde ao lado do botão verde do WhatsApp confunde.
- **Modo escuro** é comum em sites modernos, mas é uma decisão maior (muda todos os componentes); ficou de fora por ora.

**As quatro novas** (contrastes WCAG AA conferidos por `scripts/paletas.py` e pelo axe nas nove páginas, em 390 e 1440 px). Saiu a Azul claro, que o Vinícius rejeitou.

| Paleta | Contraste | Ideia | Fundo | Texto | Principal (branco no botão) | Pet sitter |
|---|---|---|---|---|---|---|
| Do logo | médio | cores do próprio logo: azul #4890B0, creme e caramelo da pelagem, marrom-cacau no texto | #F8F3EC | 13,2:1 | #2F7494 (5,2:1) | caramelo (5,1:1) |
| Nuvem | suave | branco-nuvem, azul-ardósia, canela; acento quente só no pet sitter | #F0EEE9 | 11,1:1 | ardósia (5,0:1) | canela (4,8:1) |
| Tinta azul | médio | papel quente com o texto em azul-tinta, como impresso editorial; pet sitter em tijolo | #F6F3EC | 10,4:1 | azul (5,3:1) | tijolo (5,5:1) |
| Cobalto e ouro | forte | cobalto vivo e ouro; rodapé cobalto escuro | #FAF7F0 | 14,8:1 | cobalto (6,6:1) | ouro-escuro (5,2:1) |
