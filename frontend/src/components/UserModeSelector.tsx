import React from "react";

const modes = [
  "Beginner",
  "Pro",
  "Quant",
  "High Security",
  "Ultra Performance",
  "Super Tuner",
  "Extreme",
  "Custom"
];

const UserModeSelector: React.FC = () => (
  <div className="user-mode-selector">
    <label htmlFor="mode-select">User Mode:</label>
    <select id="mode-select">
      {modes.map((mode) => (
        <option key={mode} value={mode.toLowerCase()}>
          {mode}
        </option>
      ))}
    </select>
  </div>
);

export default UserModeSelector;
