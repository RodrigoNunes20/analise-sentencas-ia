# 📊 Análise de Sentenças com IA

Este repositório atende ao desafio: criar um arquivo com sentenças, rodar uma análise simples e documentar o processo com prints e insights.

---

## 🚀 Processo

1. Criei o arquivo `inputs/sentences.txt` com frases sobre clima, vendas de sorvete e comportamento de clientes.
2. Rodei a análise usando o script `src/analyze.py`.
3. A análise gerou automaticamente:
   - `outputs/report.md` → relatório com resumo.
   - `outputs/keywords.csv` → tabela com palavras mais frequentes.
   - `outputs/keywords_bar.png` → gráfico de palavras.

---

## 📸 Prints


<img width="1527" height="854" alt="Captura de tela 2025-09-22 162837" src="https://github.com/user-attachments/assets/64b04111-d182-44b6-9181-e77c127127eb" />

---

## 💡 Insights obtidos

- O **clima** influencia diretamente as vendas (quente ↑, frio/chuva ↓).  
- **Finais de semana** apresentam maior movimento que dias úteis.  
- **Promoções** e o uso do **Instagram** ajudam a atrair clientes.  
- A análise automatizada facilita enxergar padrões sem precisar ler todas as frases manualmente.  

---

## 🔮 Possibilidades futuras

- Ampliar o dataset para observar mais padrões.  
- Criar dashboards interativos (BI) para acompanhamento contínuo.  
- Conectar o modelo a dados reais de vendas.  

---

## ✅ Como reproduzir localmente (opcional)

Se quiser rodar a análise no seu computador:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\analyze.py --input inputs\sentences.txt
