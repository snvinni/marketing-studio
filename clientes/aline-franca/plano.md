# Plano da cliente: Dra. Aline França

Veterinária a domicílio para cães e gatos (com carinho especial por gatos) e pet sitter, em Campinas e região.

Plano aprovado em 16/11/2026. Foi escrito para ser executado aos poucos, por agentes diferentes. Cada pacote de trabalho (PT) tem o que precisa de entrada, o que entrega e como saber que está pronto. Um agente pode pegar um PT sem ter lido a conversa que gerou o plano.

---

## 1. Contexto e decisões já tomadas

- **Objetivo:** aumentar os pedidos de atendimento a domicílio (consultas, vacinas) e, como complemento, de pet sitter.
- **Carro-chefe:** veterinária a domicílio. Pet sitter é serviço complementar.
- **Posicionamento:** a Aline ama gatos e já tem clientes felinos. O site deve ter um espaço próprio para gatos (ver PT-S5), sem deixar os cães de fora.
- **Verba de anúncios:** até R$ 300/mês, só a partir do mês 2.
- **Ponto de partida:** ela tem Instagram profissional e clientes atuais. Não tem perfil no Google. O site está pronto no repositório, mas sem deploy e sem domínio.
- **Operação:** o Vinícius cuida de tudo; a Aline atende e manda fotos e vídeos.
- **Princípio:** nada entra no site sem a Aline confirmar. Texto que depende de resposta dela fica marcado com `[CONFIRMAR]` até a entrevista.

## 2. Estado atual do repositório (`snvinni/line-vet`, branch `ccr-ddd55fa2-btz5yk`)

| Arquivo | O que é |
|---|---|
| `index.html` | Site público atual, uma página só, com CSS e JS embutidos. Hoje fala só de pet sitter. |
| `assets/aline.jpg` | Única foto (308 px, recortada do PDF original). |
| `assets/og.jpg` | Imagem de prévia para compartilhamento. |
| `materiais/` | Material de apresentação para enviar como arquivo a parceiros e contatos, sem endereço nem público específico. Fora do deploy (`.vercelignore`). |
| `vercel.json`, `robots.txt`, `sitemap.xml`, `favicon.svg`, `README.md` | Configuração de publicação. |

**Identidade visual (manter):** fundo creme `#F6F1E9`, tinta `#2B2420`, azul `#4F96B0` / `#2F6F87`, terracota `#C0704A`. Títulos em Fraunces (com itálico azul), corpo em Figtree, assinatura em Caveat. Texto em primeira pessoa. Sem cara de SaaS: sem cartões de preço, sem selos, sem fonte mono.

**Peças que já existem e devem ser reaproveitadas:** calculadora de pet sitter (lógica em `index.html`, bloco `<script>`, funções `compute`, `render`, `message`), recibo do orçamento, lista com patinhas, linha do tempo "como funciona", bloco de citação azul, bilhete de fechamento, e o comportamento sem JavaScript (classes `js`, `no-js`, `js-only`, `nojs-msg`).

**Dados fixos:** WhatsApp `5519981811227`. Preços de pet sitter: 1 animal R$ 50 (1 visita) / R$ 80 (2 visitas); adicional R$ 25 / R$ 40; exóticos R$ 50 por gaiola por visita; medicação R$ 10 a R$ 60 a combinar. Domínio escolhido: `draalinefranca.com.br`.

## 3. O que a pesquisa mostrou

**Funciona, em ordem de retorno para um negócio local de uma pessoa:**
1. Perfil da Empresa no Google com avaliações. Pesam mais: categoria principal, proximidade de quem busca, avaliações (quantidade, nota, recência, respostas). Quem atende em casa cadastra "área de atendimento" e oculta o endereço.
2. Site com uma página por serviço e uma de área atendida, ligado ao perfil.
3. Google Ads de pesquisa para quem já procura o serviço. Os pedidos chegam por WhatsApp ou ligação.
4. Indicação e parcerias locais.
5. Instagram como prova de confiança para quem veio do Google.

**Não funciona ou dá problema:** endereço falso no Google (suspensão); comprar ou trocar avaliação por desconto; impulsionar post com público amplo; Google Ads em correspondência ampla ou Display com verba pequena; postar todo dia sem perfil no Google.

