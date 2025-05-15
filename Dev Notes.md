### One-shot service

`valhalla.json`, based on `test\bindings\python\valhalla.json`. Changing paths to load extracted map tiles.

```sh
valhalla_service valhalla.json {action} {action-options-json} > response.json
```

```sh
valhalla_service valhalla.json route settings.json > response.json
```
