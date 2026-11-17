"""Gera a planilha modelo de medição da Dra. Aline França (frente 6)."""
import sys
from datetime import date, timedelta

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

saida = sys.argv[1]

ORIGENS = [
    "Perfil no Google", "Site", "Anúncio Google", "Instagram",
    "Indicação de cliente", "Parceiro", "Cartão ou ímã",
    "Já é cliente", "Não sei",
]
SERVICOS = ["Consulta em casa", "Vacina em casa", "Pet sitter", "Outro"]
STATUS = ["Sim", "Não", "Aguardando"]
N_PEDIDOS = 600          # linhas preparadas na aba Pedidos
N_SEMANAS = 26
INICIO = date(2026, 11, 16)  # segunda-feira
MESES = [date(2026, 11, 1), date(2026, 12, 1), date(2027, 1, 1), date(2027, 2, 1),
         date(2027, 3, 1), date(2027, 4, 1), date(2027, 5, 1)]

AZUL = "2F6F87"
CREME = "F6F1E9"
CINZA = "EDEDED"
cab_font = Font(bold=True, color="FFFFFF")
cab_fill = PatternFill("solid", fgColor=AZUL)
formula_fill = PatternFill("solid", fgColor=CINZA)
total_fill = PatternFill("solid", fgColor=CREME)
fino = Side(style="thin", color="CCCCCC")
borda = Border(left=fino, right=fino, top=fino, bottom=fino)
quebra = Alignment(wrap_text=True, vertical="top")

wb = Workbook()

# ---------- Leia-me ----------
ws = wb.active
ws.title = "Leia-me"
linhas = [
    ("Planilha de medição: Dra. Aline França", True),
    ("Pergunta que ela responde: de onde vêm os pedidos que viram atendimento?", False),
    ("", False),
    ("TODO DIA (2 minutos)", True),
    ("Aba Pedidos: uma linha para cada pedido novo que chegou. Preencha Data, Tutor (só o primeiro nome), Pet, Origem, Serviço e, quando souber, Fechou?.", False),
    ("A Origem é a mesma etiqueta usada no WhatsApp Business. Se a origem for Parceiro, escreva qual em Detalhe.", False),
    ("", False),
    ("TODA SEGUNDA-FEIRA (10 minutos)", True),
    ("Aba Semana, na linha da semana que passou: avaliações novas e nota no Google, números do perfil no Google (Desempenho) e gasto em anúncios.", False),
    ("O resto da linha (pedidos por origem, fechados, custo por pedido) se calcula sozinho.", False),
    ("", False),
    ("PRIMEIRA SEGUNDA-FEIRA DO MÊS (15 minutos)", True),
    ("Aba Mês: para cada origem, veja Pedidos e Fechados do mês anterior, anote Horas gastas e Gasto (cartões, impressão) e escreva uma Decisão.", False),
    ("Regras de decisão: arquivo operacao/medicao.md, seção 2.", False),
    ("", False),
    ("CUIDADOS", True),
    ("Células em cinza têm fórmula: não digite nelas.", False),
    ("Só primeiro nome do tutor e nome do pet. Nada de telefone, endereço ou sobrenome.", False),
    ("Precisa de outra origem? Acrescente na aba Listas e peça à frente 6 para atualizar as fórmulas.", False),
]
for i, (texto, negrito) in enumerate(linhas, start=1):
    c = ws.cell(row=i, column=1, value=texto)
    c.font = Font(bold=negrito, size=14 if i == 1 else 11, color=AZUL if negrito else "2B2420")
    c.alignment = Alignment(wrap_text=True, vertical="top")
ws.column_dimensions["A"].width = 110

# ---------- Listas ----------
wl = wb.create_sheet("Listas")
for col, (titulo, itens) in enumerate([("Origem", ORIGENS), ("Serviço", SERVICOS), ("Fechou?", STATUS)], start=1):
    wl.cell(row=1, column=col, value=titulo).font = Font(bold=True)
    for r, item in enumerate(itens, start=2):
        wl.cell(row=r, column=col, value=item)
    wl.column_dimensions[get_column_letter(col)].width = 24
rng_origem = f"Listas!$A$2:$A${len(ORIGENS) + 1}"
rng_servico = f"Listas!$B$2:$B${len(SERVICOS) + 1}"
rng_status = f"Listas!$C$2:$C${len(STATUS) + 1}"


def cabecalho(ws, titulos, larguras):
    for col, (t, w) in enumerate(zip(titulos, larguras), start=1):
        c = ws.cell(row=1, column=col, value=t)
        c.font = cab_font
        c.fill = cab_fill
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = borda
        ws.column_dimensions[get_column_letter(col)].width = w
    ws.row_dimensions[1].height = 45
    ws.freeze_panes = "B2"


