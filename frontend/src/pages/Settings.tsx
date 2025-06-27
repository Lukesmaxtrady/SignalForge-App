import React from "react";
import Sidebar from "../components/Sidebar";
import ThemeSwitcher from "../components/ThemeSwitcher";
import NotificationBar from "../components/NotificationBar";
import BudgetControlPanel from "../components/BudgetControlPanel";

const Settings: React.FC = () => (
  <div className="settings-screen">
    <Sidebar />
    <main>
      <h2>Settings</h2>
      <ThemeSwitcher />
      <NotificationBar />
      <BudgetControlPanel />
      {/* Add language, region, integrations, and more as needed */}
    </main>
  </div>
);

export default Settings;
