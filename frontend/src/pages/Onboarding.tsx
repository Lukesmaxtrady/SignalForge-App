import React from "react";
import OnboardingGuide from "../components/OnboardingGuide";
import Sidebar from "../components/Sidebar";

const Onboarding: React.FC = () => (
  <div className="onboarding-screen">
    <Sidebar />
    <main>
      <h2>Getting Started</h2>
      <OnboardingGuide />
    </main>
  </div>
);

export default Onboarding;
