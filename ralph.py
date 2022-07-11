import datetime
import requests
import html2text
import re
import sys

url = 'https://www.studentenwerk-muenchen.de/mensa/speiseplan/speiseplan_422_-de.html#heute'
url2 = 'https://www.studentenwerk-muenchen.de/mensa/speiseplan/speiseplan_' + datetime.date.today().strftime('%Y-%m-%d')\
		+ '_422_-de.html'

response = requests.get(url)

txt = html2text.html2text(str(response.content))

response2 = requests.get(url2)

txt2 = html2text.html2text(str(response2.content))

dayStr = datetime.date.today().strftime('%d.%m.%Y')

splByDay = str.split(txt, dayStr)

work = str.split(splByDay[1][0:2000], '\\n\\n\\t\\t\\t\n')[0]

out = str.split(work, '\\n\\n\\t\\t\\t\\t\\n\\t\n')

out = out[1:len(out)]

outStr = ''

for e in out:
	outStr += e

outStr = str.replace(outStr, '\\n', '')
outStr = str.replace(outStr, '\\t', '')

outStr = str.replace(outStr, '* Pasta\n', '* Pasta:')
outStr = str.replace(outStr, 'S\\xc3\\xbc\\xc3\\x9fspeise\n', 'Süßspeise:')
outStr = str.replace(outStr, 'Wok\n', 'Wok:')
outStr = str.replace(outStr, 'Fisch\n', 'Fisch:')
outStr = str.replace(outStr, 'Studitopf\n', 'Studitopf:')
outStr = str.replace(outStr, 'Fleisch\n', 'Fleisch:')

outStr = str.replace(outStr, '\n\n\n  * \n', '')

outStr = str.replace(outStr, '\\xc3\\xbc', 'ü')
outStr = str.replace(outStr, '\\xc3\\xb6', 'ö')
outStr = str.replace(outStr, '\\xc3\\xa4', 'ä')

outStr = re.sub("[\(\[].*?[\)\]]", "", outStr)

outStr = str.replace(outStr, '\n\n  * ', '_________________________________________\n\n')

outStr = str.replace(outStr, '  * ', '')



beiStr = str.split(txt2, 'Beilagen')[1][0:3000]

beiStr = str.replace(beiStr, '\\n', '')
beiStr = str.replace(beiStr, '\\t', '')

beiStr = str.split(beiStr, 'f = fleischlosv')[0]

beiStr = str.replace(beiStr, '\n\n\n', '')

beiStr = str.replace(beiStr, '\n  * \n', '')
beiStr = str.replace(beiStr, '    \n', '\n')
beiStr = str.replace(beiStr, '\n    \n\n', '\n')

beiStr = str.replace(beiStr, '\\xc3\\xbc', 'ü')
beiStr = str.replace(beiStr, '\\xc3\\xb6', 'ö')
beiStr = str.replace(beiStr, '\\xc3\\xa4', 'ä')

beiStr = re.sub("[\(\[].*?[\)\]]", "", beiStr)

print(beiStr)
print('\n##############################')
print(outStr)

outStr = str.replace(outStr, '_', '')

sys.exit()
