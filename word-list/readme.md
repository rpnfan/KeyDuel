# Word lists of 100 words for 14 languages

**Text files** contain all words in one line, ready to paste the list into the typing website.

**CSV files** are formatted for direct import into Google Sheets or Excel (UTF-8 with BOM, semicolon delimiter, European decimal format). Each file includes the word, its tier weight.

**Excel files** provided for convenience as well.

**.3 files** are frequency tables of n-grams for a large language corpus (University of Leipzig)

## Word List Construction Process

The word lists were built in three stages. First, high-frequency vocabulary 
was drawn from corpus frequency data for each language, grouped into the four 
tiers based on word class and frequency rank. Second, each list was reviewed 
manually for linguistic soundness, checking that the tier assignments matched 
real-world usage, removing duplicates and misclassified words, and ensuring that 
morphologically rich languages (Finnish, Turkish, Polish, Russian) had adequate 
representation of inflected forms in Tier C. Third, the completed lists were 
validated against the n-gram frequency data described above, with targeted 
corrections where coverage gaps were identified. 
The validation confirmed that the final lists achieve high n-gram coverage 
relative to what is achievable with a 100-word constraint.
