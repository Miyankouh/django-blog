from django.contrib import admin
from .models import Article, Category
# ----------------------------------------------------------------

# admin header chang
admin.site.site_header = "اولین وبلاگ جنگویی من"





# ----------------------------------------------------------------
# actions

# publish
def make_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "منتشر شد."
        else:
            message_bit = "منتشر شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

# draft
def make_draft(modeladmin, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "پیش ‌نویس شد."
        else:
            message_bit = "پیش ‌نویس شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


# ----------------------------------------------------------------
# Settings for the admin page
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug', 'parent' ,'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')

    # Simultaneous Writing Of Titles And Slug
    prepopulated_fields = {'slug':('title',)}

# Register Category Model
admin.site.register(Category, CategoryAdmin)



# ----------------------------------------------------------------
# Settings for the admin page
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag' , 'slug', 'author' , 'jpublish','status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    # Simultaneous Writing Of Titles And Slug
    prepopulated_fields = {'slug':('title',)}
    ordering = ('-status','-publish')
    actions = [make_published, make_draft]


    def category_to_str(self, obj):
        return " , ".join([category.title for category in obj.category.active()])
    category_to_str.short_description = "دسته بندی"


# Register Article model
admin.site.register(Article, ArticleAdmin)