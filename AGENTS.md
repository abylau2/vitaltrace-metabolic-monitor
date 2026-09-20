# Frontend rules

For every frontend task:

1. Read DESIGN.md before modifying UI.
2. Use ./tabler as the primary implementation and visual reference.
3. Use the installed frontend-design and anti-ai-slop-ui skills when relevant.
4. Existing application data and functionality must be preserved.
5. Existing visual styling is NOT authoritative and may be replaced.

Do not invent a new generic dashboard design when an equivalent Tabler
pattern already exists.

Before creating a component, inspect ./tabler for an existing pattern.

Do not create generic components such as:
- MetricCard
- StatCard
- DashboardCard
- InfoCard
- AlertCard

unless the content genuinely represents an independent card object.

Avoid:
- excessive cards
- large empty areas
- oversized metric numbers
- generic SaaS layouts
- decorative gradients
- excessive pills
- excessive border radius
- arbitrary sidebars
- healthcare-equals-green styling

This is desktop work software, not a landing page.

For significant UI changes:
1. inspect existing implementation;
2. inspect relevant Tabler examples;
3. implement;
4. run the application;
5. inspect the rendered result;
6. critique it visually;
7. iterate before finishing.

Do not judge frontend quality only from source code.