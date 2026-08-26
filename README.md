# 🚚 Dashboard de Desempenho Logístico (Logistics Performance Dashboard)

Um projeto completo de **Business Intelligence & Data Analytics** desenvolvido de ponta a ponta, integrando extração/tratamento de dados com **Python**, modelagem/consultas analíticas em **SQL** e visualização executiva no **Power BI**.

---

## 📌 Visão Geral do Projeto

Este projeto analisa indicadores operacionais de entregas e logística para identificar gargalos de distribuição, taxa de cumprimento de prazos (*On-Time*) e custos associados a frete e avarias.

### Key Performance Indicators (KPIs) Monitorados:
* **Total de Pedidos:** Volume total de entregas processadas.
* **% On-Time:** Porcentagem de entregas realizadas rigorosamente no prazo.
* **Custo Total de Frete:** Valor investido em operações de transporte.
* **% Avaria:** Taxa de incidência de danos ou problemas nas mercadorias enviadas.
* **Desempenho por Cidade Destino:** Distribuição regional da eficiência de entregas.
* **Detalhamento Operacional (Tabela Dinâmica):** Acompanhamento por cliente, status e indicação de atraso via formatação condicional visual.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** Limpeza, transformação, cálculo de métricas e tratamento de dados brutos (`pandas`).
* **SQL:** Estruturação de queries de agregação, filtros e modelagem relacional.
* **Power BI Desktop:** Construção do painel interativo, KPIs, gráficos de barras e formatação condicional (Alertas em Verde/Vermelho).
* **Git & GitHub:** Controle de versão e documentação.

---

## 📁 Estrutura do Repositório

```text
projeto-dashboard-logistica/
│
├── data/
│   ├── raw/                  # Dados brutos recebidos
│   └── processed/            # Dados tratados e limpos pelo script Python
│
├── scripts/
│   ├── data_processing.py    # Script de tratamento de dados (Pandas)
│   └── queries.sql           # Queries SQL de validação e agregação
│
├── dashboards/
│   └── dashboard_logistica.pbix  # Arquivo principal do Power BI Desktop
│
├── images/
│   └── dashboard_preview.png # Captura de tela do dashboard finalizado
│
├── .gitignore                # Arquivos ignorados pelo Git
└── README.md                 # Documentação do projeto