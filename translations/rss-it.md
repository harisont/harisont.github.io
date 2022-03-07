---
title: "Cosa significa RSS e perché è una tecnologia che dovremmo continuare ad utilizzare"
layout: post
---

###### __[in inglese](https://harisont.github.io/l-informatico-di-famiglia/2022/03/05/rss-en.html) - [testo parallelo](https://harisont.github.io/parallel_texts/rss.html)__

Ti sei già iscritto al mio blog? Se sì, probabilmente questo post non fa al caso tuo.
Hai provato a cliccare il bottone "Subscribe" che si trova in fondo a questa pagina ma hai subito chiuso l'inquietante pagina web piena di strane parentesi angolari che si è aperta quando lo hai fatto? In tal caso, continua a leggere.
Sei già convinto che l'RSS sia una tecnologia del web 1.0 che merita più attenzione e vuoi saperne di più? Anche tu sei finito nel posto giusto.

## Cosa significa RSS
Come immaginerai, RSS è un acronimo. Ho sempre pensato che stesse per Really Simple Syndication ("Diffusione Molto Semplice", all'incirca), che è abbastanza oscuro, ma facendo qualche ricerca per questo post mi sono imbattuta in altri due possibili significati: RDF[¹](#note) Site Summary and Rich Site Summary ("sunto arricchito del sito", o qualcosa del genere).
Quest'ultima è probabilmente quella di più semplice comprensione: l'acronimo "RSS" indica qualcosa (per l'esattezza, un file di testo, spesso chiamato _feed_, in un formato standard e _machine-readable_, cioè strutturato per l'elaborazione automatica) che riassume i contenuti di un certo sito web.

Se mai ti è capitato di aprire un feed RSS (puoi provarci [anche adesso](https://harisont.github.io/feed.xml)), avrai già notato che il fatto che un file sia machine-readable non garantisce affatto la sua human-readability, cioè la sua leggibilità per gli umani. E, in effetti, nessuno si aspetta che noi _leggiamo_ direttamente un feed RSS: ci basterà _iscriverci_ e chiedere ad un programma (un _feed reader_, per l'appunto) di presentarci i suoi contenuti in un formato più accessibile.

## Perché i feed RSS stanno cadendo nel dimenticatoio
Negli anni '90, quando questa tecnologia era stata appena inventata, iscriversi ad un feed RSS era una maniera _molto semplice_, se non addirittura la maniera _più semplice_, o forse persino l'_unica_ maniera per ricevere aggiornamenti da una pagina web. Bastava scaricare un feed reader e dargli in pasto gli URL di qualche feed RSS interessante e si poteva star certi che non ci si sarebbe persi neanche una virgola di quanto avveniva sui diversi siti seguiti, né tantomeno si sarebbe stati distratti da feed ai quali non ci si era esplicitamente iscritti. 

Un sogno, no? Be', a dirla tutta è realtà, o almeno lo è stata. 
Fino a poco tempo fa, quella dell'RSS era la tecnologia che si nascondeva dietro ad ogni giornale online, blog e pagina web aggiornata di frequente. Anche i podcast erano tutti distribuiti tramite RSS, e persino YouTube, all'inizio, era pieno di feed ai quali iscriversi (spoiler: è ancora così, ma probabilmente non te ne sei mai accorto - guarda [qui](http://www.davidesalerno.net/2016/01/come-seguire-un-canale-youtube-via-feed-rss/)!).

A questo punto, ti chiederai: ma se l'RSS è, o era, una tecnologia così utile e diffusa, perché non ne ho mai nemmeno sentito parlare? Non sarà mica stata superata perché non era poi così _tanto semplice_ da usare? La risposta è... sì e no. Ormai da un pezzo (diciamo pure dall'inizio del seconda decennio del terzo millennio), l'RSS è abbastanza fuori moda, ma questo non perché sia complicato da utilizzare. Se non sei ancora convinto, salta pure alle [istruzioni per l'uso](#rss-istruzioni-per-luso).

### Iscriversi al feed X vs. seguire Y su Z
Ma cos'è successo ad Internet dieci anni fa? Erano gli inizi del web 2.0 e quasi tutti abbiamo iniziato ad usare i social network. E i social network, quasi per definizione, hanno tutti un loro modo di farti "seguire" persone ed organizzazioni più estese.
Questa, di per sè, era già una minaccia per una tecnologia come l'RSS, e non appena piattaforme come Facebook hanno iniziato a crescere in popolarità, tutti quanti abbiamo iniziato ad "seguire" e "lasciare un mi piace" a persone e pagine invece di iscriverci ai loro vari feed. Il risultato è più o meno lo stesso. 

...Ma lo è veramente? A mio avviso, in realtà, seguire un profilo su un qualsiasi social media è molto diverso da iscriversi al feed di un sito tramite RSS. Le ragioni principali sono due:

1. Nel momento in cui rimpiazzi il tuo RSS reader con, per esempio, Instagram, potrai seguire solo ed esclusivamente persone che hanno un account su quella piattaforma. Viceversa, i vari creatori di contenuti che ti interessano, per poter essere seguiti da te, dovranno iscriversi ad Instagram ed adattare i loro contenuti alle funzionalità che offre, anche se magari non la amano o se non si presta per ciò che fanno (tanto per fare un esempio, post lunghi come questo mal si adattano a Twitter)
2. La stragrande maggioranza dei social raccoglierà quanti più dati possibile su di te per poi mostrarti inserzioni pubblicitarie personalizzate. I feed RSS, al contrario, non sono materialmente in grado di tracciarti e raramente contengono pubblicità.

### Consigliati per te!
Purtroppo, non è tutto qui: i social network sono stati seguiti a ruota dai _recommender system_. Un recommender system (letteralmente "sistema di raccomandazione") è un programma che crede di sapere a quali contenuti sei interessato e li seleziona al posto tuo. Ormai, molti recommender system fanno il loro lavoro piuttosto bene (per esempio, apprezzo molto quello di YouTube e di recente ho creato [una playlist di musica anni '50 con l'aiuto dell'intelligenza artificiale di Spotify](https://open.spotify.com/playlist/5qqrqrJudIowWBV3MIvp3D?si=b4cc1719edc04540)). Questo perché sempre più spesso sono basati su Machine Learning ("apprendimento automatico"): in poche parole, imparano _da te_ e da quel che fai quando li utilizzi. Se il termine "recommender system" continua a suonarti poco familiare, prova a rileggere questo paragrafo rimpiazzandolo mentalmente con il più comunemente usato "Algoritmo"[²](#note).

Non sono contraria ai recommender system (e, ovviamente, non posso essere contraria agli algoritmi!), ma penso che debbano essere utilizzati responsabilmente e, preferibilmente, _assieme_ ad altri modi di accedere alle informazioni. In particolare, credo vadano tenute a mente le seguenti controindicazioni:

1. __scarsa affidabilità__: solitamente, un recommender system non ti mostra _tutto_ quello che le persone che segui condividono su una certa piattaforma (YouTube ha un meccanismo che fa sì che questo, se glielo chiedi per favore, non avvenga, ma ciò non si applica a tutti i social network). Allo stesso tempo, non ti mostra neanche _esclusivamente_ i contenuti provenienti da chi hai esplicitamente deciso di seguire. Questo vuol dire che, mentre vieni bombardato di foto di travel blogger che non hai mai sentito nominare ma che "potrebbero piacerti", potresti perderti le novità dal tuo artista preferito
2. __effetto bolla__: i recommender system ti mostreranno contentuti simili a quelli che ti sono piaciuti (o i quali, comunque, ti hanno suscitato una qualche emozione) nel passato. Il rischio associato a questo è che il sistema, senza che tu te ne accorga, isoli te e il tuo gruppo di amici in una specie di "bolla", impenetrabile se non ad un certo tipo di informazioni, magari legate ad un certo orientamento politico. Se hai controllato ripetutamente le politiche per la prevenzione della diffusione del covid ma non hai mai seguito un attivista LGBTQ+, è probabile che verrai tempestivamente informato sulla [recente decisione del governo svedese di rimuovere le restrizioni](https://www.bloomberg.com/news/articles/2022-02-03/sweden-lifts-covid-restrictions-as-pandemic-enters-new-phase) ma resterai ignaro di [quel che sta accadendo in Florida](https://abcnews.go.com/US/dont-gay-bill-moves-forward-florida/story?id=82481565). In parole povere, i social media non sono un granché come fonte di notizie.

## RSS: istruzioni per l'uso

## Feed reader
Se ti è venuta voglia di seguire qualcuno dei tantissimi feed RSS che ancora adesso vengono creati e aggiornati, hai bisogno di un __feed reader__.

Come abbiamo detto, un feed reader è un programma in grado di rendere i contenuti di un feed RSS facili da leggere per noi esseri umani. 
Personalmente, al momento utilizzo [Fluent Reader](https://hyliu.me/fluent-reader/), un'applicazione desktop avanzata, open source e multipiattaforma.
Se sei un fan dei software da riga di comando o vuoi, per qualsiasi altro motivo, qualcosa di piú minimale e leggero, puoi provare invece [Newsboat](https://newsboat.org/).

Anche per smartphone e tablet c'é una vasta gamma di applicazioni free ("free" sia perché sono [software libero](https://www.fsf.org/it/il-software-libero-e-una-questione-di-liberta-non-di-prezzo) che perché sono gratuite) tra cui scegliere. Il mio compagno, per esempio, usa [Feeder](https://f-droid.org/packages/com.nononsenseapps.feeder/).

### Podcast managers
Un'app Android che utilizzo moltissimo io stessa, per non dire la mia app preferita in assoluto, é [AntennaPod](https://f-droid.org/en/packages/de.danoeh.antennapod/), specificamente pensata per i podcast.

Ebbene sí: anche la stragrande maggioranza dei podcast viene distribuita sotto forma di feed RSS, nonostante Spotify abbia deciso di fare le cose a modo suo e abbia purtroppo (lo dico da persona che, per ascoltare la musica, Spotify lo usa quotidianamente) l'esclusiva su tutta una serie di contenuti. Per i podcast, però non c'é storia: AntennaPod gioca un altro campionato, superando ogni app proprietaria.

Sfortunatamente, anche quello dei podcast é un mondo in cui la tendenza é quella di legare i contenuti ad una o piú piattaforme specifiche: se di questo Spotify é l'esempio più lampante, difatti, persino la RAI ha lanciato una sua piattaforma, [RaiPlay Sound](https://www.raiplaysound.it/), che va a sostituire un sito che, per quanto non offrisse un'esperienza di navigazione particolarmente gradevole, forniva feed RSS a cui iscriversi per tutti i programmi a cadenza periodica. Vorrà dire che, poco a poco, mi andrò dimenticando di uno dei miei preferiti, [Wikiradio](https://www.raiplaysound.it/programmi/wikiradio). In ogni caso, ne consiglio vivamente le stagioni passate, i cui sono ancora disponibili e facili da reperire, per esempio proprio tramite la funzionalità di ricerca di AntennaPod.

### Alla ricerca dei feed
In conclusione, sembra che la gente si preoccupi sempre di meno dei feed RSS, ma, fatta eccezione per i casi come quelli che abbiamo appena visto, questo significa che, se non sono moltissimi i nuovi feed che vengono creati, sono anche pochissimi i vecchi che vengono consapevolmente disabilitati. 

{% include image.html file="../assets/img/rss/rss.png" description="Il simbolo dell'RSS" %}

Nei rari casi in cui un sito é pensato per incoraggiarti attivamente ad usare i(l) suo(i) feed RSS, iscriversi sarà semplicissimo: basterà trovare un bottone con una qualche variazione sul tema del simbolo dell'RSS, cliccarci sopra e copiare l'indirizzo della pagina web che si aprirà nell'apposito campo del proprio feed reader. 

{% include image.html file="../assets/img/rss/rss_add.png" description="Aggiunta di un nuovo feed RSS ad una lista di fonti" %}

In molti casi, se non addirittura nella maggior parte, però, un bottone col simbolo dell'RSS non ci sarà affatto. A volte, nemmeno gli stessi blogger sono a conoscenza del fatto che le piattaforme su cui è hostato il loro sito offrono la possibilità di seguirlo tramite un feed generato automaticamente, perciò non mettono il link al feed a disposizione dei loro lettori.

Un trucchetto per scoprire se un sito sia _veramente_ privo di un feed RSS o meno è quello di provare ad aggiungere `/feed.xml` all'URL della sua pagina principale, ma esistono anche soluzioni migliori.
Firefox, per esempio, ha un'estensione, [Awesome RSS](https://addons.mozilla.org/en-US/firefox/addon/awesome-rss/), che va alla ricerca dei feed RSS dei siti che apri ed offre una maniera molto, _molto semplice_ per ottenerne i link.
Mettiamo che tu ci tenga davvero tanto a sapere cosa sta imparando la mia ex compagna di classe Tova nel suo corso di elaborazione del linguaggio naturale. Il suo [blog]((https://datatjej.github.io/)) è davvero carino, e probabilmente ha un feed RSS, ma proprio non si riesce a trovarlo. Con Awesome RSS, vedrai qualcosa del genere:

{% include image.html file="../assets/img/rss/rss_awe.png" description="Con Awesome RSS all'opera, cliccando sul simbolo dell'RSS sulla tua barra di ricerca. otterrai il link del suo feed RSS" %}

# Extra 1: Ma com'è fatto un feed RSS?
A questo punto, dovresti avere un buon modello concettuale di come funzionino i feed RSS e, probabilmente, sei più o meno in grado di utilizzarli. Se ti incuriosisce anche sapere come sia _fatto_ un feed RSS, qui c'è pane per i tuoi denti.

Se apri il feed di questo blog, ti troverai davanti a qualcosa di apparentemente complesso, per la precisione qualcosa di simile all'immagine qui sotto:

{% include image.html file="../assets/img/rss/rss_content.png" description="Un feed RSS come appare nel mio browser" %}

Si tratta di un file XML, e per usare un eufemismo, non si presenta benissimo. XML sta per eXtensible Markup Language ("linguaggio di marcatura estensibile"). Se vuoi sapere tutto su questo formato, puoi partire dando un'occhiata a [questa voce di Wikipedia](https://it.wikipedia.org/wiki/XML), ma l'essenziale è che:

- i linguaggi di marcatura, come l'XML, l'HTML e il Markdown (che e quello che sto utilizzando per scrivere questo post) servono per descrivere la struttura dei vari documenti elettronici. In molti casi, e l'XML non fa eccezione, ciò si ottiene tramite il _tagging_ (letteralmente, "etichettatura") delle diverse parti che li compongono, specificandone il contenuto. In XML ed HTML, i tag sono parole racchiuse tra parentesi angolari, come `<questa>`. Al titolo di un post è spesso, per esempio, assegnato il tag `<title>`, mentre il corpo del suo testo verrà probabilmente marcato con `<body>`, i suoi paragrafi con `<p>` eccetera
- il fatto che l'XML sia _estensibile_ significa che l'insieme dei tag non è immutabile - in ogni momento è possibile creare nuove "categorie".

Per esempio, i feed RSS sono solamente contraddistinti dal tag `<feed>` e contengono, fra le altre cose, i metadati, ossia qualche informazione generale sul feed e il sito da cui proviene. Per esempio, il feed del mio blog ha un titolo (`<title>`), un sottotitolo (`<subtitle>`) ed un autore (`<author>`) (che ha un nome, `<name>`, ed un'`<email>`), gli stessi del blog stesso, ma ha anche, tra le altre cose, un `<id>`:

```xml
...
<feed xmlns="http://www.w3.org/2005/Atom">
    ...
    <id>https://harisont.github.io/feed.xml</id>
    <title type="html">Hari’s online</title>
    <subtitle>A chaotically multilingual blog by Arianna Masciolini</subtitle>
    <author>
        <name>Arianna Masciolini</name>
        <email>arianna.masciolini@gmail.com</email>
    </author>
...
</feed>
```

Ogni post o `<entry>`, a sua volta, ha un titolo, un URL, una data di pubblicazione ed una di ultimo aggiornamento, un ID, un contenuto, un autore ed una specie di abstract. Per esempio:

```xml
<entry>
    <title type="html">Interesting things I read/watched/listened to this month (January 2022)</title>
    <link href="https://harisont.github.io/meaningful-media/2022/01/30/meaningful-media.html" rel="alternate" type="text/html" title="Interesting things I read/watched/listened to this month (January 2022)"/>
    <published>2022-01-30T00:00:00+00:00</published>
    <updated>2022-01-30T00:00:00+00:00</updated>
    <id>https://harisont.github.io/meaningful-media/2022/01/30/meaningful-media</id>
    <content type="html" xml:base="https://harisont.github.io/meaningful-media/2022/01/30/meaningful-media.html">This is the first of a series of posts, inspired by Nicky Case’s yearly meaningful media lists...</content>
    <author>
        <name>Arianna Masciolini</name>
        <email>arianna.masciolini@gmail.com</email>
    </author>
    <category term="meaningful-media"/>
    <summary type="html">This is the first of a series of posts...</summary>
</entry>
```

Niente di troppo complicato, tantomeno per un feed reader. Non per questo, però, vorrei mai scrive mai tutto quel codice a mano, carattere per carattere. Se sei della stessa opinione ma vorresti comunque un feed tutto tuo, continua a leggere: nella prossima sezione vedremo come ottenerlo.

## Extra 2: Un feed tutto per te
Ti sei convinto che l'RSS è fantastico e hai iniziato a seguire qualche blog. Ora è il momento di creare il tuo feed, ma l'XML ti scoraggia. La buona notizia è che probabilmente non dovrai scriverne neanche una riga.

Se hai un blog su Wordpress o utilizzi una piattaforma di podcasting decente, per esempio, probabilmente hai già un feed di alta qualità. Se non è così, ci sono un sacco di [strumenti appositi e tutorial](https://feeder.co/knowledge-base/rss-feed-creation/how-to-create-an-rss-feed-for-any-website/) che rendono il tutto comunque _veramente semplice_.

Io non ho un podcast (almeno per ora), ma per quel che riguarda i blog, per te che ne stai aprendo uno nuovo, e a maggior ragione se sei un programmatore, consiglio vivamente la piattaforma ([GitHub Pages](https://pages.github.com/)) ed il tema ([minima](https://github.com/jekyll/minima)) che utilizzo io stessa: il feed generato automaticamente è di ottima qualità e l'aspetto estetico del blog si può personalizzare senza troppi problemi.

## Extra 3: File OPML per condivisione e backup
Tutto molto bello, ma il principale vantaggio dei social network è che è permettono di vedere facilmente chi o che cosa seguono i tuoi amici e seguirli a tua volta.

In realtà, anche questo si può fare in maniera del tutto semplice con l'RSS! Per condividere la preziosa lista dei tuoi blog preferiti, puoi esportarla come OPML (Outline Processor Markup Language) e mandare a chi vuoi il file così ottenuto, che il destinatario potrà importare con un clic.
L'OPML è supportato da gran parte dei reader e può essere utile anche per passare ad una nuova applicazione senza doversi reiscrivere ai vari siti uno per uno.

{% include image.html file="../assets/img/rss/opml.png" description="Il bottone per importare/esportare come OPML nel mio feed reader" %}

Se sei curioso di sapere cosa leggo e ascolto, ecco i miei due file OPML:

- [la lista di blog e riviste online che seguo](../assets/opml/reads.opml) (ho escluso i quotidiani perché, di fatto, nessuno di quelli che seguo mi soddisfa particolarmente)
- [la mia preziosa lista di podcast in tutte e quattro le lingue che utilizzo in questo blog](../assets/opml/podcasts.opml).

---

## Fonti
- [RSS su Wikipedia](https://it.wikipedia.org/wiki/RSS)
- Nicky Case, [_Back to the Future with RSS!_](https://blog.ncase.me/back-to-the-future-with-rss/)

## Note
¹ Resource Description Framework. Eh già, un altro acronimo...

² Noto una tendenza ad utilizzare il termine "algoritmo" in modo improprio, con la conseguenza che molta gente pensa che gli algoritmi _siano_ i recommender system dei social network. In realtà, gli algoritmi che vengono usati nei recommender system sono solo una piccolissima parte dell'enorme moltitudine di algoritmi esistenti. Algoritmi che includono, tra le altre cose, le ricette di cucina e le routine mattutine.