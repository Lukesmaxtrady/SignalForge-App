import React from "react";
import Link from "next/link";

const Sidebar: React.FC = () => (
  <aside>
    <ul>
      <li><Link href="/">Home</Link></li>
      <li><Link href="/dashboard">Dashboard</Link></li>
      <li><Link href="/bots">Bots</Link></li>
      <li><Link href="/analytics">Analytics</Link></li>
      <li><Link href="/security">Security</Link></li>
      <li><Link href="/paid-features">Premium</Link></li>
      <li><Link href="/super-tuner">SuperTuner</Link></li>
      <li><Link href="/modes">Modes</Link></li>
      <li><Link href="/settings">Settings</Link></li>
      <li><Link href="/reports">Reports</Link></li>
      <li><Link href="/about">About</Link></li>
    </ul>
  </aside>
);

export default Sidebar;
