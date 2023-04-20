"""
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You"ll typically want to use:
  1. "french_cleaners" for French text
  2. "transliteration_cleaners" for non-French text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
"""
import re
from unidecode import unidecode
from synthesizer.utils.numbers import normalize_numbers


# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [(re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1]) for x in [
 ( "bjr" , "bonjour"),
("bsr" , "bonsoir"),
("auj" , "aujourd’hui"),
("ir" , "hier"),
("bi1to" , "bientôt"),
("tds" , "tout de suite"),
("vazi" , "vas-y"),
("DQP" , "dès que possible"),
("tjs" , "toujours"),
("@+" , "à plus tard"),
("@2m1" , "à demain"),
("a tt" , "à tout à l’heure"),
("kan" , "quand"),
("ALP" , "à la prochaine"),
("JMS" , "jamais"),
("slt" , "salut"),
("biz" , "bisous"),
("M" , "merci"),
("2 ri 1" , "de rien"),
("STP/SVP" , "s’il te/vous plait"),
("pk" , "pourquoi"),
("ki" , "qui"),
("p-ê" , "peut-être"),
("d’ac" , "d’accord"),
("dak" , "d’accord"),
("cb1" , "c’est bien"),
("XLent" , "excellent"),
("ama" , "à mon avis"),
("BCP" , "beaucoup"),
("NRV" , "énervé"),
("HT" , "acheter"),
("TLM" , "tout le monde"),
("ENTK" , "en tout cas"),
("EDR" , "écroulé de rire"),
("GspR b1" , "J’espère bien"),
("Chui" , "Je suis"),
("Je c" , "Je sais"),
("C1Blag" , "C’est une blague"),
("TOQP" , "T’es occupé ?"),
("QDN" , "Quoi de neuf?"),
("Koi29" , "Quoi de neuf?"),
("Tata KS" , "T’as ta caisse ?"),
("C pa 5pa" , "C’est pas sympa"),
("G1id2kdo" , "J’ai une idée de cadeau")
]]


def expand_abbreviations(text):
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text


def expand_numbers(text):
    return normalize_numbers(text)


def lowercase(text):
    """lowercase input tokens."""
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)


def convert_to_ascii(text):
    return unidecode(text)


def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def transliteration_cleaners(text):
  """Pipeline for non-Spanish text that transliterates to ASCII."""
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def french_cleaners(text):
  """Pipeline for Spanish text, including number and abbreviation expansion."""
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = expand_numbers(text)
  text = expand_abbreviations(text)
  text = collapse_whitespace(text)
  return text
