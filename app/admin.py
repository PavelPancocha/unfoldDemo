from random import choice

from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.gis.admin import GISModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.reversion.admin import VersionAdmin as CompareVersionAdminBase
from unfold.decorators import action, display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import Car, Org


class CompareVersionAdmin(CompareVersionAdminBase):
    change_list_template = "admin/change_list.html"
    recover_list_template = "reversion/recover_list.html"
    recover_form_template = "reversion/recover_form.html"
    revision_form_template = "reversion/revision_form.html"
    object_history_template = "reversion-compare/object_history.html"
    compare_template = "reversion-compare/compare.html"
    compare_raw_template = "reversion-compare/compare_raw.html"

@admin.register(Org)
class OrgAdmin(CompareVersionAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Car)
class CarAdmin(ModelAdmin, GISModelAdmin):
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
