# -*- coding: utf-8 -*-
# Infográfico: O que é software? (Tecnologia e Produção - extensão universitária)
# Uso:  pip install pillow   ->   python gerar_infografico.py
from PIL import Image, ImageDraw, ImageFont
import os, math

# ============================ DADOS (EDITE AQUI) ============================
CREDITO = "Seu Nome · Curso · Nome da Faculdade · 2026"
ARQUIVO = "infografico_software.png"
# ===========================================================================

W, H, S = 800, 1880, 2
BG, CARD, BORDA = (11, 18, 38), (21, 31, 60), (44, 58, 98)
BRANCO, CINZA = (240, 244, 255), (150, 162, 195)
CIANO, CORAL, AMARELO, VIOLETA = (56, 224, 214), (255, 107, 107), (255, 205, 86), (160, 130, 255)

def achar(lista):
    for c in lista:
        if os.path.exists(c): return c
BOLD = achar(["C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"])
REG = achar(["C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"])
MONO = achar(["C:/Windows/Fonts/consola.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
              "/System/Library/Fonts/Menlo.ttc", "C:/Windows/Fonts/cour.ttf"])
def f(t, kind="r"):
    p = {"b": BOLD, "r": REG, "m": MONO}[kind]
    return ImageFont.truetype(p, int(t * S)) if p else ImageFont.load_default()

img = Image.new("RGB", (W * S, H * S), BG)
d = ImageDraw.Draw(img)
R = lambda x: int(x * S)

def rect(x0, y0, x1, y1, fill=None, r=0, outline=None, w=1):
    d.rounded_rectangle([R(x0), R(y0), R(x1), R(y1)], R(r), fill=fill, outline=outline, width=R(w))
def circ(cx, cy, rr, fill=None, outline=None, w=1):
    d.ellipse([R(cx-rr), R(cy-rr), R(cx+rr), R(cy+rr)], fill=fill, outline=outline, width=R(w))
def line(x0, y0, x1, y1, cor, w=2):
    d.line([R(x0), R(y0), R(x1), R(y1)], fill=cor, width=R(w))
def poly(pts, fill): d.polygon([(R(a), R(b)) for a, b in pts], fill=fill)
def txt(x, y, s, font, cor, anc="la", sp=4):
    d.multiline_text((R(x), R(y)), s, font=font, fill=cor, anchor=anc, spacing=R(sp),
                     align="center" if anc[0] == "m" else "left")
def wrap(s, font, maxw):
    linhas, atual = [], ""
    for p in s.split():
        t = (atual + " " + p).strip()
        if d.textlength(t, font=font) <= R(maxw): atual = t
        else: linhas.append(atual); atual = p
    return "\n".join(linhas + [atual])
def secao(y, num, titulo, cor):
    txt(30, y, f"// {num}", f(11, "m"), cor)
    txt(30, y + 20, titulo, f(25, "b"), BRANCO)
def seta(x0, x1, y, cor):
    line(x0, y, x1 - 7, y, cor, 2.5); poly([(x1 - 9, y - 7), (x1, y), (x1 - 9, y + 7)], cor)

# ---------- Cabeçalho ----------
txt(30, 28, "// TECNOLOGIA E PRODUÇÃO · DESENVOLVIMENTO DE SOFTWARE", f(10, "m"), CIANO)
txt(30, 52, "O que é", f(58, "b"), BRANCO)
txt(30, 114, "software?", f(58, "b"), CIANO)
txt(30, 190, wrap("É a parte invisível da tecnologia: as instruções que dizem ao computador e ao "
                  "celular o que fazer. Sem software, o aparelho mais caro do mundo não passa de um objeto.", f(14), 600),
    f(14), CINZA, sp=5)
txt(W - 70, 100, "{ }", f(60, "b"), VIOLETA, "mm")

