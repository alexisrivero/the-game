import React from 'react';
import { shallow, mount } from 'enzyme';
import SugerenciaBuscador from './SugerenciaBuscador';


describe('<SugerenciaBuscador />', () => {
    it('renderea sugerencias', () => {
        let busqueda = "cla";
        let tipo = "ciudad";
        let tieneFoco = true;
        const wrapper = shallow(<SugerenciaBuscador busqueda={busqueda} tipo={tipo} />);
        expect(wrapper.find('ul').children).toBeGreaterThan(1);
    });       
    it('renderea mensaje de advertencia de que tipee más', () => {
        let busqueda = "";
        let tipo = "ciudad";
        let tieneFoco = true;
        const wrapper = shallow(<SugerenciaBuscador busqueda={busqueda} tipo={tipo} />);        
        expect(wrapper.find('li').exists()).toBeTruthy();
        expect(wrapper.find('li').text()).toBe('Tipea algo para ver sugerencias');
    });
    it('no renderea nada si no tiene foco', () => {
        let busqueda = "lele";
        let tipo = "ciudad";
        let tieneFoco = false;
        const wrapper = shallow(<SugerenciaBuscador busqueda={busqueda} tipo={tipo} />);
        expect(wrapper.find('o').exists()).toBeFalsy();
    });
});