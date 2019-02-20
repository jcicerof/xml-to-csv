#!/usr/bin/python3
import xml.etree.ElementTree as ET

tree = ET.parse('catalogo.xml')
root = tree.getroot()

csv = [[]]

print(root.tag)
for i in root:
    print('\t' + i.tag)
    campos = []
    for x in i:
        if(x.tag == 'PRICE'): # ignorando a tag <PRICE>
            continue
        if len(csv) == 1:
            csv[0].append(x.tag)
        print('\t\t{0} - {1}'.format(x.tag, x.text))
        campos.append(x.text)
    csv.append(','.join(campos))

csv[0] = ','.join(csv[0])
f = open('catalog.csv', 'w')
for linha in csv:
    f.write(linha + '\n')