---
title: LuXurY LaTeX
layout: post
---

Stuff that make LaTeX an actually pleasurable experience, but that I have to look up every single time:

- [Compilers](#compilers)
- [Macros](#macros)
- [Resizing stuff to text/column width](#resizing-stuff-to-textcolumn-width)

## Compilers
| if                                        | then     |
| ----------------------------------------- | -------- |
| Greek + Latin characters in the same text | XeLaTeX  |
| Springer Nature template                  | pdfLaTeX |

## Macros
Example macro with two arguments that creates a clean version of an unwieldy URL whilst retaining all the `https://`s and encoded mess in its clickable version:

```latex
\newcommand{\cleanurl}[2]{\href{#1}{\nolinkurl{#2}}}
% usage: \cleanurl{https://www.unwieldy.nope}{unwieldy.nope}
```

## Resizing stuff to text/column width
Essentially

```latex
\resizebox{\textwidth}{!}{whatever}
% replace \textwidth with \columnwidth as needed
```

but for tables, the box should be around the `tabular` and __not__ wrap the entire `table` environment.