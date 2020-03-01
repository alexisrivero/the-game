import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import NombreEmpresa from './NombreEmpresa';
import * as Constants from '../Constants';

describe('<NombreEmpresa />', () => {
    it('renderea un elemento div con el nombre de la empresa', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA;
        const wrapper = shallow(<NombreEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
        expect(wrapper.find('div').text()).toEqual(data.nombre);
    });
});