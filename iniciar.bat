@echo off
title Gerenciador de Senhas
echo =========================================
echo  Iniciando o Cofre de Senhas...
echo  Por favor, aguarde o navegador abrir.
echo =========================================

:: Instala as bibliotecas automaticamente se a pessoa nao tiver
python -m pip install streamlit pandas cryptography > nul 2>&1

:: Roda o aplicativo localmente e abre o navegador
streamlit run interface.py

pause