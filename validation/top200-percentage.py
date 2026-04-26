import glob
import os
import re

def calculate_top200_match(primary_path, top200_path):
    """
    Calculates what percentage of words in the primary list 
    are found in the top-200 reference list.
    """
    try:
        # Load primary words
        with open(primary_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            # Unicode-aware regex to support Russian/International characters
            primary_words = re.findall(r'\b[^\W\d_]+\b', content, re.UNICODE)
        
        if not primary_words:
            return "N/A"

        if not os.path.exists(top200_path):
            return "File Missing"

        # Load top-200 reference set
        with open(top200_path, 'r', encoding='utf-8') as f:
            top200_content = f.read().lower()
            top200_set = set(re.findall(r'\b[^\W\d_]+\b', top200_content, re.UNICODE))
        
        # Calculate intersection
        matches = [w for w in primary_words if w in top200_set]
        percentage = (len(matches) / len(primary_words)) * 100
        return f"{percentage:.1f}%"
        
    except Exception as e:
        return f"Error: {e}"

def main():
    # Find all .txt files that are NOT the top-200 lists
    primary_files = [f for f in glob.glob("*.txt") if "-top200" not in f]
    
    md_output = "# Word List Validation: Top 200 Coverage\n\n"
    # Added "Top 200 Count" to the headers
    md_output += "| Language | Word Count | Top 200 Count | Top 200 Match % |\n"
    md_output += "| :--- | :---: | :---: | :---: |\n"

    for txt_file in sorted(primary_files):
        lang_name = os.path.splitext(txt_file)[0]
        top200_file = f"{lang_name}-top200.txt"
        
        # 1. Get word count for the primary list
        primary_count = 0
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                primary_count = len(re.findall(r'\b[^\W\d_]+\b', content, re.UNICODE))
        except:
            primary_count = 0

        # 2. Get word count for the top-200 reference list
        reference_count = 0
        if os.path.exists(top200_file):
            try:
                with open(top200_file, 'r', encoding='utf-8') as f:
                    ref_content = f.read().lower()
                    reference_count = len(re.findall(r'\b[^\W\d_]+\b', ref_content, re.UNICODE))
            except:
                reference_count = 0
        else:
            reference_count = "Missing"

        # 3. Calculate match percentage
        match_result = calculate_top200_match(txt_file, top200_file)
        
        # 4. Append to table
        md_output += f"| {lang_name.capitalize()} | {primary_count} | {reference_count} | {match_result} |\n"

    with open("top200_coverage_report.md", "w", encoding="utf-8") as f:
        f.write(md_output)
    
    print("Coverage report generated: top200_coverage_report.md")

if __name__ == "__main__":
    main()