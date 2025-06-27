import React from "react";
import Sidebar from "../components/Sidebar";
import BotStatusPanel from "../components/BotStatusPanel";
import EventModePanel from "../components/EventModePanel";
import UserModeSelector from "../components/UserModeSelector";
import PaidFeatureToggle from "../components/PaidFeatureToggle";

const BotControl: React.FC = () => (
  <div className="bot-control-screen">
    <Sidebar />
    <main>
      <h2>Bot Control Center</h2>
      <UserModeSelector />
      <EventModePanel />
      <BotStatusPanel
        name="ML Signal Bot"
        status="Running"
        mode="Extreme"
        profit={921.42}
      />
      <PaidFeatureToggle
        feature="Ultra Bot Performance"
        enabled={true}
        onToggle={() => {}}
      />
    </main>
  </div>
);

export default BotControl;
