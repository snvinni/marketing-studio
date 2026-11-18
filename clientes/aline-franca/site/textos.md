# Site: textos da fase 2 (skill copy-chief, canal site)

Escritos em 17/11/2026 a partir de `perfil.md` e `entrevista.md` (entrevista de 17/11/2026), com o núcleo, o setor `veterinaria-br` e o canal `site` da skill. Os textos estão no `line-vet` (branch `ccr-ddd55fa2-btz5yk`); aqui ficam o raciocínio e o que falta. A fonte de verdade continua sendo o perfil.

## Revisão de 18/11/2026: textos diretos (pedido do Vinícius)
O Vinícius achou os textos da fase 2 poéticos e com detalhe que não ajuda o tutor (o exemplo dele: "a vacina chega em caixa térmica, com termômetro"). Ele pediu texto direto e explicativo, mais serviços citados e os sites de referência dele como base (ver `concorrentes.md`). As nove páginas foram reescritas. O que vale agora:
- **Cada frase responde a uma pergunta do tutor:** o que é, se serve para o meu pet, como marco, onde atende, quanto custa, o que acontece depois. Saíram caixa térmica, termômetro, maleta, "com quem entende de bicho", "cantinho" e as metáforas nos títulos.
- **H1 com o serviço e o lugar:** "Veterinária a domicílio em Campinas, Valinhos e Vinhedo"; "Consulta veterinária em casa, em Campinas"; "Vacinas para cães e gatos em casa"; "Veterinária para gatos, na sua casa"; "Pet sitter com olhar de veterinária"; "Onde eu atendo e como marcar"; "Perguntas frequentes".
- **Títulos de seção dizem o assunto:** "O que eu faço na sua casa", "A consulta em casa, passo a passo", "As vacinas que eu aplico", "Perguntas frequentes".
- **Grade de serviços** no início, na veterinária e em gatos. São 13 itens, todos da entrevista: consulta clínica, check-up de rotina, filhotes, pets idosos, doença crônica, vacinas, vermifugação, medicação injetável, curativos, atestado de saúde, atestado para viagem, cuidados paliativos e eutanásia em casa. O pet sitter aparece à parte.
- **Vacinas:** um cartão por espécie. Cães: V8 ou V10, antirrábica, gripe canina e giárdia. Gatos: V3, V4 ou V5 e antirrábica. O passo a passo é: manda a foto da carteira, combinamos, aplico em casa.
- **Dúvidas:** 12 perguntas do jeito que o tutor pergunta. Cada resposta começa respondendo ("Sim", "Não", "Depende").
- **Tamanho:** as páginas não ficaram mais curtas. O início foi de 488 para 661 palavras, porque ganhou a grade de serviços e quatro dúvidas. Vacinas, gatos e dúvidas também cresceram; Sobre e veterinária encolheram. O que saiu foi a voltas; o que entrou é informação.
- **Para a Aline validar, além da lista abaixo:**
  - "Check-up de rotina" como nome de serviço;
  - giárdia listada como vacina de cães;
  - "Me manda uma foto da carteira de vacinação" como primeiro passo da vacina;
  - "Dá para aproveitar a visita da vacina para uma consulta? Sim.";
  - "Gato é uma das minhas paixões".

Os briefings da fase 2, mais abaixo, ficam como histórico; os títulos e as aberturas citados neles foram trocados.

## Regras que valeram em todas as páginas
- Nome: **"Aline França", sem "Dra."**; "Aline" em primeira pessoa. CRMV-SP 66561 no rodapé de toda página e no Sobre.
- Cidades: **Campinas, Valinhos e Vinhedo**, "consulte o seu bairro", sem lista de bairros.
- **Nunca publicado:** horário de atendimento (só "com hora marcada"), preço de consulta ou vacina ("valores pelo WhatsApp"), número de clientes, nome de empresa e locais onde trabalhou, clínica parceira, coleta de exames, fluidoterapia, microchip, urgência, cavalos, a história do Meia-Noite.
- **Palavras proibidas:** "Dra.", "especialista", "bebê", "filho", "pais de pet", "humano", diminutivos e gírias. Nenhum emoji.
- Pedidos só por WhatsApp e formulário; **sem botão de ligar**.
- Desconto só como "valor reduzido", sem percentual. Pós-graduação dita como "pós-graduação em urgências e emergências intensivas", nunca como título.
- Tom: acolhedora, calma, cuidadosa. Frases curtas, em primeira pessoa. Frases dela, palavra por palavra, só no Sobre.
- Cada regra acima é conferida por teste (`tests/conteudo.spec.js`) nas nove páginas.

