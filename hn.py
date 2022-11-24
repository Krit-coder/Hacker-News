import requests
from bs4 import BeautifulSoup
import pprint

# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.titleline')
# subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title':title, 'link': href, 'votes':points})
	return sort_stories_by_votes(hn)


if __name__ == '__main__':
	global res, soup, links, subtext
	i=1
	while True:
		res = requests.get(f'https://news.ycombinator.com/news?p={i}')
		soup = BeautifulSoup(res.text, 'html.parser')
		links = soup.select('.titleline > a')
		subtext = soup.select('.subtext')
		pprint.pprint(create_custom_hn(links, subtext))
		choice = input("Want to see the next Page? (y/n): ")
		if choice.lower() == 'y':
			i+=1
			continue
		else:
			print("Thank You!!!!")
			break





