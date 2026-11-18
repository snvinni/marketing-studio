# Site: briefing

O código do site fica no repositório **`snvinni/line-vet`** (branch `ccr-ddd55fa2-btz5yk` até o primeiro merge). Este arquivo diz o que construir; os pacotes de trabalho detalhados estão na seção 5 de `../plano.md` (PT-S1 a PT-S12).

## Estado atual (17/11/2026, depois da entrevista)
- **Fase 2 feita:** as nove páginas têm os textos da entrevista (ver `textos.md`), sem nenhum `[CONFIRMAR]`. Faltam as fotos (fase 3), a escolha da paleta e tirar as marcas de prévia (faixa de rascunho, `noindex`, seletor de cores). A conferência `PUBLICAR=1` lista isso.
- O nome público é "Aline França", **sem "Dra."** (pedido dela).

## Estado antes da entrevista (17/11/2026)
- **Na branch `ccr-ddd55fa2-btz5yk`:** `index.html` e `pet-sitter.html` (o pet sitter com a calculadora), estilo e scripts em `assets/`, fontes no próprio site, guia de estilo (`guia-de-estilo.html`, fora do ar).
- **Na branch `previa/site-completo`:** prévia das nove páginas (as oito do plano e a de privacidade), com textos provisórios marcados `[CONFIRMAR]`. Não vai ao ar sem o ok do Vinícius.
- `materiais/`: apresentação da Aline para mandar como arquivo a qualquer contato, sem citar lugar (fora do deploy).
- O site não cita condomínio nem residencial (decisão do Vinícius em 17/11/2026).
- Sem deploy, sem domínio.

## Para onde vai
Site com veterinária a domicílio como serviço principal, uma página para gatos e o pet sitter como complemento. Oito páginas: início, veterinária a domicílio, vacinas em casa, gatos, pet sitter, sobre, atendimento, dúvidas. Mais uma de privacidade (PT-S11).

## Regras para quem for construir
- Textos vêm de `../perfil.md`. Nada sem confirmação vai ao ar; use `[CONFIRMAR]` no rascunho.
- Textos escritos ou revisados com a skill copy-chief (canal `site`).
- Manter identidade visual e o funcionamento sem JavaScript (ver seção 2 de `../plano.md`).
- Seguir `metodo/regras-cfmv.md`: nome e CRMV no rodapé, lista honesta do que não é feito em casa.

## Andamento
Ver tabela na seção 11 de `../plano.md`.

## Decisões de design (17/11/2026)
Base: `pesquisa-design.md`.
- **Cor por serviço:** azul na veterinária e nas páginas gerais; terracota no pet sitter.
- **Celular:** os dois serviços sempre à vista no cabeçalho. Barra de WhatsApp aparece depois do primeiro botão e some no bilhete final.
- **Sem cara de SaaS:** nada de cartões de serviço em grade, selos, contadores ou bolha flutuante.
- **Avaliações:** só link para o Google.
- **Área atendida:** uma página de atendimento com os bairros em texto, sem páginas por bairro.
- **CRMV:** no rodapé de todas as páginas.
