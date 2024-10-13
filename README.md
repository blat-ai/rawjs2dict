<div align="center">
  <a href="https://blat.ai">
    <img src="https://framerusercontent.com/assets/ZD9Sg28IboDmP0DfMFxuv0EOQBk.png" alt="Blat">
  </a>
</div>
</br>

# RawJS2Dict
A Python library that converts raw Javascript scripts into Python dictionaries, extracting the hardcoded literals in the script.

## Why?
Many websites have JS scripts that contain hardcoded JSON strings or even JS objects that contain all of the data displayed
in the website before even rendering the website. So scraping the data from this scripts can be messy because many times you
need to write and maintain regexes or executing the JS in the browser, which can be expensive.
So, this library is very useful useful for parsing the data hardcoded in these scripts using a deterministic and generic approach that would let you transform something like this:
```
var a = "b";
window.test = JSON.parse('{"a": 1, "b": 2}');
var f = function() {
    var x = 0;
    var t = function() {
        y = JSON.parse('{"c": 3, "d": 4}');
    }
};
class Test {
    constructor() {
        this.a = 1;
    }
}
```
Into something easy to parse like this:
```
{
  "a": "b",
  "window_test": {"a": 1, "b": 2},
  "f": {"x": 0.0, "t": {"y": {"c": 3, "d": 4}}},
  "Test": {"constructor": {"a": 1.0}}
}
```
## Getting Started
### Requirements
* [nodejs](https://nodejs.org/)
* [npm](https://www.npmjs.com/)
* [python3](https://www.python.org)

### Installation
Follow these steps to install rawjs2dict on your computer:

1. Install NodeJS and npm following the [official docs](https://nodejs.org/en/download/package-manager/)
2. Install rawjs2dict library
```bash
pip install rawjs2dict
```

### Usage
```python
import rawjs2dict

script = "var x = 0;"
rawjs2dict.transform(script)
```

## Getting Help
GitHub is currently the only way to interact with our team. You can [open an issue](https://github.com/blat-ai/rawjs2dict/issues/new/choose) and choose one of the templates to ask for guidance, to report a bug, or to request a new feature.

Before opening a new issue, please check if there's similar [issues](https://github.com/blat-ai/rawjs2dict/issues) already created.