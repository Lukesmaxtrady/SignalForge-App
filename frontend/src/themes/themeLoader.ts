import { createGlobalStyle, DefaultTheme } from "styled-components";

export const lightTheme: DefaultTheme = {
  colors: {
    primary: "#0070f3",
    background: "#fafbfc",
    panel: "#ffffff",
    sidebar: "#f1f5f9",
    text: "#111827",
    textSecondary: "#6b7280",
    textOnPrimary: "#fff",
    notification: "#fbbf24",
    danger: '#ef4444',
    warning: '#f59e42',
    success: '#22c55e',
    info: '#3b82f6',
  },
  borderRadius: "10px",
  fontFamily: "Inter, Arial, sans-serif",
};

export const darkTheme: DefaultTheme = {
  colors: {
    primary: "#06b6d4",
    background: "#18181b",
    panel: "#23272f",
    sidebar: "#20232a",
    text: "#f3f4f6",
    textSecondary: "#a1a1aa",
    textOnPrimary: "#18181b",
    notification: "#f59e42",
    danger: '#ef4444',
    warning: '#f59e42',
    success: '#22c55e',
    info: '#3b82f6',
  },
  borderRadius: "10px",
  fontFamily: "Inter, Arial, sans-serif",
};

export const themes = {
  light: lightTheme,
  dark: darkTheme,
};
