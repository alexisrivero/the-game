import React from 'react';
import { render, waitForElement, findByRole } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ListadoResultados from './ListadoResultados'

describe('<ListadoResultados />', () => {
    it('renderea un elemento mientras carga', () => {
        const{getByText} = render(<ListadoResultados />);
        expect(getByText('Estamos cargando broder')).toBeTruthy();
    });
});