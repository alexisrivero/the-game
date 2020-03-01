import React from 'react';
import { render, waitForElement, findByRole } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';

import * as Constants from '../Constants';
import FooterPublicidad from './FooterPublicidad';

describe('<FooterPublicidad />', () => {
    it('renderea un elemento mientras carga', () => {
        const {getByText, getByRole} = render(<FooterPublicidad />);
        expect(getByText('Estamos cargando la publicidad...')).toBeTruthy();
    });
    it('renderea una publicidad si carga bien', async () => {
        const {findByRole} = render(<FooterPublicidad />);
        const publicidad = await findByRole('publicidad');
        expect(publicidad.children.length).toBe(1);
    });
    it('muestra un error si la API de publicidad no esta disponible', async () => {
        const {findByRole} = render(<FooterPublicidad API_Url='https://qwdqdw.net.ar/publicidad.jswadwadon'/>)
        const elementoError = await findByRole('error-message');
        expect(elementoError).toHaveTextContent('Error: no se pudo contactar la API de publicidad');
    });
});
