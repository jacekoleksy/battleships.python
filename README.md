# Project battleships.py 
![Algorithm schema](./images/battleships.png)

* [General Info](#general-info "Goto General Info")
* [Technologies](#technologies "Goto General Technologies")
* [Setup](#setup "Goto General Steup")
* [Description](#description "Goto General Description")

## General Info
Projekt polega na napisaniu gry Statki o ogólnych założeniach:
* Opis zadania:
	* [x] 1. Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz przyciskiem rozpoczęcia gry i przyciskiem reset. 
	* [x] 2. Na początku gracz rozmieszcza okręty (1x czteromasztowiec, 2x trójmasztowiec, 3x dwumasztowiec, 4x jednomasztowiec). 
	* [x] 3. Po rozmieszczeniu okrętów przez gracza i wciśnięciu przycisku nowej gry przeciwnik komputerowy losowo rozmieszcza swoje okręty. 
	* [x] 4. Okręty nie mogą się dotykać ani bokami ani rogami. 
	* [x] 5. Po rozmieszczeniu okrętów przez obu graczy jeden z nich wykonuje pierwszy ruch (losowo gracz lub komputer). 
	* [x] 6. Wybór celu przez gracza następuje przez kliknięcie pola, w razie trafienia przycisk staje się czerwony, w przeciwnym razie niebieski (nie można strzelić dwa razy w to samo pole). 
	* [x] 7. Komputer strzela w losowe, nie wybrane wcześniej pole. Po trafieniu próba znalezienia orientacji statku i zestrzelenie go do końca. 
	* [x] 8. Gra kończy się gdy któryś gracz straci ostatni okręt, wyświetlane jest okno z informacją o zwycięzcy (np. "wygrana!", "Przegrana!"). 
	* [x] 9. Opcjonalnie: bardziej zaawansowana sztuczna inteligencja omijająca pola na których na pewno nie może znaleźć się okręt gracza. 
	
* Testy:
	* [x] 1. Próba niepoprawnego ustawienia okrętu (stykanie się bokami lub rogami). Oczekiwana informacja o błędzie
	* [x] 2. Poprawne rozmieszczenie wszystkich okrętów przez gracza i wciśnięcie przycisku rozpoczęcia gry. 
	* [x] 3. Strzelenie w puste pole. 
	* [x] 4. Trafienie w okręt przeciwnika. 
	* [x] 5. Próba zestrzelenia swojego okrętu - oczekiwane niepowodzenie. 
	* [x] 6. Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie. 
	* [x] 7. Próba ponownego strzelenia w okręt przeciwnika - oczekiwane niepowodzenie. 
	* [x] 8. Rozmieszczenie części okrętów, wciśnięcie przycisku reset - oczekiwany reset plansz. 
	* [x] 9. Poprawne rozmieszczenie wszystkich okrętów, oddanie kilku strzałów, rozpoczęcie nowej gry, ponowne poprawne rozmieszczenie okrętów, oddanie strzałów w te same pola. 
	* [x] 10. Wygranie gry (np. Przez pokazanie okrętów przeciwnika). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 
	* [x] 11. Przegranie gry (np. Przez aktywację super-instynktu gracza komputera). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 

## Technologies
Project is created with:
* Python version: 3.8
* Tkinter version: 8.6.9

## Setup
To run this project, just download and extract all files

## Description
Wykonanie całej gry od zera, zajęło mi zaledwie 5 dni, a tak naprawdę najwięcej czasu zajęło mi robienie grafiki, dobieranie koloru i szeroko pojęty wygląd aplikacji.
Wszystkie podpunkty z [Opisu zadania](#general-info "Goto General Info") oraz [Testów](#testy "Goto General Info")

![image](https://user-images.githubusercontent.com/47715648/118708950-a9112400-b81c-11eb-87e0-fa74e791d70b.png)
