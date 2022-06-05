
import bs4, requests
from pprint import pprint

def CleanStr(string):

    characters = "'!?<>'div''<p>' '</p>' '"

    string = ''.join( x for x in string if x not in characters)

    return(string)


def main():

    URL = "https://michael-bloomberg.netlify.app/"

    response = requests.get(URL)

    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    id_request = soup.find("p", {"id": "par1"})
    #id_request = soup.find(id="maintextMainpage") 

    pprint(CleanStr(id_request))

main()