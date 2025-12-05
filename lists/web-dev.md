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
  - [Checking the types of things](#checking-the-types-of-things)
  - [Integer to string and vice versa](#integer-to-string-and-vice-versa)


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

### Checking the types of things
Use the `typeof` operator.

### Integer to string and vice versa
```typescript
int.toString();
parseInt(str, base);
```