**Exemplos:** Vets on Call (Austrália, caso do Google: custo por cliente de US$ 23 para US$ 2,80 com Google Ads e eventos); prática solo dos EUA que cresceu com nicho claro (caso PetDesk); DogHero (vacinação em domicílio com hora marcada no Brasil); My Pet Care (plano domiciliar por assinatura em Curitiba). Não achei caso brasileiro de veterinária autônoma com números.

**Regras do CFMV:**
- Resolução 1.690/2026 (atendimento domiciliar): permite consulta, vacinação, coleta, fluidoterapia e sedação leve em casa; proíbe cirurgia, anestesia geral, transfusão e quimioterapia injetável; exige prontuário e encaminhamento formal quando preciso.
- Resolução 1.649/2025 (publicidade): permite divulgar serviços e conteúdo educativo em qualquer canal; proíbe propaganda enganosa ou sensacionalista, garantia de resultado, preço predatório e venda casada.
- **Não li o texto integral** (site do CFMV bloqueado neste ambiente). Pontos a confirmar no Manual de Publicidade do CRMV-SP: tabela de preços no site; "50% de desconto" no animal adicional; fotos de pacientes; depoimentos de tutores; uso de termos como "especialista em felinos" (exige título registrado) e "Cat Friendly" (é certificação de entidade, não pode ser usada sem tê-la).

---

## 4. Trilha A: Descoberta (vem antes de tudo)

### PT-A1: Entrevista com a Aline ("anamnese")
- **Entrega:** `clientes/aline-franca/entrevista.md` com as perguntas abaixo e espaço para respostas. Depois de preenchido, é a fonte de verdade para todos os textos.
- **Como aplicar:** conversa de 40 a 60 minutos, gravada em áudio (com autorização), ou envio por WhatsApp em blocos. Um agente transcreve e preenche o arquivo.
- **Pronto quando:** todas as perguntas dos blocos 1 a 6 têm resposta ou "não se aplica".

**Bloco 1: Quem é a Aline**
1. Nome completo como quer aparecer, número do CRMV e estado.
2. Onde se formou e em que ano. Pós-graduação, residência, cursos (em andamento também).
3. Tem título de especialista registrado no CRMV? Tem alguma certificação ligada a felinos?
4. Onde já trabalhou (clínicas, hospitais, plantões)? Ainda trabalha em algum lugar?
5. Por que escolheu veterinária? E por que atender em casa?
6. De onde vem o amor por gatos? Tem gatos? Nomes, idades, histórias.
7. Um atendimento que marcou e que ela pode contar (sem identificar o tutor).
8. Como ela se descreveria para um tutor em três frases?
9. Do que ela não abre mão num atendimento?

**Bloco 2: Serviços a domicílio**
10. Lista completa do que faz em casa: consulta, vacinas (quais), vermifugação, coleta de sangue e outros exames, microchip, curativos, medicação injetável, fluidoterapia, atestado de saúde e de viagem, cuidados paliativos, eutanásia domiciliar, orientação de filhotes, acompanhamento de idosos e crônicos.
11. O que ela **não** faz em casa e para onde encaminha.
12. Atende só cães e gatos? Exóticos entram só no pet sitter?
13. Para gatos: o que faz de diferente (manejo, tempo, feromônio, toalha, caixa de transporte)? Atende gatos ariscos? Vai a gatis ou casas com muitos gatos?
14. Quanto dura uma consulta? O que leva na maleta? Como transporta vacinas (caixa térmica, termômetro)?
15. Quais laboratórios usa e como entrega resultado?
16. Tem clínica ou hospital parceiro para internação, cirurgia e emergência? Pode citar o nome?
17. Atende urgência? Em que horários responde? O que orienta fora do horário?
18. Emite carteira de vacinação, receita e prontuário digital?

**Bloco 3: Preços e condições**
19. Preço da consulta, de cada vacina, da coleta, do retorno. Quer mostrar no site ou só "sob consulta"?
20. Cobra deslocamento? Como varia por bairro ou cidade?
21. Formas de pagamento. Parcelamento. Nota fiscal ou recibo.
22. Política de cancelamento e de atraso.
23. Pet sitter: os preços atuais continuam valendo? Tem limite de visitas por dia?
24. Tem ou quer ter pacotes (filhote, vacinas do ano, idoso)?

