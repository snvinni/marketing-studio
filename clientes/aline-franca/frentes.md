# Frentes de trabalho: Dra. Aline França

O plano (`plano.md`) dividido em seis frentes, cada uma tocada por um agente em uma sessão própria do Claude Code. Este arquivo diz o que cada frente faz, o que pode começar já, do que depende e qual prompt colar para iniciar.

## Mapa de dependências

```
ONDA 1 (começam agora, em paralelo)
  1 Entrevista ──────────────┐  precisa do Vinícius respondendo
  2 Site, fase 1 (base)      │  não depende de nada
  3 Skill, novos canais      │  não depende de nada
  4 Google, fase 1 (roteiros)│  não depende de nada
  6 Operação, fase 1         │  não depende de nada
                             │
ONDA 2 (depois da entrevista)▼
  2 Site, fase 2 (páginas)      precisa: entrevista + Site fase 1
  4 Google, fase 2 (textos)     precisa: entrevista (melhor com Skill pronta)
  5 Instagram                   precisa: entrevista (usuário do Instagram)

ONDA 3 (depois do site no ar)
  2 Site, fase 3 (fotos, medição, revisão)  precisa: fotos da Aline
  6 Operação, fase 2 (Google Ads)           precisa: site no ar + 10 avaliações
```

| Frente | Pode começar agora? | Espera por | Quem destrava |
|---|---|---|---|
| 1. Entrevista | Sim | Respostas da Aline | Vinícius |
| 2. Site | Fase 1 sim | Fase 2: frente 1. Fase 3: fotos | Frente 1; Aline |
| 3. Skill (canais) | Sim | Nada | — |
| 4. Google | Fase 1 sim | Fase 2: frente 1 | Frente 1 |
| 5. Instagram | Não | Frente 1 | Frente 1 |
| 6. Operação | Fase 1 sim | Fase 2: site no ar e 10 avaliações | Vinícius |

**Como saber se a entrevista já foi feita:** o topo de `perfil.md` diz "Fonte: entrevista de ...". Enquanto disser que a entrevista ainda não foi feita, as fases que dependem dela não começam.

## O que só uma pessoa pode fazer

| Tarefa | Quem | Destrava |
|---|---|---|
| Responder a entrevista (ou passar as respostas da Aline) | Vinícius + Aline | Frentes 2, 4 e 5 |
| Conferir os pontos de publicidade no CRMV-SP | Aline | Preços, fotos e depoimentos no site |
| Mandar as fotos (pedido em `briefing-fotos.md`) | Aline | Site fase 3, perfil no Google, Instagram |
| Registrar `draalinefranca.com.br` e publicar o site | Vinícius | Google Ads, link nos perfis |
| Criar o Perfil da Empresa no Google e gravar o vídeo de verificação | Vinícius + Aline | Avaliações, Maps |
| Pedir avaliações aos clientes atuais | Aline (mensagem pronta pela frente 4) | Google Ads |
| Publicar posts e responder mensagens | Vinícius | — |

## Regras para não haver conflito entre agentes

1. **Cada frente só mexe nos seus arquivos** (coluna "Arquivos" de cada frente). Precisa de algo fora deles? Anote em "Pedidos para outras frentes" no seu arquivo de andamento, não edite.
2. **Andamento por frente:** cada agente registra o que fez em `andamento/<frente>.md` (data, o que entregou, pendências, pedidos). Ninguém edita a tabela da seção 11 do `plano.md`; o Vinícius ou um agente de fechamento consolida depois.
3. **Só a frente 1 escreve em `perfil.md` e `entrevista.md`.** As outras leem. Faltou um dado? Use `[CONFIRMAR: ...]` no texto e liste a pendência.
4. **Só a frente 3 mexe na skill** (`.claude/skills/copy-chief/`). As outras usam; se o canal ainda não existe, a skill avisa e segue pelo núcleo.
5. **Só a frente 2 mexe no repositório `line-vet`.**
6. No `marketing-studio`, trabalhe na `main`: `git pull --rebase` antes de cada push, commits pequenos. No `line-vet`, parta da branch `ccr-ddd55fa2-btz5yk` (é a única; ainda não existe `main`) e faça push na branch que a sessão indicar.
7. Valem as regras do `CLAUDE.md`: português do Brasil, nunca inventar fato, nada com `[CONFIRMAR]` vai ao ar, texto de divulgação passa pela skill copy-chief.

---

