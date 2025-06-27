import React from "react";

const RiskPanel: React.FC = () => (
  <section className="risk-panel">
    <h3>Risk Control</h3>
    <ul>
      <li>Kill switch</li>
      <li>Drawdown limit</li>
      <li>Bot capital controls</li>
      <li>Scam/hack alert settings</li>
    </ul>
    {/* Add more dynamic risk controls as needed */}
  </section>
);

export default RiskPanel;
