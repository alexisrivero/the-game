import React from 'react';
import { shallow, mount } from 'enzyme';
import DescripcionEmpresa from './DescripcionEmpresa';
import * as Constants from '../Constants';

describe ('<DescripcionEmpresa />', () => {
    it('renderea un elemento div', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA;
        const wrapper = shallow(<DescripcionEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
        expect(wrapper.find('div').text()).toEqual(data.descripcion);
    });
});