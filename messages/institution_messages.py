from protorpc import messages as m


class InstitutionRequest(m.Message):
    name = m.StringField(1, required=True)
    code = m.StringField(2, required=True)
    logo = m.StringField(3)


class InstitutionResponse(m.Message):
    name = m.StringField(1)
    code = m.StringField(2)
    logo = m.StringField(3)


#Marcot, eh assim que faz?
class InstitutionCode(m.Message):
    code = m.StringField(1)


class InstitutionId(m.Message):
    id = m.IntegerField(1)


class InstitutionList(m.Message):
    institutions = m.MessageField(InstitutionResponse, 1, repeated=True)