## Frente 1: Entrevista

- **Objetivo:** preencher `entrevista.md` e reescrever `perfil.md`. É o que destrava quase tudo.
- **Pacotes do plano:** A1, A3 (registro) e o envio de A2.
- **Arquivos:** `clientes/aline-franca/entrevista.md`, `perfil.md`, `andamento/entrevista.md`.
- **Pronto quando:** as 42 perguntas têm resposta ou `[PENDENTE]`, o perfil foi reescrito a partir delas e a linha "Fonte" do perfil cita a data da entrevista.

**Prompt de início:**
```
Você é o agente da frente 1 (Entrevista) do projeto de marketing da Dra. Aline França. Eu sou o Vinícius e vou passar as respostas dela.

Antes de qualquer coisa, entenda o contexto. No repositório snvinni/marketing-studio leia, nesta ordem: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 1"), clientes/aline-franca/plano.md (seções 1, 3 e 4), clientes/aline-franca/perfil.md e clientes/aline-franca/entrevista.md. Veja também o git log recente e a pasta clientes/aline-franca/andamento/ para saber o que as outras frentes já fizeram.

Depois conduza a entrevista comigo:
- Blocos na ordem 1, 2, 4, 5, 3, 6.
- Use a ferramenta de perguntas com opções, em grupos de até 4 perguntas do mesmo bloco, com opções úteis; eu detalho em "Outro". Perguntas de história, frase ou exemplo podem ir em texto normal.
- Resposta genérica: peça um exemplo concreto. Guarde as frases boas da Aline palavra por palavra.
- No fim de cada bloco: resuma em 3 a 5 linhas, peça minha confirmação, grave em entrevista.md e faça commit e push.
- Pergunta 39: registre o que foi confirmado com o CRMV-SP; o que não foi continua proibido (metodo/regras-cfmv.md).
- Se eu escrever "resumo parcial", grave o que houver e marque o resto [PENDENTE].

Ao terminar: reescreva perfil.md a partir da entrevista (modelo em modelos/perfil-cliente.md), com a linha "Fonte: entrevista de <data>"; me entregue a mensagem do pedido de fotos (briefing-fotos.md) pronta para eu mandar; registre tudo em clientes/aline-franca/andamento/entrevista.md, incluindo a lista de pendências e quem resolve cada uma. Só mexa nos arquivos da sua frente.
```

## Frente 2: Site

- **Objetivo:** transformar a página única de pet sitter em um site de oito páginas, com veterinária a domicílio como serviço principal.
- **Repositório:** `snvinni/line-vet` (lê o `marketing-studio`).
- **Pacotes do plano:** S1 a S11 (S12, domínio e publicação, é do Vinícius).
- **Arquivos:** tudo no `line-vet`; no estúdio, `clientes/aline-franca/site/` e `andamento/site.md`.
- **Fase 1 (agora):** S1 (CSS e JS em `assets/site.css` e `assets/site.js`, cabeçalho e rodapé padrão, menu) e S6 (`pet-sitter.html` com a calculadora). Sem mudar o visual. Os 6 testes da calculadora continuam passando.
- **Fase 2 (depois da entrevista):** S2 a S5, S7 e S8: início, veterinária a domicílio, vacinas, gatos, sobre, atendimento, dúvidas. Textos pela skill copy-chief.
- **Fase 3 (com as fotos):** S9 a S11: fotos, busca e medição, rodapé legal, revisão final em celular real.
- **Pronto quando:** critérios de cada PT na seção 5 do `plano.md`.

