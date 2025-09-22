import argparse, re
from collections import Counter
import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path

STOPWORDS = {"a","as","o","os","um","uma","de","do","da","dos","das","e","é","em","no","na","nos","nas",
"que","com","pra","para","por","se","sem","quando","mas","mais","menos","ao","aos","à","às",
"tem","têm","foi","são","sendo","entre","sobre","um","uma","uns","umas","os","as","eu","você",
"hoje","dias"}

def tokenize(text):
    tokens = re.findall(r"[A-Za-zÀ-ÿ]+", text.lower())
    return [t for t in tokens if t not in STOPWORDS and len(t) > 2]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="inputs/sentences.txt")
    p.add_argument("--outdir", default="outputs")
    args = p.parse_args()
    text = Path(args.input).read_text(encoding="utf-8")
    tokens = tokenize(text)
    cnt = Counter(tokens).most_common(10)
    df = pd.DataFrame(cnt, columns=["palavra","frequencia"])
    Path(args.outdir).mkdir(parents=True, exist_ok=True)
    df.to_csv(Path(args.outdir)/"keywords.csv", index=False, encoding="utf-8")
    if not df.empty:
        plt.bar(df["palavra"], df["frequencia"])
        plt.xticks(rotation=30, ha="right")
        plt.title("Top palavras")
        plt.tight_layout()
        plt.savefig(Path(args.outdir)/"keywords_bar.png", dpi=160)
    print("Análise concluída. Veja outputs/.")

if __name__ == "__main__":
    main()
