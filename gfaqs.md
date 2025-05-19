---
title: FACS - FAQs about LT2214 Computational Syntax
---

This is a collection of questions about [Grammatical Framework](https://www.grammaticalframework.org/) and [Universal Dependencies](https://universaldependencies.org/) questions that I've been asked at least twice during a single edition of the [Computational Syntax](https://kursplaner.gu.se/pdf/kurs/en/LT2214.pdf) course at the University of Gothenburg, and/or that I haven't been able to answer exhaustively in class, and/or that I myself tend to forget the answer to in between years.

Categories:
- [GF](#gf)
  - [File structure](#file-structure)
  - [GF terms/types of judgments](#gf-termstypes-of-judgments)
  - [GF syntax](#gf-syntax)
  - [Encoding issues](#encoding-issues)
  - [Using GF from Python](#using-gf-from-python)
- [UD](#ud)
  - [Syntax highlighting](#syntax-highlighting)

## GF

### File structure
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
> I am getting started with lab 2 and I can't install/run the Python `pgf` library and/or the C runtime

For the moment, don't: follow [Aarne's alternative instructions for testing](https://github.com/GrammaticalFramework/comp-syntax-gu-mlt/blob/034f3a4771efd47cea9c53bcff1b493b577cce04/lab2/README.md?plain=1#L26-L30).

## UD

### Syntax highlighting
> I have tried to install the [vscode-conllu](https://marketplace.visualstudio.com/items/?itemName=lgrobol.vscode-conllu) extension but it doesn't seem to work

1. check that your filename ends in `.conllu` (which is not the same as `.connllu`)
2. check that you are using tabs and not spaces as separators
3. if it still doesn't work, save the file as `.tsv`. You'll get a different but equally good highlighting for the token lines

> I want syntax highlighting, but I don't use Visual Studio Code

GOTO step 3 of the answer above ;) 
Most editors have support for highling TSVs an CSVs 