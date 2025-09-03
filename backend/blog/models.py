from django.db import models
from django.contrib.auth.models import User # 自带用户模型，用来注册、登录、权限等
# Create your models here.


class Post(models.Model) :
    """文章表
    - 标题
    - 内容
    - 作者
    - 点赞
    - 评论
    """
    title = models.CharField(
        max_length=200 , verbose_name="标题" , help_text="请输入文章标题"
    )  # verbose_name : 后台显示的中文名字

    content = models.TextField(verbose_name="内容" , help_text="请输入文章内容")

    author = models.ForeignKey(
        User , on_delete=models.CASCADE , related_name="posts" , verbose_name="作者"
    ) # 外键关联 User表，用户被删除时，文章也会删除 user.posts.all() 返回用户的文章 

    likes = models.ManyToManyField(
        User , related_name="liked_posts" , blank=True , verbose_name="点赞"
    )  # 多对多，外键关联 User ， 反向查询时使用 user.liked_posts.all() 获取用户点赞的文章

    created_at = models.DateTimeField(auto_now_add=True , verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="更新时间")

    class Meta :
        db_table = "post" # 表名
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ["-created_at"] # 按照创建时间排序
    
    def __str__(self):
        return f"{self.title} be made by {self.author.username}"



class Comment(models.Model) :
    """评论表, 每个评论对应一个用户和一篇文章"""
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , related_name="comments" , verbose_name="文章"
    ) # 外键关联 Post
    author = models.ForeignKey(
        User , on_delete=models.CASCADE , related_name="comments" , verbose_name="评论者"
    )
    content = models.TextField(
        verbose_name="评论内容" , help_text="请输入评论内容"
    )
    created_at = models.DateTimeField(
        auto_now_add=True , verbose_name="评论时间" , db_index=True
    )

    class Meta :
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ["-created_at"] # 按照创建时间排序
    
    def __str__(self):
        return f"{self.author.username} create {self.content}"