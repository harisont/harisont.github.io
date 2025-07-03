---
title: FACS - FAQs about LT2214 Computational Syntax
---

This is a collection of questions about [Grammatical Framework](https://www.grammaticalframework.org/) and [Universal Dependencies](https://universaldependencies.org/) that I've been asked at least twice during a single edition of the [LT2214 Computational Syntax](https://kursplaner.gu.se/pdf/kurs/en/LT2214.pdf) course at the University of Gothenburg, and/or that I haven't been able to answer exhaustively in class, and/or that I myself tend to forget the answer to in between years.

Categories:
- [GF](#gf)
  - [File structure/module types](#file-structuremodule-types)
  - [GF terms/types of judgments](#gf-termstypes-of-judgments)
  - [GF syntax](#gf-syntax)
  - [Encoding issues](#encoding-issues)
  - [Using GF from Python](#using-gf-from-python)
- [UD](#ud)
  - [MultiWord tokens](#multiword-tokens)
  - [Conjunctions](#conjunctions)
  - [Syntax highlighting](#syntax-highlighting)
  - [Arborator](#arborator)
  - [MaChAmp](#machamp)
  - [UD validator](#ud-validator)

## GF

### File structure/module types
> What goes in which files?

In GF, there are several module types:

name | contents | example from the course
--- | --- | ---
`abstract` | abstract syntax (cross-lingual) | `MicroLang.gf`
`concrete` | concrete syntax (language-specific) | `MicroLangEng.gf`
`resource` | reusable collection of `oper`s (see next question), i.e. library (type signatures & bodies together) | `MicroResEng.gf`
`interface` | "abstract syntax" (type declarations) of a resource module | not used in this course
`instance` | "concrete syntax" of a resource module whose "abstract syntax"  is defined in an interface |not used in this course
`incomplete concrete` | partial "concrete syntax", used when some things are common to a few of the languages in covered in the grammar, but not all of them | not used in this course

Let's focus on the first three.

An `abstract` module typically contains:
- the list of the names of the cross-lingual `cat`egories used in the grammar (e.g. `Det`, `CN`, `NP`...)
- a list of "`fun`ctions", i.e. type signatures for the `lin`earization rules of the grammar (e.g. `DetCN : Det -> CN -> NP ;`).
An abstract module works a bit like a Java interface, or rather, if you haven't done any object-oriented programming, as _contract_ that specifies all the things the concrete syntaxes for each language have to provide for the grammar to be complete.

A `concrete` module contains the "implementations" of the `cat`s and `lin`s listed in the abstract syntax, for example:
- a `Det` in English can be represented as a record storing a string and a number:
  ```haskell
  lincat Det = {s : Str ; n : Number} ;
  ```
- the "body" of the `fun`ction (i.e. its `lin`earization rule) `DetCN` can be written as
  ```haskell
  lin DetCN det cn = {
    s = \\c => det.s ++ cn.s ! det.n ;
    a = Agr det.n } ;
  ```

Finally, a `resource` module is just a bunch of `oper`s (i.e. helper functions) and `param`eter definitions that can be imported in other modules. 
You may well decide not to have a separate resource module in your grammar, but especially if your language of choice has extensice morphology, that's a good place to store all the `param`eters and smart paradigms without cluttering your `MicroLangXxx` module.

### GF terms/types of judgments
> Can you give me a recap of what all of `cat`, `lincat`, `fun`, `lin`, `oper` and `param` mean?

There you go:

name | short for | description | found in | example
--- | --- | --- | --- | ---
`cat` | category | grammatical category | abstract modules | `cat Noun` |
`lincat` | linearization type | language-specific "implementation" of a category | concrete modules | `lincat Noun = {s : Number => Str}` 
`fun` | function | type signature of a grammar rule | abstract modules | `fun UseN : N -> CN`
`lin` | linearization rule | language-specific "implementation" of a grammar rule | concrete modules | `lin UseN n = n`
`oper` | operation | helper function | here, there and everywhere (but often in concrete __and__ resource modules) | `oper regNoun : Str -> Noun = \sg -> mkNoun sg (sg + "s")`
`param` | parameter | language-specific (inflectional) parameter tables | typically resource modules | `param Number = Sg | Pg`


### GF syntax
> What is the difference between `->` and `=>`?

`->` is for functions, `=>` is for tables.

More specifically:

- `->` is used when _declaring the type signature of a function_ (i.e. of a `fun` or an `oper`). Examples:
  - `fun PredVPS : NP -> VP -> S ;`
  - `oper regNoun : Str -> Noun = ...`
- `\ ->` is when _defining a function_ (typically in `oper`s). Example:

  ```haskell
  ... \sg -> mkNoun sg (sg + "s") ;
  ```
- `=>` is used when:
  - _declaring the type of a table_ (typically in `lincat`). Example:

    ```haskell
    lincat N = {s : Number => Str} ;
    ```
  - _filling in the cell of a table_. Example:

    ```haskell
    table { Sg => "cat" ; 
            Pl => "cats"}
    ```
- `\\ =>` is used for _filling in tables whose cells are all to be filled in the same way_ (single-branch tables). Example:
  
  ```haskell
  AdjCN a cn = {
    -- whatever the n (the number) is, use it to select the correct cell of the table for the CN
    s = \\n => a.s ++ (cn.s ! n) ;
  } ;
  ```

### Encoding issues
> I am working with a language that uses a non-latin script and, when I try to linearize a tree, I get the following error:
>   ```
>   <stdout>: commitBuffer: invalid argument (invalid character)
>   ```
> How do I fix it?

Add the line

```
flags coding = utf8 ;
```

to your concrete module. 

This is necessary because the default encoding for GF source files is iso-latin-1, which can only handle the ASCII charset and a few extra characters needed for some European languages.

### Using GF from Python
> I am getting started with lab 2 and I can't install/run the Python `pgf` library and/or the C runtime.

For the moment, don't: follow [Aarne's alternative instructions for testing](https://github.com/GrammaticalFramework/comp-syntax-gu-mlt/blob/034f3a4771efd47cea9c53bcff1b493b577cce04/lab2/README.md?plain=1#L26-L30).

## UD

### MultiWord tokens
> How do I analyze:
> 1. "do" ("de + "o") in Portuguese
> 2. "au" ("à" + "le") in French
> 3. "nel" ("in" + "il") in Italian
> 4. "dámelo" ("da" + "me" + "lo") in Spanish
> 
> and so on?

UD version 2 treats these cases (where an orthographic word consists of several syntactic units) as MultiWord Tokens (MWTs). 
Annotation consists of a so-called _range line_ with the original form but no analysis, followed by 2+ lines where each individual element is analyzed individually.
Example for portuguese.

```tsv
# text = A comida do gato.
# gloss = The food of+the cat.
1	A	o	DET	_	_	2	det	_	_
2	comida	comida	NOUN	_	_	0	root	_	_
3-4	do	_	_	_	_	_	_	_	_
3	de	de	ADP		_	5	case	_	_
4	o	o	DET	_	_	5	det	_	_
5	gato	gato	NOUN	_	_	2	nmod	_	_
6	.	.	PUNCT	_	_	2	punct	_	_
```

Unfortunately, [MaChAmp](#machamp) cannot fully handle this yet.
This is one of the reasons why you need to preprocess all of its input files as indicated in the [lab description](https://github.com/GrammaticalFramework/comp-syntax-gu-mlt/tree/main/lab3#step-2-preparing-the-training-and-development-data).

### Conjunctions
> How do I annotate conjunctions, in phrases like "A and B"?

Like this:

<svg width="149"
     height="115"
     viewBox="0 0 149 115"
     version="1.1"
     xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="108" font-size="16" fill="white">A</text>
  <text x="42" y="108" font-size="16" fill="white">and</text>
  <text x="97" y="108" font-size="16" fill="white">B</text>
  <text x="5" y="93" font-size="10" fill="white">SYM</text>
  <text x="42" y="93" font-size="10" fill="white">CCONJ</text>
  <text x="97" y="93" font-size="10" fill="white">SYM</text>
  <line x1="20" y1="20" x2="20" y2="80" stroke="white"/>
  <path d="M 20 80 17 74 23 74" fill="white"/>
  <text x="25" y="28" font-size="10" fill="white">root</text>
  <path d="M 55 80 Q 55 63 71 63 L 88 63 Q 104 63 104 80"
        stroke="white"
        fill="none"/>
  <line x1="55" y1="75" x2="55" y2="80" stroke="white"/>
  <path d="M 55 80 52 74 58 74" fill="white"/>
  <text x="75" y="58" font-size="10" fill="white">cc</text>
  <path d="M 27 80 Q 27 47 60 47 L 82 47 Q 115 47 115 80"
        stroke="white"
        fill="none"/>
  <line x1="115" y1="75" x2="115" y2="80" stroke="white"/>
  <path d="M 115 80 112 74 118 74" fill="white"/>
  <text x="62" y="42" font-size="10" fill="white">conj</text>
</svg>

> But why? Then A and B are not on the same level!

Reasonable objection.
However, remember that UD prioritizes cross-lingual parallelism by avoiding using function words (such as conjunctions) as syntactic heads.

In latin, for example "A and B" can be translated as both "A et b" and "A Bque" (e.g. "SPQR: Senatus PopolusQue Romanus"). 
If we used "et" as the head, the trees for "A and/et B" becomes:

<svg width="149"
     height="95"
     viewBox="0 0 149 95"
     version="1.1"
     xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="88" font-size="16" fill="white">A</text>
  <text x="42" y="88" font-size="16" fill="white">et/and</text>
  <text x="97" y="88" font-size="16" fill="white">B</text>
  <text x="5" y="73" font-size="10" fill="white">SYM</text>
  <text x="42" y="73" font-size="10" fill="white">CCONJ</text>
  <text x="97" y="73" font-size="10" fill="white">SYM</text>
  <path d="M 19 60 Q 19 43 33 43 L 33 43 Q 48 43 48 60"
        stroke="white"
        fill="none"/>
  <line x1="19" y1="55" x2="19" y2="60" stroke="white"/>
  <path d="M 19 60 16 54 22 54" fill="white"/>
  <text x="25" y="38" font-size="10" fill="white">conj</text>
  <line x1="57" y1="20" x2="57" y2="60" stroke="white"/>
  <path d="M 57 60 54 54 60 54" fill="white"/>
  <text x="62" y="28" font-size="10" fill="white">root</text>
  <path d="M 65 60 Q 65 43 81 43 L 98 43 Q 114 43 114 60"
        stroke="white"
        fill="none"/>
  <line x1="114" y1="55" x2="114" y2="60" stroke="white"/>
  <path d="M 114 60 111 54 117 54" fill="white"/>
  <text x="81" y="38" font-size="10" fill="white">conj</text>
</svg>

which is more different than it needs to be from

<svg width="93"
     height="95"
     viewBox="0 0 93 95"
     version="1.1"
     xmlns="http://www.w3.org/2000/svg">
  <text x="5" y="88" font-size="16" fill="white">A</text>
  <text x="42" y="88" font-size="16" fill="white">Bque</text>
  <text x="5" y="73" font-size="10" fill="white">SYM</text>
  <text x="42" y="73" font-size="10" fill="white">NOUN</text>
  <line x1="20" y1="20" x2="20" y2="60" stroke="white"/>
  <path d="M 20 60 17 54 23 54" fill="white"/>
  <text x="25" y="28" font-size="10" fill="white">root</text>
  <path d="M 29 60 Q 29 43 43 43 L 43 43 Q 58 43 58 60"
        stroke="white"
        fill="none"/>
  <line x1="58" y1="55" x2="58" y2="60" stroke="white"/>
  <path d="M 58 60 55 54 61 54" fill="white"/>
  <text x="35" y="38" font-size="10" fill="white">conj</text>
</svg>

where you can clearly see what the two conjuncts are.

> But can't "Bque" be treated as a [MWT](#multiword-tokens)?

Sure can: in that case, you would split "B" and "que" and you could in theory treat the clitic "que" as a head.
But imagine a language where conjunction is expressed by simply justaposing the conjuncts (e.g. "A B"). What would be the head then?

### Syntax highlighting
> I have tried to install the [vscode-conllu](https://marketplace.visualstudio.com/items/?itemName=lgrobol.vscode-conllu) extension but it doesn't seem to work.

1. check that your filename ends in `.conllu` (which is not the same as `.connllu`)
2. check that you are using tabs and not spaces as separators
3. if it still doesn't work, save the file as `.tsv`. You'll get a different but equally good highlighting for the token lines

> I want syntax highlighting, but I don't use Visual Studio Code.

GOTO step 3 of the answer above ;) 
Most editors have support for highlighting TSVs and CSVs. 

### Arborator
> I am using [Arborator](arborator.grew.fr) for annotation and I can't find my project under "My Projects"

...I know right? 
For the moment, look for it from the homepage using the search bar and then save the direct link.
Eventually, I hope they'll solve the [issue](https://github.com/Arborator/arborator-frontend/issues/442).

### MaChAmp
> I am trying to run a [MaChAmp](https://github.com/machamp-nlp/machamp) script but it fails complaining that some other Python file does not exist.

Check that you are running the script from Machamp's root folder (i.e. the folder named `machamp` or `machamp-master`).

> I successfully installed MaChamp and preprocessed the training and development data and I'm now trying to train my model, but training fails with something like

> ```
> 2025-05-21 10:34:51,518 - ERROR - STDERR - [enforce fail at inline_container.cc:595] . unexpected pos 196207040 vs 196206992
> ```

There is probably some formatting error in your CoNNL-U input files. 
The most common ones are:

1. missing newlines at the end of the file, which often happens when you split the data into a training and development set yourself
2. the diabolical non-unix newline characters, which some editors on Windows like adding when you simply _open_ your files.

To fix error 1, open your files and check that it ends with __two__ empty lines. 
If it doesn't, add one.

To fix error 2, run

```bash
tr -d '\r' < PATH-TO-YOUR-NONUNIX-FILE.conllu >  PATH-FOR-THE-OUTPUT-FILE.conllu
```

(which means "delete all `\r` characters from the non-unix file and write the output on a new file").

If training still fails after this, try to validate your CoNNL-U file(s) (see below).

### UD validator
> How do I use the official UD validator?

1. clone or download [the UD tools repository](https://github.com/UniversalDependencies/tools)
2. move inside the `tools` folder
3. run 
   ```
   python PATH-TO-YOUR-TREEBANK.conllu --lang=2-LETTER-LANGCODE-FOR-YOUR-LANGUAGE
   ```

MaChAmp should only be concerned about basic formatting issues, so if you are validating for MaChAmp you can add `--level=1`. If you want to check for errors in your own annotated files, however, you can go up a few levels: 
- 2 checks UD format specifics
- 3 checks that the universal UD guidelines are followed (e.g. that there are no `VERB`s used as `AUX` or multiple subjects in the same sentence)
- 4 and 5 check language-specific stuff.