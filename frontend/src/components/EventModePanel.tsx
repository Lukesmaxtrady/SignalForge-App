import React from "react";

const EventModePanel: React.FC = () => (
  <section className="event-mode-panel">
    <h3>Event Mode</h3>
    <p>
      Enable high alert and defensive strategies during high-volatility events (CPI, FOMC, etc).
    </p>
    <button>Activate Event Mode</button>
  </section>
);

export default EventModePanel;
