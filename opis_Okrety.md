Jacek Oleksy 134138 GL05
Link do repozytorium: https://github.com/jacekoleksy/battleships.python
14. Okręty (https://131.wikiDedia.org/wiki/Okr%C4%99ty) 
Opis zadania 
	o Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz przyciskiem rozpoczęcia gry i przyciskiem reset. 
	o Na początku gracz rozmieszcza okręty (1x czteromasztowiec, 2x trójmasztowiec, 3x dwumasztowiec, 4x jednomasztowiec). 
	o Po rozmieszczeniu okrętów przez gracza i wciśnięciu przycisku nowej gry przeciwnik komputerowy losowo rozmieszcza swoje okręty. 
	o Okręty nie mogą się dotykać ani bokami ani rogami. 
	o Po rozmieszczeniu okrętów przez obu graczy jeden z nich wykonuje pierwszy ruch (losowo gracz lub komputer). 
	o Wybór celu przez gracza następuje przez kliknięcie pola, w razie trafienia przycisk staje się czerwony, w przeciwnym razie niebieski (nie można strzelić dwa razy w to samo pole). 
	o Komputer strzela w losowe, nie wybrane wcześniej pole. Po trafieniu próba znalezienia orientacji statku i zestrzelenie go do końca. 
	o Gra kończy się gdy któryś gracz straci ostatni okręt, wyświetlane jest okno z informacją o zwycięzcy (np. `wygrana!", "Przegrana!"). 
	o Opcjonalnie: bardziej zaawansowana sztuczna inteligencja omijająca pola na których na pewno nie może znaleźć się okręt gracza. 
Testy 
	1. Próba niepoprawnego ustawienia okrętu (stykanie się bokami lub rogami). Oczekiwana informacja o błędzie 
	2. Poprawne rozmieszczenie wszystkich okrętów przez gracza i wciśnięcie przycisku rozpoczęcia gry. 
	3. Strzelenie w puste pole. 
	4. Trafienie w okręt przeciwnika. 
	5. Próba zestrzelenia swojego okrętu - oczekiwane niepowodzenie. 
	6. Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie. 
	7. Próba ponownego strzelenia w okręt przeciwnika - oczekiwane niepowodzenie. 
	8. Rozmieszczenie części okrętów, wciśnięcie przycisku reset - oczekiwany reset plansz. 
	9. Poprawne rozmieszczenie wszystkich okrętów, oddanie kilku strzałów, rozpoczęcie nowej gry, ponowne poprawne rozmieszczenie okrętów, oddanie strzałów w te same pola. 
	10. Wygranie gry (np. Przez pokazanie okrętów przeciwnika). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 
	11. Przegranie gry (np. Przez aktywację super-instynktu gracza komputera). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 
