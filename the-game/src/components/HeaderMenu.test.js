import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import HeaderMenu from './HeaderMenu';

describe('HeaderMenu />', () => {
    it('renderea un elemento mientras carga', () => {
        const { getByText } = render(<HeaderMenu />);
        expect(getByText('Estamos cargando broder')).toBeTruthy();
    });
    it('renderea un menu si carga bien', async () => {
        const { findByRole } = render(<HeaderMenu />);
        const menu = await findByRole('menu');
        expect(menu.children.length).toBe(256);
    });
    it('muestra un error si carga mal', async () => {
        const { findByRole } = render(<HeaderMenu url_api="https://eoqfoqef.com/asds.json" />);
        const elementoError = await findByRole('error-message');
        expect(elementoError).toHaveTextContent('error broder');
    });
});