---
title: Web development notes
layout: post
---

Modern web dev stuff I am, after all, learning while working on [a WYTIWYS (What You Tree Is What You Search) corpus query interface](https://github.com/harisont/wytiwys).

- [Nodenotes](#nodenotes)
  - [Setting up `nvm` (Node Version Manager)](#setting-up-nvm-node-version-manager)
  - [Installing version `n` of Node](#installing-version-n-of-node)
  - [Using version `n` of Node](#using-version-n-of-node)
  - [Installing a TypeScript project](#installing-a-typescript-project)
  - [Using a local module in a TypeScript project](#using-a-local-module-in-a-typescript-project)
- [TypeScript](#typescript)
  - [Array concatenation](#array-concatenation)
  - [Last element of an array](#last-element-of-an-array)
  - [Introspection](#introspection)
  - [Integer to string and vice versa](#integer-to-string-and-vice-versa)
  - [Lambdas](#lambdas)
  - [JSON object operations](#json-object-operations)


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

## TypeScript

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
- `typeof X`
- `OBJ instanceof TYPE`

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