# ---------- 01 Duas metades ----------
secao(285, "01", "Duas metades de toda tecnologia", CIANO)
# hardware
rect(30, 350, 350, 510, CARD, 16, BORDA, 1.5)
rect(52, 372, 96, 440, None, 7, AMARELO, 3); circ(74, 428, 3, AMARELO)           # celular
rect(104, 384, 160, 424, None, 5, AMARELO, 3); line(132, 424, 132, 434, AMARELO, 3); line(120, 434, 144, 434, AMARELO, 3)
txt(176, 380, "HARDWARE", f(10, "m"), AMARELO)
txt(176, 398, "A parte física", f(16, "b"), BRANCO)
txt(176, 426, wrap("O que você pode tocar: tela, teclado, processador, memória.", f(10.5), 160), f(10.5), CINZA, sp=3)
txt(190, 488, "o corpo", f(10, "m"), CINZA, "lm")
# software
rect(450, 350, 770, 510, CARD, 16, BORDA, 1.5)
rect(472, 376, 546, 440, (14, 22, 46), 7, CIANO, 2)
txt(509, 408, "</>", f(20, "m"), CIANO, "mm")
txt(562, 380, "SOFTWARE", f(10, "m"), CIANO)
txt(562, 398, "A parte lógica", f(16, "b"), BRANCO)
txt(562, 426, wrap("O que você não toca, mas usa: programas e aplicativos.", f(10.5), 160), f(10.5), CINZA, sp=3)
txt(576, 488, "a mente", f(10, "m"), CINZA, "lm")
circ(400, 430, 22, BG, VIOLETA, 2.5); txt(400, 429, "+", f(26, "b"), VIOLETA, "mm")
# definição
rect(30, 530, W - 30, 640, (14, 52, 62), 14, CIANO, 1.2)
txt(52, 548, "SOFTWARE (substantivo)", f(10, "m"), CIANO)
txt(52, 570, wrap("Conjunto de instruções, escritas por pessoas em uma linguagem de programação, "
                  "que dizem a uma máquina o que fazer, passo a passo.", f(14, "b"), 690), f(14, "b"), BRANCO, sp=5)

# ---------- 02 Três tipos ----------
secao(675, "02", "Três tipos de software", AMARELO)
def icone(tipo, cx, cy, cor):
    if tipo == "sis":
        circ(cx, cy, 11, None, cor, 3)
        for a in range(8):
            ax, ay = cx + 16 * math.cos(a * math.pi / 4), cy + 16 * math.sin(a * math.pi / 4); circ(ax, ay, 3.5, cor)
    elif tipo == "app":
        for i in range(2):
            for j in range(2): rect(cx - 17 + i * 18, cy - 17 + j * 18, cx - 3 + i * 18, cy - 3 + j * 18, None, 4, cor, 2.5)
    else:
        txt(cx, cy, "</>", f(20, "m"), cor, "mm")
tipos = [("sis", CIANO, "De sistema", "Faz a máquina funcionar e conversa com o hardware.", "Windows · Android · iOS"),
         ("app", AMARELO, "Aplicativo", "Ajuda a pessoa a fazer uma tarefa específica.", "WhatsApp · app do banco · planilhas"),
         ("dev", CORAL, "De programação", "Ferramentas usadas para criar outros softwares.", "VS Code · Python · GitHub")]
cw = (W - 60 - 28) / 3
for i, (ic, cor, ti, desc, ex) in enumerate(tipos):
    x0 = 30 + i * (cw + 14)
    rect(x0, 740, x0 + cw, 950, CARD, 16, BORDA, 1.5)
    d.rounded_rectangle([R(x0 + 24), R(740), R(x0 + cw - 24), R(744)], R(2), fill=cor)
    circ(x0 + 46, 794, 30, (30, 42, 78)); icone(ic, x0 + 46, 794, cor)
    txt(x0 + 20, 842, ti, f(17, "b"), BRANCO)
    txt(x0 + 20, 870, wrap(desc, f(10.5), cw - 40), f(10.5), CINZA, sp=3)
    txt(x0 + 20, 920, "ex.:", f(8.5, "m"), cor); txt(x0 + 48, 920, wrap(ex, f(8.5, "m"), cw - 68), f(8.5, "m"), BRANCO, sp=2)

# ---------- 03 Como funciona ----------
secao(985, "03", "Como ele funciona por dentro", VIOLETA)
txt(30, 1043, "Todo software segue o mesmo caminho: recebe algo, pensa e devolve uma resposta.", f(12), CINZA)
fl = [("ENTRADA", "O que você faz", "Toca em “agendar consulta”.", CIANO),
      ("PROCESSAMENTO", "O que o software faz", "Confere quais horários estão livres.", AMARELO),
      ("SAÍDA", "O que você vê", "Aparece a confirmação na tela.", CORAL)]