**Bloco 4: Área e agenda**
25. Cidades e bairros que atende de verdade. Até quantos quilômetros ou minutos?
26. Dias e horários. Fim de semana e feriado.
27. Antecedência para agendar. Quantos atendimentos faz por dia.
28. Como prefere receber pedidos: WhatsApp, ligação, formulário.

**Bloco 5: Clientes e prova**
29. Quantos clientes ativos tem? Quantos são de gatos?
30. Como chegaram até ela (indicação, Instagram, Google)?
31. O que os tutores mais elogiam? O que mais perguntam antes de contratar?
32. Quais medos ouve com frequência ("meu gato não deixa", "vacina em casa é segura?")?
33. Três a cinco tutores que topariam avaliar no Google e ceder foto do pet.
34. Tem depoimentos em mensagem que possam ser usados (com autorização)?

**Bloco 6: Marca, regras e limites**
35. Usuário do Instagram. Outras redes. E-mail profissional.
36. Como quer ser chamada no site: "Dra. Aline", "Aline", "Dra. Aline França"?
37. Palavras que gosta e que não gosta de ver associadas a ela.
38. Algo que não quer que apareça (endereço, vida pessoal, local de trabalho atual).
39. Já consultou o CRMV-SP sobre publicidade? (Ver os pontos a confirmar da seção 3.)
40. Tem CNPJ ou MEI? Nome fantasia?
41. Concorrentes ou colegas que admira e por quê.
42. Meta para 6 meses: quantos atendimentos por semana quer ter?

### PT-A2: Pedido de fotos
- **Entrega:** `clientes/aline-franca/briefing-fotos.md` com a lista abaixo, mais uma mensagem pronta para mandar à Aline.
- **Pronto quando:** as fotos da lista "essenciais" estão no Drive da Aline, com nome descritivo e o link anotado em `briefing-fotos.md` e autorização registrada em `clientes/aline-franca/autorizacoes.md` (nome do tutor, pet, data, onde pode ser usada).

**Como fotografar:** celular na horizontal e na vertical, luz de janela, lente limpa, sem filtro, sem flash, fundo arrumado. Mandar o arquivo original (como documento no WhatsApp ou por Drive), não print.

**Essenciais (12 a 15 fotos):**
1. Retrato da Aline de jaleco, sorrindo, fundo claro (vertical e horizontal).
2. Aline com um gato no colo e com um cão (uma de cada).
3. Aline chegando a uma casa com a maleta.
4. Maleta aberta com os materiais organizados.
5. Caixa térmica de vacinas com termômetro.
6. Aplicando vacina em gato e em cão (rosto do tutor fora do quadro ou com autorização).
7. Examinando um gato num ambiente de casa (sofá, cama, arranhador).
8. Auscultando um cão no chão da sala.
9. Preenchendo a carteira de vacinação.
10. Pet sitter: servindo ração, trocando água, limpando caixa de areia, brincando.
11. Os gatos dela (se tiver).

**Desejáveis:** diploma e carteira do CRMV; detalhe das mãos com o animal; filhotes; idosos; vídeo curto de 10 a 20 segundos de um atendimento calmo com gato; foto dela dirigindo ou no carro com a maleta.

**Regras:** só pets cujo tutor autorizou por escrito (mensagem de WhatsApp serve). Sem animal em sofrimento, sem ferida exposta, sem sangue. Sem dados do tutor visíveis (endereço, receita, tela do celular).

### PT-A3: Checagem no CRMV-SP
- **Quem:** Aline. **Entrega:** respostas aos pontos a confirmar da seção 3, anotadas em `clientes/aline-franca/entrevista.md`, bloco 6.
- **Efeito no site:** define se a tabela de preços fica visível, se "50% de desconto" vira "valor reduzido", e se fotos de pacientes e depoimentos entram.

---

## 5. Trilha B: Site

