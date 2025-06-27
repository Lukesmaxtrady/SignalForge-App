import React, { useContext } from "react";
import styled, { keyframes } from "styled-components";
import { NotificationContext } from "../App";

const slideDown = keyframes`
  from { transform: translateY(-100%); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
`;

const Bar = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9999;
  background: ${({ theme }) => theme.colors.primary};
  color: ${({ theme }) => theme.colors.textOnPrimary || "#fff"};
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 500;
  animation: ${slideDown} 0.25s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
`;

const Dismiss = styled.button`
  background: none;
  border: none;
  color: inherit;
  font-size: 1.3rem;
  cursor: pointer;
  margin-left: 1rem;
  opacity: 0.8;
  transition: opacity 0.15s;
  &:hover {
    opacity: 1;
  }
`;

const NotificationBar: React.FC = () => {
  const { message, setMessage } = useContext(NotificationContext);

  if (!message) return null;

  return (
    <Bar>
      {message}
      <Dismiss aria-label="Dismiss" onClick={() => setMessage(null)}>
        &times;
      </Dismiss>
    </Bar>
  );
};

export default NotificationBar;
