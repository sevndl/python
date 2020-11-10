phrase = "  Le lièvre et la tortue ";

# longueur de la phrase
print(len(phrase));
# 1er caractère
print(phrase[0]);
# dernier caractère
print(phrase[len(phrase) - 1]);
# 10 premiers caractères
print(phrase[0:9]);
# 10 derniers caractères 
print(phrase[-10:]);
# caractères entre 10 et 15
print(phrase[9:14]);
# phrase en minuscules
print(phrase.lower());
# phrase en majuscules
print(phrase.upper());
# première lettre du premier mot en majuscule
print(phrase[0].upper() + phrase[1:].lower());
# première lettre de chaque mot en majuscules --> on peut aussi utiliser split et utiliser cette liste
print(phrase.title());
# phrase sans espaces en début et fin --> strip() = trim() dans un autre langage
print(phrase.strip());
# remplacer les espaces par des étoiles
print(phrase.replace(' ','*'));
# liste des mots de la phrase
print(phrase.split());