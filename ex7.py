def inverser(phrase):
  return ''.join(reversed(phrase));

def palindrome(phrase):
  nouvellePhrase = ''.join(reversed(phrase));
  if nouvellePhrase == phrase:
    return True;
  else:
    return False;

print(inverser("bonjour"));
print(palindrome("bonjour"));
print(palindrome("esope reste ici et se repose"));