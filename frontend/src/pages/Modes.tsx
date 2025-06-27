import React from "react";
import Sidebar from "../components/Sidebar";
import UserModeSelector from "../components/UserModeSelector";
import BotPerformanceSelector from "../components/BotPerformanceSelector";
import SecurityModeSelector from "../components/SecurityModeSelector";

const Modes: React.FC = () => (
  <div className="modes-screen">
    <Sidebar />
    <main>
      <h2>User, Bot, and Security Modes</h2>
      <UserModeSelector />
      <BotPerformanceSelector />
      <SecurityModeSelector />
    </main>
  </div>
);

export default Modes;
