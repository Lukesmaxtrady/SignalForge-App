import { render, screen } from '@testing-library/react';
import BotControl from '../pages/BotControl';

describe('Bot Control Page', () => {
  it('shows bot management UI', () => {
    render(<BotControl />);
    expect(screen.getByText(/manage bots/i)).toBeInTheDocument();
  });
});
