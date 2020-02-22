import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import FooterPublicidad from './FooterPublicidad';

describe('<FooterPublicidad />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<FooterPublicidad />);
        return expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea una imagen con un link', async () => {
        //expect.assertions(1);
        //const wrapper = shallow (<FooterPublicidad />)
        //expect(wrapper.find('a').exists()).toBeTruthy();
        //expect(wrapper.find('img').exists()).toBeTruthy();
    });
    it('muestra un error si la API de publicidad no esta disponible', () => {
        //const wrapper = mount (<FooterPublicidad API_Url='https://cia.net.ar/publicidad.jswadwadon'/>)
        //expect(wrapper.find('p').text()).toEqual('Error: no se pudo contactar la API de publicidad')
    });
});