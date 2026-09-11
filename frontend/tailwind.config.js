/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        tinta: "#1C1F1D",
        papel: { DEFAULT: "#EFF1ED", alto: "#FFFFFF" },
        senal: "#E1922E",
        "linea-ok": "#3C8768",
        "linea-baja": "#B8483D",
        neutro: "#8B8F87",
        filete: "#D8DAD4",
      },
      fontFamily: {
        sans: ["Archivo", "system-ui", "sans-serif"],
        mono: ['"IBM Plex Mono"', "ui-monospace", "monospace"],
      },
      borderRadius: {
        DEFAULT: "4px",
      },
    },
  },
  plugins: [],
};