**Prompt de início:**
```
Você é o agente da frente 2 (Site) do projeto de marketing da Dra. Aline França. Esta sessão tem os repositórios snvinni/line-vet (código do site) e snvinni/marketing-studio (plano e conteúdo); se faltar algum, conecte com add_repo.

Antes de qualquer coisa, entenda o contexto. No marketing-studio leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 2"), clientes/aline-franca/plano.md (seções 1, 2, 3 e 5 inteiras), clientes/aline-franca/perfil.md, clientes/aline-franca/site/briefing.md e a pasta clientes/aline-franca/andamento/. No line-vet, parta da branch ccr-ddd55fa2-btz5yk, leia o README.md e o index.html inteiro, e veja o git log.

Descubra em que fase você está:
- Se assets/site.css ainda não existe: faça a fase 1 (PT-S1 e PT-S6). Não mude o visual: compare capturas de tela em 390 px e 1440 px antes e depois, e escreva testes com Playwright para a calculadora (1 animal 1 visita = R$ 50; 2 animais = R$ 75/dia; 1 animal 2 visitas = R$ 80; 2 gaiolas 2 visitas = R$ 200; 5 dias multiplica o total; data final antes da inicial bloqueia o envio). Mantenha o funcionamento sem JavaScript.
- Se a fase 1 está feita e o perfil.md já diz "Fonte: entrevista de ...": faça a fase 2 (PT-S2 a S5, S7, S8), com textos escritos pela skill copy-chief do marketing-studio (canal site) a partir do perfil. Se a entrevista ainda não foi feita, pare ao fim da fase 1 e me avise.
- Fase 3 (PT-S9 a S11) só com as fotos recebidas (briefing-fotos.md).

Regras: visual editorial e acolhedor já existente (creme, Fraunces, primeira pessoa), sem cara de SaaS; nada com [CONFIRMAR] vai ao ar; siga metodo/regras-cfmv.md. Me mostre capturas de cada página pronta. Commit e push ao fim de cada PT, e registre o andamento em clientes/aline-franca/andamento/site.md no marketing-studio (git pull --rebase antes do push). Não edite perfil.md, a skill nem arquivos de outras frentes.
```

## Frente 3: Skill copy-chief (novos canais)

- **Objetivo:** dar à skill os canais que as outras frentes vão usar e rodar a segunda rodada de testes.
- **Pacotes do plano:** continuação de K1 e K2.
- **Arquivos:** `.claude/skills/copy-chief/`, `relatorios/`, `clientes/aline-franca/andamento/skill.md`.
- **Entregas:** `referencias/canais/google-perfil.md`, `whatsapp.md`, `site.md`, `anuncios-google.md`; um caso de teste novo por canal; segunda rodada dos testes (os critérios reforçados da primeira ainda não rodaram); relatório em `relatorios/`.
- **Pronto quando:** os quatro canais existem, todos os casos passam com a skill e o relatório está no repositório.

**Prompt de início:**
```
Você é o agente da frente 3 (Skill copy-chief) do estúdio de marketing. Trabalhe no repositório snvinni/marketing-studio.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 3"), clientes/aline-franca/plano.md (seção 7B), metodo/regras-cfmv.md, metodo/pesquisa.md, toda a pasta .claude/skills/copy-chief/ (SKILL.md, referencias/, evals/), relatorios/copy-chief-iteracao-1.md e a pasta clientes/aline-franca/andamento/. Veja o git log.

Sua tarefa:
1. Escrever os canais que faltam em .claude/skills/copy-chief/referencias/canais/, no mesmo formato de instagram.md: google-perfil.md (descrição de até 750 caracteres, lista de serviços, publicações, resposta a avaliações boas e ruins), whatsapp.md (saudação, respostas rápidas, pedido de avaliação, lembrete de reforço de vacina, pedido de autorização de foto), site.md (título e descrição de página, abertura, página de serviço, perguntas frequentes) e anuncios-google.md (títulos de até 30 caracteres, descrições de até 90, sem promessa nem preço). Pesquise os limites atuais de cada plataforma antes de escrever e cite a fonte.
2. Criar um caso de teste por canal novo em evals/, no formato dos existentes.
3. Rodar todos os casos com e sem a skill usando a skill skill-creator (os critérios adicionados no fim da primeira rodada ainda não foram rodados), corrigir a skill onde falhar e gravar o relatório em relatorios/copy-chief-iteracao-2.html e .md.

Mantenha o núcleo agnóstico: nada de veterinária em principios.md, revisao.md ou nos canais; o que é do setor fica em setores/. Commit e push ao fim de cada item (git pull --rebase antes), e registre em clientes/aline-franca/andamento/skill.md. Não edite arquivos de clientes além do seu arquivo de andamento.
```

## Frente 4: Perfil no Google

- **Objetivo:** deixar tudo pronto para o Vinícius criar, verificar e alimentar o Perfil da Empresa no Google.
- **Pacotes do plano:** G1 a G5.
- **Arquivos:** `clientes/aline-franca/google/`, `andamento/google.md`.
- **Fase 1 (agora):** `passo-a-passo.md` (como criar o perfil de área de atendimento, com as telas atuais), `roteiro-verificacao.md` (vídeo), `mensagens-avaliacao.md` (pedido de avaliação com espaço para o link e modelos de resposta).
- **Fase 2 (depois da entrevista):** `textos-perfil.md` (categorias, serviços, descrição, horários, área atendida) e as quatro primeiras publicações semanais.
- **Pronto quando:** o Vinícius consegue criar e verificar o perfil só seguindo os arquivos.

