---
title: Rarely Asked Questions about Swedish UD
layout: post
---

## _Går att `VERB`a_ and other equally tough constructions
[[go to discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1128)

How to annotate sentences like _detta går att debattera_?
Well, that sparked a whole debate.

Semantically, _detta_ is the object of _debattera_.
If we rephrase the sentence into _det går att debattera detta_ or _att debattera detta går_, the syntactic analysis coincides with the semantic one:

<svg width="324" height="115" viewBox="0 0 324 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
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

<svg width="268" height="115" viewBox="0 0 268 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
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

<svg width="268" height="115" viewBox="0 0 268 115" version="1.1" xmlns="http://www.w3.org/2000/svg">
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

1. this problem is tough to solve
2. it is tough to solve this problem
3. to solve this problem is tough

In sentences like (1), the syntactic subject _problem_ of the main verb _is_ is logically the object of an embedded non-finite verb _solve_ (although in UD, the root of the sentence would be _tough_, not _is_), whereas in paraphrases (2) and (3) logical and grammatical structure coincide. 
General guidelines about the annotations of _tough_-constructions, though, are still [under debate](https://github.com/UniversalDependencies/docs/issues/923) at the time of writing.

## Subword-level coordination
[[go to the discussion on GitHub]](https://github.com/UniversalDependencies/docs/issues/1150)

How to analyze constructions like _levnads- och beteendemässigt_?

Ideally, we would want the conjuncts _levnads-_ och _beteende(-)_, and to form a compound with _mässigt_, but this is currently beyond the expressive capacity of UD.
To circumvent the problem, we lemmatize _levnad_ as _levnadsmässigt_, obtaining a conjunction of two adverbs.

---


TODO: intro (context, Eukalyptus, SweLL, who's involved, links to issues...)

TODO: closed issues
- [ ] https://github.com/UniversalDependencies/docs/issues/1088
- [ ] https://github.com/UniversalDependencies/docs/issues/1092
- [ ] https://github.com/UniversalDependencies/docs/issues/1100
- [ ] https://github.com/UniversalDependencies/docs/issues/1107
- [ ] https://github.com/UniversalDependencies/docs/issues/1126
- [x] https://github.com/UniversalDependencies/docs/issues/1128
- [x] https://github.com/UniversalDependencies/docs/issues/1150

TODO: open issues
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
