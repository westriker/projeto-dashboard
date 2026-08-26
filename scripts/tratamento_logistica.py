import pandas as pd
import os

# Pega o caminho da pasta onde este script (tratamento_logistica.py) está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho para a pasta 'data' que está no mesmo nível da pasta 'scripts'
caminho_entrada = os.path.join(diretorio_script, "..", "data", "entregas_brutas.csv")
caminho_saida = os.path.join(diretorio_script, "..", "data", "entregas_tratadas.csv")

# 1. Carregar os dados
df = pd.read_csv(caminho_entrada)

# 2. Converter colunas de data para datetime
colunas_data = ["data_envio", "data_entrega_prevista", "data_entrega_real"]
for col in colunas_data:
    df[col] = pd.to_datetime(df[col])

# 3. Remover pedidos cancelados do fluxo principal de performance
df_limpo = df[df["status"] != "Cancelado"].copy()

# 4. Tratar valores nulos no custo de frete
df_limpo["custo_frete"] = df_limpo["custo_frete"].fillna(0)

# 5. Criar regra de Atraso (1 = Atrasou, 0 = No Prazo / Em Trânsito)
df_limpo["atrasado"] = df_limpo.apply(
    lambda x: 1 if (pd.notnull(x["data_entrega_real"]) and x["data_entrega_real"] > x["data_entrega_prevista"]) else 0,
    axis=1
)

# 6. Calcular Dias de SLA (Tempo de entrega real vs envio)
df_limpo["dias_entrega"] = (df_limpo["data_entrega_real"] - df_limpo["data_envio"]).dt.days

# 7. Exportar base tratada para CSV
df_limpo.to_csv(caminho_saida, index=False)
print("Tratamento de dados concluído com sucesso!")