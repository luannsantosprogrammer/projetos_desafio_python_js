# 📊 Visualizador & Criador de Gráficos Interativo (SAS Gráfico)

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green?style=for-the-badge)

> **Uma aplicação web intuitiva e interativa desenvolvida com Python e Streamlit para exploração rápida de dados e geração dinâmica de gráficos a partir de arquivos CSV e Excel.**

---

## 📌 Sobre o Projeto

O **SAS Gráfico** é uma ferramenta web focada em simplificar a análise exploratória de dados (EDA). Ela permite que usuários realizem upload de conjuntos de dados nos formatos `.csv` ou `.xlsx` e gerem visualizações gráficas em tempo real, sem a necessidade de escrever uma única linha de código.

Desenvolvido com foco em **usabilidade, performance e flexibilidade**, o projeto demonstra o uso prático de **Streamlit** para criação rápida de dashboards de dados e **Pandas** para manipulação e leitura eficiente de DataFrames.

---

## 🚀 Funcionalidades Principais

- 📁 **Upload Multi-formato:** Suporte nativo para carregamento de dados via arquivos `.csv` e `.xlsx` (Excel).
- 🎛️ **Seleção Dinâmica de Colunas:** Filtro interativo para selecionar quais atributos visualizar no gráfico.
- 📈 **Múltiplos Tipos de Gráficos:**
  - **Gráfico de Barras:** Ideal para comparações categóricas e valores acumulados.
  - **Gráfico de Linha:** Perfeito para tendências e séries temporais.
  - **Gráfico de Dispersão (Scatter Plot):** Excelente para analisar correlações e distribuições entre variáveis.
- ⚡ **Renderização em Tempo Real:** Atualização instantânea da visualização ao alterar os parâmetros no menu lateral.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Python** | Linguagem base para processamento de dados e controle da aplicação. |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white) **Streamlit** | Framework web para criação de dashboards e aplicações de data science interativas. |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas** | Leitura, manipulação e estruturação dinâmica de DataFrames a partir dos dados enviados. |
| **OpenPyXL** | Engine para suporte à leitura de planilhas em formato Excel (`.xlsx`). |

---

## 📂 Arquitetura do Projeto

```text
sas_grafico/
├── interface_grafico.py  # Aplicação principal (Streamlit UI & lógica de gráficos)
├── sas_grafico.md        # Documentação do projeto
├── README.md             # Documentação principal para visualização no GitHub
└── requirements.txt      # Lista de dependências do projeto
```

---

## 🔧 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/python/sas_grafico
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, recomendado)
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install streamlit pandas openpyxl
```

### 4. Executar a Aplicação
```bash
streamlit run interface_grafico.py
```

Acesse a aplicação no navegador em: `http://localhost:8501`

---

## 💡 Próximos Passos & Roadmap de Evolução

- [ ] Adicionar suporte à biblioteca **Plotly** para gráficos customizáveis com zoom e tooltips interativos.
- [ ] Exportação dos gráficos gerados em formatos de imagem (`.png`, `.svg`) ou `.pdf`.
- [ ] Painel de estatísticas descritivas automáticas (média, mediana, desvio padrão, valores nulos).
- [ ] Opção de download dos dados filtrados ou limpos.

---

## 👨‍💻 Autor

Desenvolvido por **Luann Santos**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/luannsantosprogrammer)
