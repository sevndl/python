def inverser(phrase):
  return ''.join(reversed(phrase));

def palindrome(phrase):
  nouvellePhrase = ''.join(reversed(phrase));
  if nouvellePhrase == phrase:
    return True;
  else:
    return False;

inverser("bonjour");
palindrome("bonjour");
palindrome("radar");