from django import template
from app02_blog import models
from django.db.models import Count
from django.db.models.functions import TruncMonth
register = template.Library()

## 自定义 inclusion_tag
@register.inclusion_tag('right_menu.html')
def right_menu(username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    # 查询当前用户所有的分类，以及分类下的文章（聚合函数）
    category_list = models.Category.objects.filter(blog=blog).annotate(count_num = Count('article__pk')).values('name','count_num','pk')
    # 查询当前用户所有标签及标签下文章数
    tag_list = models.Tags.objects.filter(blog=blog).annotate(count_num = Count('article__pk')).values('name','count_num','pk')
    # 按年月归档
    date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values('month').annotate(count_num = Count('pk')).values('month','count_num','pk')

    return locals()