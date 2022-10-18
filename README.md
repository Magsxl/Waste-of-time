# **Waste-of-time**

## *Analiza stanu wiedzy:*
### 1. [Pierwszy artykuł](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiLhYH4wer6AhVN6CoKHX7gCToQFnoECA0QAQ&url=https%3A%2F%2Fwww.mdpi.com%2F2071-1050%2F14%2F16%2F10226%2Fpdf%3Fversion%3D1660737939&usg=AOvVaw2gwoqcSkbKwttH8brH17_p):
  * Najpierw mapują obraz na siatkowej, komórkowej strukturze - macierzy, którą następnie konwertują na skalę szarości
  * Zdjęcie jest segmentowane na komórki za pomocą VGG-16, każda komórka jest przetwarza w celu wstępnego uzyskania pojedynczych śmieci w przybliżeniu
  * Następnie każda komórka jest oddzielnie przetwarzana w celu jak najdokładniejszego rozpoznania śmiecia
  * Korzystają z VGG-16, czyli 16 poziomowej konwolucyjnej sieci neuronowej
  * Podział smieci na plastik, szkło, papier, metal, trash(unknown). Dzięki temu uzyskują największą dokładność wynoszącą 96.1%
  * etc
-
## *Wymagania pozafunkcjonalne:*
-
-
-
-
## *Wymagania funkcjonalne:*
-
-
-
-
