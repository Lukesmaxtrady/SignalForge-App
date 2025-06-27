import React, { useState, useMemo } from "react";
import { ThemeProvider } from "styled-components";
import { themes } from "./themes/themeLoader";
import GlobalStyle from "./themes/GlobalStyle";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import NotificationBar from "./components/NotificationBar";
import SignalOverlay from "./components/SignalOverlay";

// DO NOT import './main.css' here. Import global CSS in pages/_app.tsx only.

// Notification Context for global notifications
export const NotificationContext = React.createContext<{
  message: string | null;
  setMessage: (msg: string | null) => void;
}>({
  message: null,
  setMessage: () => {},
});

const App: React.FC = () => {
  const [notification, setNotification] = useState<string | null>(null);

  // Theme mode: 'dark' or 'light'
  const [themeMode, setThemeMode] = useState<'dark' | 'light'>('dark');
  const currentTheme = useMemo(() => themes[themeMode], [themeMode]);

  // Optional: Add theme toggle button
  const toggleTheme = () => setThemeMode((prev) => (prev === 'dark' ? 'light' : 'dark'));

  return (
    <ThemeProvider theme={currentTheme}>
      <GlobalStyle />
      <NotificationContext.Provider value={{ message: notification, setMessage: setNotification }}>
        <button
          onClick={toggleTheme}
          style={{
            position: "absolute",
            top: 12,
            right: 24,
            zIndex: 9999,
            padding: "0.5rem 1rem",
            borderRadius: "8px",
            background: currentTheme.colors.primary,
            color: currentTheme.colors.textOnPrimary,
            border: "none",
            cursor: "pointer"
          }}
        >
          Switch to {themeMode === "dark" ? "Light" : "Dark"} Mode
        </button>
        <Navbar />
        <Sidebar />
        <NotificationBar />
        <SignalOverlay />
        {/* Add other content/routes/components here */}
      </NotificationContext.Provider>
    </ThemeProvider>
  );
};

export default App;
