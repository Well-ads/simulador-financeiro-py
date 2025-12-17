@echo off
TITLE Servidor Financeiro (Nao feche esta janela!)
echo ==========================================
echo      INICIANDO SEU SISTEMA FINANCEIRO
echo ==========================================
echo.
echo 1. Ligando o motor Python...
echo.

:: Abre o navegador no seu site (espera 2 segundinhos pro servidor ligar antes)
start "" "http://127.0.0.1:8000/docs" 
:: O comando acima abre a documentação, mas para abrir seu site HTML direto:
:: Se quiser abrir o index.html direto, troque a linha acima por:
start index.html

:: Inicia o servidor (o /k mantem a janela aberta)
cmd /k "uvicorn main_api:app --reload"