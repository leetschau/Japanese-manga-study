# Toolchain Setup

Prerequisite:

* `entr`: install with `apt`
* `reload`: install with `npm` of node.js

## Toolchain

Write Japanese sentences into a Quarto file (.qmd, say vol-01.qmd),
and render it in browser automatically:
```sh
ls *.qmd | entr quarto render vol-01.qmd
reload -n 10.162.2.83 -p 8282 -e html
```

Then open http://10.162.2.83:8282/vol-01.html in browser.
Now you can study the sentences word by word With browser extensions like JapaneseIO
or rikaikun.
