# RV Level Sensor v1.0.1 Beta 3

Test release with more robust automatic entity detection.

## Changes
- Automatic prefix detection now scores related inclination, height, battery, connect/disconnect and connection entities together.
- A manually set `entity_prefix` remains unchanged as an override.
- The automatic dashboard resource registration that worked in Beta 2 is retained.
- Frontend cache identifier bumped to `1.0.1-beta.3`.

## Test
First test without a prefix:

```yaml
type: custom:xparkle-rv-level-card
```

If required, the manual variant is still available:

```yaml
type: custom:xparkle-rv-level-card
entity_prefix: sensor.rvlevel_410f
```
