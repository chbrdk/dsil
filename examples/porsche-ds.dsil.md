# DSIL Manifest: Porsche Design System v3 (Refined)

> **Version**: 1.1.0  
> **Basiert auf**: PDS v3.x (https://designsystem.porsche.com/v3/)  
> **Änderungen**: Event-Payloads explizit, Icon-Liste, CSS Custom Properties, Beispiele

---

## Verbesserungen gegenüber v1.0

| Bereich | v1.0 | v1.1 (Refined) |
|---------|------|----------------|
| Events | Nur Namen | Vollständige Payload-Struktur |
| Icons | `@type(IconName)` | Konkrete Icon-Liste |
| Styling | Fehlend | CSS Custom Properties |
| Beispiele | Wenige | Code-Beispiele pro Komponente |
| Constraints | Abstrakt | Mit konkreten Fehlermeldungen |

---

## Full Format (Refined)

```dsil
# ============================================================================
# PORSCHE DESIGN SYSTEM v3 – DSIL Manifest (Refined)
# Version: 1.1.0
# ============================================================================

@meta {
  name: "porsche-design-system"
  version: "3.x"
  dsil-version: "1.1.0"
  prefix: {
    html: "p-"          # <p-button>
    react: "P"          # <PButton>
    angular: "p-"       # <p-button>
    vue: "P"            # <PButton>
  }
  
  config: {
    strict: true
    allowCustom: false
    controlled: true    # Die meisten Komponenten sind controlled
  }
  
  imports: {
    react: "@porsche-design-system/components-react"
    angular: "@porsche-design-system/components-angular"
    vue: "@porsche-design-system/components-vue"
    vanilla: "@porsche-design-system/components-js"
    styles: "@porsche-design-system/components-{framework}/styles"
  }
}

# ----------------------------------------------------------------------------
# TOKENS (Refined with CSS Custom Properties)
# ----------------------------------------------------------------------------

@tokens {
  
  # === THEME ===
  theme: {
    values: [light, dark, auto]
    default: "light"
    css: "--p-theme"
  }
  
  # === SPACING ===
  spacing: {
    @group static {
      @doc "Feste Pixel-Werte, nicht responsive"
      xs: { value: "4px", css: "$pds-spacing-static-xs" }
      sm: { value: "8px", css: "$pds-spacing-static-sm" }
      md: { value: "16px", css: "$pds-spacing-static-md" }
      lg: { value: "24px", css: "$pds-spacing-static-lg" }
      xl: { value: "32px", css: "$pds-spacing-static-xl" }
      2xl: { value: "48px", css: "$pds-spacing-static-2xl" }
    }
    
    @group fluid {
      @doc "Responsive Werte, skalieren mit Viewport"
      xs: { css: "$pds-spacing-fluid-xs", tailwind: "p-fluid-xs" }
      sm: { css: "$pds-spacing-fluid-sm", tailwind: "p-fluid-sm" }
      md: { css: "$pds-spacing-fluid-md", tailwind: "p-fluid-md" }
      lg: { css: "$pds-spacing-fluid-lg", tailwind: "p-fluid-lg" }
      xl: { css: "$pds-spacing-fluid-xl", tailwind: "p-fluid-xl" }
    }
  }
  
  # === COLORS ===
  color: {
    @group theme-light {
      primary: { value: "#010205", css: "$pds-theme-light-primary" }
      background-base: { value: "#F2F2F2", css: "$pds-theme-light-background-base" }
      background-surface: { value: "#FFFFFF", css: "$pds-theme-light-background-surface" }
      contrast-low: { value: "#96989A", css: "$pds-theme-light-contrast-low" }
      contrast-medium: { value: "#626669", css: "$pds-theme-light-contrast-medium" }
      contrast-high: { value: "#323639", css: "$pds-theme-light-contrast-high" }
    }
    
    @group theme-dark {
      primary: { value: "#FBFCFC", css: "$pds-theme-dark-primary" }
      background-base: { value: "#0E0E12", css: "$pds-theme-dark-background-base" }
      background-surface: { value: "#1A1B1E", css: "$pds-theme-dark-background-surface" }
      contrast-low: { value: "#7C7F82", css: "$pds-theme-dark-contrast-low" }
      contrast-medium: { value: "#B0B2B4", css: "$pds-theme-dark-contrast-medium" }
      contrast-high: { value: "#E4E5E6", css: "$pds-theme-dark-contrast-high" }
    }
    
    @group notification {
      success: { value: "#018A16", css: "$pds-theme-light-notification-success" }
      warning: { value: "#FF9B00", css: "$pds-theme-light-notification-warning" }
      error: { value: "#E00000", css: "$pds-theme-light-notification-error" }
      info: { value: "#2762D9", css: "$pds-theme-light-notification-info" }
    }
  }
  
  # === TYPOGRAPHY ===
  typography: {
    family: {
      default: { 
        value: '"Porsche Next", Arial, Helvetica, sans-serif'
        css: "$pds-font-family"
      }
    }
    
    @group display {
      @doc "Für Hero-Bereiche, Stats, emotionale Momente"
      large: { css: "@include pds-display-large", tailwind: "prose-display-lg" }
      medium: { css: "@include pds-display-medium", tailwind: "prose-display-md" }
      small: { css: "@include pds-display-small", tailwind: "prose-display-sm" }
    }
    
    @group heading {
      @doc "Für Überschriften und Abschnitte"
      xx-large: { css: "@include pds-heading-xx-large", tailwind: "prose-heading-2xl" }
      x-large: { css: "@include pds-heading-x-large", tailwind: "prose-heading-xl" }
      large: { css: "@include pds-heading-large", tailwind: "prose-heading-lg" }
      medium: { css: "@include pds-heading-medium", tailwind: "prose-heading-md" }
      small: { css: "@include pds-heading-small", tailwind: "prose-heading-sm" }
    }
    
    @group text {
      @doc "Für Fließtext"
      x-large: { css: "@include pds-text-x-large", tailwind: "prose-text-xl" }
      large: { css: "@include pds-text-large", tailwind: "prose-text-lg" }
      medium: { css: "@include pds-text-medium", tailwind: "prose-text-md" }
      small: { css: "@include pds-text-small", tailwind: "prose-text-sm", default: true }
      x-small: { css: "@include pds-text-x-small", tailwind: "prose-text-xs" }
      xx-small: { css: "@include pds-text-xx-small", tailwind: "prose-text-2xs", usage: "Nur für Disclaimers" }
    }
    
    weight: {
      regular: { value: 400, css: "$pds-font-weight-regular" }
      semi-bold: { value: 600, css: "$pds-font-weight-semi-bold" }
      bold: { value: 700, css: "$pds-font-weight-bold" }
    }
  }
  
  # === BORDERS ===
  border: {
    radius: {
      small: { value: "4px", css: "$pds-border-radius-small", tailwind: "rounded-sm" }
      medium: { value: "8px", css: "$pds-border-radius-medium", tailwind: "rounded-md" }
      large: { value: "16px", css: "$pds-border-radius-large", tailwind: "rounded-lg" }
    }
    width: {
      thin: { value: "1px", tailwind: "border-thin" }
      regular: { value: "2px", tailwind: "border-regular" }
    }
  }
  
  # === SHADOWS ===
  shadow: {
    low: { css: "$pds-drop-shadow-low", tailwind: "shadow-low" }
    medium: { css: "$pds-drop-shadow-medium", tailwind: "shadow-md" }
    high: { css: "$pds-drop-shadow-high", tailwind: "shadow-high" }
  }
  
  # === BREAKPOINTS ===
  breakpoint: {
    base: { value: "0px", @doc "Mobile first" }
    xs: { value: "480px" }
    s: { value: "760px", @doc "Tablet" }
    m: { value: "1000px", @doc "Desktop" }
    l: { value: "1300px" }
    xl: { value: "1760px" }
    xxl: { value: "1920px" }
  }
  
  # === GRID ===
  grid: {
    columns: {
      mobile: 6
      desktop: 12
    }
    areas: {
      full: "Volle Breite inkl. Safe-Zone"
      wide: "16 Spalten"
      extended: "14 Spalten"
      basic: "12 Spalten (Standard)"
      narrow: "8 Spalten"
    }
    gap: { css: "$pds-grid-gap" }
  }
  
  # === MOTION ===
  motion: {
    duration: {
      short: { value: "0.25s", css: "$pds-motion-duration-short" }
      moderate: { value: "0.4s", css: "$pds-motion-duration-moderate" }
      long: { value: "0.6s", css: "$pds-motion-duration-long" }
    }
    easing: {
      base: { value: "cubic-bezier(0.25, 0.1, 0.25, 1)", css: "$pds-motion-easing-base" }
    }
  }
}

# ----------------------------------------------------------------------------
# ICONS (Vollständige Liste)
# ----------------------------------------------------------------------------

@icons {
  @doc "Alle verfügbaren Icons im PDS"
  
  @group navigation {
    arrow-head-up, arrow-head-down, arrow-head-left, arrow-head-right
    arrow-up, arrow-down, arrow-left, arrow-right
    arrow-first, arrow-last
    arrow-double-up, arrow-double-down, arrow-double-left, arrow-double-right
    external, return, logout
  }
  
  @group action {
    add, plus, minus, subtract
    close, check, edit, delete
    search, filter, sort, refresh
    download, upload, copy, paste, cut
    save, print, share
    increase, reset
  }
  
  @group media {
    play, pause, stop
    fast-forward, fast-backward
    skip-forward, skip-backward
    replay
    volume-up, volume-off
    camera, video, image, microphone
  }
  
  @group communication {
    email, phone, chat, send
    bell, broadcast
    new-chat
  }
  
  @group status {
    information, information-filled
    success, success-filled
    warning, warning-filled
    error, error-filled
    question, question-filled
    exclamation, exclamation-filled
  }
  
  @group user {
    user, user-filled, user-group
    heart, heart-filled
    star, star-filled
    bookmark, bookmark-filled
    like, like-filled
    dislike, dislike-filled
  }
  
  @group device {
    mobile, tablet, laptop, screen
  }
  
  @group misc {
    home, globe, map, pin, pin-filled
    calendar, clock, duration, stopwatch
    lock, lock-open, key
    view, view-off
    configurate, grip, menu-lines, menu-dots-horizontal, menu-dots-vertical
    shopping-cart, shopping-cart-filled, shopping-bag, shopping-bag-filled
    document, news, work
    car, garage, charging-station
  }
  
  @group social {
    logo-facebook, logo-instagram, logo-linkedin, logo-x, logo-twitter
    logo-youtube, logo-tiktok, logo-whatsapp, logo-telegram
    logo-pinterest, logo-reddit, logo-snapchat
    logo-apple-podcast, logo-spotify
  }
  
  special: none  # Zeigt kein Icon an
}

# ----------------------------------------------------------------------------
# TYPES (Wiederverwendbare Typen)
# ----------------------------------------------------------------------------

@type BreakpointCustomizable<T> {
  @doc "Erlaubt responsive Werte pro Breakpoint"
  
  format: |
    // Einfacher Wert
    prop="value"
    
    // Responsive Object (als JSON-String in HTML, Object in JS)
    prop="{'base': 'value', 's': 'otherValue', 'l': 'anotherValue'}"
  
  example-html: |
    <p-button compact="{'base': true, 's': false}">Label</p-button>
  
  example-react: |
    <PButton compact={{ base: true, s: false }}>Label</PButton>
}

@type AriaAttribute {
  'aria-label'?: string
  'aria-labelledby'?: string
  'aria-describedby'?: string
  'aria-expanded'?: boolean
  'aria-pressed'?: boolean
  'aria-haspopup'?: boolean
  'aria-controls'?: string
  'aria-live'?: 'polite' | 'assertive' | 'off'
  'aria-busy'?: boolean
}

@type FormState {
  values: [none, success, error]
  default: none
  styling: {
    none: "Standard-Styling"
    success: "Grüner Rand, Success-Icon möglich"
    error: "Roter Rand, Error-Message wird angezeigt"
  }
}

# ----------------------------------------------------------------------------
# COMPONENTS (Refined with Examples)
# ----------------------------------------------------------------------------

# === BUTTON ===
@component p-button {
  @doc "Interaktives Element für Benutzeraktionen"
  @controlled false
  @tag-react PButton
  
  variants: {
    variant: {
      primary: {
        @doc "Haupt-CTA, gefüllter Hintergrund"
        @usage "Maximal 1x pro sichtbarem Bereich"
      }
      secondary: {
        @doc "Sekundäre Aktion, umrandet"
        @usage "Für wichtige aber nicht primäre Aktionen"
      }
      ghost: {
        @doc "Minimale Darstellung, nur Text"
        @usage "Für tertiäre Aktionen, Abbrechen, etc."
      }
      tertiary: {
        @deprecated "Verwende 'ghost' stattdessen"
      }
    }
  }
  
  props: {
    variant: {
      type: ButtonVariant
      default: "primary"
    }
    compact: {
      type: boolean | BreakpointCustomizable<boolean>
      default: false
      @doc "Kompaktere Darstellung"
    }
    disabled: {
      type: boolean
      default: false
      @doc "Deaktiviert den Button. Keine Events werden ausgelöst."
    }
    loading: {
      type: boolean
      default: false
      @doc "Zeigt Lade-Indikator. Impliziert disabled."
    }
    hideLabel: {
      type: boolean | BreakpointCustomizable<boolean>
      default: false
      @doc "Versteckt das Label. Nicht empfohlen für Barrierefreiheit."
    }
    icon: {
      type: IconName
      default: "none"
      @doc "Icon das angezeigt wird. 'none' = kein Icon."
    }
    iconSource: {
      type: string
      @doc "URL zu einem benutzerdefinierten SVG-Icon"
    }
    type: {
      type: "button" | "submit" | "reset"
      default: "submit"
      @doc "HTML button type"
    }
    name: {
      type: string
      @doc "Name für Formular-Submission"
    }
    value: {
      type: string
      @doc "Value für Formular-Submission"
    }
    form: {
      type: string
      @doc "ID des zugehörigen Formular-Elements"
    }
    theme: {
      type: Theme
      default: "light"
    }
    aria: {
      type: AriaAttribute
      @doc "ARIA-Attribute als Objekt"
    }
  }
  
  slots: {
    default: {
      required: true
      type: text
      @doc "Button-Label"
    }
  }
  
  events: {
    click: {
      native: true
      @doc "Standard DOM click event"
    }
    focus: { native: true }
    blur: { native: true }
  }
  
  constraints: {
    @rule "loading:true → disabled implizit" {
      error: "Button mit loading=true verhält sich wie disabled"
      auto-fix: true
    }
    @rule "hideLabel:true && icon:'none' → ungültig" {
      error: "Button braucht entweder sichtbares Label oder Icon"
    }
    @rule "nur Icon (hideLabel:true) → aria-label erforderlich" {
      error: "Icon-only Button benötigt aria-label für Screenreader"
    }
  }
  
  a11y: {
    role: "button"
    @rule "disabled → aria-disabled:true (nicht disabled-Attribut)"
    @rule "loading → aria-busy:true"
    @rule "focus-visible für Keyboard-Navigation"
  }
  
  examples: {
    basic: |
      // React
      <PButton>Speichern</PButton>
      
      // HTML
      <p-button>Speichern</p-button>
    
    variants: |
      <PButton variant="primary">Primär</PButton>
      <PButton variant="secondary">Sekundär</PButton>
      <PButton variant="ghost">Ghost</PButton>
    
    with-icon: |
      <PButton icon="arrow-right">Weiter</PButton>
      <PButton icon="download" hideLabel aria={{ 'aria-label': 'Herunterladen' }} />
    
    loading: |
      <PButton loading>Wird gespeichert...</PButton>
    
    responsive: |
      <PButton compact={{ base: true, m: false }}>
        Responsive Button
      </PButton>
  }
}

# === BUTTON GROUP ===
@component p-button-group {
  @doc "Container für gruppierte Buttons"
  @controlled false
  @tag-react PButtonGroup
  
  props: {
    direction: {
      type: "column" | "row" | BreakpointCustomizable
      default: "row"
      @doc "Ausrichtung der Buttons"
    }
  }
  
  slots: {
    default: {
      required: true
      allows: [p-button, p-button-pure, p-link, p-link-pure]
      @doc "Button-Elemente"
    }
  }
  
  constraints: {
    @rule "max 1 primary Button"
    @rule "primary Button → Position am Ende (rechts/unten)"
    @rule "Empfohlen: max 3 Buttons"
  }
  
  examples: {
    standard: |
      <PButtonGroup>
        <PButton variant="ghost">Abbrechen</PButton>
        <PButton variant="primary">Speichern</PButton>
      </PButtonGroup>
    
    responsive: |
      <PButtonGroup direction={{ base: 'column', s: 'row' }}>
        <PButton variant="secondary">Zurück</PButton>
        <PButton variant="primary">Weiter</PButton>
      </PButtonGroup>
  }
}

# === ACCORDION ===
@component p-accordion {
  @doc "Aufklappbarer Content-Bereich. CONTROLLED COMPONENT."
  @controlled true
  @tag-react PAccordion
  
  props: {
    heading: {
      type: string
      required: true
      @doc "Überschrift des Accordion-Headers"
    }
    headingTag: {
      type: "h1" | "h2" | "h3" | "h4" | "h5" | "h6"
      default: "h2"
      @doc "Semantisches Heading-Level"
    }
    tag: {
      @deprecated "Verwende headingTag stattdessen"
    }
    size: {
      type: "small" | "medium"
      default: "small"
    }
    open: {
      type: boolean
      default: false
      @doc "CONTROLLED: Geöffnet-Status. Muss via State verwaltet werden."
    }
    compact: {
      type: boolean
      default: false
    }
    theme: {
      type: Theme
      default: "light"
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "Inhalt des Accordion-Panels"
    }
  }
  
  events: {
    update: {
      payload: {
        open: boolean   # Der neue gewünschte Status
      }
      @doc "Wird ausgelöst wenn User auf Header klickt"
      handling: |
        // Der Event gibt den GEWÜNSCHTEN neuen Status zurück.
        // Du MUSST den State updaten, sonst passiert nichts!
        
        // React:
        const [isOpen, setIsOpen] = useState(false);
        <PAccordion 
          open={isOpen} 
          onUpdate={(e) => setIsOpen(e.detail.open)}
        />
        
        // Vanilla JS:
        accordion.addEventListener('update', (e) => {
          e.target.open = e.detail.open;
        });
    }
  }
  
  constraints: {
    @rule "MUSS update-Event handlen" {
      error: "Accordion öffnet/schließt nicht ohne Event-Handler"
      critical: true
    }
    @rule "open prop MUSS mit State synchronisiert sein"
  }
  
  a11y: {
    @rule "Header → button role mit aria-expanded"
    @rule "Panel → region role mit aria-labelledby"
    @rule "Keyboard: Enter/Space zum Öffnen/Schließen"
  }
  
  examples: {
    basic-react: |
      const [isOpen, setIsOpen] = useState(false);
      
      <PAccordion
        heading="FAQ Frage"
        open={isOpen}
        onUpdate={(e) => setIsOpen(e.detail.open)}
      >
        <PText>Hier steht die Antwort.</PText>
      </PAccordion>
    
    multiple-independent: |
      // Jedes Accordion hat eigenen State
      const [openStates, setOpenStates] = useState({
        faq1: false,
        faq2: false,
        faq3: true, // Standardmäßig offen
      });
      
      <PAccordion
        heading="Frage 1"
        open={openStates.faq1}
        onUpdate={(e) => setOpenStates(s => ({ ...s, faq1: e.detail.open }))}
      >
        Antwort 1
      </PAccordion>
      
      <PAccordion
        heading="Frage 2"
        open={openStates.faq2}
        onUpdate={(e) => setOpenStates(s => ({ ...s, faq2: e.detail.open }))}
      >
        Antwort 2
      </PAccordion>
    
    exclusive-mode: |
      // Nur ein Accordion gleichzeitig offen
      const [openId, setOpenId] = useState(null);
      
      {faqs.map((faq) => (
        <PAccordion
          key={faq.id}
          heading={faq.question}
          open={openId === faq.id}
          onUpdate={(e) => setOpenId(e.detail.open ? faq.id : null)}
        >
          {faq.answer}
        </PAccordion>
      ))}
  }
}

# === MODAL ===
@component p-modal {
  @doc "Overlay-Dialog für fokussierte Interaktionen. CONTROLLED COMPONENT."
  @controlled true
  @tag-react PModal
  
  props: {
    open: {
      type: boolean
      required: true
      @doc "CONTROLLED: Sichtbarkeits-Status"
    }
    heading: {
      type: string
      @doc "Modal-Titel"
    }
    dismissButton: {
      type: boolean
      default: true
      @doc "Zeigt X-Button zum Schließen"
    }
    disableCloseButton: {
      type: boolean
      default: false
      @doc "Verhindert Schließen via X-Button"
    }
    disableBackdropClick: {
      type: boolean
      default: false
      @doc "Verhindert Schließen durch Klick auf Overlay"
    }
    fullscreen: {
      type: boolean | BreakpointCustomizable<boolean>
      default: false
      @doc "Vollbild-Modus (empfohlen nur für Mobile)"
    }
    theme: {
      type: Theme
      default: "light"
    }
    aria: {
      type: AriaAttribute
    }
  }
  
  slots: {
    header: {
      type: node
      @doc "Benutzerdefinierter Header-Inhalt"
    }
    default: {
      required: true
      type: node
      @doc "Modal-Body"
    }
    footer: {
      type: node
      @doc "Aktions-Bereich (Buttons)"
    }
  }
  
  events: {
    dismiss: {
      payload: {}
      @doc "Wird ausgelöst wenn Schließen angefordert wird (X, ESC, Backdrop)"
      handling: |
        // Du MUSST open auf false setzen!
        
        // React:
        const [isOpen, setIsOpen] = useState(false);
        <PModal 
          open={isOpen} 
          onDismiss={() => setIsOpen(false)}
        />
    }
  }
  
  constraints: {
    @rule "MUSS dismiss-Event handlen" {
      error: "Modal schließt nicht ohne Event-Handler"
      critical: true
    }
    @rule "Braucht immer einen Schließ-Mechanismus"
    @rule "disableBackdropClick && !dismissButton → ESC muss funktionieren"
    @rule "fullscreen → nur für Mobile empfohlen"
  }
  
  a11y: {
    role: "dialog"
    aria-modal: true
    @rule "Focus-Trap innerhalb des Modals"
    @rule "Focus zurück auf Trigger bei Schließen"
    @rule "ESC schließt (wenn nicht deaktiviert)"
    @rule "aria-labelledby → heading"
  }
  
  examples: {
    info-dialog: |
      const [isOpen, setIsOpen] = useState(false);
      
      <PButton onClick={() => setIsOpen(true)}>Info anzeigen</PButton>
      
      <PModal
        open={isOpen}
        heading="Information"
        onDismiss={() => setIsOpen(false)}
      >
        <PText>Wichtige Information für den Benutzer.</PText>
        
        <template slot="footer">
          <PButton variant="primary" onClick={() => setIsOpen(false)}>
            Verstanden
          </PButton>
        </template>
      </PModal>
    
    confirmation-dialog: |
      const [isOpen, setIsOpen] = useState(false);
      const [isDeleting, setIsDeleting] = useState(false);
      
      const handleDelete = async () => {
        setIsDeleting(true);
        await deleteItem();
        setIsDeleting(false);
        setIsOpen(false);
      };
      
      <PModal
        open={isOpen}
        heading="Löschen bestätigen"
        onDismiss={() => !isDeleting && setIsOpen(false)}
      >
        <PInlineNotification
          state="warning"
          heading="Achtung"
          description="Diese Aktion kann nicht rückgängig gemacht werden."
        />
        
        <template slot="footer">
          <PButtonGroup>
            <PButton 
              variant="ghost" 
              onClick={() => setIsOpen(false)}
              disabled={isDeleting}
            >
              Abbrechen
            </PButton>
            <PButton 
              variant="primary"
              loading={isDeleting}
              onClick={handleDelete}
              style={{ background: 'var(--p-color-notification-error)' }}
            >
              Endgültig löschen
            </PButton>
          </PButtonGroup>
        </template>
      </PModal>
  }
}

# === INPUT TEXT ===
@component p-input-text {
  @doc "Einzeiliges Texteingabefeld mit Label und Validierung"
  @controlled false
  @tag-react PInputText
  
  props: {
    label: {
      type: string
      required: true
      @doc "Beschriftung des Eingabefelds"
    }
    name: {
      type: string
      @doc "Name für Formular-Submission"
    }
    value: {
      type: string
      @doc "Aktueller Wert"
    }
    placeholder: {
      type: string
      @doc "Platzhalter-Text"
    }
    description: {
      type: string
      @doc "Hilfetext unter dem Label"
    }
    message: {
      type: string
      @doc "Feedback-Nachricht (für Fehler/Erfolg)"
    }
    state: {
      type: FormState
      default: "none"
      @doc "Validierungs-Status"
    }
    disabled: {
      type: boolean
      default: false
    }
    readOnly: {
      type: boolean
      default: false
    }
    required: {
      type: boolean
      default: false
      @doc "Markiert Feld als Pflichtfeld (zeigt * im Label)"
    }
    maxLength: {
      type: number
      @doc "Maximale Zeichenanzahl"
    }
    minLength: {
      type: number
    }
    showCounter: {
      type: boolean
      default: false
      @doc "Zeigt Zeichen-Zähler bei maxLength"
    }
    hideLabel: {
      type: boolean
      default: false
      @doc "Versteckt Label visuell (bleibt für Screenreader)"
    }
    theme: {
      type: Theme
      default: "light"
    }
  }
  
  slots: {
    label: { type: node, @doc "Benutzerdefiniertes Label mit Links etc." }
    description: { type: node }
    message: { type: node }
  }
  
  events: {
    input: {
      native: true
      payload: { target: { value: string } }
      @doc "Bei jeder Eingabe"
    }
    change: {
      native: true
      payload: { target: { value: string } }
      @doc "Bei Blur nach Änderung"
    }
    focus: { native: true }
    blur: { native: true }
  }
  
  constraints: {
    @rule "state:'error' → message sollte Fehler erklären"
    @rule "hideLabel:true → aria-label muss gesetzt sein"
  }
  
  examples: {
    basic: |
      <PInputText
        label="Name"
        name="name"
        placeholder="Max Mustermann"
        required
      />
    
    with-validation: |
      const [email, setEmail] = useState('');
      const [error, setError] = useState('');
      
      const validate = (value) => {
        if (!value.includes('@')) {
          setError('Bitte gültige E-Mail eingeben');
          return false;
        }
        setError('');
        return true;
      };
      
      <PInputText
        label="E-Mail"
        name="email"
        value={email}
        state={error ? 'error' : 'none'}
        message={error}
        onInput={(e) => setEmail(e.target.value)}
        onBlur={() => validate(email)}
      />
    
    with-counter: |
      <PInputText
        label="Titel"
        maxLength={100}
        showCounter
      />
  }
}

# === SELECT ===
@component p-select {
  @doc "Dropdown-Auswahl. CONTROLLED COMPONENT."
  @controlled true
  @tag-react PSelect
  
  props: {
    label: {
      type: string
      required: true
    }
    name: { type: string }
    value: {
      type: string
      @doc "Aktuell ausgewählter Wert"
    }
    description: { type: string }
    message: { type: string }
    state: {
      type: FormState
      default: "none"
    }
    disabled: { type: boolean, default: false }
    required: { type: boolean, default: false }
    hideLabel: { type: boolean, default: false }
    dropdownDirection: {
      type: "auto" | "down" | "up"
      default: "auto"
    }
    filter: {
      type: boolean
      default: false
      @doc "Aktiviert Suche/Filter im Dropdown"
    }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    default: {
      required: true
      allows: [p-select-option, p-optgroup]
    }
    label: { type: node }
    description: { type: node }
    message: { type: node }
  }
  
  events: {
    update: {
      payload: {
        value: string      # Ausgewählter Wert
        name: string       # Name des Select-Elements
      }
      @doc "Wird bei Auswahl-Änderung ausgelöst"
      handling: |
        // React:
        const [selected, setSelected] = useState('');
        
        <PSelect
          value={selected}
          onUpdate={(e) => setSelected(e.detail.value)}
        >
          ...
        </PSelect>
    }
  }
  
  examples: {
    basic: |
      const [country, setCountry] = useState('de');
      
      <PSelect
        label="Land"
        name="country"
        value={country}
        onUpdate={(e) => setCountry(e.detail.value)}
      >
        <PSelectOption value="de">Deutschland</PSelectOption>
        <PSelectOption value="at">Österreich</PSelectOption>
        <PSelectOption value="ch">Schweiz</PSelectOption>
      </PSelect>
    
    with-optgroup: |
      <PSelect label="Fahrzeug" value={model} onUpdate={(e) => setModel(e.detail.value)}>
        <POptgroup label="Sportwagen">
          <PSelectOption value="911">911</PSelectOption>
          <PSelectOption value="718">718</PSelectOption>
        </POptgroup>
        <POptgroup label="SUV">
          <PSelectOption value="cayenne">Cayenne</PSelectOption>
          <PSelectOption value="macan">Macan</PSelectOption>
        </POptgroup>
      </PSelect>
    
    with-filter: |
      <PSelect label="Land" filter>
        {countries.map(c => (
          <PSelectOption key={c.code} value={c.code}>
            {c.name}
          </PSelectOption>
        ))}
      </PSelect>
  }
}

# === SWITCH ===
@component p-switch {
  @doc "Toggle-Schalter für binäre Einstellungen mit sofortiger Wirkung"
  @controlled false
  @tag-react PSwitch
  
  props: {
    label: { type: string, required: true }
    name: { type: string }
    value: { type: string }
    checked: {
      type: boolean
      default: false
      @doc "Aktiviert/Deaktiviert Status"
    }
    disabled: { type: boolean, default: false }
    loading: { type: boolean, default: false }
    alignLabel: {
      type: "start" | "end"
      default: "end"
      @doc "Label-Position relativ zum Switch"
    }
    hideLabel: { type: boolean, default: false }
    stretch: {
      type: boolean | BreakpointCustomizable<boolean>
      default: false
      @doc "Volle Breite mit Label am Start, Switch am End"
    }
    message: { type: string }
    state: { type: FormState, default: "none" }
    theme: { type: Theme, default: "light" }
  }
  
  events: {
    update: {
      payload: {
        checked: boolean   # Neuer Status
        name: string
        value: string
      }
      handling: |
        const [enabled, setEnabled] = useState(false);
        
        <PSwitch
          label="Benachrichtigungen"
          checked={enabled}
          onUpdate={(e) => setEnabled(e.detail.checked)}
        />
    }
  }
  
  a11y: {
    role: "switch"
    @rule "aria-checked reflektiert Status"
  }
  
  usage: {
    do: [
      "Für Einstellungen mit sofortiger Wirkung",
      "Für binäre On/Off-Zustände",
      "Wenn keine Formular-Submission nötig"
    ]
    dont: [
      "In Formularen die submitted werden → Checkbox verwenden",
      "Für Mehrfachauswahl",
      "Wenn Bestätigung nötig ist"
    ]
  }
  
  examples: {
    settings-panel: |
      const [settings, setSettings] = useState({
        notifications: true,
        darkMode: false,
        tracking: false,
      });
      
      <PSwitch
        label="Push-Benachrichtigungen"
        checked={settings.notifications}
        onUpdate={(e) => setSettings(s => ({ ...s, notifications: e.detail.checked }))}
        stretch
      />
      
      <PSwitch
        label="Dark Mode"
        checked={settings.darkMode}
        onUpdate={(e) => setSettings(s => ({ ...s, darkMode: e.detail.checked }))}
        stretch
      />
  }
}

# === CHECKBOX ===
@component p-checkbox {
  @doc "Einzelne Checkbox für Ja/Nein-Auswahl in Formularen"
  @controlled false
  @tag-react PCheckbox
  
  props: {
    label: { type: string, required: true }
    name: { type: string }
    value: { type: string }
    checked: { type: boolean, default: false }
    indeterminate: {
      type: boolean
      default: false
      @doc "Unbestimmter Zustand (für Parent-Checkboxen)"
    }
    disabled: { type: boolean, default: false }
    required: { type: boolean, default: false }
    message: { type: string }
    state: { type: FormState, default: "none" }
    hideLabel: { type: boolean, default: false }
    loading: { type: boolean, default: false }
    theme: { type: Theme, default: "light" }
  }
  
  events: {
    update: {
      payload: {
        checked: boolean
        name: string
        value: string
      }
    }
  }
  
  usage: {
    do: [
      "In Formularen die submitted werden",
      "Für 'Ich akzeptiere...' Bestätigungen",
      "Für Mehrfachauswahl aus wenigen Optionen"
    ]
    dont: [
      "Für sofort wirksame Einstellungen → Switch verwenden"
    ]
  }
}

# === INLINE NOTIFICATION ===
@component p-inline-notification {
  @doc "Kontextuelle Inline-Nachricht"
  @controlled false
  @tag-react PInlineNotification
  
  props: {
    heading: { type: string }
    description: { type: string }
    state: {
      type: "success" | "warning" | "error" | "info"
      default: "info"
    }
    dismissButton: {
      type: boolean
      default: false
      @doc "Zeigt Schließen-Button"
    }
    persistent: {
      type: boolean
      default: false
      @doc "Wenn true, kein Auto-Dismiss"
    }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    heading: { type: node }
    description: { type: node }
  }
  
  events: {
    dismiss: {
      payload: {}
      @doc "Bei Klick auf Schließen-Button"
    }
    action: {
      payload: { name: string }
      @doc "Bei Klick auf Action-Button (falls vorhanden)"
    }
  }
  
  examples: {
    states: |
      <PInlineNotification state="success" heading="Erfolg" description="Änderungen gespeichert." />
      <PInlineNotification state="warning" heading="Warnung" description="Ungespeicherte Änderungen." />
      <PInlineNotification state="error" heading="Fehler" description="Verbindung fehlgeschlagen." />
      <PInlineNotification state="info" description="Tipp: Drücken Sie Strg+S zum Speichern." />
    
    dismissible: |
      const [showNotification, setShowNotification] = useState(true);
      
      {showNotification && (
        <PInlineNotification
          state="success"
          heading="Erfolgreich"
          description="Ihre Änderungen wurden gespeichert."
          dismissButton
          onDismiss={() => setShowNotification(false)}
        />
      )}
  }
}

# === SPINNER ===
@component p-spinner {
  @doc "Lade-Indikator"
  @controlled false
  @tag-react PSpinner
  
  props: {
    size: {
      type: "small" | "medium" | "large" | "inherit"
      default: "small"
    }
    aria: { type: AriaAttribute }
    theme: { type: Theme, default: "light" }
  }
  
  a11y: {
    @rule "aria-label für Screenreader"
    @rule "role='status' oder aria-live='polite'"
  }
  
  examples: {
    sizes: |
      <PSpinner size="small" />
      <PSpinner size="medium" />
      <PSpinner size="large" />
    
    with-text: |
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <PSpinner size="small" />
        <PText>Wird geladen...</PText>
      </div>
  }
}

# === TEXT ===
@component p-text {
  @doc "Formatierter Textabsatz"
  @controlled false
  @tag-react PText
  
  props: {
    size: {
      type: "xx-small" | "x-small" | "small" | "medium" | "large" | "x-large" | "inherit"
      default: "small"
    }
    weight: {
      type: "regular" | "semi-bold" | "bold"
      default: "regular"
    }
    align: {
      type: "start" | "center" | "end"
      default: "start"
    }
    color: {
      type: "primary" | "contrast-low" | "contrast-medium" | "contrast-high" |
            "notification-success" | "notification-warning" | "notification-error" |
            "notification-info" | "inherit"
      default: "primary"
    }
    ellipsis: {
      type: boolean
      default: false
      @doc "Kürzt Text mit ... bei Überlauf"
    }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    default: {
      required: true
      type: node
    }
  }
  
  usage: {
    note: "Für Performance: CSS-Styles direkt verwenden wenn möglich"
    alternative: "@include pds-text-small oder prose-text-sm (Tailwind)"
  }
}

# === HEADING ===
@component p-heading {
  @doc "Formatierte Überschrift"
  @controlled false
  @tag-react PHeading
  
  props: {
    size: {
      type: "xx-large" | "x-large" | "large" | "medium" | "small"
      default: "xx-large"
    }
    tag: {
      type: "h1" | "h2" | "h3" | "h4" | "h5" | "h6"
      default: "h2"
      @doc "Semantisches HTML-Element"
    }
    align: {
      type: "start" | "center" | "end"
      default: "start"
    }
    color: {
      type: "primary" | "contrast-low" | "contrast-medium" | "contrast-high" | "inherit"
      default: "primary"
    }
    ellipsis: { type: boolean, default: false }
    theme: { type: Theme, default: "light" }
  }
  
  slots: {
    default: { required: true, type: node }
  }
  
  usage: {
    @rule "size und tag müssen nicht übereinstimmen"
    @rule "Verwende korrektes tag für Semantik, size für visuelles"
    example: |
      // Visuell große Überschrift, aber semantisch h3
      <PHeading size="x-large" tag="h3">Untertitel</PHeading>
  }
}

# ----------------------------------------------------------------------------
# PATTERNS (Refined)
# ----------------------------------------------------------------------------

@pattern form-field {
  @doc "Standardstruktur für Formularfelder"
  
  structure: |
    ┌─────────────────────────────┐
    │ Label (+ required *)        │
    │ Description (optional)      │
    │ ┌─────────────────────────┐ │
    │ │ Input / Select / ...    │ │
    │ └─────────────────────────┘ │
    │ Message (optional)          │
    └─────────────────────────────┘
  
  components: [
    label: "p-text oder slot='label'"
    field: "p-input-* | p-select | p-textarea | p-checkbox | p-radio-group"
    description: "p-text[size:x-small] oder slot='description'"
    message: "p-text[size:x-small] oder slot='message'"
  ]
  
  states: {
    none: "Standard-Darstellung"
    success: "Grüner Rahmen, ggf. Success-Icon"
    error: "Roter Rahmen, Error-Message erforderlich"
  }
  
  constraints: {
    @rule "state:'error' → message muss Fehler erklären"
    @rule "required:true → Label zeigt * Indikator"
  }
}

@pattern button-actions {
  @doc "Button-Gruppe für Formulare und Dialoge"
  
  structure: |
    Mobile (base):
    ┌─────────────────────┐
    │ [  Primary Button  ]│  ← Primary zuerst (volle Breite)
    │ [Secondary / Ghost ]│
    └─────────────────────┘
    
    Desktop (s+):
    ┌─────────────────────────────────────┐
    │        [Ghost] [Secondary] [Primary]│  ← Primary am Ende
    └─────────────────────────────────────┘
  
  implementation: |
    <PButtonGroup direction={{ base: 'column', s: 'row' }}>
      <PButton variant="ghost">Abbrechen</PButton>
      <PButton variant="secondary">Zurück</PButton>
      <PButton variant="primary">Speichern</PButton>
    </PButtonGroup>
  
  constraints: {
    @rule "Primary Button immer am Ende (visuell rechts)"
    @rule "Max 1 Primary Button"
    @rule "Max 3 Buttons empfohlen"
    @rule "Destruktive Aktion → Primary mit Error-Styling"
  }
}

@pattern modal-confirmation {
  @doc "Bestätigungs-Dialog für kritische Aktionen"
  
  structure: |
    ┌──────────────────────────────────────┐
    │ Heading                          [X] │
    ├──────────────────────────────────────┤
    │                                      │
    │  ⚠ InlineNotification               │
    │  Beschreibung der Konsequenzen      │
    │                                      │
    ├──────────────────────────────────────┤
    │           [Abbrechen] [Bestätigen]  │
    └──────────────────────────────────────┘
  
  implementation: |
    <PModal
      open={isOpen}
      heading="Löschen bestätigen"
      onDismiss={() => setIsOpen(false)}
    >
      <PInlineNotification
        state="warning"
        heading="Achtung"
        description="Diese Aktion kann nicht rückgängig gemacht werden."
      />
      
      <template slot="footer">
        <PButtonGroup>
          <PButton variant="ghost" onClick={() => setIsOpen(false)}>
            Abbrechen
          </PButton>
          <PButton 
            variant="primary"
            onClick={handleConfirm}
            // Destruktive Aktion: Error-Farbe verwenden
          >
            Endgültig löschen
          </PButton>
        </PButtonGroup>
      </template>
    </PModal>
}

# ----------------------------------------------------------------------------
# SEMANTICS (Refined with Conditions)
# ----------------------------------------------------------------------------

@semantics {
  
  @intent "user selects one from options" {
    @alias "Einzelauswahl", "Radio", "Dropdown"
    
    decision-tree: |
      Wie viele Optionen?
      ├─ ≤ 5 UND horizontal passt → p-segmented-control
      ├─ ≤ 7 → p-radio-group
      ├─ > 7 → p-select
      └─ > 7 UND durchsuchbar → p-select[filter:true]
    
    conditions: {
      "options ≤ 5, inline-space": {
        component: "p-segmented-control"
        reason: "Alle Optionen sofort sichtbar, schnelle Auswahl"
      }
      "options ≤ 7": {
        component: "p-radio-group"
        reason: "Optionen auf einen Blick erkennbar"
      }
      "options > 7": {
        component: "p-select"
        reason: "Spart Platz, Scrollbar bei vielen Optionen"
      }
      "options > 7, durchsuchbar": {
        component: "p-select[filter:true]"
        reason: "Benutzer kann schnell filtern"
      }
    }
  }
  
  @intent "user selects multiple from options" {
    @alias "Mehrfachauswahl", "Multi-Select"
    
    conditions: {
      "options ≤ 5": {
        component: "multiple p-checkbox"
        reason: "Alle Optionen sichtbar, klare Checkbox-Semantik"
      }
      "options > 5": {
        component: "p-multi-select"
        reason: "Kompakte Darstellung, Scrollbar"
      }
      "options > 5, durchsuchbar": {
        component: "p-multi-select[filter:true]"
      }
    }
  }
  
  @intent "user toggles binary setting" {
    @alias "An/Aus", "Aktivieren/Deaktivieren"
    
    decision-tree: |
      Wirkt die Änderung sofort?
      ├─ Ja → p-switch
      └─ Nein (Formular muss submitted werden) → p-checkbox
    
    conditions: {
      "sofortige Wirkung": {
        component: "p-switch"
        reason: "Switch signalisiert: Änderung gilt sofort"
        examples: ["Push-Benachrichtigungen", "Dark Mode", "Sound an/aus"]
      }
      "Formular-Submit erforderlich": {
        component: "p-checkbox"
        reason: "Checkbox ist Standard für Formulare"
        examples: ["AGB akzeptieren", "Newsletter abonnieren"]
      }
    }
  }
  
  @intent "user enters text" {
    conditions: {
      "E-Mail": { component: "p-input-email", reason: "Validierung + korrektes Keyboard (Mobile)" }
      "Telefon": { component: "p-input-tel", reason: "Numerisches Keyboard" }
      "URL": { component: "p-input-url", reason: "URL-Validierung" }
      "Suche": { component: "p-input-search", reason: "Search-Icon + Clear-Button" }
      "Passwort": { component: "p-input-password", reason: "Maskierung + Toggle" }
      "Datum": { component: "p-input-date", reason: "Native Date-Picker" }
      "Uhrzeit": { component: "p-input-time", reason: "Native Time-Picker" }
      "Zahl": { component: "p-input-number", reason: "Validierung + Stepper" }
      "Mehrzeilig": { component: "p-textarea", reason: "Für längere Texte" }
      "Einzeilig, allgemein": { component: "p-input-text", reason: "Standard-Texteingabe" }
    }
  }
  
  @intent "show feedback to user" {
    conditions: {
      "Seiten-Level, wichtig, dismissible": {
        component: "p-banner"
        reason: "Prominent am oberen Rand"
      }
      "Inline, kontextuell, persistent": {
        component: "p-inline-notification"
        reason: "Im Content-Flow, bei relevanter Stelle"
      }
      "Temporär, Aktion-Feedback": {
        component: "p-toast"
        reason: "Verschwindet automatisch, nicht störend"
      }
      "Zusatzinfo bei Hover/Focus": {
        component: "p-popover"
        reason: "Nicht invasiv, on-demand"
      }
    }
  }
  
  @intent "user confirms critical action" {
    conditions: {
      "Destruktiv (Löschen, Abbrechen)": {
        component: "p-modal"
        pattern: "modal-confirmation"
        reason: "Unterbricht Workflow, erzwingt bewusste Entscheidung"
        implementation: "Warning-Notification + Ghost/Danger Buttons"
      }
      "Einfache Bestätigung": {
        component: "p-modal"
        reason: "Fokussiert Aufmerksamkeit"
        implementation: "Text + Primary Button"
      }
    }
  }
  
  @intent "show/hide content" {
    conditions: {
      "Einzelner Bereich, on-demand": {
        component: "p-accordion (einzeln)"
      }
      "Mehrere unabhängige Bereiche": {
        component: "mehrere p-accordion mit eigenem State"
      }
      "Mehrere exklusive Bereiche (nur einer offen)": {
        component: "mehrere p-accordion mit shared State"
        implementation: "openId-Pattern"
      }
      "Gleichwertige Inhalts-Bereiche": {
        component: "p-tabs"
        reason: "Schneller Wechsel zwischen Views"
      }
    }
  }
  
  @intent "indicate loading state" {
    conditions: {
      "Button-Aktion läuft": {
        component: "p-button[loading:true]"
        reason: "Zeigt: Button wurde geklickt, Aktion läuft"
      }
      "Content wird geladen": {
        component: "p-spinner"
        reason: "Allgemeiner Lade-Indikator"
      }
      "Ganzer Bereich lädt": {
        component: "p-spinner size='large' + Overlay"
      }
    }
  }
}
```

---

## Compact Format (Refined)

```dsil
#DSIL:1.1 porsche-design-system v3.x

## Meta
prefix.html: "p-"
prefix.react: "P"
controlled: true (most components)
import.react: "@porsche-design-system/components-react"

## Tokens
T.theme[light|dark|auto]=light
T.spacing.static[xs:4|sm:8|md:16|lg:24|xl:32|2xl:48]px
T.spacing.fluid[xs|sm|md|lg|xl] (viewport-responsive)
T.color.light[primary:#010205|bg-base:#F2F2F2|bg-surface:#FFF|contrast-low|medium|high]
T.color.dark[primary:#FBFCFC|bg-base:#0E0E12|bg-surface:#1A1B1E]
T.color.notification[success:#018A16|warning:#FF9B00|error:#E00000|info:#2762D9]
T.typography.display[large|medium|small]
T.typography.heading[xx-large|x-large|large|medium|small]
T.typography.text[x-large|large|medium|small*|x-small|xx-small]
T.weight[regular:400|semi-bold:600|bold:700]
T.radius[small:4|medium:8|large:16]px
T.breakpoint[base:0|xs:480|s:760|m:1000|l:1300|xl:1760|xxl:1920]px

## Icons (Selection)
I.nav: arrow-head-*, arrow-*, external, return, logout
I.action: add, plus, minus, close, check, edit, delete, search, filter, sort, refresh, download, upload, save
I.status: information(-filled), success(-filled), warning(-filled), error(-filled), question(-filled)
I.user: user(-filled), heart(-filled), star(-filled), bookmark(-filled)
I.special: none (no icon)

## Types
@BreakpointCustomizable<T>: T | {base:T, xs?:T, s?:T, m?:T, l?:T, xl?:T, xxl?:T}
@FormState: none | success | error

## Components

### Buttons
C.p-button:
  v[primary|secondary|ghost]
  p[variant=primary, compact?:BC<bool>, disabled?, loading?, hideLabel?:BC<bool>, 
    icon?:Icon=none, iconSource?:url, type?=submit, name?, value?, form?, theme?=light, aria?]
  s[label!:text]
  e[click, focus, blur]
  !loading→disabled !hideLabel+no-icon=invalid !icon-only→aria-label
  
  ex.basic: <PButton>Speichern</PButton>
  ex.variants: <PButton variant="ghost">Abbrechen</PButton>
  ex.loading: <PButton loading>Wird gespeichert...</PButton>

C.p-button-group:
  p[direction?:BC<row|column>=row]
  s→[p-button, p-button-pure, p-link, p-link-pure]
  !max-1-primary !primary-at-end !max-3-recommended

### Form Fields
C.p-input-text:
  p[label!, name?, value?, placeholder?, description?, message?, state?:FormState=none,
    disabled?, readOnly?, required?, maxLength?, minLength?, showCounter?, hideLabel?, theme?]
  s[label?, description?, message?]
  e[input(value), change(value), focus, blur]
  
  ex: <PInputText label="Name" required onInput={(e) => setValue(e.target.value)} />

C.p-input-email: @extends p-input-text
C.p-input-password: @extends p-input-text +showPasswordToggle?
C.p-input-number: @extends p-input-text +min?, max?, step?
C.p-input-search: @extends p-input-text +submitButton? e[+search(value)]
C.p-input-tel: @extends p-input-text
C.p-input-url: @extends p-input-text
C.p-input-date: @extends p-input-text
C.p-input-time: @extends p-input-text

C.p-textarea:
  p[label!, name?, value?, placeholder?, rows?=3, description?, message?, state?, 
    disabled?, readOnly?, required?, maxLength?, showCounter?, hideLabel?, theme?]
  e[input, change, focus, blur]

C.p-select @controlled:
  p[label!, name?, value?, description?, message?, state?, disabled?, required?,
    hideLabel?, dropdownDirection?=auto, filter?, theme?]
  s→[p-select-option, p-optgroup]
  e[update({value:string, name:string})]
  
  ex: <PSelect value={v} onUpdate={(e) => setV(e.detail.value)}>
        <PSelectOption value="a">A</PSelectOption>
      </PSelect>

C.p-multi-select @controlled:
  p[label!, name?, value?:string[], description?, message?, state?, disabled?,
    required?, hideLabel?, filter?, theme?]
  s→[p-multi-select-option, p-optgroup]
  e[update({value:string[], name:string})]

C.p-checkbox:
  p[label!, name?, value?, checked?, indeterminate?, disabled?, required?,
    message?, state?, hideLabel?, loading?, theme?]
  e[update({checked:bool, name:string, value:string})]

C.p-radio-group @controlled:
  p[name!, value?, label?, direction?=vertical, disabled?, required?,
    message?, state?, hideLabel?, theme?]
  s→[p-radio-group-option]
  e[update({value:string, name:string})]

C.p-switch:
  p[label!, name?, value?, checked?, disabled?, loading?, alignLabel?=end,
    hideLabel?, stretch?:BC<bool>, message?, state?, theme?]
  e[update({checked:bool, name:string, value:string})]
  use: immediate-effect settings (NOT for form-submit → use checkbox)

C.p-segmented-control @controlled:
  p[value?=0, backgroundColor?, theme?]
  s→[p-segmented-control-item]
  e[update({value:number})]
  !2-5-options

C.p-fieldset:
  p[label!, labelSize?, required?, state?, message?, theme?]
  s[fields!, label?, message?]

C.p-pin-code:
  p[label!, length?=4, value?, type?=number, disabled?, required?, state?, message?, hideLabel?, theme?]
  e[update({value:string, isComplete:bool})]

### Overlays
C.p-accordion @controlled:
  p[heading!, headingTag?=h2, size?, open?=false, compact?, theme?]
  s[content!:node]
  e[update({open:bool})]
  !MUST-handle-update-event
  
  ex: const [open, setOpen] = useState(false);
      <PAccordion heading="FAQ" open={open} onUpdate={(e) => setOpen(e.detail.open)}>
        Content
      </PAccordion>

C.p-modal @controlled:
  p[open!, heading?, dismissButton?=true, disableCloseButton?, disableBackdropClick?,
    fullscreen?:BC<bool>, theme?, aria?]
  s[header?, body!:node, footer?]
  e[dismiss({})]
  !MUST-handle-dismiss-event
  
  ex: <PModal open={isOpen} heading="Titel" onDismiss={() => setIsOpen(false)}>
        <p>Content</p>
        <template slot="footer"><PButton>OK</PButton></template>
      </PModal>

C.p-flyout @controlled:
  p[open!, position?=end, theme?]
  s[header?, body!, footer?, sub-footer?]
  e[dismiss({})]

C.p-sheet @controlled:
  p[open!, theme?]
  s[header?, body!]
  e[dismiss({})]

C.p-popover:
  p[direction?=bottom, description?, theme?]
  s[trigger!:node]

### Feedback
C.p-banner @controlled:
  p[open!, heading?, description?, state?=info, dismissButton?, persistent?, theme?]
  e[dismiss({})]

C.p-inline-notification:
  p[heading?, description?, state?=info, dismissButton?, persistent?, theme?]
  s[heading?, description?]
  e[dismiss({}), action?({name:string})]

C.p-toast @singleton:
  api: addMessage({text:string, state?:info|success})

### Display
C.p-text:
  p[size?=small, weight?, align?, color?, ellipsis?, theme?]
  s[content!:node]
  perf: prefer CSS styles (@include pds-text-small)

C.p-heading:
  p[size?=xx-large, tag?=h2, align?, color?, ellipsis?, theme?]
  s[content!:node]
  note: size≠tag (size=visual, tag=semantic)

C.p-display:
  p[size?=large, tag?=h1, align?, color?, ellipsis?, theme?]
  s[content!:node]
  use: hero, stats, emotional moments

C.p-spinner:
  p[size?=small, aria?, theme?]

C.p-icon:
  p[name?:Icon, source?:url, size?, color?, lazy?, aria?, theme?]
  !name-OR-source

C.p-tag:
  p[color?, icon?, iconSource?, theme?]
  s[label!:text]

C.p-divider:
  p[orientation?=horizontal, color?, theme?]

## Patterns

P.form-field: [label?, field!(input|select|textarea|checkbox|radio), description?, message?]
  state[none|success|error] !error→message-required !required→label-asterisk

P.button-actions: <PButtonGroup direction={{base:'column',s:'row'}}>
  [ghost?, secondary?, primary!]  # primary LAST
  !max-1-primary !destructive→primary-with-error-color

P.modal-confirmation: <PModal>[
  heading + <PInlineNotification state="warning"> + 
  footer: <PButtonGroup>[ghost:Abbrechen, primary:Bestätigen]
]

## Semantics

S."select 1/n":
  ≤5+inline → p-segmented-control
  ≤7 → p-radio-group
  >7 → p-select
  >7+searchable → p-select[filter]

S."select n/n":
  ≤5 → multiple p-checkbox
  >5 → p-multi-select

S."toggle":
  immediate-effect → p-switch
  form-submit-required → p-checkbox

S."text-input":
  email → p-input-email
  phone → p-input-tel
  url → p-input-url
  search → p-input-search
  password → p-input-password
  date → p-input-date
  time → p-input-time
  number → p-input-number
  multiline → p-textarea
  default → p-input-text

S."feedback":
  page-level → p-banner
  inline-contextual → p-inline-notification
  temporary → p-toast
  on-demand → p-popover

S."confirm-action":
  destructive → p-modal + warning-notification + danger-button
  simple → p-modal + primary-button

S."show/hide":
  single → p-accordion
  multiple-independent → multiple p-accordion (own state each)
  multiple-exclusive → multiple p-accordion (shared openId state)
  switchable-views → p-tabs

S."loading":
  button-action → p-button[loading]
  content-area → p-spinner
```

---

## Changelog v1.0 → v1.1

| Änderung | Beschreibung |
|----------|--------------|
| **Event Payloads** | Vollständige Payload-Struktur mit Typen dokumentiert |
| **Icon-Liste** | Alle Icons kategorisiert und aufgelistet |
| **CSS Custom Properties** | SCSS-Variablen und Tailwind-Klassen pro Token |
| **Code-Beispiele** | Konkrete React/HTML-Beispiele pro Komponente |
| **Constraint-Errors** | Fehlermeldungen für Constraint-Verletzungen |
| **Patterns verfeinert** | ASCII-Diagramme und vollständige Implementierungen |
| **Semantics erweitert** | Decision-Trees und Begründungen für Komponentenwahl |
| **@controlled Marker** | Explizite Kennzeichnung controlled vs. uncontrolled |
| **Usage Guidelines** | Do/Don't Listen mit konkreten Beispielen |
