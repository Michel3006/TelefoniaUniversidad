import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "./lib/query-client";
import { AuthProvider } from "./lib/auth-context";
import { ToastProvider } from "./components/ui/Toast";
import { AppRouter } from "./app/router";
// Fuentes autoalojadas (M4): sin requests externos a fonts.googleapis.com.
import "@fontsource/open-sans/400.css";
import "@fontsource/open-sans/500.css";
import "@fontsource/open-sans/600.css";
import "@fontsource/open-sans/700.css";
import "@fontsource/ibm-plex-mono/400.css";
import "@fontsource/ibm-plex-mono/500.css";
import "@fontsource/ibm-plex-mono/600.css";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <ToastProvider>
        <AuthProvider>
          <AppRouter />
        </AuthProvider>
      </ToastProvider>
    </QueryClientProvider>
  </React.StrictMode>
);
