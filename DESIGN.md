# VitalTrace Design Direction

VitalTrace is a desktop patient monitoring application.

## Primary UI reference

Use ./openmrs-reference as the source of truth for:

- patient header
- patient context
- clinical navigation
- vitals organization
- clinical hierarchy
- density
- status presentation

Do not copy OpenMRS branding or text.

## Monitoring reference

Use ./grafana-reference as the source of truth for:

- time-series visualization
- chart density
- axes
- thresholds
- current value highlighting
- alert hierarchy
- monitoring states

Do not copy Grafana branding.

## Existing project

The current application is the source of truth only for:

- medical data
- functionality
- content
- behavior

The existing visual design is not authoritative.

## Goal

Combine:

OpenMRS clinical structure
+
Grafana monitoring patterns
+
our existing data

Do not invent a generic SaaS dashboard.

This is desktop operational software, not a landing page.

Prefer real patterns found in the reference repositories over newly invented
cards, layouts, navigation, or status components.