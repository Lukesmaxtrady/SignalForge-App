import React from "react";
import Navbar from "../components/Navbar";
import DashboardCard from "../components/DashboardCard";
import SignalOverlay from "../components/SignalOverlay";
import OnboardingGuide from "../components/OnboardingGuide";

const Home: React.FC = () => (
  <div className="home-screen">
    <Navbar />
    <main>
      <h1>Welcome to SignalForge</h1>
      <DashboardCard />
      <SignalOverlay />
      <OnboardingGuide />
    </main>
  </div>
);

export default Home;
