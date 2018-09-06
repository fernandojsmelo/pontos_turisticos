def reprova_comentarios(modeladmin, request, qerysert):
    request.update(aprovado=False)


def aprova_comentarios(modeladmin, request, qerysert):
    request.update(aprovado=True)

reprova_comentarios.short_description = 'Reprova Comentarios'
aprova_comentarios.short_description = 'Aprova Comentarios'
