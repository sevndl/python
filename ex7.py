def inverser(phrase):
  return ''.join(reversed(phrase));

def palindrome(phrase):
  nouvellePhrase = inverser(phrase);
  phrase = phrase.replace(' ', '');
  phrase = phrase.lower();
  nouvellePhrase = nouvellePhrase.replace(' ', '');
  nouvellePhrase = nouvellePhrase.lower();
  if nouvellePhrase == phrase:
    return True;
  else:
    return False;

print(inverser("bonjour"));
print(palindrome("bonjour"));
print(palindrome("Esope reste ici et se repose"));