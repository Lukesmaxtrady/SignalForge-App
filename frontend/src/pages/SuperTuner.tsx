import React from "react";
import Sidebar from "../components/Sidebar";
import SuperTunerPanel from "../components/SuperTunerPanel";
import EdgeMeter from "../components/PerformanceGraph";
import BudgetControlPanel from "../components/BudgetControlPanel";

const SuperTuner: React.FC = () => (
  <div className="super-tuner-screen">
    <Sidebar />
    <main>
      <h2>SuperTuner – Advanced Bot Control</h2>
      <SuperTunerPanel />
      <EdgeMeter />
      <BudgetControlPanel />
    </main>
  </div>
);

export default SuperTuner;
