# 🚀 Sistema de Telemetria e Verificação de Decolagem

Este projeto é um simulador de controle de missão desenvolvido em **Python** para a atividade integradora da **FIAP**. O objetivo é analisar dados de telemetria em tempo real (temperatura, pressão, energia e sistemas críticos) para autorizar ou abortar a decolagem de uma aeronave/foguete com base em protocolos de segurança e integridade estrutural.

---

## 🛠️ Funcionalidades e Regras de Negócio

O sistema realiza o processamento de dados brutos para gerar indicadores inteligentes de decisão:

*   **Análise de Estresse Térmico:** Calcula o diferencial entre a temperatura interna e externa ($\Delta T$). Se a variação for superior a 60°C, a integridade estrutural é automaticamente comprometida (Status 0).
*   **Gestão Energética Realista:** Calcula a energia útil disponível aplicando um fator de eficiência que varia conforme o clima externo (perda de eficiência em temperaturas extremas abaixo de 0°C ou acima de 40°C).
*   **Monitoramento de Pressão:** Verifica a estabilidade individual dos tanques e a simetria de pressão entre eles para evitar empuxo desigual.
*   **Checklist de Módulos Críticos:** Validação de prontidão dos sistemas de controle, ignição e comunicação.

---

## 📊 Parâmetros de Segurança (Limites Críticos)

| Parâmetro | Faixa Segura / Condição |
| :--- | :--- |
| **Pressão dos Tanques** | Entre 45 e 55 PSI |
| **Diferencial de Pressão** | Máximo de 5 PSI entre Tanque A e B |
| **Diferencial Térmico ($\Delta T$)** | Máximo de 60°C (Evita fadiga de material) |
| **Energia Útil** | Deve ser $\ge$ ao Consumo Estimado (400 kWh) |
| **Status de Módulos** | Deve retornar "OK" |

---

## 💻 Como Executar o Projeto

1.  **Pré-requisitos:** Certifique-se de ter o **Python 3.x** instalado.
2.  **Clonar o Repositório:**
    ```bash
    git clone [https://github.com/x864dev/sistema-telemetria-decolagem.git](https://github.com/x864dev/sistema-telemetria-decolagem.git)
    ```
3.  **Executar o Script:**
    Navegue até a pasta do projeto e execute:
    ```bash
    python script.py
    ```
4.  **Interação:** Insira os valores de telemetria solicitados no terminal para receber o relatório final de prontidão.

---

## 📝 Estrutura do Código

O script utiliza uma arquitetura de **Processamento em Lote**:
1.  **Entrada:** Captura manual de dados via `input()` com conversão para `float`.
2.  **Processo:** Cálculos de física aplicada (Termodinâmica e Pressão) e definições de variáveis dependentes (Integridade).
3.  **Decisão:** Lógica em cascata que valida cada requisito de segurança.
4.  **Saída:** Dashboard visual no console com mensagens de "PRONTO PARA DECOLAR" ou "DECOLAGEM ABORTADA" (listando os erros encontrados).

---

## 🧑‍💻 Autor
*  [https://github.com/x864dev]
*   **Instituição:** FIAP (Atividade Integradora)

