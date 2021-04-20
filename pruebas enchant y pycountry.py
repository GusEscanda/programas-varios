def langs(p):
    for l in enchant.list_languages():
       if l == 'he':
          continue
       d = enchant.Dict(l)
       if d.check(p):
          print(l, langDesc[l])
 
import pycountry

enchant_codes = enchant.list_languages()

def langDescriptions(codes):
    myDict = {}
    for code in codes:
        langCode, _, countryCode = code.partition("_")
        if len(langCode) == 2:
            language = pycountry.languages.get(alpha_2=langCode)
        elif len(langCode) == 3:
            language = pycountry.languages.get(alpha_3=langCode)
        else:
            language = None
        languageName = language.name if language else "(unknown language)"
        country = pycountry.countries.get(alpha_2=countryCode) if countryCode else None
        countryName = country.name if country else ""
        myDict[code] = languageName + (" ("+countryName+")" if countryName else "")
    return myDict


def testLangs(palabras, dicts):
    testDicts = []
    for d in dicts:
        testDicts.append( enchant.Dict(d) )
    for palabra in palabras:
        checks = []
        for d in testDicts: # check this word in all the dictionaries and save the results in an array
            checks.append(d.check(palabra))
        if True not in checks: # if the word was not in any disctinary, continue with the next one
            continue
        if False not in checks: # if the word is in every dict checked, continue with the next one
            continue
        # The word is in some dictionary but not in some another, lets inform that...
        print(palabra, ': ', end='')
        for i in range(len(dicts)):
            if checks[i]:
                print((dicts[i]+'        ')[0:5], ' ', end='')
            else:
                print('                   '[0:5], ' ', end='')
        print()