## Página por página
Cada bloco traz o briefing de cinco linhas da skill, o título e a descrição (limites do canal: ≤ ~60 e 120 a 155 caracteres), a abertura em duas versões e a escolha.

### Início (`/`)
- **Objetivo:** o tutor chama no WhatsApp. **Público:** tutor de Campinas, Valinhos ou Vinhedo, com gato que sofre fora de casa, pet idoso ou sem tempo e carro. **Uma ideia:** a consulta vem até a casa e acontece sem pressa. **Prova:** consulta e vacina em casa; explica tudo; manejo gentil com gato; CRMV. **Chamada:** WhatsApp.
- Título (46): "Veterinária em casa em Campinas | Aline França". Descrição (127): "Consulta e vacina para cães e gatos na sua casa, em Campinas, Valinhos e Vinhedo, com calma e sem pressa. Marque pelo WhatsApp."
- **A:** "Veterinária em casa, com calma e sem pressa." **B:** "Seu pet no conforto de casa. Eu vou até vocês." **Escolhida: A.** Diz o serviço (importante para quem busca) e leva o que ela não abre mão; a B fica para o Instagram.
- Subtítulo: "Oi, eu sou a Aline, médica-veterinária. Atendo cães e gatos na sua casa, pelo conforto deles, e explico tudo com calma." Botão: "Chamar no WhatsApp".

### Veterinária a domicílio (`/veterinaria-a-domicilio`)
- **Uma ideia:** a consulta vem até a casa, sem pressa. **Prova:** a lista honesta do que faz e não faz em casa; a maleta; o prontuário digital. **Chamada:** marcar pelo WhatsApp ou formulário.
- Título (50) e descrição (126): "Veterinária a domicílio em Campinas | Aline França"; "Consulta para cães e gatos na sua casa, em Campinas, Valinhos e Vinhedo. Veja o que faço em casa e quando o caso pede clínica."
- **A:** "A consulta vem até a sua casa, sem pressa." **B:** "Consulta em casa, no tempo do seu pet." **Escolhida: A** (diz de onde vem a consulta).
- "Na clínica": exames de sangue, urina e imagem; internação; cirurgia e anestesia geral; emergências graves. Encaminha para "a clínica de confiança de vocês ou um hospital veterinário 24 horas".

### Vacinas em casa (`/vacinas-em-casa`)
- **Uma ideia:** a vacina chega com cuidado e a carteira sai preenchida. **Prova:** caixa térmica com termômetro; as vacinas que aplica.
- Título (42) e descrição (141): "Vacinas em casa em Campinas | Aline França"; "Vacina para cães e gatos aplicada na sua casa, em Campinas, Valinhos e Vinhedo, com a carteira de vacinação preenchida. Marque pelo WhatsApp."
- **A:** "Vacina em dia, sem sair de casa." **B:** "A vacina vai até o seu pet." **Escolhida: A.**
- **Ficou de fora de propósito** (não está na entrevista): tabela do calendário de vacinas, lembrete de reforço pelo WhatsApp, "examino antes de vacinar".

### Gatos (`/gatos`)
- **Uma ideia:** o gato fica em casa e a consulta é no tempo dele. **Prova:** manejo gentil (toalha, pouca contenção, voz baixa; não insiste se estressar); as três gatas resgatadas.
- Título (53) e descrição (128): "Gatos: veterinária em casa em Campinas | Aline França"; "Consulta e vacina para gatos na sua casa, com manejo gentil e sem pressa, em Campinas, Valinhos e Vinhedo. Me chame no WhatsApp."
- **A:** "Seu gato fica em casa. Eu vou até ele." **B:** "Para o gato, ficar em casa faz diferença." **Escolhida: A** (é a frase mais perto da voz dela).
- **Cuidado de setor:** nada de "especialista em felinos" nem "Cat Friendly"; a página diz "atendimento pensado para gatos". Saíram "como preparar a casa" e "ele escolhe o lugar", que não vieram dela.

### Sobre (`/sobre`)
- **Uma ideia:** quem é a Aline e por que atende em casa. **Prova:** as frases dela; UniFAJ 2023; pós; CRMV; as gatas; a Milka.
- Título (45) e descrição (114): "Sobre a Aline França, veterinária em Campinas"; "Conheça a Aline França, médica-veterinária que atende cães e gatos na casa deles, em Campinas, Valinhos e Vinhedo."
- Frases dela, sem retoque: "Sempre amei os animais e tive uma infância repleta deles."; "Comecei aos 14 anos cursos de auxiliar de veterinária e nunca me desviei desse caminho."; "O que me motiva cada vez mais é poder estar perto dessas almas tão queridas, que nos ensinam cada dia mais."
- A Milka só com o que foi dito: resgatada, "conquistou todos nós", já faleceu, inspirou o logo. O trabalho atual aparece só como "também trabalho na área de medicamentos veterinários".

