import React from 'react';
import { shallow, mount } from 'enzyme';
import Buscador from './Buscador';


describe('<Buscador />', () => {
    it('renderea inputs de búsqueda', () => {
        let tipo = "ciudad";
        let nombre = "ciudad";
        const wrapper = shallow(<Buscador tipo={tipo} nombre={nombre} />);
        let id_buscador = "buscador_" + nombre;
        expect(wrapper.find('input#' + id_buscador).exists()).toBeTruthy();
    });       
});