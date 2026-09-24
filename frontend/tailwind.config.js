/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        tinta: "#1C1F1D",
        papel: { DEFAULT: "#F2F2F2", alto: "#FFFFFF" },
        senal: "#006633",
        "verde": "#006E53",
        "verde-suave": "#E8F2EC",
        aviso: "#C98A1B",
        "linea-ok": "#006E53",
        "linea-baja": "#B8483D",
        neutro: "#8B8F87",
        filete: "#D8DAD4",
      },
      fontFamily: {
        sans: ["Open Sans", "system-ui", "sans-serif"],
        mono: ['"IBM Plex Mono"', "ui-monospace", "monospace"],
      },
      borderRadius: {
        DEFAULT: "4px",
      },
    },
  },
  plugins: [],
};