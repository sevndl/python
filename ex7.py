def inverser(phrase):
  print(''.join(reversed(phrase)));

def palindrome(phrase):
  nouvellePhrase = ''.join(reversed(phrase));
  if nouvellePhrase == phrase:
    print("true");
  else:
    print("false");

inverser("bonjour");
palindrome("bonjour");
palindrome("radar");