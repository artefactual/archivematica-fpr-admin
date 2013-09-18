from django.db import models

def dependent_objects(object_):
    """ Returns all the objects that rely on 'object_'. """
    links = [rel.get_accessor_name() for rel in object_._meta.get_all_related_objects()]
    dependent_objects = []
    for link in links:
        linked_objects = getattr(object_, link).all()
        for linked_object in linked_objects:
            dependent_objects.append(
                {'model': linked_object._meta.verbose_name,
                 'value': linked_object})
    return dependent_objects

def update_references_to_object(model_referenced, key_field_name, old_object, new_object):
    for model in models.get_models():
        for field in model._meta.fields:
            type = field.get_internal_type()
            # update each foreign key reference to the target model
            if type == 'ForeignKey' and field.rel != None and field.rel.to == model_referenced and field.rel.field_name == key_field_name:
                filter_criteria = {field.name: old_object}
                parent_objects = model.objects.filter(**filter_criteria)
                for parent in parent_objects:
                    setattr(parent, field.name, new_object)
                    parent.save()

def update_many_to_many_references(to_model, set_name, old_object, new_object):
  filter_criteria = {set_name: old_object}
  parent_objects = to_model.objects.filter(**filter_criteria)
  for parent in parent_objects:
     manager = getattr(parent, set_name)
     manager.remove(old_object)
     manager.add(new_object)
     parent.save()
