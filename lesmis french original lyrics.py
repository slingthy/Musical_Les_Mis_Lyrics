import requests,os
from bs4 import BeautifulSoup


def save(path):
	'''
	latin_letters = ['é',
 		'à', 'è', 'ù',
        'â', 'ê', 'î', 'ô', 'û',
        'ç',
        'ë', 'ï', 'ü']
    '''
	with open(path, 'w',encoding ='utf-8') as file:
		file.write(headbody)
		for i in range(1,33):
			url = 'http://www.placedauphine.net/translations/ofc{}.html'.format(i)
			resq = requests.get(url, headers = headers, verify = False)
			resq.encoding = 'latin1'
			soup = BeautifulSoup(resq, 'html.parser')
			soup.table['class'] = 'gridtable'
			file.write(str(soup.table))
			print('Nov.{} html is downloading...'.format(i))

		file.write(end)
	
	file.close()				
	print('ALL Downloaded!')

if __name__ == '__main__':
	path = os.path.join(os.getcwd(),'Les miserable French Original Lyrics')
	if not os.path.exists(path):
		os.makedirs(path)

	filename = 'Les Mis(French Original) Lyrics'
	abpath = '%s\\%s.html'%(path,filename)
	headers = {
			'Host': 'www.placedauphine.net',
			'Connection': 'keep-alive',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'Referer': 'http://www.placedauphine.net/translations/ofc.html',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6' 
		}
	headbody = '''
	<html>
	<head>
	    <meta charset="UTF-8">
	    <title>Les Mis(French Original) Lyrics-Slingthy</title>
	    <style type="text/css">
	    	body {
	    		background-color:#c7edcc;
	    		color:#663300;
	    	}
	    	table.gridtable {
			    width:90%;
			    font-family: verdana,arial,sans-serif，times;
			    font-size: 14px;
			    text-align: center;
			    border-width: 1px;
			    border-collapse: collapse;
			}
			table.gridtable th {
			    border-width: 1px;
			}
			table.gridtable td {
			    border-width: 1px;
			}
	    </style>
	</head>
	<body>
	<h1 align=center>Les Misérables Original French Concept Album</br>Lyrics: Original - Translation</h1>
	'''

	end = '''
	<p align=center>Author: Github @Slingthy - Goto <a href=https://github.com/slingthy> Slingthy Home</a></p>
	</body>
	</html>
	'''
	save(abpath)


