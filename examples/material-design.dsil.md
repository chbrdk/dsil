# DSIL Manifest: Material Design 3

> **Version**: 1.0.0  
> **Based on**: Google Material Design 3 (Material You)  
> **Source**: https://m3.material.io/

---

## Overview

This is a DSIL representation of Google's Material Design 3 system, focusing on core web components and their APIs. Material Design 3 emphasizes personalization, dynamic color, and adaptive layouts.

---

## Full Format

```dsil
# ============================================================================
# MATERIAL DESIGN 3 – DSIL Manifest
# Version: 1.0.0
# Based on: Material Design 3 (Material You)
# ============================================================================

@meta {
  name: "material-design"
  version: "3.0.0"
  dsil-version: "1.0.0"
  description: "Google Material Design 3 - Material You design system"
  
  prefix: {
    html: "mdc-"       # Material Design Components
    react: "MDC"       # Material Design Components React
  }
  
  imports: {
    react: "@material/react-components"
    styles: "@material/react-components/styles"
  }
  
  config: {
    strict: true
    controlled: false   # Most components are uncontrolled by default
    theme: "light"
    allowCustom: false
  }
  
  links: {
    documentation: "https://m3.material.io/"
    figma: "https://www.figma.com/community/file/1035203688168086460"
    github: "https://github.com/material-components"
  }
}

# ============================================================================
# TOKENS: Material Design 3 Tokens
# ============================================================================

@tokens {
  theme: {
    values: [light, dark]
    default: "light"
  }
  
  spacing: {
    @group static {
      0: { value: "0px", css: "--md-sys-spacing-0" }
      4: { value: "4px", css: "--md-sys-spacing-4" }
      8: { value: "8px", css: "--md-sys-spacing-8" }
      12: { value: "12px", css: "--md-sys-spacing-12" }
      16: { value: "16px", css: "--md-sys-spacing-16" }
      24: { value: "24px", css: "--md-sys-spacing-24" }
      32: { value: "32px", css: "--md-sys-spacing-32" }
      48: { value: "48px", css: "--md-sys-spacing-48" }
      64: { value: "64px", css: "--md-sys-spacing-64" }
    }
  }
  
  color: {
    @group primary {
      primary: { value: "var(--md-sys-color-primary)", css: "--md-sys-color-primary" }
      on-primary: { value: "var(--md-sys-color-on-primary)", css: "--md-sys-color-on-primary" }
      primary-container: { value: "var(--md-sys-color-primary-container)", css: "--md-sys-color-primary-container" }
      on-primary-container: { value: "var(--md-sys-color-on-primary-container)", css: "--md-sys-color-on-primary-container" }
    }
    
    @group secondary {
      secondary: { value: "var(--md-sys-color-secondary)", css: "--md-sys-color-secondary" }
      on-secondary: { value: "var(--md-sys-color-on-secondary)", css: "--md-sys-color-on-secondary" }
      secondary-container: { value: "var(--md-sys-color-secondary-container)", css: "--md-sys-color-secondary-container" }
      on-secondary-container: { value: "var(--md-sys-color-on-secondary-container)", css: "--md-sys-color-on-secondary-container" }
    }
    
    @group tertiary {
      tertiary: { value: "var(--md-sys-color-tertiary)", css: "--md-sys-color-tertiary" }
      on-tertiary: { value: "var(--md-sys-color-on-tertiary)", css: "--md-sys-color-on-tertiary" }
      tertiary-container: { value: "var(--md-sys-color-tertiary-container)", css: "--md-sys-color-tertiary-container" }
      on-tertiary-container: { value: "var(--md-sys-color-on-tertiary-container)", css: "--md-sys-color-on-tertiary-container" }
    }
    
    @group error {
      error: { value: "var(--md-sys-color-error)", css: "--md-sys-color-error" }
      on-error: { value: "var(--md-sys-color-on-error)", css: "--md-sys-color-on-error" }
      error-container: { value: "var(--md-sys-color-error-container)", css: "--md-sys-color-error-container" }
      on-error-container: { value: "var(--md-sys-color-on-error-container)", css: "--md-sys-color-on-error-container" }
    }
    
    @group surface {
      surface: { value: "var(--md-sys-color-surface)", css: "--md-sys-color-surface" }
      on-surface: { value: "var(--md-sys-color-on-surface)", css: "--md-sys-color-on-surface" }
      surface-variant: { value: "var(--md-sys-color-surface-variant)", css: "--md-sys-color-surface-variant" }
      on-surface-variant: { value: "var(--md-sys-color-on-surface-variant)", css: "--md-sys-color-on-surface-variant" }
    }
  }
  
  typography: {
    family: {
      sans: { value: "Roboto, sans-serif", css: "--md-sys-typescale-font-family-name" }
    }
    
    scale: {
      display-large: { value: "57px/64px", css: "--md-sys-typescale-display-large-size" }
      display-medium: { value: "45px/52px", css: "--md-sys-typescale-display-medium-size" }
      display-small: { value: "36px/44px", css: "--md-sys-typescale-display-small-size" }
      headline-large: { value: "32px/40px", css: "--md-sys-typescale-headline-large-size" }
      headline-medium: { value: "28px/36px", css: "--md-sys-typescale-headline-medium-size" }
      headline-small: { value: "24px/32px", css: "--md-sys-typescale-headline-small-size" }
      title-large: { value: "22px/28px", css: "--md-sys-typescale-title-large-size" }
      title-medium: { value: "16px/24px", css: "--md-sys-typescale-title-medium-size", default: true }
      title-small: { value: "14px/20px", css: "--md-sys-typescale-title-small-size" }
      body-large: { value: "16px/24px", css: "--md-sys-typescale-body-large-size" }
      body-medium: { value: "14px/20px", css: "--md-sys-typescale-body-medium-size" }
      body-small: { value: "12px/16px", css: "--md-sys-typescale-body-small-size" }
      label-large: { value: "14px/20px", css: "--md-sys-typescale-label-large-size" }
      label-medium: { value: "12px/16px", css: "--md-sys-typescale-label-medium-size" }
      label-small: { value: "11px/16px", css: "--md-sys-typescale-label-small-size" }
    }
    
    weight: {
      regular: { value: 400, css: "--md-sys-typescale-weight-regular" }
      medium: { value: 500, css: "--md-sys-typescale-weight-medium" }
      bold: { value: 700, css: "--md-sys-typescale-weight-bold" }
    }
  }
  
  elevation: {
    level0: { value: "0px", css: "--md-sys-elevation-level0" }
    level1: { value: "1px", css: "--md-sys-elevation-level1" }
    level2: { value: "3px", css: "--md-sys-elevation-level2" }
    level3: { value: "6px", css: "--md-sys-elevation-level3" }
    level4: { value: "8px", css: "--md-sys-elevation-level4" }
    level5: { value: "12px", css: "--md-sys-elevation-level5" }
  }
  
  shape: {
    corner: {
      none: { value: "0px", css: "--md-sys-shape-corner-none" }
      extra-small: { value: "4px", css: "--md-sys-shape-corner-extra-small" }
      small: { value: "8px", css: "--md-sys-shape-corner-small" }
      medium: { value: "12px", css: "--md-sys-shape-corner-medium" }
      large: { value: "16px", css: "--md-sys-shape-corner-large" }
      extra-large: { value: "28px", css: "--md-sys-shape-corner-extra-large" }
      full: { value: "9999px", css: "--md-sys-shape-corner-full" }
    }
  }
  
  motion: {
    duration: {
      short1: { value: "50ms", css: "--md-sys-motion-duration-short1" }
      short2: { value: "200ms", css: "--md-sys-motion-duration-short2" }
      short3: { value: "250ms", css: "--md-sys-motion-duration-short3" }
      short4: { value: "300ms", css: "--md-sys-motion-duration-short4" }
      medium1: { value: "250ms", css: "--md-sys-motion-duration-medium1" }
      medium2: { value: "300ms", css: "--md-sys-motion-duration-medium2" }
      medium3: { value: "350ms", css: "--md-sys-motion-duration-medium3" }
      medium4: { value: "400ms", css: "--md-sys-motion-duration-medium4" }
      long1: { value: "300ms", css: "--md-sys-motion-duration-long1" }
      long2: { value: "400ms", css: "--md-sys-motion-duration-long2" }
      long3: { value: "500ms", css: "--md-sys-motion-duration-long3" }
      long4: { value: "600ms", css: "--md-sys-motion-duration-long4" }
    }
    
    easing: {
      standard: { value: "cubic-bezier(0.2, 0, 0, 1)", css: "--md-sys-motion-easing-standard" }
      emphasized: { value: "cubic-bezier(0.2, 0, 0, 1)", css: "--md-sys-motion-easing-emphasized" }
      decelerated: { value: "cubic-bezier(0, 0, 0.2, 1)", css: "--md-sys-motion-easing-decelerated" }
      accelerated: { value: "cubic-bezier(0.4, 0, 1, 1)", css: "--md-sys-motion-easing-accelerated" }
    }
  }
  
  breakpoint: {
    mobile: { value: "0px" }
    tablet: { value: "600px" }
    desktop: { value: "840px" }
    wide: { value: "1200px" }
  }
}

# ============================================================================
# ICONS: Material Symbols
# ============================================================================

@icons {
  @group navigation {
    arrow_back, arrow_forward, arrow_upward, arrow_downward
    chevron_left, chevron_right, chevron_up, chevron_down
    menu, close, home, more_vert, more_horiz
    expand_less, expand_more, refresh, search
  }
  
  @group action {
    add, edit, delete, save, done, cancel, check, clear
    download, upload, share, print, copy, cut, paste
    favorite, favorite_border, star, star_border
    bookmark, bookmark_border, settings
  }
  
  @group communication {
    email, phone, chat, send, reply, forward
    notification, notifications_off, announcement
  }
  
  @group content {
    content_copy, content_cut, content_paste
    file_download, file_upload, attach_file
    image, video, audio, description
  }
  
  @group social {
    person, person_add, group, share, public
    facebook, twitter, google, linkedin, instagram
  }
  
  @group status {
    check_circle, error, warning, info, help
    check_circle_outline, error_outline, warning_amber
    done_all, pending, schedule
  }
  
  special: {
    none: { @doc "No icon" }
  }
}

# ============================================================================
# TYPES
# ============================================================================

@types {
  @type Density {
    values: [comfortable, compact, default]
    default: default
    @doc "Component density level"
  }
  
  @type State {
    values: [enabled, disabled, hover, focused, pressed, dragged]
    @doc "Component interaction state"
  }
  
  @type Elevation {
    values: [level0, level1, level2, level3, level4, level5]
    default: level1
    @doc "Material elevation level"
  }
  
  @type IconName {
    @doc "Material Symbols icon name"
    definition: "@ref(icons.*)"
    special: none
  }
}

# ============================================================================
# COMPONENTS
# ============================================================================

@component mdc-button {
  @doc "Material Design button component with multiple variants"
  @controlled false
  @tag-react MDCButton
  
  variants: {
    variant: {
      filled: { @doc "Filled button with solid background" }
      outlined: { @doc "Outlined button with border" }
      text: { @doc "Text button, minimal appearance" }
      elevated: { @doc "Filled button with elevation shadow" }
      tonal: { @doc "Filled button with tonal background" }
    }
  }
  
  props: {
    variant: {
      type: "filled" | "outlined" | "text" | "elevated" | "tonal"
      default: "filled"
    }
    disabled: {
      type: boolean
      default: false
    }
    icon: {
      type: @type(IconName)
      @doc "Leading icon name"
    }
    trailingIcon: {
      type: @type(IconName)
      @doc "Trailing icon name"
    }
    href: {
      type: string
      @doc "Makes button a link"
    }
    target: {
      type: "_blank" | "_self" | "_parent" | "_top"
      @doc "Link target (requires href)"
    }
    density: {
      type: @type(Density)
      default: "default"
    }
  }
  
  slots: {
    default: {
      required: true
      type: text
      @doc "Button label"
    }
  }
  
  events: {
    click: { native: true }
    focus: { native: true }
    blur: { native: true }
  }
  
  constraints: {
    @rule "trailingIcon requires icon or content"
    @rule "href makes button non-submittable"
    @rule "target requires href"
  }
  
  a11y: {
    role: "button"
    focusable: true
    rules: [
      "Enter/Space activates",
      "Focus ring visible",
      "Icon-only needs aria-label"
    ]
  }
  
  usage: {
    do: [
      "Use filled for primary actions",
      "Use text for secondary actions",
      "Use outlined for medium emphasis",
      "Maximum one filled button per screen section"
    ]
    dont: [
      "Don't use multiple filled buttons together",
      "Don't use button for navigation (use link)"
    ]
  }
  
  examples: {
    filled: |
      <MDCButton variant="filled">Click me</MDCButton>
    
    outlined: |
      <MDCButton variant="outlined">Cancel</MDCButton>
    
    with-icon: |
      <MDCButton variant="filled" icon="add">Add item</MDCButton>
    
    text-button: |
      <MDCButton variant="text">Learn more</MDCButton>
  }
}

@component mdc-text-field {
  @doc "Material Design text input field with floating label"
  @controlled false
  @tag-react MDCTextField
  
  variants: {
    variant: {
      filled: { @doc "Filled text field with background" }
      outlined: { @doc "Outlined text field with border" }
    }
  }
  
  props: {
    variant: {
      type: "filled" | "outlined"
      default: "filled"
    }
    label: {
      type: string
      required: true
      @doc "Floating label text"
    }
    value: {
      type: string
      @doc "Input value (controlled)"
    }
    placeholder: {
      type: string
      @doc "Placeholder text (shown when empty)"
    }
    type: {
      type: "text" | "email" | "password" | "number" | "tel" | "url" | "search"
      default: "text"
    }
    disabled: {
      type: boolean
      default: false
    }
    required: {
      type: boolean
      default: false
    }
    helperText: {
      type: string
      @doc "Helper text below input"
    }
    errorText: {
      type: string
      @doc "Error message (replaces helperText)"
    }
    leadingIcon: {
      type: @type(IconName)
      @doc "Leading icon (e.g., search, person)"
    }
    trailingIcon: {
      type: @type(IconName)
      @doc "Trailing icon (e.g., clear, visibility)"
    }
    maxLength: {
      type: number
      @doc "Maximum character count"
    }
    minLength: {
      type: number
      @doc "Minimum character count"
    }
    pattern: {
      type: string
      @doc "Input pattern (regex)"
    }
    density: {
      type: @type(Density)
      default: "default"
    }
  }
  
  slots: {
    default: {
      required: false
      type: node
      @doc "Custom input element (advanced)"
    }
  }
  
  events: {
    input: {
      native: true
      payload: { value: string }
    }
    change: {
      native: true
      payload: { value: string }
    }
    focus: { native: true }
    blur: { native: true }
  }
  
  constraints: {
    @rule "errorText replaces helperText when present"
    @rule "required requires label indicator (*)"
    @rule "trailingIcon clear requires value"
    @rule "type=password typically uses visibility trailingIcon"
  }
  
  a11y: {
    role: "textbox"
    rules: [
      "aria-label from label prop",
      "aria-required from required prop",
      "aria-invalid from errorText",
      "aria-describedby for helper/error text"
    ]
  }
  
  examples: {
    basic: |
      <MDCTextField 
        variant="filled"
        label="Email"
        type="email"
        required
      />
    
    with-helper: |
      <MDCTextField 
        variant="outlined"
        label="Password"
        type="password"
        helperText="Must be at least 8 characters"
        required
      />
    
    with-error: |
      <MDCTextField 
        variant="filled"
        label="Email"
        type="email"
        errorText="Please enter a valid email address"
      />
    
    with-icons: |
      <MDCTextField 
        variant="outlined"
        label="Search"
        leadingIcon="search"
        trailingIcon="clear"
      />
  }
}

@component mdc-card {
  @doc "Material Design card container component"
  @controlled false
  @tag-react MDCCard
  
  props: {
    variant: {
      type: "elevated" | "filled" | "outlined"
      default: "elevated"
    }
    elevation: {
      type: @type(Elevation)
      default: "level1"
      @doc "Shadow elevation (elevated variant only)"
    }
    href: {
      type: string
      @doc "Makes entire card clickable as link"
    }
    disabled: {
      type: boolean
      default: false
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "Card content"
    }
    media: {
      required: false
      type: node
      @doc "Media area (image/video) at top"
    }
    header: {
      required: false
      type: node
      @doc "Header section"
    }
    actions: {
      required: false
      type: node
      @doc "Action buttons area"
    }
  }
  
  events: {
    click: { native: true }
  }
  
  constraints: {
    @rule "elevation only applies to elevated variant"
    @rule "href makes card non-interactive for child buttons"
    @rule "media should be first slot"
    @rule "actions typically contains buttons"
  }
  
  usage: {
    do: [
      "Use for grouped content",
      "Use elevated for interactive cards",
      "Use outlined for contained lists"
    ]
    dont: [
      "Don't nest cards",
      "Don't use card for simple containers"
    ]
  }
  
  examples: {
    basic: |
      <MDCCard variant="elevated">
        <div slot="header">
          <h3>Card Title</h3>
        </div>
        <p>Card content goes here</p>
        <div slot="actions">
          <MDCButton variant="text">Action 1</MDCButton>
          <MDCButton variant="filled">Action 2</MDCButton>
        </div>
      </MDCCard>
    
    with-media: |
      <MDCCard variant="filled">
        <img slot="media" src="image.jpg" alt="Card image" />
        <h3>Card with Image</h3>
        <p>Content below image</p>
      </MDCCard>
  }
}

@component mdc-dialog {
  @doc "Material Design modal dialog component"
  @controlled true
  @tag-react MDCDialog
  
  props: {
    open: {
      type: boolean
      required: true
      @doc "Controls dialog visibility (controlled)"
    }
    fullscreen: {
      type: boolean
      default: false
      @doc "Fullscreen dialog on mobile"
    }
    fullWidth: {
      type: boolean
      default: false
      @doc "Full width dialog"
    }
    maxWidth: {
      type: "xs" | "sm" | "md" | "lg" | "xl" | false
      default: "sm"
    }
    persistent: {
      type: boolean
      default: false
      @doc "Prevents closing on backdrop click"
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "Dialog content"
    }
    header: {
      required: false
      type: node
      @doc "Dialog header/title"
    }
    actions: {
      required: false
      type: node
      @doc "Action buttons (typically in footer)"
    }
  }
  
  events: {
    close: {
      payload: { action: string }
      @doc "Fired when dialog closes, action indicates how (backdrop, escape, button)"
      handling: |
        const [open, setOpen] = useState(false);
        
        <MDCDialog 
          open={open}
          onClose={(e) => {
            setOpen(false);
            // e.detail.action: 'backdrop' | 'escape' | 'action-button'
          }}
        >
          Content
        </MDCDialog>
    }
  }
  
  constraints: {
    @rule "close event must be handled" {
      critical: true
      error: "Dialog requires onClose handler to manage open state"
    }
    @rule "actions typically contains buttons"
    @rule "persistent prevents backdrop dismiss but escape still works"
  }
  
  a11y: {
    role: "dialog"
    aria-modal: true
    focus-management: {
      open: "Focus first focusable element"
      close: "Return focus to trigger"
    }
    requirements: [
      "Focus trap within dialog",
      "ESC key closes",
      "aria-labelledby on header",
      "Backdrop click closes (unless persistent)"
    ]
  }
  
  examples: {
    basic: |
      const [open, setOpen] = useState(false);
      
      <MDCDialog open={open} onClose={() => setOpen(false)}>
        <div slot="header">
          <h2>Dialog Title</h2>
        </div>
        <p>Dialog content</p>
        <div slot="actions">
          <MDCButton variant="text" onClick={() => setOpen(false)}>Cancel</MDCButton>
          <MDCButton variant="filled" onClick={() => setOpen(false)}>Confirm</MDCButton>
        </div>
      </MDCDialog>
  }
}

@component mdc-checkbox {
  @doc "Material Design checkbox component"
  @controlled false
  @tag-react MDCCheckbox
  
  props: {
    checked: {
      type: boolean
      default: false
    }
    indeterminate: {
      type: boolean
      default: false
      @doc "Indeterminate state (e.g., for select all)"
    }
    disabled: {
      type: boolean
      default: false
    }
    required: {
      type: boolean
      default: false
    }
    value: {
      type: string
      @doc "Form value when checked"
    }
    name: {
      type: string
      @doc "Form field name"
    }
    density: {
      type: @type(Density)
      default: "default"
    }
  }
  
  slots: {
    default: {
      required: false
      type: node
      @doc "Label content (alternative to aria-label)"
    }
  }
  
  events: {
    change: {
      payload: { checked: boolean, value: string }
    }
  }
  
  constraints: {
    @rule "indeterminate requires checked=false"
    @rule "label required (either slot content or aria-label)"
  }
  
  a11y: {
    role: "checkbox"
    rules: [
      "aria-checked from checked/indeterminate",
      "aria-required from required",
      "Space toggles when focused"
    ]
  }
  
  examples: {
    basic: |
      <MDCCheckbox>Accept terms</MDCCheckbox>
    
    controlled: |
      const [checked, setChecked] = useState(false);
      <MDCCheckbox 
        checked={checked} 
        onChange={(e) => setChecked(e.detail.checked)}
      >
        Subscribe to newsletter
      </MDCCheckbox>
    
    indeterminate: |
      <MDCCheckbox indeterminate>Select all</MDCCheckbox>
  }
}

@component mdc-switch {
  @doc "Material Design switch (toggle) component"
  @controlled false
  @tag-react MDCSwitch
  
  props: {
    checked: {
      type: boolean
      default: false
    }
    disabled: {
      type: boolean
      default: false
    }
    required: {
      type: boolean
      default: false
    }
    value: {
      type: string
      @doc "Form value when checked"
    }
    name: {
      type: string
      @doc "Form field name"
    }
  }
  
  slots: {
    default: {
      required: false
      type: node
      @doc "Label content"
    }
  }
  
  events: {
    change: {
      payload: { checked: boolean }
    }
  }
  
  constraints: {
    @rule "label required (slot content or aria-label)"
    @rule "Use for immediate effect toggles, not form submissions"
  }
  
  a11y: {
    role: "switch"
    rules: [
      "aria-checked from checked prop",
      "Space toggles when focused"
    ]
  }
  
  examples: {
    basic: |
      <MDCSwitch>Enable notifications</MDCSwitch>
    
    controlled: |
      const [enabled, setEnabled] = useState(false);
      <MDCSwitch 
        checked={enabled}
        onChange={(e) => setEnabled(e.detail.checked)}
      >
        Dark mode
      </MDCSwitch>
  }
}

@component mdc-radio {
  @doc "Material Design radio button component (use in group)"
  @controlled false
  @tag-react MDCRadio
  
  props: {
    checked: {
      type: boolean
      default: false
    }
    disabled: {
      type: boolean
      default: false
    }
    value: {
      type: string
      required: true
      @doc "Radio value (must be unique in group)"
    }
    name: {
      type: string
      required: true
      @doc "Group name (all radios in group share same name)"
    }
    density: {
      type: @type(Density)
      default: "default"
    }
  }
  
  slots: {
    default: {
      required: false
      type: node
      @doc "Label content"
    }
  }
  
  events: {
    change: {
      payload: { value: string, checked: boolean }
    }
  }
  
  constraints: {
    @rule "Must be used in radio-group with shared name"
    @rule "Only one checked per group"
    @rule "label required (slot content or aria-label)"
  }
  
  a11y: {
    role: "radio"
    rules: [
      "aria-checked from checked",
      "Arrow keys navigate within group",
      "Space selects when focused"
    ]
  }
}

@component mdc-radio-group {
  @doc "Material Design radio button group container"
  @controlled true
  @tag-react MDCRadioGroup
  
  props: {
    value: {
      type: string
      @doc "Selected value (controlled)"
    }
    name: {
      type: string
      required: true
      @doc "Group name (shared by all child radios)"
    }
    required: {
      type: boolean
      default: false
    }
    disabled: {
      type: boolean
      default: false
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "Radio button children"
    }
  }
  
  events: {
    change: {
      payload: { value: string }
    }
  }
  
  constraints: {
    @rule "All child radios must have same name as group"
    @rule "Only one radio can be checked"
    @rule "required means one must be selected"
  }
  
  examples: {
    basic: |
      <MDCRadioGroup name="theme" value={selected} onChange={(e) => setSelected(e.detail.value)}>
        <MDCRadio value="light">Light</MDCRadio>
        <MDCRadio value="dark">Dark</MDCRadio>
        <MDCRadio value="auto">Auto</MDCRadio>
      </MDCRadioGroup>
  }
}

@component mdc-chip {
  @doc "Material Design chip component (filter, choice, input)"
  @controlled false
  @tag-react MDCChip
  
  variants: {
    variant: {
      assist: { @doc "Assist chip - triggers action" }
      filter: { @doc "Filter chip - toggles filter state" }
      input: { @doc "Input chip - removable entry" }
      suggestion: { @doc "Suggestion chip - suggests action" }
    }
  }
  
  props: {
    variant: {
      type: "assist" | "filter" | "input" | "suggestion"
      default: "assist"
    }
    selected: {
      type: boolean
      default: false
      @doc "Selected state (filter chips)"
    }
    disabled: {
      type: boolean
      default: false
    }
    icon: {
      type: @type(IconName)
      @doc "Leading icon"
    }
    trailingIcon: {
      type: @type(IconName)
      @doc "Trailing icon (typically close for input chips)"
    }
    href: {
      type: string
      @doc "Makes chip a link (assist chips)"
    }
  }
  
  slots: {
    default: {
      required: true
      type: text
      @doc "Chip label"
    }
  }
  
  events: {
    click: { native: true }
    remove: {
      payload: {}
      @doc "Fired when remove icon clicked (input chips)"
    }
  }
  
  constraints: {
    @rule "trailingIcon typically 'close' for input variant"
    @rule "selected only applies to filter variant"
    @rule "href only applies to assist variant"
  }
  
  examples: {
    filter: |
      <MDCChip variant="filter" selected>Active</MDCChip>
      <MDCChip variant="filter">Inactive</MDCChip>
    
    input: |
      <MDCChip variant="input" trailingIcon="close" onRemove={handleRemove}>
        Tag name
      </MDCChip>
  }
}

@component mdc-snackbar {
  @doc "Material Design snackbar/toast notification"
  @controlled true
  @tag-react MDCSnackbar
  
  props: {
    open: {
      type: boolean
      required: true
      @doc "Controls visibility (controlled)"
    }
    message: {
      type: string
      required: true
      @doc "Message text"
    }
    actionLabel: {
      type: string
      @doc "Action button label"
    }
    timeout: {
      type: number
      default: 4000
      @doc "Auto-close timeout in ms (0 = no auto-close)"
    }
    variant: {
      type: "fill" | "outline"
      default: "fill"
    }
  }
  
  slots: {
    action: {
      required: false
      type: node
      @doc "Custom action button"
    }
  }
  
  events: {
    close: {
      payload: { reason: "action" | "dismiss" | "timeout" }
      @doc "Fired when snackbar closes"
    }
    action: {
      payload: {}
      @doc "Fired when action button clicked"
    }
  }
  
  constraints: {
    @rule "close event must be handled" {
      critical: true
    }
    @rule "actionLabel or action slot required for action button"
    @rule "timeout=0 means manual close only"
  }
  
  a11y: {
    role: "status"
    aria-live: "polite"
    announcements: {
      show: "{message}"
      action: "{message}. {actionLabel} available"
    }
  }
  
  examples: {
    basic: |
      const [open, setOpen] = useState(false);
      
      <MDCSnackbar 
        open={open}
        message="Changes saved"
        onClose={() => setOpen(false)}
      />
    
    with-action: |
      <MDCSnackbar 
        open={open}
        message="Item deleted"
        actionLabel="Undo"
        onAction={handleUndo}
        onClose={() => setOpen(false)}
      />
  }
}

@component mdc-bottom-sheet {
  @doc "Material Design bottom sheet (mobile drawer from bottom)"
  @controlled true
  @tag-react MDCBottomSheet
  
  props: {
    open: {
      type: boolean
      required: true
    }
    modal: {
      type: boolean
      default: true
      @doc "Modal bottom sheet blocks interaction"
    }
    dismissible: {
      type: boolean
      default: true
      @doc "Can be dismissed by swipe/backdrop"
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
    }
    handle: {
      required: false
      type: node
      @doc "Drag handle indicator"
    }
  }
  
  events: {
    close: {
      payload: { reason: "backdrop" | "swipe" | "action" }
    }
  }
  
  constraints: {
    @rule "close event must be handled"
    @rule "typically contains list items or actions"
  }
  
  a11y: {
    role: "dialog"
    aria-modal: true
  }
}

@component mdc-list {
  @doc "Material Design list component"
  @controlled false
  @tag-react MDCList
  
  props: {
    variant: {
      type: "one-line" | "two-line" | "three-line"
      default: "one-line"
    }
    dense: {
      type: boolean
      default: false
      @doc "Compact spacing"
    }
    nonInteractive: {
      type: boolean
      default: false
      @doc "List items are not interactive"
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "List item children"
    }
  }
  
  a11y: {
    role: "list"
  }
}

@component mdc-list-item {
  @doc "Material Design list item"
  @controlled false
  @tag-react MDCListItem
  
  props: {
    selected: {
      type: boolean
      default: false
    }
    disabled: {
      type: boolean
      default: false
    }
    href: {
      type: string
      @doc "Makes item a link"
    }
    leadingIcon: {
      type: @type(IconName)
    }
    trailingIcon: {
      type: @type(IconName)
    }
  }
  
  slots: {
    default: {
      required: true
      type: node
      @doc "Primary text content"
    }
    supportingText: {
      required: false
      type: text
      @doc "Secondary/supporting text"
    }
    overline: {
      required: false
      type: text
      @doc "Overline text (three-line variant)"
    }
    leading: {
      required: false
      type: node
      @doc "Leading content (icon/avatar)"
    }
    trailing: {
      required: false
      type: node
      @doc "Trailing content (icon/meta)"
    }
  }
  
  events: {
    click: { native: true }
  }
  
  constraints: {
    @rule "supportingText requires two-line or three-line parent"
    @rule "overline requires three-line parent"
  }
}

# ============================================================================
# PATTERNS
# ============================================================================

@patterns {
  @pattern form-field {
    @doc "Standard Material form field structure"
    
    structure: [label, field!, helper?, error?]
    
    components: {
      label: "mdc-text-field[label] or separate label"
      field: "mdc-text-field | mdc-select | mdc-textarea"
      helper: "Helper text component"
      error: "Error text component (replaces helper)"
    }
    
    constraints: {
      @rule "error replaces helper when present"
      @rule "required shows * indicator in label"
    }
  }
  
  @pattern button-group {
    @doc "Material button group for dialogs/forms"
    
    structure: [text?, filled!]
    
    constraints: {
      @rule "Filled button last (right)"
      @rule "Maximum one filled button"
      @rule "Maximum 3 buttons total"
    }
    
    implementation: |
      <div className="mdc-dialog__actions">
        <MDCButton variant="text">Cancel</MDCButton>
        <MDCButton variant="filled">Confirm</MDCButton>
      </div>
  }
  
  @pattern dialog-confirmation {
    @doc "Material confirmation dialog pattern"
    
    structure: [header!, content!, actions!]
    
    components: {
      header: "Dialog title (h2)"
      content: "Confirmation message"
      actions: "@pattern(button-group)"
    }
    
    constraints: {
      @rule "Cancel (text) + Confirm (filled) actions"
      @rule "Header must be present"
    }
  }
  
  @pattern search-bar {
    @doc "Material search bar pattern"
    
    structure: [text-field!]
    
    components: {
      "text-field": "mdc-text-field[variant:filled, leadingIcon:search, trailingIcon:clear]"
    }
    
    constraints: {
      @rule "Search icon required as leadingIcon"
      @rule "Clear icon shown only when value present"
    }
  }
  
  @pattern filter-chips {
    @doc "Filter chip group pattern"
    
    structure: [chip+, chip+]
    
    components: {
      chips: "mdc-chip[variant:filter]"
    }
    
    constraints: {
      @rule "Multiple chips can be selected"
      @rule "At least one chip required"
    }
  }
}

# ============================================================================
# SEMANTICS
# ============================================================================

@semantics {
  @intent "user triggers primary action" {
    @alias "button click", "cta", "primary action"
    
    conditions: {
      "primary action": {
        component: "mdc-button[variant:filled]"
        reason: "Filled button for primary actions"
      }
      "secondary action": {
        component: "mdc-button[variant:text]"
        reason: "Text button for secondary actions"
      }
      "medium emphasis": {
        component: "mdc-button[variant:outlined]"
        reason: "Outlined for medium emphasis"
      }
      "navigation to URL": {
        component: "mdc-button[href]"
        reason: "Use href prop for navigation"
      }
    }
  }
  
  @intent "user enters text" {
    conditions: {
      "single line, with background": {
        component: "mdc-text-field[variant:filled]"
        reason: "Filled variant for forms"
      }
      "single line, outlined": {
        component: "mdc-text-field[variant:outlined]"
        reason: "Outlined variant alternative"
      }
      "email input": {
        component: "mdc-text-field[type:email]"
      }
      "password input": {
        component: "mdc-text-field[type:password, trailingIcon:visibility]"
      }
      "search input": {
        component: "mdc-text-field[type:search, leadingIcon:search]"
      }
    }
  }
  
  @intent "user selects one from options" {
    conditions: {
      "≤ 5 options, vertical": {
        component: "mdc-radio-group"
        reason: "Radio group for small option sets"
      }
      "> 5 options, or space constrained": {
        component: "mdc-select"
        reason: "Select dropdown for many options"
      }
      "binary immediate toggle": {
        component: "mdc-switch"
        reason: "Switch for immediate effect toggles"
      }
      "binary form submission": {
        component: "mdc-checkbox"
        reason: "Checkbox for form submissions"
      }
    }
  }
  
  @intent "user selects multiple from options" {
    conditions: {
      "small set (≤ 5)": {
        component: "multiple mdc-checkbox"
        reason: "Multiple checkboxes for small sets"
      }
      "many options": {
        component: "mdc-select[multiple]"
        reason: "Multi-select for many options"
      }
      "tags/chips": {
        component: "mdc-chip[variant:filter]"
        reason: "Filter chips for tag selection"
      }
    }
  }
  
  @intent "system shows notification" {
    conditions: {
      "temporary, non-critical": {
        component: "mdc-snackbar"
        reason: "Snackbar for temporary notifications"
      }
      "important, needs action": {
        component: "mdc-dialog"
        reason: "Dialog for important messages"
      }
      "mobile, bottom sheet": {
        component: "mdc-bottom-sheet"
        reason: "Bottom sheet for mobile interactions"
      }
    }
  }
  
  @intent "user navigates menu/list" {
    conditions: {
      "mobile drawer": {
        component: "mdc-bottom-sheet or mdc-drawer"
      }
      "simple list": {
        component: "mdc-list"
      }
      "navigation menu": {
        component: "mdc-list with mdc-list-item[href]"
      }
    }
  }
}

# ============================================================================
# A11Y: Accessibility Guidelines
# ============================================================================

@a11y {
  requirements: {
    focus: [
      "All interactive elements focusable",
      "Visible focus indicators (focus ring)",
      "Logical tab order",
      "Focus trap in dialogs"
    ]
    contrast: [
      "Text: minimum 4.5:1 (WCAG AA)",
      "Large text: minimum 3:1",
      "UI components: minimum 3:1"
    ]
    keyboard: [
      "All functions accessible via keyboard",
      "Enter/Space for buttons and controls",
      "Arrow keys for radio groups and lists",
      "ESC closes dialogs and sheets",
      "Tab navigation logical"
    ]
    screen-readers: [
      "Proper ARIA roles",
      "aria-label for icon-only buttons",
      "aria-describedby for help text",
      "aria-invalid for errors",
      "Live regions for dynamic content"
    ]
  }
  
  components: {
    "mdc-button": {
      keyboard: ["Enter/Space: activate", "Tab: focus"]
      aria: "button role, aria-label for icon-only"
    }
    
    "mdc-text-field": {
      aria: "textbox role, aria-label from label, aria-describedby from helper/error"
      announcements: "Error messages announced when present"
    }
    
    "mdc-dialog": {
      focus: "Trap focus within dialog, return to trigger on close"
      keyboard: ["ESC: close", "Tab: navigate within dialog"]
      aria: "dialog role, aria-labelledby on header, aria-modal"
    }
    
    "mdc-snackbar": {
      aria-live: "polite"
      role: "status"
      announcements: "Message announced when shown"
    }
  }
}

# ============================================================================
# ANIMATION: Motion Guidelines
# ============================================================================

@animation {
  tokens: {
    duration: {
      short: "200ms"
      medium: "300ms"
      long: "400ms"
    }
    easing: {
      standard: "cubic-bezier(0.2, 0, 0, 1)"
      emphasized: "cubic-bezier(0.2, 0, 0, 1)"
      decelerated: "cubic-bezier(0, 0, 0.2, 1)"
    }
  }
  
  reduced-motion: {
    @doc "Respects prefers-reduced-motion"
    behavior: [
      "Disable decorative animations",
      "Shorten functional transitions",
      "Keep loading animations"
    ]
  }
  
  components: {
    "mdc-dialog": {
      animations: {
        backdrop: { property: "opacity", duration: "medium" }
        content: { property: "transform, opacity", duration: "medium" }
      }
    }
    
    "mdc-bottom-sheet": {
      animations: {
        slide: { property: "transform", duration: "medium" }
        backdrop: { property: "opacity", duration: "medium" }
      }
    }
    
    "mdc-snackbar": {
      animations: {
        enter: { property: "transform, opacity", duration: "short" }
        exit: { property: "transform, opacity", duration: "short" }
      }
    }
  }
  
  guidelines: [
    "Use standard easing for most transitions",
    "Duration 200-400ms for responsiveness",
    "Respect prefers-reduced-motion",
    "Use transform and opacity for performance"
  ]
}

---

## Compact Format

```
#DSIL:1.0 material-design v3.0.0

