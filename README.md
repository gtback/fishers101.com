# fishers101.com

Source text for <https://fishers101.com>.

## Usage

Build the site:

```shell
mkdir -p out
cp styles.css out
python ./build.py index.md > out/index.html
```

Serve the site:

```shell
python -m http.server -b 127.0.0.1 -d out 8000
```
