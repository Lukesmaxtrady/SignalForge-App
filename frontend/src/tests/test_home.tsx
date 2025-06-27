import { render, screen } from '@testing-library/react';
import Home from '../pages/Home';

describe('Home Page', () => {
  it('renders welcome text', () => {
    render(<Home />);
    expect(screen.getByText(/welcome/i)).toBeInTheDocument();
  });
});
