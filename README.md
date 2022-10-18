# **Waste-of-time**

## *Analiza stanu wiedzy:*
### 1. [Pierwszy artykuł](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiLhYH4wer6AhVN6CoKHX7gCToQFnoECA0QAQ&url=https%3A%2F%2Fwww.mdpi.com%2F2071-1050%2F14%2F16%2F10226%2Fpdf%3Fversion%3D1660737939&usg=AOvVaw2gwoqcSkbKwttH8brH17_p):
  * Najpierw mapują obraz na siatkowej, komórkowej strukturze - macierzy, którą następnie konwertują na skalę szarości
  * Zdjęcie jest segmentowane na komórki za pomocą VGG-16, każda komórka jest przetwarza w celu wstępnego uzyskania pojedynczych śmieci w przybliżeniu
  * Następnie każda komórka jest oddzielnie przetwarzana w celu jak najdokładniejszego rozpoznania śmiecia
  * Na każdą z kategorii wykorzystują ok. 500 zdjęć
  * Korzystają z VGG-16, czyli 16 poziomowej konwolucyjnej sieci neuronowej
  * Liczba "epochów" (cokolwiek to jest xd) potrzebna do wytrenowania modelu to około 100 (prawdopodobnie to jakieś iteracje po zdjęciach czy coś takiego
  * Podział śmieci na plastik, szkło, papier, metal, trash(unknown). Dzięki temu uzyskują największą dokładność wynoszącą 96.1%
### 2. [Drugi artykuł](https://www.nature.com/articles/s41598-022-06146-2#Abs1)
  * Nature.com hohoho
  * Twórcy prawią o rozpoznawaniu medycznych odpadów (ibm u know biomed medmed, zesra się tam)
  * Do nauki modelu wykorzystują ResNeXt, uzyskują dokładność 97.2%
## *Wymagania pozafunkcjonalne:*
- aplikacja webowa: Flask/FastAPI
-
-
-
## *Wymagania funkcjonalne:*
- Klient WWW wysyła zdjęcie do serwera
- Serwer pobiera zdjęcie i uruchamia model uczenia głębokiego do klasyfikacji odpadów
- Serwer przesyła JSONa do klienta
- Klient wyświetla zdjęcie wraz z przypisaną klasą danego odpadu
- Obsługa REST i wielu klientów
