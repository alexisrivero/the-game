class Subject():
    changed = False
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_changed(self):
        self.changed = True

    def notify(self):
        pass


class Observer():
    def notify(self):
        pass


class ServerChat(Subject):
    def notify(self):
        print("actualizando clientes de chat")
        for observer in self._observers:
            observer.update()


class ClienteChat(Observer):
    def update(self):
        print("me actualizaron")


valve = ServerChat()
amigoso = ClienteChat()
inp = ClienteChat()
respeto = ClienteChat()
javo = ClienteChat()
valve.attach(amigoso)
valve.attach(inp)
valve.attach(javo)
valve.attach(respeto)
valve.notify()
