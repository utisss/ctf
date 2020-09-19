# Web: Opacity 0
Difficulty: Easy

In this challenge, you're given a website which shows nothing but a small string of text.

Viewing the source tells us that there is some custom CSS:
```
img {
    opacity: 0;
    display: none;
    width: 0;
    height: 0;
}
```

This CSS causes the img tag below it to not show up in the browser. We can open Inspect Element,
click on the img tag, then uncheck the styles being applied to it to make it show up.

Alternatively, we can copy the base64 string that describes the image, then decode the base64 to
obtain the raw .png file. 