import csv
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


class Product:
    """Repräsentiert ein Produkt aus dem Produktkatalog."""

    def __init__(self, name: str, prices: list[float], description: str, category: str):
        """Initialisiert ein neues Produkt.

        Args:
          name (str): Name des Produkts.
          prices (list[float]): Liste mit den Preisen des Produkts. Das Element an erster Position
            ist der Preis des Produkts am ersten Tag, das Element an zweiter Position ist der Preis
            des Produkts am zweiten Tag, etc.
          description (str): Beschreibung des Produkts.
          category (str): Kategorie des Produkts.
        """
        self.__name = name
        self.__prices = prices
        self.__description = description
        self.__category = category

    @property
    def name(self) -> str:
        """Name des Produkts"""
        return self.__name

    @property
    def prices(self) -> list[float]:
        """Liste mit den Preisen des Produkts."""
        return self.__prices

    @property
    def description(self) -> str:
        """Beschreibung des Produkts"""
        return self.__description

    @property
    def category(self) -> str:
        """Kategorie des Produkts"""
        return self.__category


def init_soup(url: str) -> BeautifulSoup:
    """Initialisiert ein BeautifulSoup-Objekt mit dem Inhalt einer Website.

    Args:
        url (str): URL der Website
    Returns:
        BeautifulSoup: BeautifulSoup-Objekt mit der Baumstruktur der spezifizierten Website
    Raises:
        Exception: Falls der HTTP-Request nicht erfolgreich war
    """
    r = requests.get(url)

    if not r.ok:
        raise Exception(
            f"HTTP-Request nicht erfolgreich. Hast Du den Webserver gestartet? Status-Code: {r.status_code}"
        )

    return BeautifulSoup(r.content, "html.parser")


# TODO: Schreibt hier euren Code für die Aufgabe
class Differences:
    def __init__(self, name:str, description:str, category:str, price_day1:int, price_day2:int, price_difference_absolut:int, price_procent:int):
        self.name = name
        self.description = description
        self.category = category
        self.price_day1 = price_day1
        self.price_day2 = price_day2
        self.price_difference_absolut = price_difference_absolut
        self.price_procent = price_procent

