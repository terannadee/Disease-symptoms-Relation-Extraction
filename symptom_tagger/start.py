from symptom_tagger.TextAnalyse.fuzzy import benchmark_fuzzy_match

text =  'Signs and symptoms of active TB include: Coughing that lasts three or more weeks, Coughing up blood, Chest pain, or pain with breathing or coughing, Unintentional weight loss, Fatigue, Fever, Night sweats, Chills, Loss of appetite, Tuberculosis can also affect other parts of your body, including your kidneys, spine or brain. '

print(benchmark_fuzzy_match(text))