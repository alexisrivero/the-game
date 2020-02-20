import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import HeaderMenuItem from './HeaderMenuItem';

describe('<HeaderMenuItem />', () => {
    it('renderea un elemento li', () => {
        const wrapper = shallow(<HeaderMenuItem link="https://cia.net.at" texto='Green' key='123' color='#00ff00' />);
        expect(wrapper.find('li').exists()).toBeTruthy();    
    });
    it('renderea un elemento button', () => {
        const wrapper = shallow(<HeaderMenuItem link="https://cia.net.at" texto='Green' key='123' color='#00ff00' />);
        expect(wrapper.find('button').exists()).toBeTruthy();    
    });
    it('renderea un texto dentro del boton', () => {
        const wrapper = shallow(<HeaderMenuItem link="https://cia.net.at" texto='Green' key='123' color='#00ff00' />);
        expect(wrapper.find('button').text()).toEqual('Green');    
    });
    it('renderea el boton con la clase de color correspondiente', () => {
        const wrapper = shallow(<HeaderMenuItem link="https://cia.net.at" texto='Green' key='123' color='#00ff00' />);
        expect(wrapper.find('.c-green').exists()).toBeTruthy();    
    });
    it('cambia el titulo al clickear el boton', () => {
        const handleClick = sinon.spy();
        const wrapper = mount(<HeaderMenuItem link="https://cia.net.at" texto='Green' key='123' color='#00ff00' onClick={handleClick} />);
        wrapper.find('button').simulate('click');
        expect(global.window.document.title).toBe('Impar');
        wrapper.find('button').simulate('click');
        expect(global.window.document.title).toBe('cliqueaste 4 veces');    
    });
});