def read_create_array_and_parse(url:str) -> Product:
    content = init_soup(url=url)

    '''    
    print(content_day_one)
    print(content_day_two)
    '''
    

    array_content = content.find_all("div", class_="product")


    #print(array_content[0])

    product = []

    for i in array_content:
        name = i.find("h2", class_="product-name").text.strip()
        price = float(i.find("span", class_="price-number").text)
        description = i.find("p", class_="product-description").text.strip()
        category = i.find("p", class_="product-category").text.strip()

        product.append(Product(name=name,prices=price,description=description,category=category))

    return product

    ''' output vom parse
</head>
<body>
<div class="product-container">
<div class="product">
<h2 class="product-name">Bergsteiger Rucksack</h2>
<p class="product-price"><span class="price-number">49.95</span> CHF</p>
<p class="product-description">Robuster Rucksack ideal für Wanderungen und Tagestouren</p>
<p class="product-category">Outdoor</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Organischer Dünger</h2>
<p class="product-price"><span class="price-number">15.50</span> CHF</p>
<p class="product-description">Natürlicher Dünger für Pflanzen und Garten</p>
<p class="product-category">Garten</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Keramik-Teetasse</h2>
<p class="product-price"><span class="price-number">9.90</span> CHF</p>
<p class="product-description">Handgefertigte Teetasse aus hochwertiger Keramik</p>
<p class="product-category">Haushalt</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Digitale Armbanduhr</h2>
<p class="product-price"><span class="price-number">120.00</span> CHF</p>
<p class="product-description">Wasserdichte Armbanduhr mit vielen digitalen Funktionen</p>
<p class="product-category">Accessoires</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Yoga-Matte</h2>
<p class="product-price"><span class="price-number">35.00</span> CHF</p>
<p class="product-description">Rutschfeste Yoga-Matte für alle Arten von Yoga</p>
<p class="product-category">Sport</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Bluetooth-Lautsprecher</h2>
<p class="product-price"><span class="price-number">59.50</span> CHF</p>
<p class="product-description">Kompakter, kraftvoller Lautsprecher mit Bluetooth-Verbindung</p>
<p class="product-category">Elektronik</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Veganes Kochbuch</h2>
<p class="product-price"><span class="price-number">24.95</span> CHF</p>
<p class="product-description">Über 100 vegane Rezepte für gesunde und leckere Gerichte</p>
<p class="product-category">Bücher</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">LED Schreibtischlampe</h2>
<p class="product-price"><span class="price-number">29.50</span> CHF</p>
<p class="product-description">Energieeffiziente LED-Lampe mit einstellbarer Helligkeit</p>
<p class="product-category">Büro</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Wandkalender 2024</h2>
<p class="product-price"><span class="price-number">14.50</span> CHF</p>
<p class="product-description">Großer Wandkalender midst beeindruckenden Landschaftsfotos</p>
<p class="product-category">Papierwaren</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Isolierkanne</h2>
<p class="product-price"><span class="price-number">19.95</span> CHF</p>
<p class="product-description">Hält Getränke stundenlang warm oder kalt</p>
<p class="product-category">Haushalt</p>
<p class="product-available">Auf Lager</p>
</div>
</div>
</body>
</html>


<!DOCTYPE html>

<html>
<head>
<meta charset="utf-8"/>
<title>Produktkatalog</title>
<style>
        body { font-family: Arial, sans-serif; }
        .product-container { display: flex; flex-wrap: wrap; justify-content: space-around; padding: 10px; }
        .product { box-sizing: border-box; width: 30%; margin: 10px 0; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        .product-name { font-size: 24px; color: #333; }
        .product-price { font-size: 18px; color: #c80000; font-weight: bold; }
        .product-description { font-size: 16px; color: #444; }
        .product-category { font-size: 14px; color: #666; }
        .product-available { font-size: 14px; color: #12ca1c; }
        .product-not-available { font-size: 14px; color: #FF4500; }
        .price-number { font-family: monospace; }
    </style>
</head>
<body>
<div class="product-container">
<div class="product">
<h2 class="product-name">Bergsteiger Rucksack</h2>
<p class="product-price"><span class="price-number">49.95</span> CHF</p>
<p class="product-description">Robuster Rucksack ideal für Wanderungen und Tagestouren</p>
<p class="product-category">Outdoor</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Organischer Dünger</h2>
<p class="product-price"><span class="price-number">15.50</span> CHF</p>
<p class="product-description">Natürlicher Dünger für Pflanzen und Garten</p>
<p class="product-category">Garten</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Keramik-Teetasse</h2>
<p class="product-price"><span class="price-number">10.20</span> CHF</p>
<p class="product-description">Handgefertigte Teetasse aus hochwertiger Keramik</p>
<p class="product-category">Haushalt</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Digitale Armbanduhr</h2>
<p class="product-price"><span class="price-number">115.00</span> CHF</p>
<p class="product-description">Wasserdichte Armbanduhr mit vielen digitalen Funktionen</p>
<p class="product-category">Accessoires</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Yoga-Matte</h2>
<p class="product-price"><span class="price-number">35.00</span> CHF</p>
<p class="product-description">Rutschfeste Yoga-Matte für alle Arten von Yoga</p>
<p class="product-category">Sport</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Bluetooth-Lautsprecher</h2>
<p class="product-price"><span class="price-number">59.50</span> CHF</p>
<p class="product-description">Kompakter, kraftvoller Lautsprecher mit Bluetooth-Verbindung</p>
<p class="product-category">Elektronik</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Veganes Kochbuch</h2>
<p class="product-price"><span class="price-number">24.95</span> CHF</p>
<p class="product-description">Über 100 vegane Rezepte für gesunde und leckere Gerichte</p>
<p class="product-category">Bücher</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">LED Schreibtischlampe</h2>
<p class="product-price"><span class="price-number">29.50</span> CHF</p>
<p class="product-description">Energieeffiziente LED-Lampe mit einstellbarer Helligkeit</p>
<p class="product-category">Büro</p>
<p class="product-available">Auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Wandkalender 2024</h2>
<p class="product-price"><span class="price-number">14.50</span> CHF</p>
<p class="product-description">Großer Wandkalender mit beeindruckenden Landschaftsfotos</p>
<p class="product-category">Papierwaren</p>
<p class="product-not-available">Nicht auf Lager</p>
</div>
<div class="product">
<h2 class="product-name">Isolierkanne</h2>
<p class="product-price"><span class="price-number">20.50</span> CHF</p>
<p class="product-description">Hält Getränke stundenlang warm oder kalt</p>
<p class="product-category">Haushalt</p>
<p class="product-available">Auf Lager</p>
</div>
</div>
</body>
</html>
'''

def compare_prices(day_one:Product, day_two:Product) -> Differences:
    if day_one.name != day_two.name:
        print("not the same products (compare_prices)")
        raise ValueError
    price = round((day_one.prices - day_two.prices) *-1 ,2)
    print(day_one.name)
    print(day_one.prices, day_two.prices)
    print(price)
    procentage = round(((day_two.prices - day_one.prices) / day_one.prices) * 100,2)
    print(procentage)
    differences =Differences(name=day_one.name,description=day_one.description,category=day_one.category,price_day1=day_one.prices, price_day2=day_two.prices, price_difference_absolut=price,price_procent=procentage)
    return differences

def write_into_csv(difference:Differences):

    with open("products_reference.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Produkt", "Beschreibung", "Kategorie","Preis Tag 1 (in CHF)","Preis Tag 2 (in CHF)","Preisdifferenz (in CHF)","Preisdifferenz (in Prozent)"])
        for i in difference:
            writer.writerow([i.name, i.description, i.category,i.price_day1,i.price_day2,i.price_difference_absolut,i.price_procent])

listDayOne = read_create_array_and_parse("http://localhost:8080/Product_Catalog_Day_1.html")
listDayTwo = read_create_array_and_parse("http://localhost:8080/Product_Catalog_Day_2.html")

differences_list = []

for i in range(len(listDayOne)):
    differences_list.append(compare_prices(listDayOne[i],listDayTwo[i]))

write_into_csv(difference=differences_list)