### Atendimento (`/atendimento`) e Dúvidas (`/duvidas`)
- **Atendimento:** as três cidades, "consulte o seu bairro", com hora marcada (às vezes no mesmo dia, se houver vaga), remarcar é só avisar, deslocamento varia com a distância, pagamento, formulário. Título (56): "Onde atendo: Campinas, Valinhos e Vinhedo | Aline França".
- **Dúvidas:** as três que os tutores fazem (gato que não deixa pegar; quanto custa e deslocamento; exame e cirurgia), mais cidade, pagamento, remarcar, vacina segura, cuidados paliativos e emergência; e as do pet sitter, da página dela. Título (33): "Dúvidas frequentes | Aline França".

### Pet sitter (`/pet-sitter`) e Privacidade (`/privacidade`)
- **Pet sitter:** texto e preços como estavam (do PDF dela). Mudou só "valor reduzido" no lugar de "50% de desconto" e as três cidades.
- **Privacidade:** o que o site faz hoje (não guarda nada, sem cookies, sem ferramenta de medição). **Atualizar quando a medição for ligada.**

## Revisão pelo checklist da skill (`referencias/revisao.md`)
- **Bloqueante:** nenhum. Sem promessa de resultado, sem título, sem imagem de paciente, sem desconto em destaque, sem "especialista".
- **Fato:** todo fato está em `perfil.md`. Frases **minhas**, derivadas do que ela disse, que valem uma leitura dela (ver abaixo).
- **Voz:** frases curtas, primeira pessoa, sem vícios de texto automático; sem as palavras proibidas. As palavras que ela gosta ainda não existem no perfil.
- **Clareza:** uma chamada por página; abertura responde quem, o quê, onde e como chamar (WhatsApp na primeira tela em 390 px).
- **Canal:** títulos de 26 a 56 caracteres e descrições de 109 a 149 (limites do canal: ~60 e 120 a 155; só a de Privacidade, com 109, fica abaixo dos 120, por ser página de apoio); CRMV no rodapé de todas as páginas.

## O que a Aline precisa ler com atenção (para validar)
1. **Cuidados paliativos e eutanásia:** aparecem na lista da veterinária e numa dúvida ("Faço. Me chama no WhatsApp, e a gente conversa com calma…"). A frase é minha.
2. **A Milka:** "A gata que inspirou o meu logo se chamava Milka. Foi resgatada, conquistou todos nós e já faleceu."
3. **Medicamentos:** "Hoje também trabalho na área de medicamentos veterinários."
4. **Vacinas:** "Gripe canina" e "V8 ou V10" como vacinas de cães; "giárdia" sem espécie.
5. **"Atendo todos na mesma visita"** (casa com vários animais) e **"Doença crônica: acompanhamento em casa, com receita e prontuário digital"**.
6. **A lista "Na clínica":** exames de sangue, urina e imagem; internação; cirurgia e anestesia geral; emergências graves.
7. **Gato:** "Depende do gato…" como primeira resposta ao "meu gato não deixa ninguém pegar".

## Pendências que sobraram (nenhuma é `[CONFIRMAR]` no texto)
| Pendência | Quem |
|---|---|
| Fotos (8 espaços de foto e a galeria do Sobre; legendas com os nomes das gatas quando as fotos chegarem) | Aline (frente 1 pede); depois, fase 3 |
| Calendário de vacinas (idades e intervalos) para uma tabela, e se ela quer oferecer lembrete de reforço | Aline |
| Dicas para o tutor preparar a casa antes da visita de um gato (opcional; ela escreve ou aprova) | Aline |
| Instituição e ano da pós, idades das gatas: não são publicados; só entram se ela quiser | Aline |
| Palavras que ela gosta (para afinar a voz) | Aline |
| Bloco de avaliações do Google na página inicial | volta quando o perfil existir (frente 4) |
| Atualizar o texto de privacidade quando a medição de cliques for ligada | frente 2 |
| Registrar `alinefranca.vet.br` (no CPF da Aline; conferir no registro.br o que o `.vet.br` pede para comprovar o CRMV). O domínio já está no site | Vinícius |
