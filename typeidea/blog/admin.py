from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Tag,Post,Category


class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器只展示当前用户分类'''

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self,request,model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','created_time','owner','post_count')
    fields = ('name','status','is_nav')

    def post_count(self,obj):
        return obj.post_set.count()

    # list_filter = [CategoryOwnerFilter]

    post_count.short_description = '文章数量'
    # list_filter = [CategoryOwnerFilter]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin,self).save_model(request,obj,form,change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_time','owner')
    fields = ('name','status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin,self).save_model(request,obj,form,change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title','desc','status','category',
        'created_time','operator'
    ]

    exclude = ('owner',)
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title','category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change',
                    args=(obj.id,)
                    )
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(PostAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

