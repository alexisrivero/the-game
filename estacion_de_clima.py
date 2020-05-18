# el patron de observador o observer define una dependencia de uno o muchos en la cual cuando un objeto cambia su estado, todos sus dependientes son notificados y actualizados automaticamente
# hacer twitch usando el patron observer
# observer = el que quiere ser notificados
# subject = el que quiere enviar las notificaciones


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


class StreamerTwitch(Subject):
    def notify(self):
        print("actualizando lista de subs")
        for observer in self._observers:
            observer.update()


class SubsTwitch(Observer):
    def update(self):
        print("yeeeia")


twitch = StreamerTwitch()
pamp = SubsTwitch()
twitch.attach(pamp)
twitch.notify()
