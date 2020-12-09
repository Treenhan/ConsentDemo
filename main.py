import uuid

class DeonticToken:
    def __init__(self, grantor, grantee, field):
        self.grantor = grantor
        self.grantee = grantee
        self.field = field

    def __eq__(self, other): 
        if not isinstance(other, Action):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.grantor == other.grantor and self.grantee == other.grantee and self.field == other.field

class Embargo(DeonticToken):
    pass

class Permit(DeonticToken):
    pass

class Burden(DeonticToken):
    pass

class Action:
    def __init__(self, grantor, grantee, field):
        self.grantor = grantor
        self.grantee = grantee
        self.field = field

class ConscentAuthority:
    def __init__(self):
        self.permits = []

    def perform(self, action):
        
        for permit in self.permits:
            if permit == action:
                print("{}'s {} is accessed successfully by {}".format(action.grantor.name, action.field, action.grantee.name))
                return

        print("{} cannot access {}'s {}".format(action.grantee.name, action.grantor.name, action.field))

    def register(self, permit):
        self.permits.append(permit)


class Party():
    def __init__(self, name):
        self.name = name


class Grantor(Party):
    def __init__(self, name):
        super().__init__(name)
        self.data = {}

    def setData(self, data):
        self.data = data

class Grantee(Party):
    pass

def setScenario():
    # Set up Conscent Authority
    ca = ConscentAuthority()

    # Setup Zoran as grantee to get information from Nathan
    zoran = Grantee("Zoran")

    # Set up Nathan and his data
    nathan = Grantor("Nathan")
    nathan.setData({
        "age": 25,
        "address": "UK"
    })

    # Nathan allows Zoran to access his age
    age_permit = Permit(nathan, zoran, "age")
    ca.register(age_permit)
    
    # Zoran tries to access different pieces of data
    action1 = Action(nathan, zoran, "address")
    ca.perform(action1)

    action2 = Action(nathan, zoran, "age")
    ca.perform(action2)

def main():
    setScenario()

if __name__ == "__main__":
    main()