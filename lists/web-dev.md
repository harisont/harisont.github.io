---
title: Web development notes
layout: post
---

Modern web dev stuff I stumbled upon while working on [a WYTIWYS (What You Tree Is What You Search) corpus query interface](https://github.com/harisont/wytiwys) and [a recipe website by and for programmers](https://github.com/rapunschel/concurrent-cooking).

I learned the very, very basics of web development several years ago and didn't like it very much. 
These are two projects that I approached with a strong intention to get things done, but no particular desire to learn anything new systematically. 
The [_Changing Stuff and Seeing What Happens_](https://orlybooks.com/books/changing-stuff-and-seeing) approach worked to a surprising extent, and as I trial-and-errored my way through the code (and occasionally resorted to actually look up oddly specific stuff), I noted down random things I found remarkable, regretful, revolting, or (rarely) reasonable and even rewarding.

- [Nodenotes](#nodenotes)
  - [Setting up `nvm` (Node Version Manager)](#setting-up-nvm-node-version-manager)
  - [Installing version `n` of Node](#installing-version-n-of-node)
  - [Using version `n` of Node](#using-version-n-of-node)
  - [Installing a TypeScript project](#installing-a-typescript-project)
  - [Using a local module in a TypeScript project](#using-a-local-module-in-a-typescript-project)
- [CSS (Cursed Style Sheets)](#css-cursed-style-sheets)
  - [Hiding stuff](#hiding-stuff)
  - [Selectors](#selectors)
- [So-called TypeScript](#so-called-typescript)
  - [Array concatenation](#array-concatenation)
  - [Last element of an array](#last-element-of-an-array)
  - [Introspection](#introspection)
  - [Integer to string and vice versa](#integer-to-string-and-vice-versa)
  - [Lambdas](#lambdas)
  - [JSON object operations](#json-object-operations)
  - [Ternary operator](#ternary-operator)
  - [Kind of the same or actually identical?](#kind-of-the-same-or-actually-identical)
- [React](#react)
  - [Using variables](#using-variables)
  - [Passing a tag its props](#passing-a-tag-its-props)
- [Vue](#vue)
  - [Single File Components](#single-file-components)
  - [Passing a tag its props](#passing-a-tag-its-props-1)
  - [Instantiating components programmatically](#instantiating-components-programmatically)
  - [Events](#events)


## Nodenotes

### Setting up `nvm` (Node Version Manager)
1. install `nvm` from your package manager
2. add
   ```
    . /usr/share/nvm/init-nvm.sh
   ```
   to the shell config file.


### Installing version `n` of Node
```
nvm install n
```

### Using version `n` of Node
```
nvm use n
```

### Installing a TypeScript project
```
npm install
```

### Using a local module in a TypeScript project
1. package the module into a `.tgz`:
   ```
   npm pack
   ```
2. move to the project folder and install the package:
   ```
   npm install --save PATH-TO-TGZ
   ```

## CSS (Cursed Style Sheets)

### Hiding stuff
- `visibility: hidden` is like the invisibility cloak (the element becomes transparent, but still takes up space)
- `display: none` prevents the element from showing up at all

### Selectors

Basic selectors:

- `*`
- `tag`
- `.class`
- `#id`
- `[attribute]`

Useful combinations:
- `tag.class` (all `tag`s of a given class)
- `.class tag` (all `tag`s that are descendants of a tag with a given `class`)
- `.class>tag` (all `tag`s that are _direct_ descendants (children) of a tag with a given `class`)
- `tag[attribute]` (all `tag`s with a given `attribute`)
- `.class1.class2` (all elements that have both `class1` and `class2`)



## So-called TypeScript
(much of which also applies to JavaScript)

### Array concatenation
Given

```typescript
const a: number[] = [1, 2];
const b: number[] = [3, 4];
const c: number[] = [5];
```

- spread operator:

   ```typescript
   const abc = [...a, ...b, ...c];
   ```

- `concat` method:

   ```typescript
   const abc = a.concat(b).concat(c);
   ```
   
   but also: 

   ```typescript
   const abc = a.concat(b, c);
   ```

   and even:

   ```typescript
   const abc = a.concat(3, 4, 5); // wild!
   ```

### Last element of an array

```typescript
xs.slice(-1)[0]
```

### Introspection
Two operators:
- `typeof x` for simple built-in types (`boolean`, `number`, `string`, `object`, `function`). It returns a __lowercase string__ with the name of the type
- `x instanceof Y` for custom types (classes) and complex built-in types, whatever they are (but `Array` is one of them). The operands are an object and a class (__not a string__ containing the name of the class!) 

Examples:

```typescript
typeof [] == 'object'   // true
[] instanceof Object    // true
[] instanceof Array     // also true, because arrays are objects

typeof null == 'object' // true, but for no good reason at all
```


### Integer to string and vice versa
```typescript
int.toString();
parseInt(str, base);
```

### Lambdas
```typescript
(par1: type2, par2: type2): returnType => expression
```

### JSON object operations
Kinda like a Python dictionary:

- does a `json` object have a certain `key`? 
  ```typescript
  key in json
  ```
- delete a `key`-value pair from a `json` object:
  ```typescript
  delete json[key]
  ```
- add a `key`-`val` pair to a `json` object:
  ```typescript
  json[key] = val
  ```

### Ternary operator
I guess Javascript _is_ a bit like Java:

```typescript
condition ? what_if_true : what_if_not
```

### Kind of the same or actually identical?
- `==` (abstract equality operator) compares two values after doing the "necessary" type conversions
- `===` (strict equality operator) also requires the types to be the same

Examples:
```typescript
false == 0     // as true as in Python
false == '0'   // also true!
false === 0    // false
false === '0'  // also false, thankfully
```

## React

### Using variables
```html
{variable}
```

### Passing a tag its props
If a tag was a function, props would be its (named) parameters:

```html
<Tag propName={propVal}/>

<!--or simply-->
<Tag {propVal}/>
```

## Vue
(which did not change my views on web development)

### Single File Components
This is the idea that everything you learned about the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns#HTML,_CSS,_JavaScript) is wrong and that it is indeed a good idea to have everything in one file, which will end up looking something like this:

```html
<template>
  <p ref="example">Normal HTML but with {{ holes }}, called "slots" and filled with "props" (like in React)</p>
  <!-- ...and and some weird attributes. 
  For example, ref basically means id but isn't a synonym for id -->
</template>

<script>
  // JS/TS but maybe with some additional structure, like
  export default {
    name: "HolyParagraph",
    props: {
    holeFiller: String
  },
  // not to mention that components are like classes enough that they can have
  methods: {
    onClickOrSomething() {
      // why would I even click on a paragraph?
    },
    ...
  }
</script>

<style>
  /* some of those cursed rules, if you really have to */
</style>
```

### Passing a tag its props
Like [React](#passing-a-tag-its-props), but worse:

```html
<HolyParagraph :holeFiller="stuff">
```

note that `"stuff"` is not a string whose content is the word "stuff", but _the name of a variable_ (or it could be anything, really) in quotes. 

### Instantiating components programmatically
[Kushagra Gour](https://css-tricks.com/creating-vue-js-component-instances-programmatically/) said it better than me, but I will say it shorter.

If a component is like a class enough that it has methods, you would think that you can use it like an class:

```typescript
var p = new HolyParagraph(stuff);
// append to another component or do whatever you want with it
```

...but no, it's more like:

```typescript
import Vue from 'vue'
var HolyParagraphClass = Vue.extend(HolyParagraph); // make the component a class, I guess?
var p = new HolyParagraphClass({                     // instantiate it
    propsData: { holeFiller: stuff }            // concisely pass it the props
})); 
instance.$mount()                               // go figure
// append to another component or do whatever you want with it
```

In Kushagra's tutorial there's [another step](https://css-tricks.com/creating-vue-js-component-instances-programmatically/#aa-setting-the-slot) too, but I skipped that because I was not sure what it was talking about and my code worked anyway.

### Events
When children want to communicate with their parents, they `$emit` events:

```html
<!-- Excerpt form a hypothetical Child.vue -->
...
<script>
export default {
  methods: {
    askDad() {
      this.$emit("question", "Why is there time? Why is there space? Why are there dogs and cats and trees and the human race?");
    }
  }
}
</script>
...
```
Here's how parents handle specific events:

```html
<!-- Excerpt form a hypothetical Dad.vue -->
<template>
  <Child @question="handle"/>
</template>

<script>
export default {
  methods: {
    handle(message) {
      console.log("Go ask your mom or just go away!");
    }
  }
}
</script>
```

`@event` is a newer synonym for `v-on:event`, which in turn is similar to plain JS `onEvent` (so for instance `onClick` becomes `v-on:click` in Vue and now also `@click`).