# v1.0.1

Bugfix-Release für frische HACS-Installationen.

## Behoben

- Dashboard-Karte wird in Lovelace Storage Mode automatisch als JavaScript-Modul registriert.
- Vorhandene RV-Level-Ressource wird auf `?v=1.0.1` aktualisiert statt doppelt angelegt.
- `add_extra_js_url()` bleibt als Fallback erhalten.
- Versionsanzeige der Karte auf 1.0.1 aktualisiert.

## Unverändert

- Sensor- und Berechnungslogik
- Fahrzeug- und Keildaten
- Canada AD 2019 Sondergrafiken
- gemeinsamer Grafiksatz der übrigen Fahrzeuge
- bestehende Entity-IDs / Domain `xparkle_rvlevel`

Hinweis: Bei Lovelace im YAML-Ressourcenmodus kann Home Assistant Ressourcen nicht über die Storage-Sammlung verwalten; dort bleibt eine manuelle Ressourcen-Konfiguration erforderlich.
