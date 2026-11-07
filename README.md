# Ranthox OWL Widgets — Reusable Odoo Frontend Widgets (16 → 19)

![Odoo](https://img.shields.io/badge/Odoo-16-blue)![Odoo](https://img.shields.io/badge/Odoo-17-blue)![Odoo](https://img.shields.io/badge/Odoo-18-purple)![Odoo](https://img.shields.io/badge/Odoo-19-purple) ![License](https://img.shields.io/badge/License-LGPL--3-green)

A reusable **OWL JS widget library** maintained across **four Odoo framework versions** (16, 17, 18, 19) — inline **Excel editors**, **camera/photo capture** fields, and **live search bars for x2many lists**, with ready-made usage modules on sale orders.

```
ranthox-owl-widgets/
├── odoo16/                    # 16 ports
│   ├── excel_editor_widget/        # Excel upload & inline viewer widget
│   ├── photograph_capture_widget/  # Camera capture binary image field widget
│   ├── sale_order/                 # Sale Order + Excel editor field
│   ├── sale_photo_capture/         # Photo capture on sale orders
│   ├── sale_searchbar_test/        # Widget demo on Sale Order
│   └── x2many_searchbar/           # Live search above One2many/Many2many lists
├── odoo17/  … same family (ranthox_*) + sale_photo_capture
├── odoo18/  … same family (ranthox_*) + sale_photo_capture
└── odoo19/  … same family (ranthox_*) + excel_editor_widget + sale_order_excel
```

## Widgets

| Widget | What it does |
|---|---|
| **Excel Editor** (`ranthox_excel_editor` / `excel_editor_widget`) | OWL widget to upload and view Excel files inline (SheetJS-style parsing & rendering inside form views) |
| **Image Capture** (`ranthox_image_capture` / `photograph_capture_widget`) | Reusable camera/photograph capture OWL field widget for binary image fields (webcam, capture, retake) |
| **X2Many Search Bar** (`ranthox_x2many_search` / `x2many_searchbar`) | Adds a live search bar above any One2many or Many2many list in form views |

## Usage modules

- **Sale Order Excel Editor** — adds an Excel field to `sale.order` wired to the inline editor widget.
- **Sale Order Photo Capture** — capture a photograph directly on sale orders.

## Why version folders?

The same widget family is re-ported per Odoo major version because the OWL framework & asset registries change with each release. Each folder is a self-contained, installable module set for that Odoo version.

## License

LGPL-3 (as declared in module manifests).