# ---------- Pedidos ----------
wp = wb.create_sheet("Pedidos", 1)
tit_p = ["Data", "Semana (segunda)", "Mês", "Tutor (primeiro nome)", "Pet", "Origem",
         "Detalhe (qual parceiro)", "Serviço", "Fechou?", "Valor (R$)", "Observação"]
cabecalho(wp, tit_p, [12, 14, 11, 18, 14, 20, 28, 18, 12, 12, 40])
for r in range(2, N_PEDIDOS + 2):
    wp.cell(row=r, column=1).number_format = "DD/MM/YYYY"
    b = wp.cell(row=r, column=2, value=f'=IF(A{r}="","",A{r}-WEEKDAY(A{r},2)+1)')
    b.number_format = "DD/MM/YYYY"
    c = wp.cell(row=r, column=3, value=f'=IF(A{r}="","",DATE(YEAR(A{r}),MONTH(A{r}),1))')
    c.number_format = "MMM/YYYY"
    for col in (2, 3):
        wp.cell(row=r, column=col).fill = formula_fill
    wp.cell(row=r, column=10).number_format = '"R$" #,##0.00'
dv = DataValidation(type="list", formula1=f"={rng_origem}", allow_blank=True)
dv.add(f"F2:F{N_PEDIDOS + 1}")
dv2 = DataValidation(type="list", formula1=f"={rng_servico}", allow_blank=True)
dv2.add(f"H2:H{N_PEDIDOS + 1}")
dv3 = DataValidation(type="list", formula1=f"={rng_status}", allow_blank=True)
dv3.add(f"I2:I{N_PEDIDOS + 1}")
dvd = DataValidation(type="date", operator="greaterThan", formula1="DATE(2026,1,1)", allow_blank=True,
                     error="Digite uma data, por exemplo 18/11/2026.", showErrorMessage=True)
dvd.add(f"A2:A{N_PEDIDOS + 1}")
for d in (dv, dv2, dv3, dvd):
    wp.add_data_validation(d)
# exemplo apagável
wp["A2"] = INICIO + timedelta(days=1)
wp["D2"] = "Exemplo"
wp["E2"] = "Mimi"
wp["F2"] = "Site"
wp["H2"] = "Vacina em casa"
wp["I2"] = "Aguardando"
wp["K2"] = "Linha de exemplo: apague antes de começar."

P = f"Pedidos!$B$2:$B${N_PEDIDOS + 1}"      # semana
PM = f"Pedidos!$C$2:$C${N_PEDIDOS + 1}"     # mês
PO = f"Pedidos!$F$2:$F${N_PEDIDOS + 1}"     # origem
PF = f"Pedidos!$I$2:$I${N_PEDIDOS + 1}"     # fechou

# ---------- Semana ----------
wsem = wb.create_sheet("Semana", 2)
tit_s = (["Semana (segunda)", "Mês"] + [f"Pedidos: {o}" for o in ORIGENS] +
         ["Total de pedidos", "Atendimentos fechados", "Taxa de fechamento",
          "Avaliações novas no Google", "Nota média no Google",
          "Google: visualizações do perfil", "Google: ligações", "Google: cliques no site",
          "Google: conversas ou WhatsApp",
          "Gasto em anúncio (R$)", "Custo por pedido do anúncio", "Fechados do anúncio",
          "Custo por atendimento do anúncio", "Observação"])
