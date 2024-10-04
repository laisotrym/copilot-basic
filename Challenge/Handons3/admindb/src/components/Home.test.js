import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import axios from 'axios';
import Home from './Home';

jest.mock('axios');

describe('Home Component', () => {
    test('renders welcome message', () => {
        render(<Home />);
        const welcomeMessage = screen.getByText(/Welcome to the Admin Dashboard/i);
        expect(welcomeMessage).toBeInTheDocument();
    });

    test('renders table headers', () => {
        render(<Home />);
        const headers = ['Full Name', 'Username', 'Phone', 'Email', 'Age'];
        headers.forEach(header => {
            expect(screen.getByText(header)).toBeInTheDocument();
        });
    });

    test('fetches and displays users', async () => {
        const users = [
            { id: 1, firstname: 'John', lastname: 'Doe', username: 'johndoe', phone: '1234567890', email: 'john@example.com', age: 30 },
            { id: 2, firstname: 'Jane', lastname: 'Doe', username: 'janedoe', phone: '0987654321', email: 'jane@example.com', age: 25 }
        ];

        axios.get.mockResolvedValue({ data: users });

        render(<Home />);

        await waitFor(() => {
            users.forEach(user => {
                expect(screen.getByText(`${user.firstname} ${user.lastname}`)).toBeInTheDocument();
                expect(screen.getByText(user.username)).toBeInTheDocument();
                expect(screen.getByText(user.phone)).toBeInTheDocument();
                expect(screen.getByText(user.email)).toBeInTheDocument();
                expect(screen.getByText(user.age.toString())).toBeInTheDocument();
            });
        });
    });

    test('handles fetch error', async () => {
        axios.get.mockRejectedValue(new Error('Error fetching data'));

        render(<Home />);

        await waitFor(() => {
            expect(screen.queryByText(/John Doe/i)).not.toBeInTheDocument();
        });
    });
});