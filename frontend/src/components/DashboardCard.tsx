import React from "react";

type DashboardCardProps = {
  title?: string;
  value?: string | number;
  icon?: React.ReactNode;
  description?: string;
};

const DashboardCard: React.FC<DashboardCardProps> = ({
  title = "Balance",
  value = "$0.00",
  icon,
  description = "",
}) => (
  <div className="dashboard-card">
    {icon && <span className="dashboard-icon">{icon}</span>}
    <h3>{title}</h3>
    <p className="dashboard-value">{value}</p>
    <span className="dashboard-desc">{description}</span>
  </div>
);

export default DashboardCard;
