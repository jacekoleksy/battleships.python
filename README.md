# Project battleships.py 
![Algorithm schema](./images/battleships.png)

* [General Info](#general-info "Goto General Info")
* [Description](#description "Goto General Description")
* [Technologies](#technologies "Goto General Technologies")
* [Setup](#setup "Goto General Steup")

## General Info
Projekt polega na napisaniu gry Statki o ogólnych założeniach:
* Opis zadania:
	* [x] 1. Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz przyciskiem rozpoczęcia gry i przyciskiem reset. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L114-L117 "Goto")
	* [x] 2. Na początku gracz rozmieszcza okręty (1x czteromasztowiec, 2x trójmasztowiec, 3x dwumasztowiec, 4x jednomasztowiec). [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L118 "Goto")
	* [x] 3. Po rozmieszczeniu okrętów przez gracza i wciśnięciu przycisku nowej gry przeciwnik komputerowy losowo rozmieszcza swoje okręty. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L196-L217 "Goto")
	* [x] 4. Okręty nie mogą się dotykać ani bokami ani rogami. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L124-L129 "Goto")
	* [x] 5. Po rozmieszczeniu okrętów przez obu graczy jeden z nich wykonuje pierwszy ruch (losowo gracz lub komputer). [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/app.py#L294-L303 "Goto")
	* [x] 6. Wybór celu przez gracza następuje przez kliknięcie pola, w razie trafienia przycisk staje się czerwony, w przeciwnym razie niebieski (nie można strzelić dwa razy w to samo pole). [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/app.py#L314-L348 "Goto")
	* [x] 7. Komputer strzela w losowe, nie wybrane wcześniej pole. Po trafieniu próba znalezienia orientacji statku i zestrzelenie go do końca. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L256-L285 "Goto")
	* [x] 8. Gra kończy się gdy któryś gracz straci ostatni okręt, wyświetlane jest okno z informacją o zwycięzcy (np. "wygrana!", "Przegrana!"). [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/app.py#L350-L384 "Goto")
	* [x] 9. Opcjonalnie: bardziej zaawansowana sztuczna inteligencja omijająca pola na których na pewno nie może znaleźć się okręt gracza. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d2d4c55d3eb90bdc9926d0d0f29ec8a9969dc2a7/battleships.py#L256-L288 "Goto")
	
* Testy:
	* [x] 1. Próba niepoprawnego ustawienia okrętu (stykanie się bokami lub rogami). Oczekiwana informacja o błędzie [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L10-L35 "Goto")
	* [x] 2. Poprawne rozmieszczenie wszystkich okrętów przez gracza i wciśnięcie przycisku rozpoczęcia gry. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L37-L62 "Goto")
	* [x] 3. Strzelenie w puste pole. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L64-L98 "Goto")
	* [x] 4. Trafienie w okręt przeciwnika. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L100-L134 "Goto")
	* [x] 5. Próba zestrzelenia swojego okrętu - oczekiwane niepowodzenie. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L136-L171 "Goto")
	* [x] 6. Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L173-L211 "Goto")
	* [x] 7. Próba ponownego strzelenia w okręt przeciwnika - oczekiwane niepowodzenie. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L213-L251 "Goto")
	* [x] 8. Rozmieszczenie części okrętów, wciśnięcie przycisku reset - oczekiwany reset plansz. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L253-L286 "Goto")
	* [x] 9. Poprawne rozmieszczenie wszystkich okrętów, oddanie kilku strzałów, rozpoczęcie nowej gry, ponowne poprawne rozmieszczenie okrętów, oddanie strzałów w te same pola. [`code1`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L288-L335 "Goto")
	* [x] 10. Wygranie gry (np. Przez pokazanie okrętów przeciwnika). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L337-L386 "Goto")
	* [x] 11. Przegranie gry (np. Przez aktywację super-instynktu gracza komputera). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. [`code`](https://github.com/jacekoleksy/battleships.python/blob/d86f5133a04675f244a8a4136dbdb244aa075492/test.py#L388-L438 "Goto")

* Wymagane konstrukcje:
	* [x] 1. Wyrażenia lambda <br/>[`code1`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/app.py#L121 "Goto") [`code2`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/app.py#L129 "Goto") [`code3`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/app.py#L195 "Goto")
	* [x] 2. List comprehensions <br/>[`code1`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/battleships.py#L53-L61 "Goto") [`code2`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/battleships.py#L67-L81 "Goto") [`code3`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/battleships.py#L116 "Goto")
	* [x] 3. Wyjątki <br/>[`code1`](https://github.com/jacekoleksy/battleships.python/blob/6486582cdcc28c33d141a93ceda200d275c50232/app.py#L446-L464 "Goto") [`error`](https://github.com/jacekoleksy/battleships.python/blob/6486582cdcc28c33d141a93ceda200d275c50232/app.py#L250-L263 "Goto")
	* [x] 4/5. Moduły i klasy: cała gra znajduje się w dwóch plikach:
		* app.by - Odpowiedzialnej z caly interfejs graficzny i wykonywanie czynności w dobrej kolejności
		* battleships.py - Odpowiedzialnej za obliczanie, walidację i logikę aplikacji
		
		W module app.by jest tylko jedna klasa [`Application`](https://github.com/jacekoleksy/battleships.python/blob/6486582cdcc28c33d141a93ceda200d275c50232/app.py#L13 "Goto"), której wszystkie pola są prywatne.
		W module battleships.py jest również klasa [`RandomBoard`](https://github.com/jacekoleksy/battleships.python/blob/3397dbcd9a3e9de246cfffa3428dbae665e844ac/battleships.py#L196-L217 "Goto"), która dziedziczy po klasie `Board`. Podobnie było wstępnie z klasą dla gracza, jednak nie było sensu implementować

## Description
Wykonanie całej gry od zera, zajęło mi zaledwie 5 dni, a tak naprawdę najwięcej czasu zajęło mi robienie grafiki, dobieranie koloru i szeroko pojęty wygląd aplikacji.

Od razu nadmienię, że program nie jest najbardziej optymalną wersją na jaką było mnie stać: chociażby zamiast ustawiać `command=''` dla przycisków po tym jak nie można ich już kliknąć - wolałem użyć metody `destroy()`, aby przyciski zniknęły, po czym znowu (jeśli będą potrzebne) wyświetlić je (wszystko po to, aby nie wyświetlały się przyciski których nie można użyć). Tak samo grafika aktualnie stawianego statku - zamiast obracać jeden obraz o 90° - stworzyłem 4 różne, aby nie zmieniać każdorazowo położenia obrazka (x, y).

Wszystkie podpunkty z [Opisu zadania](#general-info "Goto General Info") zawarłem w programie, a [Testy](#general-info "Goto General Info") wszystkie przechodzą pozytywnie.

Swój program rozwinąłem o dodatkowe funkcjonalności:
* Dodanie funkcjonalności trafiony-zatopiony, która pomaga graczowi oraz przeciwnikowi, aby przypadkowo nie strzelił w pola, na których nie może być juz statku [`code`](https://github.com/jacekoleksy/battleships.python/blob/092d2bc3a9c70c24b28bf1b8199a6e9e531ca640/battleships.py#L161-L169 "Goto")
* Ulepszona sztuczna inteligencja, która po trafieniu i nie zatopieniu statku - strzela losowo w jedno z 4ch sąsiadujących pól, po czym jeśli trafi 2gi raz i nie zatopi - szuka orientacji statku (ma w tym przypadku juz tylko 2 pola do wyboru). Po zatopieniu statku AI oznacza pola dookoła jako te, w które już nie będzie strzelać. Sprawiło to, że mimo dużej losowości gry Statki - potrafiłem przegrać po 10 razy pod rząd [`code`](https://github.com/jacekoleksy/battleships.python/blob/092d2bc3a9c70c24b28bf1b8199a6e9e531ca640/battleships.py#L256-L288 "Goto")
* Mozliwość losowego, poprawnego ustawienia statków na własnej planszy (możliwe po naciśnięciu przycisku Start, w trakcie rozstawiania statków i po resecie lub zakończeniu gry) [`code`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/app.py#L166-L177 "Goto")
* Dzięki użyciu `self.__root.update()` i `time.sleep(0.5)` umożliwiłem, zakolejkowanie ruchów od ostatniego do pierwszego zaznaczonego, co sprawiło, że gra może przebiegać szybciej, jednocześnie nie sprawiając, że przeciwnik (AI) zostaje w tyle [`code`](https://github.com/jacekoleksy/battleships.python/blob/492f9faea3105d48c24f7a6594ad9708cd7fd037/app.py#L315-L317 "Goto")
* Możliwość ustawienia orientacji statku, od klikniętego pola (kierunki: NESW) oraz wyswietlenie ile aktualnie statków zostało do rozstawienia i jakiego typu:

![image](https://user-images.githubusercontent.com/47715648/118711331-c1cf0900-b81f-11eb-9e61-0bfd4feb9ccf.png)

* Dodanie własnych grafik, zorientowanych w poziomie lub pionie, w zależności od orientacji statku:

![image](https://user-images.githubusercontent.com/47715648/118708950-a9112400-b81c-11eb-87e0-fa74e791d70b.png)

* Po porażce - pokazanie, jak wygląda plansza przeciwnika (odsłonięcie nietrafionych statków, oraz wyświetlenie ikonki podpalonego statku ![image](https://user-images.githubusercontent.com/47715648/118712514-2ccd0f80-b821-11eb-80db-61a44cdf7a86.png)
 zamiast ikonki trafionego strzału ![image](https://user-images.githubusercontent.com/47715648/118712427-1030d780-b821-11eb-9fbb-e36e5f7a0b80.png):

![image](https://user-images.githubusercontent.com/47715648/118712388-05764280-b821-11eb-87df-7b045e3cb100.png)

![image](https://user-images.githubusercontent.com/47715648/118712052-9993da00-b820-11eb-9394-2c987de6afb9.png)

* W grze na dole ekranu jest również pasek powiadomień, oto przykładowe komendy, które wyświetla:

![image](https://user-images.githubusercontent.com/47715648/118859238-4f6f2f00-b8da-11eb-9f48-eb9dbaa56cbb.png)
![image](https://user-images.githubusercontent.com/47715648/118859284-5b5af100-b8da-11eb-996c-829121f0ec16.png)
![image](https://user-images.githubusercontent.com/47715648/118859322-644bc280-b8da-11eb-8621-b775e9e6dc4b.png)
![image](https://user-images.githubusercontent.com/47715648/118859365-6f065780-b8da-11eb-9f2d-7852b116ed5f.png)
![image](https://user-images.githubusercontent.com/47715648/118859492-952bf780-b8da-11eb-939d-b6ce7d4882cf.png)


## Technologies
Project is created with:
* Python version: 3.8
* Tkinter version: 8.6.9

## Setup
To run this project, just download and extract all files
