# RV Level Sensor v1.0.1 Beta 3

Testversion mit robusterer automatischer Entity-Erkennung.

## Änderungen
- Automatische Prefix-Erkennung bewertet jetzt zusammengehörige Neigungs-, Höhen-, Batterie-, Connect/Disconnect- und Verbindungs-Entities.
- Manuell gesetztes `entity_prefix` bleibt unverändert als Override erhalten.
- Die in Beta 2 funktionierende automatische Dashboard-Ressourcenregistrierung bleibt erhalten.
- Frontend-Cachekennung auf `1.0.1-beta.3` erhöht.

## Test
Zuerst ohne Prefix testen:

```yaml
type: custom:xparkle-rv-level-card
```

Bei Bedarf bleibt die manuelle Variante möglich:

```yaml
type: custom:xparkle-rv-level-card
entity_prefix: sensor.rvlevel_410f
```
