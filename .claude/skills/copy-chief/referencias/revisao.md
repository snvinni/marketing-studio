# Checklist de revisão

Use na ordem. Cada problema encontrado recebe uma gravidade.

## Gravidades

| Gravidade | O que é | Efeito no veredito |
|---|---|---|
| **BLOQUEANTE** | Fere regra do setor ou da lei; promessa de resultado; título ou certificação que o cliente não tem; foto ou depoimento sem autorização; dado pessoal de terceiro exposto | Não pode publicar. AJUSTAR se dá para corrigir trocando trechos; REFAZER se a ideia do texto depende do problema |
| **FATO** | Afirma algo que não está confirmado no perfil (preço, região, horário, formação, número, experiência) | Não pode publicar até confirmar ou trocar por `[CONFIRMAR]` |
| **VOZ** | Não soa como o cliente; usa palavra proibida do perfil; vício de texto de IA | AJUSTAR |
| **CLAREZA** | Mais de uma ideia; abertura fraca; sem chamada ou com chamada vaga; frase longa; erro de português; fora do formato ou limite do canal | AJUSTAR |

## Perguntas, em ordem

### 1. Regras (BLOQUEANTE)
- O texto fere alguma regra do arquivo do setor? Confira a lista de proibições item por item.
- Promete resultado, cura, garantia, "sem dor", "sem estresse nenhum", "100%"?
- Usa título, especialidade ou selo que o perfil não confirma?
- Mostra paciente, cliente ou depoimento sem autorização registrada?
- Expõe dado de outra pessoa (nome completo, endereço, rosto)?

### 2. Fatos (FATO)
- Cada número, preço, prazo, lugar e credencial está no perfil como confirmado?
- Algum fato foi "arredondado" para parecer melhor ("anos de experiência", "centenas de clientes")?
- Todo fato não confirmado está marcado `[CONFIRMAR]` no próprio texto, em cada versão e em cada parte (roteiro, tela, legenda)? Estar só na lista de pendências não basta.

### 3. Ideia e leitor (CLAREZA)
- Dá para dizer a ideia em uma frase?
- A primeira frase é sobre o leitor e faz querer ler a segunda?
- Tem uma chamada clara, e só uma? Se há mais de uma versão, cada uma tem a sua?
- Traz a identificação que o setor exige no canal (nome, registro), em cada versão?

### 4. Voz (VOZ)
- Soa como as frases de exemplo do perfil? Usa as palavras dele?
- Tem algum vício da lista do item 8 de `principios.md`?
- Tem palavra da lista "evitar" do perfil?

### 5. Canal (CLAREZA)
- Respeita os limites e o formato de `canais/<canal>.md` (tamanho, estrutura, hashtags, emoji)?

### 6. Português (CLAREZA)
- Ortografia, acentuação, crase, concordância.

## Como escrever cada problema
`[GRAVIDADE] "trecho exato" — por que é problema — como corrigir`

Exemplo:
`[BLOQUEANTE] "você vai perder 10 kg em um mês" — promessa de resultado é vedada pela regra do conselho do setor (cite a norma do arquivo do setor) — trocar por "montamos juntos um treino que cabe na sua rotina e acompanhamos a cada semana"`
