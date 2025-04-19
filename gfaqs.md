---
title: GFAQs
---

This is a collection of questions about [Grammatical Framework](https://www.grammaticalframework.org/) that I've been asked at least twice during a single edition of the [Computational Syntax](https://kursplaner.gu.se/pdf/kurs/en/LT2214.pdf) course at the University of Gothenburg, and/or that I haven't been able to answer exhaustively in class, and/or that I myself tend to forget the answer to in between years.

Categories:
- [GF syntax](#gf-syntax)
- [Encoding issues](#encoding-issues)


## GF syntax
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

## Encoding issues
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
