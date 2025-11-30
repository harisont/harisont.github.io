---
title: "Fai-da-te digitale: riviste personali con Percollate"
date: 2025-11-30
layout: post
langs: ["en", "it"] 
---

###### __[in English](https://harisont.github.io/2025/11/30/hmm.html)__

{% include image.html file="../assets/img/hmm/hmm9_pb.png" description="Un post dal blog autonomin.fritext.org sul mio amato, enorme e-reader" %}

Tempo addietro, ho scritto sia della [splendida semplicità del protocollo RSS](https://harisont.github.io/translations/rss-it.html), sia della [pila infinita di contenuti che mi ha portata ad accumulare](https://harisont.github.io/2025/02/27/webruary.html).
Quest'anno, determinata a lasciarmi alle spalle la brutta abitudine di mettere da parte le cose senza leggerle, mi sono ingegnata per trovare una soluzione artigianale che, per il momento, sembra funzionare piuttosto bene: una rivista digitale personale fai-da-te.
L'idea di mettere assieme ogni nuovo numero solo una volta finito di leggere il precedente e sono già arrivata al nono.
In questo post, vi spiego come assemblo le mie riviste e come potete farlo facilmente anche voi.

Per prima cosa, serve un modo di trovare dei contenuti per la rivista. 
I feed RSS di tutta una serie di blog e siti di attualità sono tuttora le mie fonti principali, ma un sacco di cose interessanti mi arrivano anche da amici, familiari e colleghi su varie piattaforme di messaggistica e, da un paio di settimane, anche [Mastodon](https://mstdn.social/@harisont).

Ciò crea la necessità di avere un posto dove conservare temporaneamente i link provenienti dalle varie fonti. 
A questo scopo ho deciso di utilizzare [i segnalibri di Nextcloud](https://apps.nextcloud.com/apps/bookmarks), che mi permettono di sincronizzare diversi dispositivi, ma in molti casi un semplice file di testo è più che sufficiente.

Quando arriva il momento di creare un nuovo numero della rivista, apro il mio lettore RSS ([Newsflash](https://apps.gnome.org/NewsFlash/)) e compilo tutto in un singolo file.
Nel corso degli anni, ho testato vari metodi per trasformare un gruppo di pagine web in un ebook. 
Gira che ti rigira, ho scelto [Percollate](https://danburzo.ro/projects/percollate/), un programma open source che mi permette di creare degli EPUB più che presentabili con uno sforzo davvero minimo, direttamente dalla riga di comando.
Consiglio caldamente questa soluzione, ma se non vi sentiste a vostro agio con il terminale, potete saltare direttamente a [Creare riviste dal browser](#creare-riviste-dal-browser).


## Creare riviste dalla riga di comando (consigliato)

### Come installare Percollate
Se il vostro sistema operativo è Arch o uno qualsiasi dei suoi derivati, la cosa è facilissima: Percollate, come d'altronde quasi tutto il resto, [è disponibile tramite AUR](https://aur.archlinux.org/packages/nodejs-percollate). 
Io l'ho installato con

```
yay -S nodejs-percollate
```

A quanto sembra, anche NixOS ed Alpine Linux hanno i loro pacchetti belli pronti per l'uso.

Sugli altri sistemi operativi, bisogna prima [installare Node.js](https://nodejs.org/en/download) (versione 14.17.0 o successive) e poi eseguire il comando

```
npm install -g percollate
```

### Come usare Percollate - le basi
Percollate ha un buon numero di funzionalità avanzate (vedi [README](https://github.com/danburzo/percollate?tab=readme-ov-file#usage)), ma io lo uso sempre nella stessa banalissima maniera:

```
percollate FORMAT -o OUTPUT-PATH -a AUTHOR -t TITLE BUNCH-OF-URLS
```

Per esempio, per creare l'ultimo numero della mia rivista ho usato

```
percollate epub -o hmm9.epub -a "Editor: harisont" -t "hmm #9" https://mn.eumans.eu/nl/link\?c\=4b459\&d\=2rk\&h\=2piae6c01pj71f0i5rhf11ib13\&hpl\=CCG6883941KNE83E41O20SP0EDN20Q3GDG\&i\=67i\&iw\=8\&n\=2hl\&p\=H301718942\&s\=wv\&sn\=2hl https://blog.uaar.it/2025/11/23/la-divulgazione-scientifica-nellepoca-dei-social-network/ https://theconversation.com/criar-a-los-hijos-en-una-lengua-no-materna-lo-que-dice-la-ciencia-268113 https://autonomin.fritext.org/ett-friare-och-roligare-satt-att-lyssna-pa-musik/ ...
```

(l'onomatopea "hmm" non è solo un'onomatopea, ma sta anche per "harisont's multilingual magazine", la rivista multilingue di harisont).

L'output è un file EPUB pulito e ben formattato con copertina, metadati per titolo e autore, indice, immagini e link a tutte le fonti originali. 
Qui sotto, potete farvi un'idea di come appaia quando lo si apre con [Foliate](https://johnfactotum.github.io/foliate/) (che, tra l'altro, è un eccellente lettore EPUB per Linux):

![Il numero 9 della rivista "hmm" aperto con Foliate.](https://harisont.github.io/assets/img/hmm/hmm9_foliate.png)

### Altri formati
Dei formati di file che Percollate è in grado di produrre, l'EPUB è di gran lunga il migliore per leggere sui dispositivi ad inchiostro elettronico. 
Il formato PDF è ottimo per la stampa.
Ma che fare se siete tra quelli che hanno la sfortuna di possedere un Kindle e il buonsenso di non sostituirlo finché non si rompe?
Niente paura: altro software libero arriva in vostro soccorso!
[Installate Calibre](https://calibre-ebook.com/download), lasciate perdere la sua antiquata interfaccia grafica, tornate al terminale ed eseguite

```
ebook-convert INPUT-PATH.epub OUTPUT-PATH.mobi
```

Lo stesso metodo funziona per diversi altri formati di ebook più esotici, la cui lista completa è disponibile [qui](https://manual.calibre-ebook.com/generated/en/ebook-convert.html).

## Creare riviste dal browser
Se usare la linea di comando vi mette pensiero o se volete creare le vostre riviste da un dispositivo mobile in cui non avete neppure accesso a nulla del genere, buone notizie: Percollate è alla base di [Novel Service](https://novelservice.github.io/), un servizio che permette di fare più o meno la stessa cosa: copiate e incollate i vostri link nel campo di testo e lasciate fare al sito.

### Formati disponibili
Novel Service produce solo ed esclusivamente file EPUB e PDF.
Il primo di questi due formati va alla grande su _gran parte_ degli e-reader, il secondo è perfetto per la stampa.
Se siete gli sfortunati proprietari di un Kindle, in cui gli EPUB non sono supportati e i PDF sono scomodi per via delle dimensioni ridotte dello schermo, il mio suggerimento è di creare comunque un EPUB e utilizzare un convertitore EPUB-MOBI dei tanti che sono disponibili online (basta cercare "epub to mobi converter") per trasformarlo in qualcosa di adatto al vostro e-reader (attenzione al [SaaSS](https://www.gnu.org/philosophy/who-does-that-server-really-serve.it.html), però).

### Limitazioni
Sfortunatamente, Novel Service non rende fruibili tutte le funzionalità di Percollate.
La cosa più fastidiosa è che non c'è modo di specificare titolo e autore della rivista, il che significa che tutte le riviste avranno Untitled ("senza titolo") scritto a caratteri cubitali sulla copertina:

![Proprietà di una rivista creata con Novel Service. In copertina ci sono solo la scritta "Untitled" ed un timestamp.](https://harisont.github.io/assets/img/hmm/untitled.png)

Per fortuna, il timestamp (data ed ora) sotto il titolo permette comunque di distinguere un numero dall'altro.

Un altro piccolo svantaggio é la lentezza del servizio (generare riviste con questo sito richiede tempi decisamente più lunghi che non farlo su un qualsiasi portatile). 

Non credo sarebbe troppo difficile realizzare un'interfaccia web più completa per Percollate, e forse prima o poi dovrei fare un tentativo, dal momento che, per altri motivi, [sto già imparando qualcosina di sviluppo web](https://harisont.github.io/lists/web-dev.html) (se usereste un servizio del genere, fatemelo sapere!).
Nel frattempo, mi pare che Novel Service sia comunque una buona alternativa all'utilizzo di Percollate dal terminale.

Buona lettura!