### Arquitetura
| Endereço | Arquivo | Objetivo |
|---|---|---|
| `/` | `index.html` | Apresentar a Aline e os dois serviços; levar ao WhatsApp. |
| `/veterinaria-a-domicilio` | `veterinaria-a-domicilio.html` | Consulta em casa: como funciona, o que faz e o que não faz. |
| `/vacinas-em-casa` | `vacinas-em-casa.html` | Vacinação de cães e gatos em casa. |
| `/gatos` | `gatos.html` | Atendimento pensado para gatos. Página-assinatura. |
| `/pet-sitter` | `pet-sitter.html` | Conteúdo atual da home, com a calculadora. |
| `/sobre` | `sobre.html` | História, formação, CRMV, fotos. |
| `/atendimento` | `atendimento.html` | Bairros e cidades, horários, como agendar. |
| `/duvidas` | `duvidas.html` | Perguntas frequentes reunidas. |

Menu: Veterinária em casa · Vacinas · Gatos · Pet sitter · Sobre · botão "Falar no WhatsApp". No celular, menu recolhido simples.

### PT-S1: Base técnica compartilhada
- **Depende de:** nada. **Pode começar já.**
- **Fazer:** tirar o CSS e o JS de dentro do `index.html` e pôr em `assets/site.css` e `assets/site.js`. Sem etapa de build: HTML estático, como hoje. Cabeçalho e rodapé repetidos em cada página (copiados, com um comentário marcando o bloco). Manter as classes `js`/`no-js`.
- **Em `assets/site.js`:** função única que monta o link do WhatsApp com mensagem e origem da página; calculadora do pet sitter isolada num bloco que só roda se o formulário existir.
- **Pronto quando:** o `index.html` atual tem a mesma aparência de antes (comparar capturas em 390 px e 1440 px) e os 6 testes da calculadora passam.

### PT-S2: Página inicial nova
- **Depende de:** PT-S1; textos finais dependem de PT-A1.
- **Seções, em ordem:** (1) abertura: "Veterinária em casa, para cães e gatos" + frase pessoal + botão WhatsApp + foto; (2) três caminhos: consulta em casa, vacinas em casa, pet sitter, cada um com link; (3) por que em casa: menos estresse, sem transporte, rotina preservada, atenção sem pressa; (4) bloco dos gatos com link para `/gatos`; (5) como funciona em 3 passos; (6) quem é a Aline, resumo com link para `/sobre`; (7) avaliações reais do Google `[quando houver]`; (8) área atendida resumida; (9) bilhete de fechamento.
- **Pronto quando:** em 390 px o botão de WhatsApp aparece sem rolar; nenhum `[CONFIRMAR]` sobra depois da entrevista.

### PT-S3: Veterinária a domicílio
- **Conteúdo:** para quem é (gato que estressa, cão grande ou idoso, vários animais, tutor sem carro); o que está incluso na consulta; lista do que faz em casa; lista honesta do que não faz e para onde encaminha (Resolução 1.690/2026); como é a visita; valores ou "sob consulta" conforme PT-A3; dúvidas.
- **Formulário curto que monta a mensagem do WhatsApp:** espécie, nome e idade do pet, bairro, motivo, melhor dia. Sem JavaScript, vira botão direto.
- **Pronto quando:** a mensagem gerada chega legível no WhatsApp e identifica a página de origem.

### PT-S4: Vacinas em casa
- **Conteúdo:** vacinas que aplica para cães e para gatos `[CONFIRMAR lista]`; calendário de filhote e de adulto em tabela simples; cuidado com conservação (caixa térmica); carteira assinada e carimbada; o que observar depois; lembrete de reforço pelo WhatsApp.
- **Pronto quando:** a Aline revisou o calendário e a lista.

### PT-S5: Gatos
- **Conteúdo:** por que gato sofre mais com transporte e clínica; como ela conduz a consulta (tempo para o gato se aproximar, manejo com pouca contenção, exame onde o gato escolhe); orientações para o tutor preparar a casa; casos comuns (idoso, renal, arisco, casa com muitos gatos); pet sitter para gatos; fotos dos pacientes felinos e dos gatos dela.
- **Cuidados:** não usar "especialista em felinos" nem "Cat Friendly" sem título ou certificação (perguntas 3 e 39). Usar "atendimento pensado para gatos".
- **Pronto quando:** texto aprovado por ela e pelo menos 3 fotos reais de gatos.

