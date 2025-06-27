import React from "react";

interface BotStatusPanelProps {
  name: string;
  status: string;
  mode: string;
  profit: number;
}

const BotStatusPanel: React.FC<BotStatusPanelProps> = ({ name, status, mode, profit }) => (
  <div className="bot-status-panel">
    <h4>{name}</h4>
    <p>Status: {status}</p>
    <p>Mode: {mode}</p>
    <p>Profit: ${profit.toFixed(2)}</p>
  </div>
);

export default BotStatusPanel;
