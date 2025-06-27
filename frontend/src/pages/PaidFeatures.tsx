import React from "react";
import Sidebar from "../components/Sidebar";
import PaidFeatureToggle from "../components/PaidFeatureToggle";
import BudgetControlPanel from "../components/BudgetControlPanel";

const PaidFeatures: React.FC = () => (
  <div className="paid-features-screen">
    <Sidebar />
    <main>
      <h2>Premium Features & Toggles</h2>
      <PaidFeatureToggle feature="Ultra Performance Mode" enabled={false} onToggle={() => {}} />
      <PaidFeatureToggle feature="High Security Mode" enabled={false} onToggle={() => {}} />
      <PaidFeatureToggle feature="Advanced Analytics" enabled={true} onToggle={() => {}} />
      <PaidFeatureToggle feature="Custom Voice Alerts" enabled={true} onToggle={() => {}} />
      <BudgetControlPanel />
      {/* Add more toggles as new paid features are introduced */}
    </main>
  </div>
);

export default PaidFeatures;