larg_s = [13, 11] + [12] * len(ORIGENS) + [11, 12, 11, 12, 11, 13, 11, 11, 13, 12, 13, 11, 13, 36]
cabecalho(wsem, tit_s, larg_s)
wsem.freeze_panes = "C2"
n_o = len(ORIGENS)
col_total = 3 + n_o            # Total de pedidos
col_fech = col_total + 1
col_taxa = col_total + 2
col_aval = col_total + 3
col_gasto = col_total + 9
col_cpp = col_total + 10
col_fech_ads = col_total + 11
col_cpa = col_total + 12
idx_ads = 3 + ORIGENS.index("Anúncio Google")
L = get_column_letter
for i in range(N_SEMANAS):
    r = i + 2
    a = wsem.cell(row=r, column=1, value=INICIO + timedelta(weeks=i))
    a.number_format = "DD/MM/YYYY"
    m = wsem.cell(row=r, column=2, value=f"=DATE(YEAR(A{r}),MONTH(A{r}),1)")
    m.number_format = "MMM/YYYY"
    m.fill = formula_fill
    for j, o in enumerate(ORIGENS):
        col = 3 + j
        c = wsem.cell(row=r, column=col, value=f'=COUNTIFS({P},$A{r},{PO},"{o}")')
        c.fill = formula_fill
    wsem.cell(row=r, column=col_total, value=f"=SUM({L(3)}{r}:{L(2 + n_o)}{r})").fill = formula_fill
    wsem.cell(row=r, column=col_fech, value=f'=COUNTIFS({P},$A{r},{PF},"Sim")').fill = formula_fill
    t = wsem.cell(row=r, column=col_taxa, value=f'=IF({L(col_total)}{r}=0,"",{L(col_fech)}{r}/{L(col_total)}{r})')
    t.fill = formula_fill
    t.number_format = "0%"
    wsem.cell(row=r, column=col_aval + 1).number_format = "0.0"
    wsem.cell(row=r, column=col_gasto).number_format = '"R$" #,##0.00'
    c = wsem.cell(row=r, column=col_cpp,
                  value=f'=IF(OR({L(col_gasto)}{r}="",{L(idx_ads)}{r}=0),"",{L(col_gasto)}{r}/{L(idx_ads)}{r})')
    c.fill = formula_fill
    c.number_format = '"R$" #,##0.00'
    c = wsem.cell(row=r, column=col_fech_ads,
                  value=f'=COUNTIFS({P},$A{r},{PO},"Anúncio Google",{PF},"Sim")')
    c.fill = formula_fill
    c = wsem.cell(row=r, column=col_cpa,
                  value=f'=IF(OR({L(col_gasto)}{r}="",{L(col_fech_ads)}{r}=0),"",{L(col_gasto)}{r}/{L(col_fech_ads)}{r})')
    c.fill = formula_fill
    c.number_format = '"R$" #,##0.00'
S_MES = f"Semana!$B$2:$B${N_SEMANAS + 1}"
S_AVAL = f"Semana!${L(col_aval)}$2:${L(col_aval)}${N_SEMANAS + 1}"
S_GASTO = f"Semana!${L(col_gasto)}$2:${L(col_gasto)}${N_SEMANAS + 1}"

# ---------- Mês ----------
wm = wb.create_sheet("Mês", 3)
tit_m = ["Mês", "Origem", "Pedidos", "Atendimentos fechados", "Taxa de fechamento",
         "Horas gastas", "Gasto (R$)", "Custo por atendimento", "Avaliações novas no Google", "Decisão para o mês seguinte"]
cabecalho(wm, tit_m, [11, 20, 10, 12, 11, 10, 12, 13, 12, 60])
wm.freeze_panes = "C2"
r = 2
for mes in MESES:
    primeira = r
    for o in ORIGENS + ["Total do mês"]:
        wm.cell(row=r, column=1, value=mes).number_format = "MMM/YYYY"
        wm.cell(row=r, column=2, value=o)
        total = o == "Total do mês"
        if total:
            f_ped = f"=SUM(C{primeira}:C{r - 1})"
            f_fech = f"=SUM(D{primeira}:D{r - 1})"
            f_horas = f"=SUM(F{primeira}:F{r - 1})"
            f_gasto = f"=SUM(G{primeira}:G{r - 1})"
            wm.cell(row=r, column=6, value=f_horas).fill = formula_fill
            g = wm.cell(row=r, column=7, value=f_gasto)
            g.fill = formula_fill
            av = wm.cell(row=r, column=9, value=f"=SUMIFS({S_AVAL},{S_MES},$A{r})")
            av.fill = formula_fill
        else:
            f_ped = f'=COUNTIFS({PM},$A{r},{PO},$B{r})'
            f_fech = f'=COUNTIFS({PM},$A{r},{PO},$B{r},{PF},"Sim")'
            if o == "Anúncio Google":
                g = wm.cell(row=r, column=7, value=f"=SUMIFS({S_GASTO},{S_MES},$A{r})")
                g.fill = formula_fill
        wm.cell(row=r, column=3, value=f_ped).fill = formula_fill
        wm.cell(row=r, column=4, value=f_fech).fill = formula_fill
        tx = wm.cell(row=r, column=5, value=f'=IF(C{r}=0,"",D{r}/C{r})')
        tx.fill = formula_fill
        tx.number_format = "0%"
        wm.cell(row=r, column=7).number_format = '"R$" #,##0.00'
        cpa = wm.cell(row=r, column=8, value=f'=IF(OR(G{r}="",G{r}=0,D{r}=0),"",G{r}/D{r})')
        cpa.fill = formula_fill
        cpa.number_format = '"R$" #,##0.00'
        wm.cell(row=r, column=10).alignment = quebra
        if total:
            for col in range(1, 11):
                c = wm.cell(row=r, column=col)
                c.font = Font(bold=True)
                if col in (1, 2, 10):
                    c.fill = total_fill
        r += 1

