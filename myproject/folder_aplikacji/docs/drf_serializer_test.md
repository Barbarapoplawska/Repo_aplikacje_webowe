from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Tworzenie nowych obiektów
stanowisko = Stanowisko.objects.create(nazwa="Kierownik", opis="Zarządza tymi, co zarządzają")
osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec=2, stanowisko=stanowisko)

# Inicjacja serializera dla Osoby
osoba_serializer = OsobaSerializer(osoba)
print("Dane serializowane (Osoba):", osoba_serializer.data)

# Renderowanie danych do formatu JSON
osoba_json = JSONRenderer().render(osoba_serializer.data)
print("Dane JSON (Osoba):", osoba_json)

# Strumień danych JSON
stream = io.BytesIO(osoba_json)

# Parsowanie JSON-a do słownika
data = JSONParser().parse(stream)

# Tworzenie obiektu deserializera dla danych JSON
deserializer = OsobaSerializer(data=data)

# Walidacja danych
if deserializer.is_valid():
    print("Dane są poprawne:")
    print(deserializer.validated_data)
else:
    print("Błędy walidacji (Osoba):")
    print(deserializer.errors)

# Próba zapisu z błędnymi danymi
invalid_data = {
    'imie': 'Adam',
    'nazwisko': 'Nowak',
    'plec': 'Nieznana',  # Nieprawidłowa wartość
    'stanowisko': stanowisko.id  # Poprawne ID stanowiska
}
invalid_serializer = OsobaSerializer(data=invalid_data)

if invalid_serializer.is_valid():
    print("Dane są poprawne (nieoczekiwane):")
    print(invalid_serializer.validated_data)
else:
    print("Błędy walidacji (Błędne dane):")
    print(invalid_serializer.errors)

# Walidacja poprawnych danych
if deserializer.is_valid():
    deserializer.save()

# Inicjacja stanowiska dla serializera
stanowisko_serializer = StanowiskoSerializer(stanowisko)
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print("Dane JSON (Stanowisko):", stanowisko_json)

# Deserializacja JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

# Tworzenie obiektu deserializera dla Stanowiska
stanowisko_deserializer = StanowiskoSerializer(data=data)

if stanowisko_deserializer.is_valid():
    print("Dane stanowiska są poprawne:")
    print(stanowisko_deserializer.validated_data)
    stanowisko_deserializer.save()
else:
    print("Błędy walidacji (Stanowisko):")
    print(stanowisko_deserializer.errors)
