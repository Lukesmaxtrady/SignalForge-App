import React from "react";
import Sidebar from "../components/Sidebar";
import SecurityAlert from "../components/SecurityAlert";
import SecurityModeSelector from "../components/SecurityModeSelector";
import ScamAlertBar from "../components/ScamAlertBar";
import HackAlertBar from "../components/HackAlertBar";

const Security: React.FC = () => (
  <div className="security-screen">
    <Sidebar />
    <main>
      <h2>Security & Scam/Hack Protection</h2>
      <SecurityModeSelector />
      <SecurityAlert message="Ultra security enabled. All bot actions monitored." type="warning" />
      <ScamAlertBar />
      <HackAlertBar />
    </main>
  </div>
);

export default Security;
