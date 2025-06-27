import React from "react";

interface PaidFeatureToggleProps {
  feature: string;
  enabled: boolean;
  onToggle: (val: boolean) => void;
}

const PaidFeatureToggle: React.FC<PaidFeatureToggleProps> = ({ feature, enabled, onToggle }) => (
  <div className="paid-feature-toggle">
    <span>{feature}</span>
    <input
      type="checkbox"
      checked={enabled}
      onChange={(e) => onToggle(e.target.checked)}
    />
  </div>
);

export default PaidFeatureToggle;
