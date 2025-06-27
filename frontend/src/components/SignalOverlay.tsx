import React from "react";
import { FaArrowUp, FaArrowDown, FaExclamationTriangle } from "react-icons/fa";

type SignalType = "BUY" | "SELL" | "ALERT";

interface SignalOverlayProps {
  type?: SignalType;
  message?: string;
  show?: boolean;
}

const SignalOverlay: React.FC<SignalOverlayProps> = ({
  type = "ALERT",
  message = "No signal",
  show = false,
}) =>
  show ? (
    <div className={`signal-overlay signal-${type.toLowerCase()}`}>
      {type === "BUY" && <FaArrowUp color="#00e676" size={40} />}
      {type === "SELL" && <FaArrowDown color="#ff1744" size={40} />}
      {type === "ALERT" && <FaExclamationTriangle color="#ffd600" size={36} />}
      <span>{message}</span>
    </div>
  ) : null;

export default SignalOverlay;
