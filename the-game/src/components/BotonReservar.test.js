import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import BotonReservar from './BotonReservar';

describe('<BotonReservar />', () => {
    it('renderea un elemento p', () => {
        const wrapper = shallow (<BotonReservar />)
        expect(wrapper.find('p').exists()).toBeTruthy();
    });
    it('renderea un elemento boton', () => {
        const wrapper = mount(<BotonReservar />);
        expect(wrapper.find('button').exists()).toBeTruthy();
    });
    it('alerta sobre reserva al clickear el boton', () => {
        window.alert = jest.fn()
        const wrapper = shallow(<BotonReservar onClick={window.alert('Confirmar Reserva')} />)
        wrapper.simulate('click')
        expect(window.alert.mock.calls.length).toBe(1)
        expect(window.alert).toHaveBeenCalledWith('Confirmar Reserva')
      });
});