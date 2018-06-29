from bs4 import BeautifulSoup
from pathlib import Path

# Read corpus and get the class values to an array
# filepath = 'CTD_diseases.xml'
# filepath = 'CTD_diseases.xml'


'''with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1

soup = BeautifulSoup.BeautifulSoup(filepath)
for node in soup.findAll('category="SpecificDisease'):
    print (''.join(node.findAll(text=True)))

percent = soup.find_all(id="productYoyo_Relative", text=True)
for item in percent:
    3
product = str(item)'''

contents = Path('symptom_tagger/TextAnalyse/CTD_disease.xml').read_text()

tlist = []
_, found, t = contents.partition('<DiseaseName>')
while found:
    t, found, more = t.partition('</DiseaseName>')
    if found:
        tlist.append(t)  ## no assignment, just append

    else:
        raise ValueError("Missing end tag: " + t)

    _, found, t = more.partition('<DiseaseName>')


# print(tlist)


# Remove duplicates from this list.
def remove_duplicates(val):
    output = []
    seen = set()
    for value in val:
        if value not in seen:
            output.append(value)
            seen.add(value)
    # print(output)
    return output


# values= tlist
# result= remove_duplicates(values)
# print(result)

def disease_list():
    val = tlist
    # print(val)
    result = remove_duplicates(val)
    return result
    # print(result)
    # print(len(result))


disease_list()
