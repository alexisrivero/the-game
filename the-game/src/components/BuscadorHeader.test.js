import React from 'react';
import { shallow, mount } from 'enzyme';
import BuscadorHeader from './BuscadorHeader';


describe('<BuscadorHeader />', () => {
    it('renderea inputs de búsqueda', () => {
        const wrapper = shallow(<BuscadorHeader />)
        expect(wrapper.find('input').length).toBe(2);
    });
    it('renderea un elemento para enviar la busqueda', () => {
        const wrapper = shallow(<BuscadorHeader />)
        expect(wrapper.find('button').exists()).toBeTruthy();
        
    });
       
});