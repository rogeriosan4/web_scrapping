from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_filmes():
    url = "http://www.adorocinema.com"
    html_doc = urlopen(url + "/filmes/numero-cinemas/").read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    filmes = []
    for data in soup.find_all('div', class_='card entity-card entity-card-list cf'):
        #titulo do filme
        titulo_filme = data.find('h2', class_='meta-title').find('a',class_="meta-title-link").text.strip()
        link_filme = url + data.find('a', class_='meta-title-link')['href']
        lancamento_filme = data.find('div', class_='meta-body-item meta-body-info').find('span', class_='date').text.strip()
        sinopse_filme = data.find('div', class_='content-txt').text.strip()
        img_src_filme = data.find('img', class_='thumbnail-img')
        # captura link do poster em 'src' ou 'data-src'
        if 'data-src' in img_src_filme.attrs:     
            poster_filme = img_src_filme['data-src']
        else:
            poster_filme = img_src_filme['src']
        
        filmes.append({'titulo': titulo_filme, 
                    'lancamento':lancamento_filme, 
                    'sinopse':sinopse_filme, 
                    'poster':poster_filme,
                    'link': link_filme})
    return filmes

if __name__ == "__main__":
    
    movies = get_filmes()

    for f in movies:
        print(f['link'])
        #break