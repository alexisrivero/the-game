import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import ListadoResultados from './ListadoResultados'

describe('<ListadoResultados />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<ListadoResultados />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento p', () => {
        const wrapper = shallow(<ListadoResultados />);
        expect(wrapper.find('p').exists()).toBeTruthy();
    });
});