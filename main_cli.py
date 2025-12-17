from app.services import obter_selic_atual
from app.core import calcular_aporte_mensal

def main():
    print("\n" + "="*40)
    print("   COACH FINANCEIRO | SIMULADOR v2.1")
    print("="*40 + "\n")
    
    try:
        meta = float(input("1. Qual sua meta financeira? (Ex: 20000): "))
        meses = int(input("2. Em quantos meses? (Ex: 24): "))
        inicial = float(input("3. Quanto já tem investido? (Ex: 0): "))
    except ValueError:
        print("Erro: Digite apenas números (use ponto para centavos).")
        return
    
    print("\nCalculando com dados do Banco Central...")
    selic = obter_selic_atual()
    
    # Estimativa líquida conservadora (aprox 85% do CDI para Renda Fixa) [cite: 1]
    taxa_liquida = selic * 0.85 
    
    aporte = calcular_aporte_mensal(meta, inicial, taxa_liquida, meses)
    
    print("-" * 40)
    print(f"CENÁRIO ATUAL (Selic: {selic}% a.a.)")
    print("-" * 40)
    print(f"Para juntar R$ {meta:,.2f} em {meses} meses...")
    print(f"► VOCÊ PRECISA INVESTIR: R$ {aporte:,.2f} / mês")
    print("-" * 40)
    print("Sugestão de Ativos Seguros (FGC/Tesouro)[cite: 1]:")
    print("1. Tesouro Selic (Pós-fixado)")
    print("2. CDB Liquidez Diária (Itaú, Sofisa, Inter - 100% CDI)")

if __name__ == "__main__":
    main()