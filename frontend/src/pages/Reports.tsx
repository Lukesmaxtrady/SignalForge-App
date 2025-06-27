import React from "react";
import Sidebar from "../components/Sidebar";
import DashboardCard from "../components/DashboardCard";
import PerformanceGraph from "../components/PerformanceGraph";

const Reports: React.FC = () => (
  <div className="reports-screen">
    <Sidebar />
    <main>
      <h2>Reports & Exports</h2>
      <DashboardCard />
      <PerformanceGraph />
      {/* Insert export/download/report controls here */}
      <button>Export as PDF</button>
      <button>Export as CSV</button>
    </main>
  </div>
);

export default Reports;