**Prompt de início:**
```
Você é o agente da frente 4 (Perfil no Google) do projeto de marketing da Dra. Aline França. Trabalhe no repositório snvinni/marketing-studio.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 4"), clientes/aline-franca/plano.md (seções 1, 3 e 6), metodo/pesquisa.md, metodo/regras-cfmv.md, clientes/aline-franca/perfil.md, clientes/aline-franca/google/README.md e a pasta clientes/aline-franca/andamento/. Veja o git log.

Fase 1 (faça agora): pesquise na Central de Ajuda do Google como está hoje o cadastro e a verificação de empresa de área de atendimento (sem endereço público) no Brasil e escreva, em clientes/aline-franca/google/:
- passo-a-passo.md: criação do perfil, tela por tela, com as escolhas certas para a Aline (categoria principal Veterinário, secundária de pet sitter, endereço oculto, área atendida) e o que não fazer (endereço falso, nome com palavras-chave).
- roteiro-verificacao.md: roteiro do vídeo de verificação para quem não tem fachada (jaleco, maleta, caixa térmica, carteira do CRMV), com o que mostrar em cada trecho.
- mensagens-avaliacao.md: mensagem de WhatsApp para pedir avaliação aos clientes atuais e depois de cada atendimento, e modelos de resposta para avaliação boa, neutra e ruim. Escreva com a skill copy-chief; nada de trocar avaliação por desconto.

Fase 2 (só se perfil.md já disser "Fonte: entrevista de ..."): textos-perfil.md com categorias, lista de serviços, descrição de até 750 caracteres, horários e área atendida, e publicacoes.md com as quatro primeiras publicações semanais, tudo pela skill copy-chief. Se a entrevista ainda não foi feita, pare ao fim da fase 1 e me avise.

Diga com clareza o que eu (Vinícius) preciso fazer à mão e em que ordem. Commit e push ao fim de cada arquivo (git pull --rebase antes) e registre em clientes/aline-franca/andamento/google.md. Não edite perfil.md, a skill nem arquivos de outras frentes.
```

## Frente 5: Instagram

- **Objetivo:** arrumar o perfil e entregar o primeiro mês de conteúdo.
- **Pacotes do plano:** I1 a I6 e K3.
- **Depende de:** frente 1 (usuário do Instagram, voz, serviços confirmados). Não começa antes.
- **Arquivos:** `clientes/aline-franca/instagram/`, `andamento/instagram.md`.
- **Entregas:** `diagnostico.md`, `perfil.md` (nome, bio, destaques), `linha-editorial.md`, `calendario.md` com 8 posts completos (roteiro, legenda, chamada, material a gravar), lista de correções sugeridas para a skill.
- **Pronto quando:** a Aline aprova a bio e os 8 posts.

**Prompt de início:**
```
Você é o agente da frente 5 (Instagram) do projeto de marketing da Dra. Aline França. Trabalhe no repositório snvinni/marketing-studio.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 5"), clientes/aline-franca/plano.md (seções 1, 3 e 7), metodo/pesquisa.md, metodo/regras-cfmv.md, clientes/aline-franca/perfil.md, clientes/aline-franca/entrevista.md, modelos/calendario-instagram.md, a skill em .claude/skills/copy-chief/ e a pasta clientes/aline-franca/andamento/. Veja o git log.

Confira primeiro se perfil.md diz "Fonte: entrevista de ...". Se a entrevista ainda não foi feita, pare e me avise: esta frente depende dela.

Com a entrevista feita, entregue em clientes/aline-franca/instagram/:
1. diagnostico.md: estado atual do perfil dela. Você não tem acesso ao Instagram; me peça capturas de tela do perfil e dos números dos últimos posts e trabalhe a partir delas.
2. perfil.md: nome do perfil, três opções de bio, destaques e o que cada um contém.
3. linha-editorial.md: os quatro pilares (em casa, gatos, orientação, prova), com 5 ideias de post por pilar tiradas das dúvidas e medos reais da entrevista.
4. calendario.md: 8 posts para o primeiro mês, dois por semana, alternando Reels e carrossel, cada um com roteiro ou telas, legenda, chamada e o material que a Aline precisa gravar.

Todo texto é escrito pela skill copy-chief no modo escrever e conferido no modo revisar. Nada de promessa de resultado, "especialista em felinos" ou foto de paciente sem autorização. Anote em andamento/instagram.md o que a skill errou ou deixou a desejar, como pedido para a frente 3. Commit e push ao fim de cada arquivo (git pull --rebase antes). Não edite perfil.md do cliente, a skill nem arquivos de outras frentes.
```

