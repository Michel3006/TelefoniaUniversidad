/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        tinta: "#0E2E27",
        papel: { DEFAULT: "#F3F5F1", alto: "#FFFFFF" },
        senal: "#1F8F5F",
        "cujae-verde": "#0F7A57",
        "cujae-verde-oscuro": "#0A523D",
        "cujae-verde-claro": "#DDEEE7",
        "cujae-dorado": "#D4A84A",
        "linea-ok": "#3C8768",
        "linea-baja": "#B8483D",
        neutro: "#64706B",
        filete: "#D8DAD4",
      },
      fontFamily: {
        sans: ["Archivo", "system-ui", "sans-serif"],
        mono: ['"IBM Plex Mono"', "ui-monospace", "monospace"],
      },
      borderRadius: { DEFAULT: "4px" },
      boxShadow: { cujae: "0 16px 38px rgba(10, 82, 61, 0.18)" },
    },
  },
  plugins: [],
};
