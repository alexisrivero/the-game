import React from 'react';
import { shallow, mount } from 'enzyme';
import DisponibilidadDia from './DisponibilidadDia';
import * as Constants from '../Constants';

describe('<DisponibilidadDia />', () => {
    it('renderea un elemento div', () => {
        const data = Constants.DATOS_PRUEBA_DISPONIBILIDAD;
        const wrapper= shallow(<DisponibilidadDia disponibilidad={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento ul', () => {
        const data = Constants.DATOS_PRUEBA_DISPONIBILIDAD;
        const wrapper = shallow(<DisponibilidadDia disponibilidad={data}  />);
        expect(wrapper.find('ul').exists()).toBeTruthy();
    });
    it('renderea un elemento li', () => {
        const data = Constants.DATOS_PRUEBA_DISPONIBILIDAD;
        const wrapper = shallow(<DisponibilidadDia disponibilidad={data}  />)
        expect(wrapper.find('li').exists()).toBeTruthy();
    })
});