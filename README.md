# About
A small module to explore a large json object or string or file and print out its structure to the console.

# Usage
### Explore JSON file
```python
import json_explorer

json_explorer.explore_file("/home/user/json_explorer/test.json")

# The exploration will be printed to the console.
```

### Explore JSON object
```python
import json_explorer

json_string = '[{"_id": "58c5821a7601f427b5234503", "tags": ["occaecat", "cillum"]}]'
json_explorer.explore_string(json_string)

# The exploration will be printed to the console.
```

### Explore JSON object
```python
import json
import json_explorer

json_string = '[{"_id": "58c5821a7601f427b5234503", "tags": ["occaecat", "cillum"]}]'
json_object = json.loads(json_string)
json_explorer.explore_object(json_object)

# The exploration will be printed to the console.
```

## Output of the snippets
```
HEAD
LIST
	DICT
		_id
			VALUE: 58c5821a7601f427b5234503
			TYPE : <type 'unicode'>
		tags
		LIST
			VALUE: occaecat
			TYPE : <type 'unicode'>
			.
			.
			.
```

# Installation
## Install using pip
`pip install git+https://github.com/nitred/json_explorer.git --upgrade`

## Install using setup.py
```
git clone https://github.com/nitred/json_explorer.git
cd json_explorer
pytho setup.py install
```
