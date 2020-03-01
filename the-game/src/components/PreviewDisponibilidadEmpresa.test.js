import React from 'react';
import { shallow, mount } from 'enzyme';
import PreviewDisponibilidadEmpresa from './PreviewDisponibilidadEmpresa';
import * as Constants from '../Constants'

describe('<PreviewDisponibilidadEmpresa />', () => {
    it('renderea un elemento div', () => {

    });
    it('renderea N dias disponibles', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA
        console.log(data.disponibilidad.length);
    });
});