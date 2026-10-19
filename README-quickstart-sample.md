# Los Pollos Hermanos — Website Handoff & Quickstart

**SAMPLE — fictional client (Los Pollos Hermanos), illustrative only.**

Welcome! Your new website is finished and ready to go. This guide tells you exactly what's in the package, how to put it online, and how to update the two things you'll change most often — **menu items** and **locations** — without needing a developer.

Nothing here requires coding skills. If you can edit a Word document, you can do everything in this guide.

---

## What was delivered

**4 pages:**

| Page | File | What it does |
|---|---|---|
| Home | `index.html` | First impression — tagline, what makes you special, menu teaser, locations teaser, catering button |
| Menu | `menu.html` | Full menu: Chicken, Sides, Drinks & Desserts, plus the allergen note |
| Locations | `locations.html` | The three restaurants (Albuquerque, Santa Fe, El Paso) + the "coming soon: Tucson" announcement |
| Contact | `contact.html` | Catering quote form and the franchise inquiry block |

**Plus the theme package** — one file (`theme.css`) that holds every color, font, and spacing choice for the whole site. Change a color there, and it changes everywhere automatically.

---

## Quickstart: how to view and publish the files

You received a zip file containing the 4 pages, the `theme.css` file, and this README.

1. **To preview it:** unzip the folder, then double-click `index.html`. It opens in your browser like any webpage. The other pages link to each other — click around and make sure everything looks right.
2. **To publish it:** give the folder to your web host (or the person who manages your domain) and ask them to upload it. The pages work as-is — no special software needed. Once uploaded, your site is live at your domain.

> Tip: view `index.html` on your phone too. Most of your visitors arrive on mobile, and the site is built to look good there.

---

## How to update MENU ITEMS

Menu items live in **one clearly marked spot** in the `menu.html` file. You'll never have to hunt for them.

**Step by step:**

1. Open the `menu.html` file in a plain text editor. On Windows, use **Notepad**. On Mac, use **TextEdit** (switch it to plain-text mode first: Format → Make Plain Text).
2. Scroll until you see this marker — it looks exactly like this:

   ```
   <!-- ✏️ EDIT MENU ITEMS BELOW THIS LINE — safe to change -->
   ```

   Everything between that marker and the matching "STOP" marker below it is yours to edit.
3. Each menu item looks like this:

   ```
   <div class="menu-item">
     <span class="name">Curly Fries</span>
     <span class="price">$3.99</span>
   </div>
   ```

4. To change a price: replace the number inside the `price` line (keep the dollar sign). Example: change `$3.99` to `$4.49`.
5. To add a new item: copy a whole `menu-item` block, paste it right below the original, and change the name and price.
6. To remove an item: delete its whole `menu-item` block (from `<div class="menu-item">` through `</div>`).
7. Save the file, then double-click it again to check your change looks right. Re-upload the single file to your host.

Do **not** touch anything above or below the markers — that's the page's structure, and it doesn't need you.

---

## How to update LOCATIONS

Locations work the same way, in `locations.html`. Scroll to this marker:

```
<!-- ✏️ EDIT LOCATIONS BELOW THIS LINE — safe to change -->
```

Each location looks like this:

```
<div class="location-card">
  <h3>Albuquerque NM — Flagship</h3>
  <p>Central Ave</p>
  <p>Mon–Sun 10am–10pm</p>
  <p>(555) 123-4567</p>
</div>
```

- **To change hours or the phone number:** edit the text, leave the surrounding lines alone.
- **To add a new location:** copy a whole `location-card` block, paste it below, and fill in the new details.
- **To remove one:** delete the whole block.
- **The "coming soon" note** (currently Tucson AZ) is its own marked line — edit the city name the same way.

Save, preview, re-upload the one file. Done.

---

## How to change colors

All colors live in one file: **`theme.css`**. You don't need to open any other file to change how the site looks.

Near the top you'll see a marked section like this:

```
/* ✏️ EDIT COLORS BELOW THIS LINE — safe to change */
--lph-red: #B3122E;
--lph-yellow: #FFC72C;
--lph-cream: #FFF6E5;
--lph-brown: #4A2C1A;
```

**Step by step:**

1. Open `theme.css` in Notepad or TextEdit (plain text).
2. Find the color you want to change — each one has a plain-English label next to it, e.g. `--lph-red` is the main brand red used for headers and buttons.
3. Replace the code after it (the part starting with `#`, e.g. `#B3122E`) with your new color code. Keep the `#` and the semicolon at the end.
4. Save. Every page that uses that color updates automatically — no other files to touch.

> Don't know a color's code? Any free "color picker" site lets you pick a shade and copy its `#` code.

---

## What NOT to touch

Everything **outside** the marked edit regions is the site's machinery. Changing it can break how pages look or work. Specifically, leave alone:

- Any line that doesn't sit between the ✏️ edit markers.
- The SAMPLE banner ribbon code (the thin banner at the top of every page). This is part of the demo package and is removed on the live build.
- The header, footer, and form code.
- File names — renaming a page file breaks the links between pages.

**Golden rule:** if it's between the ✏️ markers, it's yours. If it's not, hands off.

---

## FAQ

**Q: I updated the menu, but the website still shows the old one. What happened?**
A: You updated the file on your computer — now upload the updated file to your web host. The live site only changes when the new file is uploaded. (If it still looks old after uploading, hard-refresh your browser: Ctrl+Shift+R on Windows, Cmd+Shift+R on Mac.)

**Q: Can I add a photo of a new dish?**
A: This design uses illustrations instead of photos, so there's no photo slot to fill — the site is built to look complete without them. If you'd like real photography added later, that's a separate design change.

**Q: Can I add a 5th page (like "Our Story") or online ordering?**
A: The build covers the 4 pages agreed in the spec. Online ordering was explicitly out of scope (no payments, no accounts). Additional pages or features are new work — see "Support terms" below.

**Q: I broke something and the page looks wrong. Help?**
A: Don't panic. Re-download your original files (or unzip your original zip again) and re-upload the broken page — you're back to where you started. Then make your edit again, more carefully, staying between the markers.

---

## Support terms

**What's included after handoff (at no extra charge):**
- Fixing anything that doesn't work the way this README or the spec describes (bugs are on us).
- One walkthrough call or email thread to get you comfortable updating menus and locations.
- Keeping your files archived, so a lost file can be re-sent.

**What isn't included:**
- New pages, new features, design changes, or new functionality (e.g. adding online ordering) — those are quoted as separate work.
- Uploading future edits to your host for you — this README shows you how, and it's a two-minute job.
- Support ends 60 days after handoff, after which help is billed at the standard hourly rate.

Questions? Reply to your handoff email — we're happy to help.

**It's the chicken, man. 🍗**

© 2026 Keith Soyka / GestaltView · SAMPLE.