## Meta
prefix[html:mdc-|react:MDC]
import.react: "@material/react-components"
config[strict|theme:light]

## Tokens
T.theme[light*|dark]
T.spacing[0|4|8|12|16|24|32|48|64]px
T.color.primary[primary|on-primary|primary-container|on-primary-container]
T.color.error[error|on-error|error-container|on-error-container]
T.typography.scale[display-large|headline-large|title-medium*|body-medium|label-large]
T.elevation[level0|level1*|level2|level3|level4|level5]
T.shape.corner[ none|xs:4px|sm:8px|md:12px|lg:16px|xl:28px|full:9999px]
T.motion.duration[short1:50ms|short2:200ms|medium:300ms|long:400ms]
T.breakpoint[mobile:0|tablet:600|desktop:840|wide:1200]px

## Icons
I.nav: arrow_*, chevron_*, menu, close, home, search
I.action: add, edit, delete, save, done, favorite, star, settings
I.communication: email, phone, chat, notification
I.status: check_circle, error, warning, info

## Components
C.mdc-button: v[filled*|outlined|text|elevated|tonal] p[disabled?:bool,icon?,trailingIcon?,href?,density?] s[default!:text] e[click] !trailingIcon→icon|content

C.mdc-text-field: v[filled*|outlined] p[label!:str,value?:str,type?:str=text,disabled?:bool,required?:bool,helperText?:str,errorText?:str,leadingIcon?:Icon,trailingIcon?:Icon] s[default?:node] e[input,change] !errorText→-helperText

