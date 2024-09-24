import time
from selenium import webdriver

# Lista de URLs que você deseja acessar
urls = [
    "https://www.wikipedia.org/",
    "https://www.youtube.com/",
    "https://github.com/",
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.twitter.com/",
    "https://www.instagram.com/",
    "https://www.linkedin.com/",
    "https://www.reddit.com/",
    "https://www.amazon.com/",
    "https://www.stackoverflow.com/",
    "https://www.medium.com/",
    "https://www.netflix.com/",
    "https://www.apple.com/",
    "https://www.microsoft.com/",
    "https://www.quora.com/",
    "https://www.bbc.com/",
    "https://www.cnn.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.twitch.tv/",
    "https://www.nytimes.com/",
    "https://www.forbes.com/",
    "https://www.ebay.com/",
    "https://www.salesforce.com/",
    "https://www.spotify.com/",
    "https://www.dropbox.com/",
    "https://www.adobe.com/",
    "https://www.wordpress.com/",
    "https://www.slack.com/",
    "https://www.airbnb.com/",
    "https://www.booking.com/",
    "https://www.tripadvisor.com/",
    "https://www.paypal.com/",
    "https://www.shopify.com/",
    "https://www.pinterest.com/",
    "https://www.tumblr.com/",
    "https://www.deviantart.com/",
    "https://www.khanacademy.org/",
    "https://www.coursera.org/",
    "https://www.udemy.com/",
    "https://www.edx.org/",
    "https://www.duolingo.com/",
    "https://www.vimeo.com/",
    "https://www.ted.com/",
    "https://www.wattpad.com/",
    "https://www.soundcloud.com/",
    "https://www.last.fm/",
    "https://www.imdb.com/",
    "https://www.rottentomatoes.com/",
    "https://www.hulu.com/",
    "https://www.etsy.com/",
    "https://www.canva.com/",
    "https://www.behance.net/",
    "https://www.dribbble.com/",
    "https://www.producthunt.com/",
    "https://www.digitalocean.com/",
    "https://www.heroku.com/",
    "https://www.gitlab.com/",
    "https://www.bitbucket.org/",
    "https://www.sourcetreeapp.com/",
    "https://www.cloudflare.com/",
    "https://www.codecademy.com/",
    "https://www.pluralsight.com/",
    "https://www.lynda.com/",
    "https://www.screencast.com/",
    "https://www.techcrunch.com/",
    "https://www.theverge.com/",
    "https://www.engadget.com/",
    "https://www.gizmodo.com/",
    "https://www.huffpost.com/",
    "https://www.buzzfeed.com/",
    "https://www.wired.com/",
    "https://www.lifehacker.com/",
    "https://www.mashable.com/",
    "https://www.vice.com/",
    "https://www.ign.com/",
    "https://www.gamespot.com/",
    "https://www.polygon.com/",
    "https://www.cnet.com/",
    "https://www.weather.com/",
    "https://www.accuweather.com/",
    "https://www.reuters.com/",
    "https://www.bloomberg.com/",
    "https://www.marketwatch.com/",
    "https://www.nationalgeographic.com/",
    "https://www.history.com/",
    "https://www.discovery.com/",
    "https://www.scientificamerican.com/",
    "https://www.livescience.com/",
    "https://www.space.com/",
    "https://www.howstuffworks.com/",
    "https://www.nasa.gov/",
    "https://www.un.org/",
    "https://www.who.int/",
    "https://www.worldbank.org/",
    "https://www.imf.org/",
    "https://www.wto.org/",
    "https://www.oecd.org/",
    "https://www.weforum.org/",
    "https://www.unicef.org/",
    "https://www.amnesty.org/",
    "https://www.greenpeace.org/"
]

def fetch_page(url):
    # Configuração do WebDriver (no caso, Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa o Chrome em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(options=options)

    start_time = time.time()  # Marca o início da requisição

    try:
        # Acessa a página
        driver.get(url)
        print(f"Página carregada: {url}")

        # Faça qualquer ação que desejar na página aqui
        time.sleep(2)  # Simula um tempo de espera para cada requisição

    finally:
        # Fecha o driver
        driver.quit()

    end_time = time.time()  # Marca o fim da requisição
    print(f"Tempo de execução para {url}: {end_time - start_time:.2f} segundos")
    return end_time - start_time

# Marca o início da execução sequencial
total_start_time = time.time()

# Executa cada URL de forma sequencial
times = [fetch_page(url) for url in urls]

# Marca o fim da execução sequencial
total_end_time = time.time()
total_execution_time = total_end_time - total_start_time

print(f"\nTempo total de execução sequencial: {total_execution_time:.2f} segundos")
print(f"Maior tempo de execução individual: {max(times):.2f} segundos")