# ---------- Reforços ----------
wr = wb.create_sheet("Reforços", 4)
tit_r = ["Tutor (primeiro nome)", "Pet", "Cão ou gato", "Vacina", "Data da dose",
         "Mês do próximo reforço", "Aceitou o lembrete?", "Lembrete enviado em", "Reforço marcado?", "Observação"]
cabecalho(wr, tit_r, [18, 14, 11, 22, 12, 14, 12, 14, 12, 36])
for r in range(2, 302):
    wr.cell(row=r, column=5).number_format = "DD/MM/YYYY"
    wr.cell(row=r, column=6).number_format = "MMM/YYYY"
    wr.cell(row=r, column=8).number_format = "DD/MM/YYYY"
dv_sn = DataValidation(type="list", formula1='"Sim,Não"', allow_blank=True)
dv_sn.add("G2:G301")
dv_sn.add("I2:I301")
dv_esp = DataValidation(type="list", formula1='"Cão,Gato,Outro"', allow_blank=True)
dv_esp.add("C2:C301")
wr.add_data_validation(dv_sn)
wr.add_data_validation(dv_esp)
nota = wr.cell(row=1, column=12, value=(
    "Mês do próximo reforço: a Aline diz qual (depende da vacina). Digite o dia 1 do mês, por exemplo 01/03/2027. "
    "Para ver quem vence no mês seguinte, use o filtro da coluna F. Só mande lembrete para quem tem 'Sim' na coluna G."))
nota.alignment = quebra
wr.column_dimensions["L"].width = 60
wr.auto_filter.ref = "A1:J301"
wb["Leia-me"].append([""])
wb["Leia-me"].append(["REFORÇO DE VACINA"])
wb["Leia-me"].cell(row=wb["Leia-me"].max_row, column=1).font = Font(bold=True, color=AZUL)
wb["Leia-me"].append(["Aba Reforços: um pet por linha depois de cada vacina. Na última semana do mês, filtre quem vence no mês seguinte e mande o lembrete (operacao/whatsapp-business.md, seção 9)."])

# ---------- Parceiros ----------
wpa = wb.create_sheet("Parceiros", 5)
TIPOS = ["Banho e tosa", "Pet shop", "Adestrador", "Hotel ou creche", "Outro"]
tit_pa = ["Nome (igual ao Detalhe da aba Pedidos)", "Tipo", "Bairro", "Pessoa de contato", "Abordado em",
          "Resposta", "Cartões entregues", "Indicações recebidas", "Atendimentos fechados",
          "Indicações que a Aline fez para ele", "Próximo passo", "Observação"]
cabecalho(wpa, tit_pa, [26, 15, 16, 18, 12, 14, 10, 11, 11, 13, 30, 30])
PD = f"Pedidos!$G$2:$G${N_PEDIDOS + 1}"
for r in range(2, 152):
    wpa.cell(row=r, column=5).number_format = "DD/MM/YYYY"
    c = wpa.cell(row=r, column=8, value=f'=IF(A{r}="","",COUNTIFS({PD},A{r}))')
    c.fill = formula_fill
    c = wpa.cell(row=r, column=9, value=f'=IF(A{r}="","",COUNTIFS({PD},A{r},{PF},"Sim"))')
    c.fill = formula_fill
dv_tipo = DataValidation(type="list", formula1='"' + ",".join(TIPOS) + '"', allow_blank=True)
dv_tipo.add("B2:B151")
dv_resp = DataValidation(type="list", formula1='"Aguardando,Topou,Não topou,Sem resposta"', allow_blank=True)
dv_resp.add("F2:F151")
wpa.add_data_validation(dv_tipo)
wpa.add_data_validation(dv_resp)
wpa.auto_filter.ref = "A1:L151"
wb["Leia-me"].append([""])
wb["Leia-me"].append(["PARCEIROS"])
wb["Leia-me"].cell(row=wb["Leia-me"].max_row, column=1).font = Font(bold=True, color=AZUL)
wb["Leia-me"].append(["Aba Parceiros: um parceiro por linha. Escreva o nome igual ao que vai na coluna Detalhe da aba Pedidos: assim as indicações se contam sozinhas (operacao/parcerias.md)."])

# realce: taxa e linha "Não sei" acima de 25% dos pedidos
wsem.conditional_formatting.add(
    f"{L(2 + n_o)}2:{L(2 + n_o)}{N_SEMANAS + 1}",
    FormulaRule(formula=[f"AND({L(col_total)}2>0,{L(2 + n_o)}2/{L(col_total)}2>0.25)"],
                fill=PatternFill("solid", fgColor="F4D6C6")))

for w in (wp, wsem, wm):
    w.sheet_view.zoomScale = 110

wb.active = 1
wb.save(saida)
print("ok", saida)
