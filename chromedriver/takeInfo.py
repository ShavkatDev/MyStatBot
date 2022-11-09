def main():
    from bs4 import BeautifulSoup

    with open("index.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "lxml")

    name = soup.find("a", "fio-stud").text
    placeOnGroup = soup.find("div", "rating-position").text
    score = soup.find(id="all-pricess").text
    gems = soup.find(id="all-christal").text
    coins = soup.find(id="all-coin").text
    badges = soup.find(id="all-badges").text

    getInfo = [name, placeOnGroup, score, gems, coins, badges]

    return getInfo
