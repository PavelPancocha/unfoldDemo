from random import choice

from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.gis.admin import GISModelAdmin
from fsm_admin.mixins import FSMTransitionMixin
from unfold.admin import ModelAdmin
from unfold.decorators import action, display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import Car, Org


@admin.register(Org)
class OrgAdmin(ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Car)
class CarAdmin(FSMTransitionMixin, ModelAdmin, GISModelAdmin):
    list_display = ("heading", "show_status", "owner")
    search_fields = ("name", "brand", "owner__username")
    autocomplete_fields = ("owner",)

    @display(header=True)
    def heading(self, obj):
        return obj.name, obj.brand

    @display(
        description="Status",
        label={"success": "success", "warning": "warning", "danger": "danger"},
    )
    def show_status(self, obj):
        return choice(["success", "warning", "danger"])

    @action(description="Submit test")
    def submit_line_action(self, request, obj):
        pass

    @action(description="Global test", url_path="global-action")
    def changelist_global_action(self, request):
        pass

    @action(description="Row", url_path="row-action")
    def changelist_row_action(self, request, object_id):
        pass

    @action(description="Detail", url_path="change")
    def change_detail_action(self, request, object_id):
        pass


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    search_fields = ("username", "first_name", "last_name", "email")


admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(GroupAdmin, ModelAdmin):
    pass
