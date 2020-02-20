import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import Contenido from './Contenido';

describe('<Contenido />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<Contenido />)
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
});