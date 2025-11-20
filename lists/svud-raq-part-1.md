- [Comparative constructions (they are simpler than you think!)](#comparative-constructions-they-are-simpler-than-you-think)
- [_Går att `VERB`a_ and other equally tough constructions](#går-att-verba-and-other-equally-tough-constructions)
- [Participles](#participles)
- [_Att `VERB`a själv_](#att-verba-själv)
- [Subword-level coordination](#subword-level-coordination)
- [Morphological analysis of syncretic adjective forms](#morphological-analysis-of-syncretic-adjective-forms)
- [_Att vara X år gammal_ or _to be X years old_](#att-vara-x-år-gammal-or-to-be-x-years-old)


## Comparative constructions (they are simpler than you think!)

[[go to discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1092)

Comparative constructions such as 

1. _att annotera dessa konstruktioner är enklare än du tror_ and 
2. _vissa konstruktioner är lättare än andra_ 

look tricky, but the [guidelines](https://universaldependencies.org/u/overview/comparatives.html) for them have recently gotten more comprehensive and, at least when it comes to Swedish, easier to understand and follow.

The first question might be what UPOS tag to assign to the word _än_.
The answer to that is [`SCONJ`](https://universaldependencies.org/sv/pos/SCONJ.html). 
In (1), this is clear as _än_ clearly introduces a subordinate clause, _än du tror_. 
As for (2), the guidelines state that ["if the same conjunction is used with bare nominals, we still tag it `SCONJ`"](https://universaldependencies.org/u/overview/comparatives.html#:~:text=If%20the%20same%20conjunction%20is%20used%20with%20bare%20nominals%2C%20we%20still%20tag%20it%20SCONJ%20(but%20we%20use%20dependency%20relations%20that%20are%20reserved%20for%20nominals%2C%20see%20below).).

When it comes to the dependency structure of the construction, the clause or nominal introduced by _än_ should always be attached to the property whose degree is compared:

<svg width="272" height="135" style="background-color:white" viewBox="0 10 272 140" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="128" font-size="16">X</text>
  <text x="24" y="128" font-size="16">är</text>
  <text x="52" y="128" font-size="16">(mer)</text>
  <text x="98" y="128" font-size="16">enkel/</text>
  <text x="98" y="142" font-size="16">enklare</text>
  <text x="171" y="128" font-size="16">än</text>
  <text x="218" y="128" font-size="16">Y</text>
  <text x="24" y="113" font-size="10">AUX</text>
  <text x="52" y="113" font-size="10">ADV</text>
  <text x="98" y="113" font-size="10">ADJ</text>
  <text x="171" y="113" font-size="10">ADP</text>
  <path d="M 17 100 Q 17 50 61 50 L 61 50 Q 106 50 106 100" stroke="black" fill="none"></path>
  <line x1="17" y1="95" x2="17" y2="100" stroke="black"></line>
  <path d="M 17 100 14 94 20 94"></path>
  <path d="M 36 100 Q 36 67 69 67 L 73 67 Q 106 67 106 100" stroke="black" fill="none"></path>
  <line x1="36" y1="95" x2="36" y2="100" stroke="black"></line>
  <path d="M 36 100 33 94 39 94"></path>
  <text x="64" y="62" font-size="10">cop</text>
  <path d="M 75 100 Q 75 83 89 83 L 89 83 Q 104 83 104 100" stroke="black" fill="none"></path>
  <line x1="75" y1="95" x2="75" y2="100" stroke="black"></line>
  <path d="M 75 100 72 94 78 94"></path>
  <text x="60" y="78" font-size="10">advmod</text>
  <line x1="113" y1="20" x2="113" y2="100" stroke="black"></line>
  <path d="M 113 100 110 94 116 94"></path>
  <text x="118" y="28" font-size="10">root</text>
  <path d="M 185 100 Q 185 83 199 83 L 199 83 Q 214 83 214 100" stroke="black" fill="none"></path>
  <line x1="185" y1="95" x2="185" y2="100" stroke="black"></line>
  <path d="M 185 100 182 94 188 94"></path>
  <path d="M 119 100 Q 119 67 153 67 L 193 67 Q 227 67 227 100" stroke="black" fill="none"></path>
  <line x1="227" y1="95" x2="227" y2="100" stroke="black"></line>
  <path d="M 227 100 224 94 230 94"></path>
</svg>

The specific labels depend on whether the standard of comparison is a clause or a nominal.

For sentences like (1), we use [`advcl`](https://universaldependencies.org/sv/dep/advcl.html) for the subordinate clause and [`mark`](https://universaldependencies.org/sv/dep/mark.html) for _än_:


<svg width="656" height="135" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 656 135" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="128" font-size="16">att</text>
  <text x="51" y="128" font-size="16">annotera</text>
  <text x="133" y="128" font-size="16">dessa</text>
  <text x="188" y="128" font-size="16">konstruktioner</text>
  <text x="324" y="128" font-size="16">är</text>
  <text x="361" y="128" font-size="16">enklare</text>
  <text x="434" y="128" font-size="16">än</text>
  <text x="489" y="128" font-size="16">du</text>
  <text x="535" y="128" font-size="16">tror</text>
  <text x="5" y="113" font-size="10">PART</text>
  <text x="51" y="113" font-size="10">VERB</text>
  <text x="133" y="113" font-size="10">DET</text>
  <text x="188" y="113" font-size="10">NOUN</text>
  <text x="324" y="113" font-size="10">AUX</text>
  <text x="361" y="113" font-size="10">ADJ</text>
  <text x="434" y="113" font-size="10">SCONJ</text>
  <text x="489" y="113" font-size="10">PRON</text>
  <text x="535" y="113" font-size="10">VERB</text>
  <path d="M 18 100 Q 18 83 35 83 L 41 83 Q 58 83 58 100" stroke="black" fill="none"></path>
  <line x1="18" y1="95" x2="18" y2="100" stroke="black"></line>
  <path d="M 18 100 15 94 21 94"></path>
  <text x="29" y="78" font-size="10">mark</text>
  <path d="M 61 100 Q 61 50 111 50 L 321 50 Q 371 50 371 100" stroke="black" fill="none"></path>
  <line x1="61" y1="95" x2="61" y2="100" stroke="black"></line>
  <path d="M 61 100 58 94 64 94"></path>
  <text x="205" y="45" font-size="10">csubj</text>
  <path d="M 146 100 Q 146 83 162 83 L 179 83 Q 195 83 195 100" stroke="black" fill="none"></path>
  <line x1="146" y1="95" x2="146" y2="100" stroke="black"></line>
  <path d="M 146 100 143 94 149 94"></path>
  <text x="164" y="78" font-size="10">det</text>
  <path d="M 72 100 Q 72 67 105 67 L 174 67 Q 207 67 207 100" stroke="black" fill="none"></path>
  <line x1="207" y1="95" x2="207" y2="100" stroke="black"></line>
  <path d="M 207 100 204 94 210 94"></path>
  <text x="133" y="62" font-size="10">obj</text>
  <path d="M 338 100 Q 338 83 353 83 L 353 83 Q 367 83 367 100" stroke="black" fill="none"></path>
  <line x1="338" y1="95" x2="338" y2="100" stroke="black"></line>
  <path d="M 338 100 335 94 341 94"></path>
  <text x="346" y="78" font-size="10">cop</text>
  <line x1="376" y1="20" x2="376" y2="100" stroke="black"></line>
  <path d="M 376 100 373 94 379 94"></path>
  <text x="381" y="28" font-size="10">root</text>
  <path d="M 445 100 Q 445 67 479 67 L 510 67 Q 544 67 544 100" stroke="black" fill="none"></path>
  <line x1="445" y1="95" x2="445" y2="100" stroke="black"></line>
  <path d="M 445 100 442 94 448 94"></path>
  <text x="485" y="62" font-size="10">mark</text>
  <path d="M 502 100 Q 502 83 519 83 L 525 83 Q 542 83 542 100" stroke="black" fill="none"></path>
  <line x1="502" y1="95" x2="502" y2="100" stroke="black"></line>
  <path d="M 502 100 499 94 505 94"></path>
  <text x="511" y="78" font-size="10">nsubj</text>
  <path d="M 382 100 Q 382 50 432 50 L 504 50 Q 554 50 554 100" stroke="black" fill="none"></path>
  <line x1="554" y1="95" x2="554" y2="100" stroke="black"></line>
  <path d="M 554 100 551 94 557 94"></path>
  <text x="457" y="45" font-size="10">advcl</text>
</svg>

In cases such as (2), we use [`obl`](https://universaldependencies.org/sv/dep/obl.html) and [`case`](https://universaldependencies.org/sv/dep/case.html):

<svg width="443" height="115" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 443 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16">vissa</text>
  <text x="60" y="108" font-size="16">konstruktioner</text>
  <text x="196" y="108" font-size="16">är</text>
  <text x="233" y="108" font-size="16">lättare</text>
  <text x="306" y="108" font-size="16">än</text>
  <text x="343" y="108" font-size="16">andra</text>
  <text x="5" y="93" font-size="10">DET</text>
  <text x="60" y="93" font-size="10">NOUN</text>
  <text x="196" y="93" font-size="10">AUX</text>
  <text x="233" y="93" font-size="10">ADJ</text>
  <text x="306" y="93" font-size="10">ADP</text>
  <text x="343" y="93" font-size="10">PRON</text>
  <path d="M 18 80 Q 18 63 34 63 L 51 63 Q 67 63 67 80" stroke="black" fill="none"></path>
  <line x1="18" y1="75" x2="18" y2="80" stroke="black"></line>
  <path d="M 18 80 15 74 21 74"></path>
  <text x="36" y="58" font-size="10">det</text>
  <path d="M 71 80 Q 71 47 104 47 L 209 47 Q 242 47 242 80" stroke="black" fill="none"></path>
  <line x1="71" y1="75" x2="71" y2="80" stroke="black"></line>
  <path d="M 71 80 68 74 74 74"></path>
  <text x="145" y="42" font-size="10">nsubj</text>
  <path d="M 210 80 Q 210 63 225 63 L 225 63 Q 239 63 239 80" stroke="black" fill="none"></path>
  <line x1="210" y1="75" x2="210" y2="80" stroke="black"></line>
  <path d="M 210 80 207 74 213 74"></path>
  <text x="218" y="58" font-size="10">cop</text>
  <line x1="248" y1="20" x2="248" y2="80" stroke="black"></line>
  <path d="M 248 80 245 74 251 74"></path>
  <text x="253" y="28" font-size="10">root</text>
  <path d="M 320 80 Q 320 63 335 63 L 335 63 Q 349 63 349 80" stroke="black" fill="none"></path>
  <line x1="320" y1="75" x2="320" y2="80" stroke="black"></line>
  <path d="M 320 80 317 74 323 74"></path>
  <text x="325" y="58" font-size="10">case</text>
  <path d="M 254 80 Q 254 47 288 47 L 328 47 Q 362 47 362 80" stroke="black" fill="none"></path>
  <line x1="362" y1="75" x2="362" y2="80" stroke="black"></line>
  <path d="M 362 80 359 74 365 74"></path>
  <text x="301" y="42" font-size="10">obl</text>
</svg>

The only remaining issue is where to draw the line between clausal and nominal comparison.
Sentences like 

3. _parsern annoterar dessa konstruktioner bättre än jag_ 

can be rephrased as both

- _parsern annoterar dessa konstruktioner bättre än **jag skulle göra**_ (clausal) and
- _parsern annoterar dessa konstruktioner bättre än **mig**_ (nominal).

Ambiguous cases like (3) are treated like (2).

## _Går att `VERB`a_ and other equally tough constructions
[[go to discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1128)

How to annotate sentences like _detta går att debattera_?
Well, that sparked a whole debate.

Semantically, _detta_ is the object of _debattera_.
If we rephrase the sentence into _det går att debattera detta_ or _att debattera detta går_, the syntactic analysis coincides with the semantic one:

<svg width="324" height="115" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 324 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16">det</text>
  <text x="51" y="108" font-size="16">går</text>
  <text x="97" y="108" font-size="16">att</text>
  <text x="143" y="108" font-size="16">debattera</text>
  <text x="234" y="108" font-size="16">detta</text>
  <text x="5" y="93" font-size="10">PRON</text>
  <text x="51" y="93" font-size="10">VERB</text>
  <text x="97" y="93" font-size="10">PART</text>
  <text x="143" y="93" font-size="10">VERB</text>
  <text x="234" y="93" font-size="10">PRON</text>
  <path d="M 18 80 Q 18 63 35 63 L 41 63 Q 58 63 58 80" stroke="black" fill="none"></path>
  <line x1="18" y1="75" x2="18" y2="80" stroke="black"></line>
  <path d="M 18 80 15 74 21 74"></path>
  <text x="29" y="58" font-size="10">expl</text>
  <line x1="66" y1="20" x2="66" y2="80" stroke="black"></line>
  <path d="M 66 80 63 74 69 74"></path>
  <text x="71" y="28" font-size="10">root</text>
  <path d="M 110 80 Q 110 63 127 63 L 133 63 Q 150 63 150 80" stroke="black" fill="none"></path>
  <line x1="110" y1="75" x2="110" y2="80" stroke="black"></line>
  <path d="M 110 80 107 74 113 74"></path>
  <text x="121" y="58" font-size="10">mark</text>
  <path d="M 73 80 Q 73 47 106 47 L 128 47 Q 161 47 161 80" stroke="black" fill="none"></path>
  <line x1="161" y1="75" x2="161" y2="80" stroke="black"></line>
  <path d="M 161 80 158 74 164 74"></path>
  <text x="106" y="42" font-size="10">csubj</text>
  <path d="M 165 80 Q 165 63 181 63 L 236 63 Q 252 63 252 80" stroke="black" fill="none"></path>
  <line x1="252" y1="75" x2="252" y2="80" stroke="black"></line>
  <path d="M 252 80 249 74 255 74"></path>
  <text x="202" y="58" font-size="10">obj</text>
</svg>

<svg width="268" height="115" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 268 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16">att</text>
  <text x="51" y="108" font-size="16">debattera</text>
  <text x="142" y="108" font-size="16">detta</text>
  <text x="197" y="108" font-size="16">går</text>
  <text x="5" y="93" font-size="10">PART</text>
  <text x="51" y="93" font-size="10">VERB</text>
  <text x="142" y="93" font-size="10">PRON</text>
  <text x="197" y="93" font-size="10">VERB</text>
  <path d="M 18 80 Q 18 63 35 63 L 41 63 Q 58 63 58 80" stroke="black" fill="none"></path>
  <line x1="18" y1="75" x2="18" y2="80" stroke="black"></line>
  <path d="M 18 80 15 74 21 74"></path>
  <text x="29" y="58" font-size="10">mark</text>
  <path d="M 62 80 Q 62 47 95 47 L 173 47 Q 206 47 206 80" stroke="black" fill="none"></path>
  <line x1="62" y1="75" x2="62" y2="80" stroke="black"></line>
  <path d="M 62 80 59 74 65 74"></path>
  <text x="123" y="42" font-size="10">csubj</text>
  <path d="M 73 80 Q 73 63 89 63 L 144 63 Q 160 63 160 80" stroke="black" fill="none"></path>
  <line x1="160" y1="75" x2="160" y2="80" stroke="black"></line>
  <path d="M 160 80 157 74 163 74"></path>
  <text x="110" y="58" font-size="10">obj</text>
  <line x1="212" y1="20" x2="212" y2="80" stroke="black"></line>
  <path d="M 212 80 209 74 215 74"></path>
  <text x="217" y="28" font-size="10">root</text>
</svg>

In _detta går att debattera_, on the other hand, _detta_ acts like the syntactic subject of _går_, which becomes the head of the construction.
It remains to decide how to annotate the subordinate clause _att debattera_. 
Since its subject of not controlled by that of the superordinate, we use [`ccomp`](https://universaldependencies.org/sv/dep/ccomp.html) rather than [`xcomp`](https://universaldependencies.org/sv/dep/xcomp.html):

<svg width="268" height="115" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 268 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16">detta</text>
  <text x="60" y="108" font-size="16">går</text>
  <text x="106" y="108" font-size="16">att</text>
  <text x="152" y="108" font-size="16">debattera</text>
  <text x="5" y="93" font-size="10">PRON</text>
  <text x="60" y="93" font-size="10">VERB</text>
  <text x="106" y="93" font-size="10">PART</text>
  <text x="152" y="93" font-size="10">VERB</text>
  <path d="M 18 80 Q 18 63 34 63 L 51 63 Q 67 63 67 80" stroke="black" fill="none"></path>
  <line x1="18" y1="75" x2="18" y2="80" stroke="black"></line>
  <path d="M 18 80 15 74 21 74"></path>
  <text x="31" y="58" font-size="10">nsubj</text>
  <line x1="75" y1="20" x2="75" y2="80" stroke="black"></line>
  <path d="M 75 80 72 74 78 74"></path>
  <text x="80" y="28" font-size="10">root</text>
  <path d="M 119 80 Q 119 63 136 63 L 142 63 Q 159 63 159 80" stroke="black" fill="none"></path>
  <line x1="119" y1="75" x2="119" y2="80" stroke="black"></line>
  <path d="M 119 80 116 74 122 74"></path>
  <text x="130" y="58" font-size="10">mark</text>
  <path d="M 82 80 Q 82 47 115 47 L 137 47 Q 170 47 170 80" stroke="black" fill="none"></path>
  <line x1="170" y1="75" x2="170" y2="80" stroke="black"></line>
  <path d="M 170 80 167 74 173 74"></path>
  <text x="115" y="42" font-size="10">ccomp</text>
</svg>

It turns out that this is similar to [_tough_-movement](https://en.wikipedia.org/wiki/Tough_movement), so called because the prototypical English example sentences for the phenomenon involve the word _tough_:

1. _this problem is tough to solve_
2. _it is tough to solve this problem_
3. _to solve this problem is tough_

In sentences like (1), the syntactic subject _problem_ of the main verb _is_ is logically the object of an embedded non-finite verb _solve_ (although in UD, the root of the sentence would be _tough_, not _is_), whereas in paraphrases (2) and (3) logical and grammatical structure coincide. 
General guidelines about the annotations of _tough_-constructions, though, are still [being debated](https://github.com/UniversalDependencies/docs/issues/923) at the time of writing.

## Participles
[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1088)

Participles may look nearly as tough as _tough_-constructions because they work as different parts of speech depending on the context. 
Consider the following cases:

1. _skolan får **ökade** möjligheter_
2. _jag blev **bjuden** på te_
3. _flickan var **strålande** glad_
4. _detta **sökande** gav inget resultat_

Cases like (1) are by far the most frequent. 
The past participle _ökade_ clearly modifies the noun _möjligheter_ and should therefore be tagged as [`ADJ`](https://universaldependencies.org/sv/pos/ADJ.html).
However, since it is derived from the verb _öka_, it also takes the typically verbal features [`Tense`](https://universaldependencies.org/sv/feat/Tense.html) and [`VerbForm`](https://universaldependencies.org/sv/feat/VerbForm.html). 

In (2), _bjuden_ may also be seen as an adjective, but _bli_ + participle passive constructions are treated differently: the participle is tagged as [`VERB`](https://universaldependencies.org/sv/pos/VERB.html) (with `Tense` and `VerbFrom`) and _bli_ is annotated as a [passive auxiliary](https://universaldependencies.org/sv/dep/aux-pass.html):

<svg width="279" height="115" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 279 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16">jag</text>
  <text x="51" y="108" font-size="16">blev</text>
  <text x="97" y="108" font-size="16">bjuden</text>
  <text x="161" y="108" font-size="16">på</text>
  <text x="198" y="108" font-size="16">te</text>
  <text x="5" y="93" font-size="10">PRON</text>
  <text x="51" y="93" font-size="10">AUX</text>
  <text x="97" y="93" font-size="10">VERB</text>
  <text x="161" y="93" font-size="10">ADP</text>
  <text x="198" y="93" font-size="10">NOUN</text>
  <path d="M 17 80 Q 17 47 50 47 L 72 47 Q 105 47 105 80" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="17" y1="75" x2="17" y2="80" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 17 80 14 74 20 74"></path>
  <text x="39" y="42" font-size="10">nsubj:pass</text>
  <path d="M 64 80 Q 64 63 81 63 L 87 63 Q 104 63 104 80" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="64" y1="75" x2="64" y2="80" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 64 80 61 74 67 74"></path>
  <text x="66" y="58" font-size="10">aux:pass</text>
  <line x1="112" y1="20" x2="112" y2="80" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 112 80 109 74 115 74"></path>
  <text x="117" y="28" font-size="10">root</text>
  <path d="M 175 80 Q 175 63 189 63 L 189 63 Q 204 63 204 80" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="175" y1="75" x2="175" y2="80" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 175 80 172 74 178 74"></path>
  <text x="181" y="58" font-size="10">case</text>
  <path d="M 118 80 Q 118 47 152 47 L 183 47 Q 217 47 217 80" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="217" y1="75" x2="217" y2="80" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 217 80 214 74 220 74"></path>
  <text x="161" y="42" font-size="10">obl</text>
</svg>

In (3), the present participle _strålande_ modifies an adjective, _glad_. 
We therefore give it the [`ADV`](https://universaldependencies.org/sv/pos/ADV.html) UPOS tag, again with the `Tense` and `VerbForm` features.

Finally, in cases like (4), the participle should be tagged as [`NOUN`](https://universaldependencies.org/sv/pos/NOUN.html).
Its morphological analysis should be consistent with the UPOS tag, so rather than using `Tense` and `VerbForm` we annotate for [`Case`](https://universaldependencies.org/sv/feat/Case.html), [`Definite`](https://universaldependencies.org/sv/feat/Definite.html)ness, [`Gender`](https://universaldependencies.org/sv/feat/Gender.html) and [`Number`](https://universaldependencies.org/sv/feat/Number.html).

In all four cases, including when the UPOS tag is `VERB`, the lemma of the participial form is the participial form itself.

## _Att `VERB`a själv_

[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1126)

Constructions like _att bestämma själv_ are clear when it comes to dependency structure (the root is the verb and _själv_ is one of its direct dependents). 
Talbanken and LinES, the two largest Swedish UD treebanks, used to label this edge differently: the former used [`amod`](https://universaldependencies.org/sv/dep/amod.html), the latter [`advmod`](https://universaldependencies.org/sv/dep/amod.html).

But while two dispute, the third enjoys! 
Recent discussion led to re-analyzing this as [secondary predication](https://universaldependencies.org/u/overview/complex-syntax.html#secondary-predicates), which implies using a clausal relation type. 
Since _själv_ is optional, the relation of choice is [`advcl`](https://universaldependencies.org/sv/dep/advcl.html).
This is consistent with the pre-existing use of [`acl`](https://universaldependencies.org/sv/dep/acl.html) in cases like _du borde vara **dig själv**_, where the head is a nominal (_dig_). 

## Subword-level coordination
[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1150)

How to analyze constructions like _levnads- och beteendemässigt_?

Ideally, we would want the conjuncts _levnads-_ and _beteende(-)_ to form a compound with _mässigt_, but this is currently beyond the expressive capacity of UD.
To circumvent the problem, we lemmatize _levnad_ as _levnadsmässigt_, obtaining a conjunction of two adverbs.

## Morphological analysis of syncretic adjective forms

[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1107)

A handful of Swedish adjectives, such as _bra_ and _äkta_ are indeclinable, or rather, they inflect for degree (and, if nominalized, case), but not gender, number or definiteness.
Other adjectives, such as _nyttig_, inflect for the latter three features as well, but with a certain degree of syncretism: the form _nyttiga_, for example, can be a singular definite (of either gender) or a plural (irrespective of both gender and number).

In (Swedish) UD, a general principle is to ground morphological annotation on the observed word form and __avoid__ inferring features based on the context.
Adjectives like _bra_ should therefore only be annotated for [`Case`](https://universaldependencies.org/sv/feat/Case.html) and [`Degree`](https://universaldependencies.org/sv/feat/Degree.html).
This amounts to saying "this form works just as well for every combination of gender, number and definiteness".

Annotation of adjectives like _nyttig_, on the other hand, partially deviates from this idea.
When assigning morphological features to -_a_ forms like _nyttiga_, we would ideally want to convey that they can be definite and/or plural (but not singular and indefinite!).
The problem is that UD v2 allows expressing disjunctions of values for a single feature (e.g. `Number=Sing,Plur`) but not of combinations of several feature-value pairs.
Leaving -_a_ forms unannotated for number and definiteness would be misleading, as it would imply that they can be used in the indefinite singular case too.
As a consequence, these two features are annotated contextually.
The current practice can be summarized as follows (case and degree are ignored for the sake of compactness):

| form      | features                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------ |
| _nyttig_  | `Definite=Ind\|Gender=Com\|Number=Sing`                                                          |
| _nyttigt_ | `Definite=Ind\|Gender=Neut\|Number=Sing`                                                         |
| _nyttiga_ | `Definite=Def` in singular definite contexts;<br> `Definite=Ind\|Number=Plur` in plural contexts |

Nyttiga regler för nyttiga adjektiv!

## _Att vara X år gammal_ or _to be X years old_

[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1100)

The expression _to be X years old_/_att vara X år gammal_ used to be treated inconsistently across English and Swedish treebanks.
As of UD 2.16, annotation has been standardized to

<svg width="396" height="135" style="background-color:white" style="background-color:white" style="background-color:white" viewBox="0 0 396 135" version="1.1" xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="128" font-size="16">att/to</text>
  <text x="69" y="128" font-size="16">vara/be</text>
  <text x="142" y="128" font-size="16">X</text>
  <text x="179" y="128" font-size="16">år/years</text>
  <text x="261" y="128" font-size="16">gammal/old</text>
  <text x="5" y="113" font-size="10">PART</text>
  <text x="69" y="113" font-size="10">AUX</text>
  <text x="142" y="113" font-size="10">NUM</text>
  <text x="179" y="113" font-size="10">NOUN</text>
  <text x="261" y="113" font-size="10">ADJ</text>
  <path d="M 16 100 Q 16 50 66 50 L 220 50 Q 270 50 270 100" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="16" y1="95" x2="16" y2="100" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 16 100 13 94 19 94"></path>
  <text x="134" y="45" font-size="10">mark</text>
  <path d="M 80 100 Q 80 67 113 67 L 237 67 Q 270 67 270 100" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="80" y1="95" x2="80" y2="100" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 80 100 77 94 83 94"></path>
  <text x="168" y="62" font-size="10">cop</text>
  <path d="M 156 100 Q 156 83 171 83 L 171 83 Q 185 83 185 100" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="156" y1="95" x2="156" y2="100" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 156 100 153 94 159 94"></path>
  <text x="157" y="78" font-size="10">nummod</text>
  <path d="M 191 100 Q 191 83 207 83 L 253 83 Q 269 83 269 100" stroke="black" fill="none" style="--darkreader-inline-stroke: var(--darkreader-text-000000, #e8e6e3);" data-darkreader-inline-stroke=""></path>
  <line x1="191" y1="95" x2="191" y2="100" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 191 100 188 94 194 94"></path>
  <text x="223" y="78" font-size="10">obl</text>
  <line x1="276" y1="20" x2="276" y2="100" stroke="black" style="--darkreader-inline-stroke: var(--darkreader-border-000000, #8c8273);" data-darkreader-inline-stroke=""></line>
  <path d="M 276 100 273 94 279 94"></path>
  <text x="281" y="28" font-size="10">root</text>
</svg>

Most importantly, _gammal/old_ is the head and _år/years_ is assigned the deprel [`obl`](https://universaldependencies.org/sv/dep/obl.html).
Some English treebank specify the subtype [`obl:unmarked` (adpositionless oblique)](https://universaldependencies.org/en/dep/obl-unmarked.html).

If you speak any other languages where a similar construction is used, check how it is annotated!

<!-- TODO:

Open issues (guess I'll make a part 2 eventually)
- [ ] https://github.com/UniversalDependencies/docs/issues/1082
- [ ] https://github.com/UniversalDependencies/docs/issues/1083
- [ ] https://github.com/UniversalDependencies/docs/issues/1121
- [ ] https://github.com/UniversalDependencies/docs/issues/1122
- [ ] https://github.com/UniversalDependencies/docs/issues/1129
- [ ] https://github.com/UniversalDependencies/docs/issues/1131
- [ ] https://github.com/UniversalDependencies/docs/issues/1132
- [ ] https://github.com/UniversalDependencies/docs/issues/1136
- [ ] https://github.com/UniversalDependencies/docs/issues/1139
- [ ] https://github.com/UniversalDependencies/docs/issues/1148
- [ ] https://github.com/UniversalDependencies/docs/issues/1149
- [ ] https://github.com/UniversalDependencies/docs/issues/1152
- [ ] https://github.com/UniversalDependencies/docs/issues/1165

-->