import React from "react";
import Sidebar from "../components/Sidebar";
import PerformanceGraph from "../components/PerformanceGraph";
import DashboardCard from "../components/DashboardCard";

const Analytics: React.FC = () => (
  <div className="analytics-screen" style={{ display: "flex", minHeight: "100vh" }}>
    <Sidebar />
    <main style={{ flex: 1, padding: "2rem", background: "#f5f6fa" }}>
      <h2 style={{ marginBottom: "2rem" }}>Analytics & Performance</h2>
      <PerformanceGraph />
      <DashboardCard />
      {/* Insert more detailed analytics components as needed */}
    </main>
  </div>
);

export default Analytics;
