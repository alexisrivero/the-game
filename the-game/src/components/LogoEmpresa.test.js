import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import * as Constants from '../Constants';
import LogoEmpresa from './LogoEmpresa';

describe ('<LogoEmpresa />', () => {
    it('renderea un elemento div', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA
        const wrapper = shallow(<LogoEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento img', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA
        const wrapper = shallow(<LogoEmpresa empresa={data} />);
        expect(wrapper.find('img').exists()).toBeTruthy();
    });
});