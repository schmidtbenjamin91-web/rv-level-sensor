# v1.0.1

Bugfix release for fresh HACS installations.

## Fixed

- Dashboard card is automatically registered as a JavaScript module in Lovelace storage mode.
- An existing RV Level resource is updated to `?v=1.0.1` instead of being created twice.
- `add_extra_js_url()` is kept as a fallback.
- Card version display updated to 1.0.1.

## Unchanged

- Sensor and calculation logic
- Vehicle and wedge data
- Canada AD 2019 dedicated graphics
- Shared graphics set for all other vehicles
- Existing entity IDs / domain `xparkle_rvlevel`

Note: with Lovelace in YAML resource mode, Home Assistant cannot manage resources through the storage collection; manual resource configuration remains necessary there.
