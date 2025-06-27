import { render, screen } from '@testing-library/react';
import Dashboard from '../pages/Dashboard';

describe('Dashboard Page', () => {
  it('shows portfolio and signals', () => {
    render(<Dashboard />);
    expect(screen.getByText(/portfolio/i)).toBeInTheDocument();
    expect(screen.getByText(/signals/i)).toBeInTheDocument();
  });
});
