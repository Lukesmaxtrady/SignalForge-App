import { render, screen } from '@testing-library/react';
import PaidFeatures from '../pages/PaidFeatures';

describe('Paid Features Page', () => {
  it('shows paid feature toggles', () => {
    render(<PaidFeatures />);
    expect(screen.getByText(/paid features/i)).toBeInTheDocument();
    expect(screen.getByRole('checkbox')).toBeInTheDocument();
  });
});
