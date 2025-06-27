import React from "react";

const themes = [
  "Default",
  "Space",
  "Gold",
  "Diamond",
  "Cyberpunk",
  "Titanium",
  "Business",
  "Robot",
  "Cartoon"
];

const ThemeSwitcher: React.FC = () => (
  <div className="theme-switcher">
    <label htmlFor="theme-select">Theme:</label>
    <select id="theme-select">
      {themes.map((theme) => (
        <option key={theme} value={theme.toLowerCase()}>
          {theme}
        </option>
      ))}
    </select>
  </div>
);

export default ThemeSwitcher;
