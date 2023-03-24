# pre-commit-enforce-https
A pre-commit hook to enforce https instead of http

## Usage
Add this to your `.pre-commit-config.yaml`:
```yaml
-   repo: https://github.com/GideonBear/pre-commit-enforce-https
    rev: v1.0.0
    hooks:
    -   id: enforce-https
```
## Examples
```diff
- [This](http://google.com) is a link to google
+ [This](https://google.com) is a link to google
```
```diff
- data = requests.get('http://api.example.com').json
+ data = requests.get('https://api.example.com').json
```
### Using `allow-http` to suppress enforce-https:
```py
protocol_sensitive_operation('http://example.com')  # allow-http
```
```md
[This](http://example.com) is a protocol-sensitive link  <!-- allow-http -->
```