bw = 212; gap = (W - 60 - 3 * bw) / 2
for i, (t, sub, ex, cor) in enumerate(fl):
    x0 = 30 + i * (bw + gap)
    rect(x0, 1065, x0 + bw, 1215, CARD, 16, cor, 2)
    txt(x0 + bw / 2, 1088, t, f(11, "m"), cor, "mm")
    txt(x0 + bw / 2, 1120, sub, f(14, "b"), BRANCO, "mm")
    txt(x0 + bw / 2, 1170, wrap(ex, f(11), bw - 36), f(11), CINZA, "mm", 3)
    if i < 2: seta(x0 + bw + 6, x0 + bw + gap - 6, 1140, VIOLETA)
txt(30, 1232, "exemplo: app de agendamento de atendimentos de uma ONG", f(9, "m"), CINZA)

# ---------- 04 Como é feito (faixa) ----------
rect(0, 1275, W, 1505, (14, 44, 60))
d.rectangle([0, R(1275), R(W), R(1277)], fill=CIANO); d.rectangle([0, R(1503), R(W), R(1505)], fill=CIANO)
txt(30, 1297, "// 04", f(11, "m"), CIANO)
txt(30, 1317, "Como um software é feito", f(25, "b"), BRANCO)
etapas = [("Entender", "Qual problema precisa ser resolvido?"), ("Programar", "Escrever o código, passo a passo."),
          ("Testar", "Procurar e corrigir erros (bugs)."), ("Publicar", "Colocar nas mãos de quem vai usar."),
          ("Melhorar", "Ouvir os usuários e atualizar.")]
pw = (W - 60) / 5
for i, (ti, ds) in enumerate(etapas):
    cx = 30 + pw * i + pw / 2
    if i < 4: seta(cx + 26, cx + pw - 26, 1397, CIANO)
    circ(cx, 1397, 22, (14, 44, 60), CIANO, 2.5); txt(cx, 1397, str(i + 1), f(16, "b"), CIANO, "mm")
    txt(cx, 1436, ti, f(14, "b"), BRANCO, "mm")
    txt(cx, 1456, wrap(ds, f(10), pw - 16), f(10), (190, 215, 225), "ma", 3)
txt(W - 30, 1320, "↻ o ciclo nunca termina", f(10, "m"), CIANO, "rm")

# ---------- 05 Para a comunidade ----------
secao(1535, "05", "Software que ajuda a comunidade", CORAL)
usos = [("saude", CORAL, "Saúde", "Agendar consultas e lembrar de vacinas."),
        ("edu", CIANO, "Educação", "Aulas online e reforço escolar."),
        ("ong", AMARELO, "ONGs", "Controlar doações, voluntários e estoque."),
        ("acc", VIOLETA, "Acessibilidade", "Leitores de tela e comunicação inclusiva.")]
uw = (W - 60 - 3 * 14) / 4
for i, (ic, cor, ti, ds) in enumerate(usos):
    x0 = 30 + i * (uw + 14); cx = x0 + uw / 2
    rect(x0, 1600, x0 + uw, 1745, CARD, 16, BORDA, 1.5)
    circ(cx, 1640, 24, (30, 42, 78))
    if ic == "saude": rect(cx - 4, cy := 1640 - 12, cx + 4, 1640 + 12, cor, 2); rect(cx - 12, 1636, cx + 12, 1644, cor, 2)
    elif ic == "edu":
        rect(cx - 15, 1630, cx - 1, 1651, None, 3, cor, 2.5); rect(cx + 1, 1630, cx + 15, 1651, None, 3, cor, 2.5)
    elif ic == "ong": txt(cx, 1641, "♥", f(24, "b"), cor, "mm")
    else:
        circ(cx, 1632, 4.5, cor); line(cx - 12, 1640, cx + 12, 1640, cor, 3); line(cx, 1640, cx, 1652, cor, 3)
        line(cx, 1652, cx - 8, 1660, cor, 3); line(cx, 1652, cx + 8, 1660, cor, 3)
    txt(cx, 1682, ti, f(14, "b"), BRANCO, "mm")
    txt(cx, 1702, wrap(ds, f(9.5), uw - 24), f(9.5), CINZA, "ma", 3)

# fecho
rect(30, 1770, W - 30, 1832, (14, 52, 62), 14, CIANO, 1.5)
txt(W / 2, 1801, "Software é ferramenta: o que importa é o problema que ele resolve e quem ele ajuda.",
    f(13, "b"), CIANO, "mm")

txt(W - 30, 1862, CREDITO, f(8, "m"), CINZA, "rs")
img.crop((0, 0, W * S, 1872 * S)).save(ARQUIVO, dpi=(200, 200))
print("Salvo:", ARQUIVO)
