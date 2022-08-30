from xml.dom import minidom
import glob
import pandas as pd


notas = glob.glob (r"C:\Users\Milton\Desktop\notas\*.xml")
dados={'Produto':[],'Ean':[],'Ncm':[]  ,'CFOP':[] }
for n in notas:
    xml = open(n,encoding="utf-8")
    nfe=minidom.parse(xml)
    itens = nfe.getElementsByTagName('det')
    
    for i in itens:        
        numitem = 1-int(i.attributes['nItem'].value)
        ean = nfe.getElementsByTagName('cEAN')
        prod = nfe.getElementsByTagName('xProd')
        ncm = nfe.getElementsByTagName ('NCM')
        cfop = nfe.getElementsByTagName('CFOP')
        
        
        dados['Produto'].append(prod[numitem].firstChild.nodeValue)
        dados['Ean'].append(ean[numitem].firstChild.nodeValue)
        dados['Ncm'].append(ncm[numitem].firstChild.nodeValue)
        dados['CEST'].append(cest[numitem].firstChild.nodeValue)
        dados['CFOP'].append(cfop[numitem].firstChild.nodeValue)
        
        
        df=pd.DataFrame(data=dados, columns=['Produto' , 'Ean' , 'Ncm' , 'CFOP'])
        df.to_csv("notas\produtos.csv",sep=';')