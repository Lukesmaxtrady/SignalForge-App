import React from "react";

const BudgetControlPanel: React.FC = () => (
  <section className="budget-control-panel">
    <h3>Budget Controls</h3>
    <div>
      <label>
        <span>Max daily spend</span>
        <input type="number" min={0} step={1} defaultValue={100} /> USD
      </label>
    </div>
    <div>
      <label>
        <span>Paid features on/off</span>
        <input type="checkbox" />
      </label>
    </div>
  </section>
);

export default BudgetControlPanel;
