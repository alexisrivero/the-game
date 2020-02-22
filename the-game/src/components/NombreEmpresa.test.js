import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import NombreEmpresa from './NombreEmpresa';

describe('NombreEmpresa />', () => {
    it('renderea un elemento li', () => {
        const wrapper = shallow(<NombreEmpresa />);
        expect(wrapper.find('li').exists()).toBeTruthy();
    });
});