### PT-S6: Pet sitter
- **Fazer:** mover o conteúdo atual do `index.html` para `pet-sitter.html`, com a calculadora intacta. Ajustar título, descrição e links.
- **Pronto quando:** os 6 testes da calculadora passam nessa página.

### PT-S7: Sobre
- **Conteúdo:** história em primeira pessoa (blocos 1 e 6 da entrevista), formação, CRMV, onde já trabalhou, os gatos dela, galeria de 4 a 6 fotos.

### PT-S8: Atendimento e dúvidas
- **`atendimento.html`:** lista de cidades e bairros em texto (não mapa falso), horários, antecedência, como agendar, deslocamento.
- **`duvidas.html`:** perguntas da entrevista (31 e 32) mais as atuais do pet sitter.

### PT-S9: Fotos
- **Depende de:** PT-A2.
- **Fazer:** escolher, recortar, gerar versões em WebP e JPEG em 480, 960 e 1440 px em `assets/fotos/`; texto alternativo descritivo; carregamento adiado fora da primeira tela; nova imagem de compartilhamento por página.
- **Pronto quando:** nenhuma página passa de 1 MB no celular e nenhuma foto sem autorização está no ar.

### PT-S10: Busca e medição
- **Fazer:** título e descrição próprios por página com "Campinas"; dados estruturados de negócio local (veterinária, área atendida, telefone) e de perguntas frequentes; `sitemap.xml` com todas as páginas; contagem de cliques no WhatsApp por página (Vercel Analytics, Cloudflare Analytics ou GA4, conforme a hospedagem); links com marcação de origem para Google, Instagram e anúncios.
- **Pronto quando:** cada clique de WhatsApp aparece no painel com a página de origem.

### PT-S11: Rodapé legal e revisão final
- **Fazer:** nome, CRMV-SP e número em todas as páginas; aviso de que não atende emergência `[CONFIRMAR]` com orientação do que fazer; página curta de privacidade (dados vão só para o WhatsApp); revisão de português; teste em iPhone e Android reais.

### PT-S12: Publicação
- **Quem:** Vinícius. Registrar o domínio no registro.br; escolher hospedagem (Vercel grátis não permite uso comercial: Vercel Pro ou Cloudflare Pages grátis); apontar DNS; conferir `https` e `www`.

**Ordem sugerida:** S1 → S6 → S2 → S3 → S4 → S5 → S7 → S8 → S9 → S10 → S11 → S12. S1 e S6 não dependem da entrevista. As demais podem ser montadas com `[CONFIRMAR]` e fechadas depois de A1.

---

## 6. Trilha C: Perfil da Empresa no Google
- **PT-G1 (criar):** categoria principal "Veterinário", secundária de pet sitter; tipo "área de atendimento" com endereço oculto; cidades reais da pergunta 25; horários; link do site e do WhatsApp.
- **PT-G2 (verificar):** vídeo com a Aline de jaleco, maleta, caixa térmica e carteira do CRMV. Um agente escreve o roteiro em `clientes/aline-franca/google/roteiro-verificacao.md`.
- **PT-G3 (preencher):** serviços, descrição de 750 caracteres, 10 a 15 fotos de PT-A2.
- **PT-G4 (avaliações):** mensagem pronta com link direto; pedir aos tutores da pergunta 33 e depois a todos, no dia seguinte ao atendimento. Meta: 10 em 30 dias, 25 em 90. Responder todas.
- **PT-G5 (rotina):** uma publicação por semana, reaproveitando o post do Instagram.

## 7. Trilha D: Instagram (executada no repositório `marketing-studio`, com a skill copy-chief)

**O que a pesquisa mostrou:** carrossel e Reels têm engajamento parecido (levantamento da Socialinsider de fev/2026 com 35 milhões de posts: 0,55% e 0,52%). Reels trazem alcance e gente nova; carrossel traz salvamentos e funciona para conteúdo em sequência (checklists, sinais, calendário de vacinas). Curtida não mede resultado: o que conta é visita ao perfil, clique no link e mensagem. Não achei dado de conversão específico de veterinários no Brasil; os números de mix que circulam são estimativas de blogs.

