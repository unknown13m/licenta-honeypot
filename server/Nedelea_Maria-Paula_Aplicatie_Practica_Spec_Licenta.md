Sistem de detecție și analiză a atacurilor cibernetice bazat pe tehnologia honeypot


Codul sursă al proiectului este disponibil la adresa:

https://github.com/unknown13m

Repository-ul este public și conține codul sursă al aplicației.

Proiectul implementează un sistem honeypot pentru detecția și analiza atacurilor cibernetice. Sistemul conține o infrastructură Docker, un honeypot SSH bazat pe Cowrie, un honeypot medical pe portul 104, o bază de date MongoDB și o aplicație web de tip dashboard dezvoltată în .NET/C#.

Componente principale:
- server/docker-compose.yml (definește serviciile Docker);
- server/Dockerfile (construiește imaginea pentru honeypot-ul medical);
- server/fisierscript.py (colectează și prelucrează log-urile);
- dashoneypot (aplicația web .NET/C#);
- MongoDB (stochează evenimentele în colecția "attacks").


Pe serverul cloud sunt necesare:
- Docker;
- Docker Compose;
- Python 3;
- biblioteca "pymongo".

Instalarea bibliotecii Python: in bash, "pip install pymongo".

Pentru aplicația web sunt necesare:

- .NET SDK;
- Visual Studio Code sau Visual Studio;
- conexiune la baza de date MongoDB de pe serverul cloud.

Repository-ul se descarcă local prin comanda:

git clone https://github.com/unknown13m/licenta-honeypot.git

Apoi se accesează directorul proiectului:

cd licenta-honeypot

Fișierele din folderul server trebuie copiate pe serverul cloud, în directorul:

/root/licenta



Pe serverul cloud se accesează directorul proiectului:

cd /root/licenta

Pornirea containerelor se face prin comanda:

docker compose up -d

Verificarea containerelor active se face prin:

docker ps

Containerele principale ale sistemului sunt:

licenta-honeypot-ssh-1
licenta-honeypot-medical-1
licenta-honeypot-db-mongo-1
licenta-honeypot-db-postgres-1
licenta-honeypot-vnc-1

Serviciile expuse sunt:

SSH honeypot Cowrie: port public 22 -> port intern 2222
Honeypot medical: port 104 -> port 104
MongoDB: port 27017 -> port 27017
PostgreSQL: port 5432 -> port 5432
VNC: port 5900 -> port 5900

Accesul administrativ real la server se face separat, prin portul 2221.
Scriptul Python se rulează pe serverul cloud din directorul /root/licenta.
Comanda de rulare directă este: python3 fisierscript.py.
Pentru rularea în fundal se folosește: nohup python3 fisierscript.py &.

Scriptul colectează logurile din containere, procesează evenimentele SSH și DICOM/Medical și le salvează în baza de date MongoDB, în baza de date honeypot_db și în colecția attacks.

Aplicația web se află în folderul "dashoneypot".

Pentru compilare, se deschide un terminal în directorul proiectului și se rulează:

cd dashoneypot
dotnet restore
dotnet build

Comanda dotnet restore descarcă dependențele necesare, iar dotnet build compilează aplicația.

Aplicația web se pornește local prin comanda: dotnet run.

După pornire, dashboard-ul poate fi accesat în browser la adresa:

http://localhost:5000

Aplicația se conectează la MongoDB, citește evenimentele salvate în colecția attacks și le afișează în interfața web.

Dashboard-ul permite:

vizualizarea numărului total de evenimente;
vizualizarea atacurilor SSH;
vizualizarea evenimentelor DICOM/Medical;
afișarea ultimelor evenimente înregistrate;
analiza atacatorilor grupați după IP;
afișarea detaliilor brute pentru fiecare eveniment.

Fișierul docker-compose.yml definește serviciile Docker ale proiectului: Cowrie SSH, honeypot medical, MongoDB, PostgreSQL, VNC, Dockerfile.

Construiește imaginea Docker pentru honeypot-ul medical de pe portul 104.


Fișierul fisierscript.py colectează logurile din containere, filtrează evenimentele relevante și salvează datele în MongoDB.

Fișierul grab_logs.sh este un script auxiliar pentru lucrul cu logurile.

Fișierul Program.cs configurează aplicația web .NET/C# și conexiunea la baza de date MongoDB.

Fișierul Index.cshtml se ocupă cu pagina principală a dashboard-ului.

Fișierul Analytics.cshtml: pagina pentru analiza atacatorilor grupați după IP.

Fișierul Details.cshtml este pentru pagina responsabilă de afișarea detaliilor brute ale unui eveniment individual.








