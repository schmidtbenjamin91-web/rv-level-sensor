# RV Level Sensor v1.0.1 Beta 2

## Changes
- Automatic detection of the entity prefix for the dashboard card.
- Connect/Disconnect uses the button entities that actually exist.
- Supports different Home Assistant naming schemes such as `rvlevel_410f` and `rv_level`.
- `entity_prefix` remains available as an optional manual override.
- Frontend cache identifier bumped to `1.0.1-beta.2`.

## Test
```yaml
type: custom:xparkle-rv-level-card
```

Optional, with multiple devices:
```yaml
type: custom:xparkle-rv-level-card
entity_prefix: sensor.rvlevel_410f
```
