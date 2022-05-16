# This data was extracted from the site below for data training purposes only:
# https://www.msstate.edu/students/lists
scores = {
             "Javad A'Arabi": 70,
             "Leila Aarabi": 35,
             "Asia A Aaron": 82,
             "Kathleen Michelle Abadie": 23,
             "Anna Katherine Abel": 98,
             "Matthew Webb Abernethy": 34,
             "Joseph Thomas Ables": 45,
             "Esther Abraham": 79,
             "Kenneth Ohene Abrefa": 79,
             "Nathaniel T Abstein": 80,
             "Savannah Grace Acree": 34,
             "Stephanie Marian Acuna": 67,
             "Rachel Lynn Adair": 45,
             "Autumn B. Adams": 89,
             "Avery Elizabeth Adams": 39,
             "Craig Aaron Adams": 90,
             "Evelyn M Adams": 78,
             "Raegan La Rue Adams": 78,
             "Ragan Lydia Adams": 78,
             "Ragan Lydia Adams ": 45,
             "Griffin Todd Adcock": 100,
             "Darrow Anne-Martha Adderholt": 100,
             "Daniel Imole Adejombo": 98,
             "William T Adema": 56,
             "Bibhor Adhikari": 67,
             "Nisha Adhikari": 89,
             "Jeremy Adriano": 78,
             "Lucas Evan Agent": 45,
             "Mary Morgan Agostinelli": 56,
             "Sean C Agsalud": 76,
             "Andrew Manuel Aguana": 60,
             "Laura L Aguinaga": 67,
             "Tekara Rose Aimer": 70,
             "Zoey E Ainsworth": 69
             
          }
# Now let's see which students succeeded.
passed = [name for name, score in scores.items() if score >= 50]
for passe in passed:
    print('{} : Yes'.format(passe))
print('Good luck for the rest!')