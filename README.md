# enforce-https
A pre-commit hook to enforce https instead of http

## Usage
Add this to your `.pre-commit-config.yaml`:
```yaml
-   repo: https://github.com/GideonBear/pre-commit-enforce-https
    rev: v1.3.0
    hooks:
    -   id: enforce-https
```
## Examples
<!-- allow-http-in-2-lines -->
```diff
- [This](http://google.com) is a link to google
+ [This](https://google.com) is a link to google
```
<!-- allow-http-in-2-lines -->
```diff
- data = requests.get('http://api.example.com').json
+ data = requests.get('https://api.example.com').json
```
### Using `allow-http` to suppress enforce-https
```py
protocol_sensitive_operation('http://example.com')  # allow-http
```
```md
[This](http://example.com) is a protocol-sensitive link  <!-- allow-http -->
```
### Using `allow-http-in-x-lines` to suppress enforce-https
````md
<!-- allow-http-in-4-lines -->
```py
from library import function

function('http://example.com')
```
````
