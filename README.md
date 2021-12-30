# Zagadnienia-Licencjat

## Jak stworzyc PDF?

Po wprowadzeniu zrobieniu ```git pull``` odpalamy ```merger.py``` kóry stworzy nam nowy plik ```master.md``` Nastepnie klikamy ```Ctrl+Shift+P``` w VSCode i wybieramy
```Markdown All In One: Print documents to HTML (selecta source folder)``` wybieramy folder tego wlasnie gita a nastepnie folder ```out```. Potem odpalamy w Chrome plik ```master.html``` klikamy ```Ctrl+P``` i opcje ```Print to PDF``` i zapisujemy plik gdzie chcemy.

## Podział pracy

|Szymon|Karyna|Maciej|Bartek|Denis|
|---|---|---|---|---|
|01 - 10|11 - 20|21 - 30|31 - 40|41 - 50|

Commity robimy do swoich branchy - pull requesty robimy, reviewer ustawiamy na @Szymonexis (zeby nie doszlo do kolizji)
### :warning: Spotkamy sie w sobote na discordzie i pewnie to jebniemy jednym strzalem

<hr />

# Markdown Cheat Sheet

Thanks for visiting [The Markdown Guide](https://www.markdownguide.org)!

This Markdown cheat sheet provides a quick overview of all the Markdown syntax elements. It can’t cover every edge case, so if you need more information about any of these elements, refer to the reference guides for [basic syntax](https://www.markdownguide.org/basic-syntax) and [extended syntax](https://www.markdownguide.org/extended-syntax).

## Basic Syntax

These are the elements outlined in John Gruber’s original design document. All Markdown applications support these elements.

### Heading

# H1
## H2
### H3

### Bold

**bold text**

### Italic

*italicized text*

### Blockquote

> blockquote

### Ordered List

1. First item
2. Second item
3. Third item

### Unordered List

- First item
- Second item
- Third item

### Code

`code`

### Horizontal Rule

---

### Link

[Markdown Guide](https://www.markdownguide.org)

### Image

![alt text](https://www.markdownguide.org/assets/images/tux.png)

## Extended Syntax

These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements.

### Table

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

### Fenced Code Block

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Footnote

Here's a sentence with a footnote. [^1]

[^1]: This is the footnote.

### Heading ID

### My Great Heading {#custom-id}

### Definition List

term
: definition

### Strikethrough

~~The world is flat.~~

### Task List

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

### Emoji

That is so funny! :joy:

(See also [Copying and Pasting Emoji](https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji))

### Highlight

I need to highlight these ==very important words==.

### Subscript

H~2~O

### Superscript

X^2^
