import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import DireccionEmpresa from './DireccionEmpresa';
import * as Constants from '../Constants';

describe ('<DireccionEmpresa />', () => {
    it('renderea un elementi div', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA;
        const wrapper = shallow(<DireccionEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
        expect(wrapper.find('div').text()).toEqual(data.direccion);
    });
});