- **PT-I1 (diagnóstico):** registrar em `clientes/aline-franca/instagram/diagnostico.md` o estado atual do perfil: usuário, bio, destaques, últimos 12 posts, o que teve mais resposta. Depende da pergunta 35 da entrevista.
- **PT-I2 (perfil):** nome com "Veterinária a domicílio · Campinas", bio de três linhas (o que faz, para quem, onde), link do site, destaques (Como funciona, Vacinas, Gatos, Pet sitter, Avaliações), foto de PT-A2.
- **PT-I3 (linha editorial):** quatro pilares em `clientes/aline-franca/instagram/linha-editorial.md`:
  1. **Em casa:** bastidor do atendimento domiciliar (Reels curtos, stories).
  2. **Gatos:** o diferencial dela; manejo, sinais de dor, gato idoso, preparo da casa (carrossel e Reels).
  3. **Orientação:** dúvida real de tutor respondida em 30 a 45 segundos ou em 5 a 7 telas.
  4. **Prova:** avaliação do Google, história de paciente com autorização.
- **PT-I4 (calendário):** 8 posts para o primeiro mês em `clientes/aline-franca/instagram/calendario.md`: dois por semana, alternando Reels e carrossel, com roteiro, legenda, chamada e a foto ou vídeo que a Aline precisa mandar. Escritos pela skill copy-chief no modo "escrever" e conferidos no modo "revisar".
- **PT-I5 (rotina):** stories nos dias de atendimento com localização do bairro; resposta a comentários e mensagens em até um dia; cada post reaproveitado como publicação no perfil do Google.
- **PT-I6 (medição):** por mês, anotar alcance, salvamentos, visitas ao perfil, cliques no link e mensagens recebidas. Repetir o formato que gerou mensagem, não o que gerou curtida.

## 7A. Repositório `marketing-studio` (estúdio para a Aline e para futuros clientes)

**Decisão:** repositório privado novo, `snvinni/marketing-studio`, guarda o método, as skills, os modelos e uma pasta por cliente. O `line-vet` continua só com o código do site da Aline.

**Estrutura:**
```
marketing-studio/
├── README.md                      como o estúdio funciona e como começar um cliente novo
├── CLAUDE.md                      regras para agentes: idioma, onde gravar, o que nunca publicar sem confirmação
├── .claude/skills/copy-chief/     a skill (ver PT-K1)
├── metodo/
│   ├── plano-base.md              este plano, generalizado (trilhas A a G)
│   ├── pesquisa.md                o que funciona e o que não funciona, com fontes e data
│   └── regras-cfmv.md             resoluções 1.649/2025 e 1.690/2026 e pontos a confirmar
├── modelos/
│   ├── entrevista.md              a "anamnese" (42 perguntas)
│   ├── briefing-fotos.md
│   ├── autorizacoes.md
│   ├── perfil-cliente.md          voz, fatos, serviços, limites
│   └── calendario-instagram.md
└── clientes/
    └── aline-franca/
        ├── perfil.md              preenchido a partir da entrevista
        ├── entrevista.md
        ├── briefing-fotos.md
        ├── autorizacoes.md
        ├── plano.md               pacotes de trabalho e andamento
        ├── site/briefing.md       seção 5 deste plano; o código fica no line-vet
        ├── google/                textos do perfil, roteiro do vídeo, mensagens de avaliação
        ├── instagram/             diagnóstico, linha editorial, calendário, posts
        └── anuncios/              estrutura do Google Ads
```
Fotos pesadas não entram no Git: ficam no Drive, com o link anotado em `briefing-fotos.md`. As versões tratadas para o site ficam no `line-vet`.

- **PT-E1 (criar o repositório):** criar `snvinni/marketing-studio` privado, adicioná-lo a esta sessão, montar a estrutura acima, gravar o plano e os modelos. Commit inicial na `main`.
- **PT-E2 (migrar a Aline):** preencher `clientes/aline-franca/` com o que já sabemos (decisões da seção 1, dados fixos da seção 2), deixando `[CONFIRMAR]` no que depende da entrevista.
- **Pronto quando:** um agente novo, abrindo só o `marketing-studio`, consegue pegar qualquer PT lendo `README.md` e `clientes/aline-franca/plano.md`.