## Frente 6: Operação (medição, parcerias, WhatsApp e anúncios)

- **Objetivo:** o que sustenta o dia a dia e, depois, os anúncios.
- **Pacotes do plano:** M1, R1 a R4, P1 e P2.
- **Arquivos:** `clientes/aline-franca/operacao/`, `clientes/aline-franca/anuncios/`, `andamento/operacao.md`.
- **Fase 1 (agora):** `medicao.md` e uma planilha modelo (pedidos por origem, atendimentos, avaliações, gasto); `whatsapp-business.md` (configuração, saudação, respostas rápidas, etiquetas de origem, lembrete de reforço de vacina); `parcerias.md` (tipos de parceiro em Campinas, mensagem de abordagem, material de apresentação agnóstico do `line-vet` (`materiais/`), texto do cartão com QR code).
- **Fase 2 (site no ar e 10 avaliações):** `anuncios/google-ads.md` (campanha, palavras, negativas, anúncios, orçamento de R$ 300) e a rotina de revisão semanal.
- **Pronto quando:** o Vinícius consegue configurar o WhatsApp Business, abordar parceiros e preencher a planilha só com os arquivos.

**Prompt de início:**
```
Você é o agente da frente 6 (Operação) do projeto de marketing da Dra. Aline França. Trabalhe no repositório snvinni/marketing-studio.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 6"), clientes/aline-franca/plano.md (seções 1, 3, 8, 9 e 10), metodo/pesquisa.md, metodo/regras-cfmv.md, clientes/aline-franca/perfil.md e a pasta clientes/aline-franca/andamento/. Veja o git log.

Fase 1 (faça agora), em clientes/aline-franca/operacao/:
- medicao.md e uma planilha modelo (.xlsx): pedidos por semana e por origem, atendimentos fechados, avaliações novas, números do perfil no Google, gasto em anúncios, e como decidir todo mês o que reforçar e o que cortar.
- whatsapp-business.md: passo a passo de configuração, catálogo de serviços, mensagem de saudação e de ausência, respostas rápidas, etiquetas por origem do contato e a lista de transmissão para lembrete de reforço de vacina. Textos pela skill copy-chief.
- parcerias.md: quem abordar em Campinas (banho e tosa, pet shops sem veterinário, adestradores, hotéis), mensagem de abordagem, proposta de indicação cruzada sem comissão que fira o código de ética, e o texto de um cartão com QR code para o WhatsApp.

Onde depender de dado que o perfil.md ainda não confirma (bairros, preços, horários), use [CONFIRMAR: ...] e liste a pendência.

Fase 2 (só quando eu disser que o site está no ar e o perfil no Google tem 10 avaliações): clientes/aline-franca/anuncios/google-ads.md com uma campanha de pesquisa para Campinas, palavras em correspondência exata ou de frase, lista de negativas, três anúncios dentro das regras do CFMV, orçamento de até R$ 300 por mês e a rotina de revisão semanal.

Commit e push ao fim de cada arquivo (git pull --rebase antes) e registre em clientes/aline-franca/andamento/operacao.md. Não edite perfil.md, a skill nem arquivos de outras frentes.
```

---

## Ordem sugerida para o Vinícius

1. **Hoje:** abrir as frentes 1, 2, 3, 4 e 6 (cinco sessões). Só a frente 1 exige você na conversa; as outras trabalham sozinhas.
2. **Entrevista feita:** mandar o pedido de fotos para a Aline; dizer "a entrevista foi feita, siga para a fase 2" nas sessões das frentes 2 e 4 (ou abrir sessões novas com o mesmo prompt); abrir a frente 5.
3. **Em paralelo, à mão:** registrar o domínio, criar o perfil no Google seguindo a frente 4, pedir as avaliações.
4. **Site no ar e 10 avaliações:** avisar a frente 6 para a fase 2 (anúncios).

Se preferir tocar por partes, a ordem mínima é: frente 1 → frente 2 → frente 4. As demais podem esperar sem travar nada.
