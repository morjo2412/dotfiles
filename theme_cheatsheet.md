# Design BlueInk
Monochromatic tonal environment optimized for Iosevka. Focuses syntax hierarchy on font anatomy instead of color shifts.

## 1. Color Palette (Tonal Grid)

All tokens derive from the base ink `#022164`.

| Semantic Token | Hexadecimal | Primary Purpose |
| :--- | :--- | :--- |
| `paper` | `#E6DED5` | General interface background. Minimizes blue light emission. |
| `paper_shadow` | `#D4C9BC` | Text selection blocks, inactive borders, and UI dividers. |
| `ink_base` | `#022164` | Standard text, identifiers, operators, and variables. |
| `ink_heavy` | `#010B22` | Critical errors (`stderr`), panics, and return controls. Maximum visual density. |
| `ink_washed` | `#516491` | String literals and raw data tokens. Backgrounded readability. |
| `ink_very_washed`| `#6C7AA0` | Code comments, line numbers, and secondary UI elements. |
| `ink_mid` | `#1C3773` | Compiler warnings, complex types, and intermediate states. |

## 2. Typographic Modifiers (Iosevka Hierarchy)

* **Regular (`[]`):** Standard flow. Variables, parameters, and primitive types.
* **Bold (`["bold"]`):** Structural anchors. Language keywords (`fn`, `struct`, `if`), function names, and macros.
* **Italic (`["italic"]`):** Context abstraction. Strings and inline documentation/comments.
* **Bold Italic (`["bold", "italic"]`):** Flow disruptions. Panic macros, explicit control returns, and developer tags (`TODO:`, `FIXME:`).
* **Underlined (`["underlined"]`):** System paths, URLs, and syntax warning spans.

## 3. Terminal Integration (ANSI Map)

Kitty redirects standard 16-color ANSI output into the `blueink` spectrum to force legacy CLI tool compliance:

* **Red Channel (ANSI 1/9) ➔** `ink_heavy` (`#010B22`)
* **Green Channel (ANSI 2/10) ➔** `ink_washed` (`#516491`)
* **Yellow Channel (ANSI 3/11) ➔** `ink_mid` (`#1C3773`)
* **Blue Channel (ANSI 4/12) ➔** `ink_base` (`#022164`)
* **White Channel (ANSI 7/15) ➔** `paper` (`#E6DED5`)
