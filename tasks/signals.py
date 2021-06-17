from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from tasks.models import TodoItem, Category
from collections import Counter


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action == "post_add":

        for cat in instance.category.all():
            slug = cat.slug

            new_count = Category.objects.filter(slug=slug).first().todos_count
            Category.objects.filter(slug=slug).update(todos_count= new_count + 1)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action == "post_remove":

        for cat in instance.category.all():
            slug = cat.slug

            new_count = Category.objects.filter(slug=slug).first().todos_count
            Category.objects.filter(slug=slug).update(todos_count=new_count - 1)