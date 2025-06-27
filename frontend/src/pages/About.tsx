import React from "react";
import Sidebar from "../components/Sidebar";

const About: React.FC = () => (
  <div className="about-screen">
    <Sidebar />
    <main>
      <h2>About SignalForge</h2>
      <p>
        SignalForge is the world’s most advanced AI-powered trading and signal automation platform. 
        <br /><br />
        Built with love by traders and engineers, it delivers professional trading tools, security, and 
        deep analytics to both beginners and pros. 
        <br /><br />
        All major integrations, bot upgrades, and performance/security modes included. 
      </p>
    </main>
  </div>
);

export default About;
