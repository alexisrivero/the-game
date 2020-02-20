import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import BotonDetalle from './BotonDetalle'

describe('<BotonDetalle />', () => {
    it('renderea un elemento p', () => {
        const wrapper = shallow (<BotonDetalle />)
        expect(wrapper.find('p').exists()).toBeTruthy();
    });
    it('renderea un elemento boton', () => {
        const wrapper = mount(<BotonDetalle />);
        expect(wrapper.find('button').exists()).toBeTruthy();
    });
    it('alerta sobre detalles al clickear el boton', () => {
        window.alert = jest.fn()
        const wrapper = shallow(<BotonDetalle onClick={window.alert('Detalles')} />)
        wrapper.simulate('click')
        expect(window.alert.mock.calls.length).toBe(1)
        expect(window.alert).toHaveBeenCalledWith('Detalles')
      });
});