import json
from collections import Counter
import xml.etree.ElementTree as ET

def json_top_ten():
	file_type = 'json'
	with open("files/newsafr.json", encoding="utf-8") as f:
		json_data = json.load(f)

	news_list = json_data["rss"]["channel"]["items"]
	top_ten(news_list, file_type)

def xml_top_ten():
	file_type = 'xml'
	parser = ET.XMLParser(encoding="utf-8")
	tree = ET.parse("files/newsafr.xml", parser)
	root = tree.getroot()

	news_list = root.findall("channel/item/description")
	top_ten(news_list, file_type)

def top_ten(news_list, file_type):
	six_letters_list = []
	for news in news_list:
		if file_type == "xml":
			str = news.text
			str = str.split(" ")
		elif file_type == "json":
			str = news["description"].split(" ")
		for word in str:
			if len(word) > 6:
				six_letters_list.append(word)
	six_letters_list = list(dict(Counter(six_letters_list)).items())
	six_letters_list.sort(key=lambda i: i[1], reverse=True)
	count = 0
	top10 = []
	for top in six_letters_list:
		top10.append(top[0])
		count += 1
		if count >= 10:
			break
	print(top10)

json_top_ten()
xml_top_ten()