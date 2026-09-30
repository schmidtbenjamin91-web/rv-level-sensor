# RV Level Sensor v1.0.1 Beta 2

## Änderungen
- Automatische Erkennung des Entity-Präfixes für die Dashboard-Karte.
- Connect/Disconnect verwendet die tatsächlich vorhandenen Button-Entities.
- Unterstützt unterschiedliche Home-Assistant-Namensschemata wie `rvlevel_410f` und `rv_level`.
- `entity_prefix` bleibt als optionale manuelle Vorgabe erhalten.
- Frontend-Cachekennung auf `1.0.1-beta.2` erhöht.

## Test
```yaml
type: custom:xparkle-rv-level-card
```

Optional bei mehreren Geräten:
```yaml
type: custom:xparkle-rv-level-card
entity_prefix: sensor.rvlevel_410f
```