## 7B. Skill `copy-chief` (agnóstica)

**O que encontrei pronto:** o plugin Marketing da Anthropic (rascunho de conteúdo, revisão de marca, plano de campanha), o plugin Brand Voice (extrai e fiscaliza tom de voz), o plugin Website Copywriting (diagnóstico e edição de texto de site) e coleções no GitHub como `coreyhaines31/marketingskills`. Todas são em inglês, pensadas para SaaS e páginas de venda, e nenhuma conhece o CFMV. Servem de referência de estrutura, não de base.

**Desenho:** um núcleo que não sabe nada de veterinária, mais três camadas trocáveis.
```
.claude/skills/copy-chief/
├── SKILL.md                       papel, quando usar, fluxo, formato de saída
├── referencias/
│   ├── principios.md              núcleo: uma ideia por peça, específico em vez de genérico,
│   │                              palavras do cliente, chamada única, português do Brasil natural,
│   │                              lista de vícios de texto de IA a cortar
│   ├── revisao.md                 checklist do modo revisar e escala de gravidade
│   ├── setores/veterinaria-br.md  regras do CFMV, o que não prometer, vocabulário (tutor, paciente),
│   │                              temas que funcionam, temas proibidos
│   └── canais/
│       ├── instagram.md           bio, gancho, roteiro de Reels, carrossel, legenda, stories
│       ├── google-perfil.md       descrição, serviços, publicações, resposta a avaliações
│       ├── whatsapp.md            saudação, respostas rápidas, pedido de avaliação, lembrete
│       ├── site.md                título, abertura, página de serviço, perguntas frequentes
│       └── anuncios-google.md     títulos e descrições dentro do limite de caracteres
└── evals/                         casos de teste
```

**Fluxo da skill:**
1. Ler o perfil do cliente (`clientes/<cliente>/perfil.md`). Sem perfil, parar e pedir.
2. Carregar o pacote do setor indicado no perfil e o pacote do canal pedido.
3. **Modo escrever:** montar o briefing (objetivo, público, uma ideia, prova, chamada), escrever duas ou três versões, passar o próprio texto pelo checklist e entregar com as pendências marcadas `[CONFIRMAR]`.
4. **Modo revisar:** receber um texto e devolver veredito (aprovado, ajustar, refazer), problemas por gravidade (regra do setor, fato não confirmado, voz, clareza) e a versão corrigida.
5. Nunca inventar fato, preço, título ou depoimento; nunca aprovar texto que fira uma regra do pacote do setor.

**Agnóstica como:** para um cliente de outro ramo, cria-se um arquivo em `setores/` e um `perfil.md`; o núcleo e os canais não mudam. Para outro veterinário, só o `perfil.md`.

- **PT-K1 (construir):** escrever a skill com a ferramenta `skill-creator`, começando por `SKILL.md`, `principios.md`, `revisao.md`, `setores/veterinaria-br.md` e `canais/instagram.md`. Os outros canais entram quando a trilha correspondente começar.
- **PT-K2 (testar):** seis casos em `evals/`: (1) legenda de carrossel sobre vacina de gato; (2) roteiro de Reels de bastidor; (3) bio; (4) revisar texto com promessa de resultado, que deve ser reprovado; (5) revisar texto com "especialista em felinos" sem título, que deve ser sinalizado; (6) pedido para um cliente fictício de outro ramo, para provar que o núcleo é agnóstico.
- **PT-K3 (primeiro uso real):** produzir o calendário de PT-I4 com a skill e ajustar a skill com o que a Aline corrigir.
- **Pronto quando:** os seis casos passam e a Aline aprova os 8 primeiros posts com poucas correções.
- **Depende de:** `regras-cfmv.md` com os pontos confirmados em PT-A3. Até lá, o pacote do setor trata os pontos em aberto como "não usar".

