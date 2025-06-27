import React from "react";
import Sidebar from "../components/Sidebar";
import DashboardCard from "../components/DashboardCard";
import BotStatusPanel from "../components/BotStatusPanel";
import PerformanceGraph from "../components/PerformanceGraph";
import SecurityAlert from "../components/SecurityAlert";

const Dashboard: React.FC = () => (
  <div className="dashboard-screen">
    <Sidebar />
    <main>
      <h2>Trading Dashboard</h2>
      <DashboardCard />
      <PerformanceGraph />
      <BotStatusPanel
        name="AlphaTrader"
        status="Active"
        mode="Ultra Performance"
        profit={1423.77}
      />
      {/* Render multiple BotStatusPanel as needed */}
      <SecurityAlert message="No current threats detected." />
    </main>
  </div>
);

export default Dashboard;
