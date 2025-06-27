import React from "react";

const OnboardingGuide: React.FC = () => (
  <section className="onboarding-guide">
    <h3>Welcome to SignalForge!</h3>
    <ol>
      <li>Create or link your trading accounts.</li>
      <li>Pick a mode (Beginner, Pro, Quant, etc).</li>
      <li>Toggle security and paid features as needed.</li>
      <li>Let your first bot run—review performance and analytics.</li>
      <li>Check the dashboard for alerts and next steps.</li>
    </ol>
  </section>
);

export default OnboardingGuide;