## 8. Trilha E: Google Ads (mês 2, R$ 300)
- **Condição:** site no ar e 10 avaliações.
- **PT-P1:** estrutura em `clientes/aline-franca/anuncios/google-ads.md`: uma campanha de pesquisa, Campinas e entorno, horário de resposta, palavras em correspondência exata ou de frase ("veterinário a domicílio campinas", "vacina gato em casa"), lista de negativas (grátis, emprego, curso, 24 horas, emergência), três anúncios, destino na página do serviço.
- **PT-P2:** revisão semanal dos termos; decisão em 60 dias pelo custo por pedido.

## 9. Trilha F: Indicações e parcerias
- **PT-R1:** material de apresentação agnóstico, sem público específico, para mandar a parceiros e contatos (arquivo em `materiais/` no `line-vet`).
- **PT-R2:** lista de banho e tosa, pet shops sem veterinário, adestradores e hotéis para indicação cruzada.
- **PT-R3:** cartão ou ímã com QR code do WhatsApp.
- **PT-R4:** lembrete de reforço de vacina por lista de transmissão.

## 10. Trilha G: Medição
- **PT-M1:** planilha semanal: pedidos por origem, atendimentos fechados, avaliações novas, números do perfil no Google, gasto em anúncios. Revisão mensal: reforçar o que trouxe pedido, cortar o que não trouxe.

---

## 11. Andamento

| PT | Responsável | Situação | Data | Entrega |
|---|---|---|---|---|
| E1. Repositório `marketing-studio` | agente | feito | 2026-11-16 | este repositório |
| E2. Pasta da Aline | agente | feito | 2026-11-16 | `clientes/aline-franca/` |
| K1. Skill copy-chief | agente | feito | 2026-11-16 | `.claude/skills/copy-chief/` |
| K2. Testes da skill | agente | feito (com skill 23/23, sem skill 20/23) | 2026-11-16 | `relatorios/copy-chief-iteracao-1.html` |
| A1. Entrevista | Vinícius + Aline | a fazer | | `entrevista.md` |
| A2. Fotos | Aline | a fazer | | `briefing-fotos.md` |
| A3. Checagem CRMV-SP | Aline | a fazer | | `entrevista.md`, bloco 6 |
| S1. Base técnica do site | agente (repo `line-vet`) | a fazer | | |
| S6. Página de pet sitter | agente (repo `line-vet`) | a fazer | | |
| S2 a S11. Páginas e revisão | agente (repo `line-vet`) | aguarda A1 | | |
| S12. Domínio e publicação | Vinícius | a fazer | | |
| G1 a G5. Perfil no Google | Vinícius + agente | aguarda A1 e A2 | | `google/` |
| I1 a I6. Instagram | Vinícius + agente | aguarda A1 | | `instagram/` |
| K3. Calendário com a skill | agente | aguarda A1 | | `instagram/calendario.md` |
| P1 e P2. Google Ads | Vinícius + agente | mês 2 | | `anuncios/` |
| R1 a R4. Parcerias | Vinícius + agente | a fazer | | |
| M1. Planilha de medição | agente | a fazer | | |

## 12. Cronograma
- **Semana 1:** repositório `marketing-studio` e skill copy-chief; entrevista; pedido de fotos; checagem no CRMV; PT-S1 e PT-S6.
- **Semanas 2 e 3:** páginas S2 a S8 com os textos da entrevista; fotos; perfil no Google criado e verificado; primeiros pedidos de avaliação.
- **Semana 4:** S9 a S12, site no ar; Instagram arrumado.
- **Mês 2:** Google Ads; parcerias; rotina de avaliações e posts.
- **Mês 3:** revisar números e decidir próximos investimentos.

## 13. Verificação
- **Site:** capturas em 390 px e 1440 px de cada página; sem rolagem horizontal; sem erro de JavaScript; 6 testes da calculadora; mensagem do WhatsApp correta em cada formulário; páginas legíveis com JavaScript desligado; teste em iPhone e Android reais.
- **Conteúdo:** nenhum `[CONFIRMAR]` no ar; toda foto de paciente com autorização registrada; CRMV em todas as páginas.
- **Resultado:** pedidos por semana e por origem na planilha, mês a mês.
