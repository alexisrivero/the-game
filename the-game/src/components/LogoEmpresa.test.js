import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import LogoEmpresa from './LogoEmpresa';

describe ('<LogoEmpresa />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<LogoEmpresa />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento img', () => {
        const wrapper = shallow(<LogoEmpresa />)
        expect(wrapper.find('img').exists()).toBeTruthy();
    });
});