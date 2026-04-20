import re
import glob
import os
from collections import defaultdict

def analyze_language_files(wordlist_path, ngram_path):
    # 1. Load the 100-word list
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            words = [w.strip().lower() for w in f.read().split() if w.strip()]
    except Exception as e:
        return f"Error: {e}"

    # 2. Aggregation Logic (Filter mid-spaces, Sum boundary variants)
    aggregated_ngrams = defaultdict(int)
    try:
        with open(ngram_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'^\s*(\d+)\s+(.+)$', line)
                if match:
                    freq = int(match.group(1))
                    raw_ngram = match.group(2).lower()
                    core = raw_ngram.strip()
                    
                    # We only keep patterns that can exist WITHIN a word
                    if " " not in core and core != "":
                        aggregated_ngrams[core] += freq
    except Exception as e:
        return f"Error: {e}"

    # 3. Re-sort by the new cumulative internal frequency
    sorted_ngrams = sorted(aggregated_ngrams.items(), key=lambda x: x[1], reverse=True)
    total_internal_freq = sum(n[1] for n in sorted_ngrams)

    limits = [100, 200, 300, 400, 500]
    results = {}

    for limit in limits:
        subset = sorted_ngrams[:limit]
        
        # Count how many top finger motions are in our wordlist
        found_count = sum(1 for ngram_core, freq in subset if any(ngram_core in w for w in words))

        # Calculate word coverage (how many of our 100 words are 'taxed')
        covered_words = sum(1 for w in words if any(ngram_core in w for ngram_core, freq in subset))
                
        freq_weight = (sum(n[1] for n in subset) / total_internal_freq) * 100
        results[limit] = {
            "count": found_count,
            "ngram_perc": (found_count / limit) * 100,
            "word_cov": (covered_words / len(words)) * 100,
            "freq_weight": freq_weight
        }
    return results

def main():
    wordlist_files = glob.glob("*.txt")
    md_output = "# Language N-gram Analysis Results (Aggregated)\n\n"
    
    for txt_file in wordlist_files:
        lang_name = os.path.splitext(txt_file)[0]
        ngram_file = f"{lang_name}.3"
        if os.path.exists(ngram_file):
            data = analyze_language_files(txt_file, ngram_file)
            if isinstance(data, dict):
                md_output += f"## Language: {lang_name.capitalize()}\n"
                md_output += "| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |\n"
                md_output += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
                
                rows = {
                    "Found Count": [str(data[lim]['count']) for lim in [100,200,300,400,500]],
                    "N-gram Match %": [f"{data[lim]['ngram_perc']:.1f}%" for lim in [100,200,300,400,500]],
                    "Word Coverage %": [f"{data[lim]['word_cov']:.1f}%" for lim in [100,200,300,400,500]],
                    "Freq. Weight %": [f"{data[lim]['freq_weight']:.1f}%" for lim in [100,200,300,400,500]]
                }
                for label, values in rows.items():
                    md_output += f"| **{label}** | {' | '.join(values)} |\n"
                md_output += "\n"

    with open("analysis_results.md", "w", encoding="utf-8") as f:
        f.write(md_output)
    print("Analysis complete. Results written to analysis_results.md")

if __name__ == "__main__":
    main()