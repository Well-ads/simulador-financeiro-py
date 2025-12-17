from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- Importação Nova
from app.models import InvestimentoRequest, InvestimentoResponse
from app.core import projetar_investimento
from app.services import obter_selic_atual
from app.charts import gerar_grafico_base64

app = FastAPI(title="Consultor Financeiro API", version="3.0")

# --- CONFIGURAÇÃO DE SEGURANÇA (CORS) ---
# Isso libera o navegador para consumir sua API localmente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceita conexões de qualquer lugar (para dev)
    allow_credentials=True,
    allow_methods=["*"],  # Aceita todos os métodos (POST, GET, etc)
    allow_headers=["*"],
)
# ----------------------------------------

@app.post("/simular", response_model=InvestimentoResponse)
def simular(request: InvestimentoRequest):
    # 1. Definir Taxa
    if request.usar_selic_atual:
        selic = obter_selic_atual()
        # Ajuste conservador para rentabilidade líquida (ex: 85% do CDI)
        taxa_calculo = selic * 0.85 
    else:
        taxa_calculo = request.taxa_manual if request.taxa_manual is not None else 10.0

    # 2. Calcular
    evolucao, valor_final, total_investido, total_juros = projetar_investimento(
        meta=request.meta,
        prazo_meses=request.prazo_meses,
        aporte_inicial=request.aporte_inicial,
        taxa_anual=taxa_calculo
    )

    # 3. Gerar Gráfico
    grafico = gerar_grafico_base64(evolucao, request.meta)
    
    # 4. Gerar Relatório de Texto
    percentual_lucro = (total_juros / total_investido * 100) if total_investido > 0 else 0.0
    
    # Evita divisão por zero se prazo for muito curto
    if request.prazo_meses > 0:
        aporte_mensal = (total_investido - request.aporte_inicial) / request.prazo_meses
    else:
        aporte_mensal = 0.0

    relatorio_texto = (
        f"RESUMO EXECUTIVO DO PLANO\n"
        f"---------------------------\n"
        f"Objetivo: Acumular R$ {request.meta:,.2f} em {request.prazo_meses} meses.\n\n"
        f"1. ESTRATÉGIA DE APORTE:\n"
        f"   - Depósito Inicial: R$ {request.aporte_inicial:,.2f}\n"
        f"   - Aporte Mensal Sugerido: R$ {aporte_mensal:,.2f}\n\n"
        f"2. PROJEÇÃO DE RETORNO (Taxa base: {taxa_calculo:.2f}% a.a.):\n"
        f"   - Total que sai do seu bolso: R$ {total_investido:,.2f}\n"
        f"   - Total pago pelo banco (Juros): R$ {total_juros:,.2f}\n"
        f"   - Rentabilidade sobre o capital: {percentual_lucro:.1f}%\n\n"
        f"3. CONCLUSÃO:\n"
        f"   Os juros compostos pagarão R$ {total_juros:,.2f} da sua meta.\n"
        f"   Isso representa uma economia de esforço graças ao tempo e à taxa Selic."
    )

    return InvestimentoResponse(
        status="Sucesso",
        taxa_aplicada_anual=round(taxa_calculo, 2),
        valor_final_bruto=round(valor_final, 2),
        total_investido_bolso=round(total_investido, 2),
        total_juros_ganhos=round(total_juros, 2),
        grafico_base64=grafico,
        relatorio=relatorio_texto,
        historico=evolucao
    )