C.mdc-card: v[elevated*|filled|outlined] p[elevation?:Elevation=level1,href?,disabled?:bool] s[media?,header?,default!:node,actions?] !elevation→elevated

C.mdc-dialog: @controlled v[] p[open!:bool,fullscreen?:bool,maxWidth?:str=sm,persistent?:bool] s[header?,default!:node,actions?] e[close(action)] !close→required

C.mdc-checkbox: p[checked?:bool,indeterminate?:bool,disabled?:bool,required?:bool,value?:str,name?:str] s[default?:node] e[change(checked,value)] !indeterminate→checked=false

C.mdc-switch: p[checked?:bool,disabled?:bool,value?:str,name?:str] s[default?:node] e[change(checked)]

C.mdc-radio: p[checked?:bool,value!:str,name!:str,disabled?:bool] s[default?:node] e[change(value,checked)] !same-name-group

C.mdc-radio-group: @controlled p[value?:str,name!:str,required?:bool] s[default!:node] e[change(value)] !one-selected

C.mdc-chip: v[assist*|filter|input|suggestion] p[selected?:bool,icon?,trailingIcon?,href?] s[default!:text] e[click,remove] !selected→filter !trailingIcon→input

C.mdc-snackbar: @controlled p[open!:bool,message!:str,actionLabel?:str,timeout?:num=4000] s[action?:node] e[close(reason),action] !close→required

## Patterns
P.form-field: [label,field!,helper?,error?] !error→-helper
P.button-group: [text?,filled!] !max-1-filled !max-3-total
P.dialog-confirmation: [header!,content!,actions!]

## Semantics
S."trigger action": primary→filled | secondary→text | nav→href
S."enter text": filled→variant:filled | outlined→variant:outlined | email→type:email | search→leadingIcon:search
S."select one": ≤5→radio-group | >5→select | immediate→switch | form→checkbox
S."notification": temporary→snackbar | important→dialog | mobile→bottom-sheet
```

---

## Usage with LLMs

When using this Material Design DSIL with LLMs, include the Compact Format in your system prompt:

```
You are a frontend developer using Material Design 3 components.

DESIGN SYSTEM:
[Paste Compact Format above]

RULES:
1. Only use components defined in the DSIL
2. Respect all constraints (marked with !)
3. Use filled buttons for primary actions
4. Use text buttons for secondary actions
5. Dialogs require controlled state management
6. Follow Material Design patterns
```

---

*Material Design 3 DSIL Example v1.0*  
*Based on Google Material Design 3 (Material You)*  
*For official Material Design documentation, visit: https://m3.material.io/*
