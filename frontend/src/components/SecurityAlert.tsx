import React from "react";

export interface SecurityAlertProps {
  message: string;
  type?: "info" | "warning" | "danger";
}

const typeColors = {
  info: "#3b82f6",
  warning: "#fbbf24",
  danger: "#ef4444"
};

const SecurityAlert: React.FC<SecurityAlertProps> = ({ message, type = "info" }) => (
  <div style={{
    padding: "0.75rem 1.5rem",
    background: typeColors[type],
    color: "#fff",
    borderRadius: "6px",
    margin: "1rem 0",
    fontWeight: 600,
    textAlign: "center"
  }}>
    🛡️ {message}
  </div>
);

export default SecurityAlert;
