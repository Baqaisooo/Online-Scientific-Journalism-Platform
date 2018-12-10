from django.contrib import admin
from .models import ( 
                        User,
                        EBM, 
                        Reviewer, 
                        Associate_Editor, 
                        Editor_in_Chief, 
                        # Guest, 
                        Subscriber, 
                        Admin, 
                        Writer, 
                        # Credit_Card,
                        Package,
                        Subscription,
                        Article,
                        Multimedia,
                        Comment,
                        Rate,
                        Purchase,
                        Feedback,
                        Article_Revision,
                        Setting,
                    )



class UserAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'first_name', 'last_name', 'birthdate', 'gender_en', 'gender_ar', 'email', 'phone_number', 'country', 'city', 'activation')

    def get_queryset(self, request):
        queryset = super(UserAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user_ID')
        return queryset


class EBMAdmin(admin.ModelAdmin):
    list_display = ('EBM_ID', 'specialty_ar', 'specialty_en', 'account_status_en', 'account_status_ar', 'password')

    def get_queryset(self, request):
        queryset = super(EBMAdmin, self).get_queryset(request)
        queryset = queryset.order_by('EBM_ID')
        return queryset


class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('reviewer_ID', 'password', 'specialty_ar', 'specialty_en','workplace', 'account_status_en', 'account_status_ar')
    
    def get_queryset(self, request):
        queryset = super(ReviewerAdmin, self).get_queryset(request)
        queryset = queryset.order_by('reviewer_ID')
        return queryset


class Associate_EditorAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        queryset = super(Associate_EditorAdmin, self).get_queryset(request)
        queryset = queryset.order_by('AE_ID')
        return queryset


class Editor_in_ChiefAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(Editor_in_ChiefAdmin, self).get_queryset(request)
        queryset = queryset.order_by('EIC_ID')
        return queryset


# class GuestAdmin(admin.ModelAdmin):
#     list_display = ('Guest_ID', 'special_number')

#     def get_queryset(self, request):
#         queryset = super(GuestAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('Guest_ID')
#         return queryset


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('subscriber_ID', 'password', 'picture')

    def get_queryset(self, request):
        queryset = super(SubscriberAdmin, self).get_queryset(request)
        queryset = queryset.order_by('subscriber_ID')
        return queryset


class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_ID', 'password')

    def get_queryset(self, request):
        queryset = super(AdminAdmin, self).get_queryset(request)
        queryset = queryset.order_by('admin_ID')
        return queryset


class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer_ID', 'writer_ID_id', 'password', 'specialty_en', 'specialty_ar','workplace', 'account_status_en', 'account_status_ar', 'picture')

    def get_queryset(self, request):
        queryset = super(WriterAdmin, self).get_queryset(request)
        queryset = queryset.order_by('writer_ID')
        return queryset


# class Credit_CardAdmin(admin.ModelAdmin):
#     list_display = ('credit_card_ID', 'user_ID', 'credit_card_number', 'name_on_card', 'expiration_date')

#     def get_queryset(self, request):
#         queryset = super(Credit_CardAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('credit_card_ID')
#         return queryset


class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_ID', 'admin_ID', 'package_name_en', 'package_name_ar', 'pakage_description_en', 'pakage_description_ar', 'duration', 'price', 'package_status_en', 'package_status_ar')

    def get_queryset(self, request):
        queryset = super(PackageAdmin, self).get_queryset(request)
        queryset = queryset.order_by('package_ID')
        return queryset


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_ID', 'package_ID', 'subscriber_ID', 'subscription_status_en', 'subscription_status_ar', 'start_date')

    def get_queryset(self, request):
        queryset = super(SubscriptionAdmin, self).get_queryset(request)
        queryset = queryset.order_by('subscription_ID')
        return queryset


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_ID', 'writer_ID', 'type', 'field_en', 'field_ar', 'cover_image', 'title_en', 'title_ar', 'brief_of_article_en', 'brief_of_article_ar', 'context_en', 'context_ar', 'submit_date', 'article_status_en', 'article_status_ar', 'price', 'is_editorial', 'publishing_date', 'number_of_views')

    def get_queryset(self, request):
        queryset = super(ArticleAdmin, self).get_queryset(request)
        queryset = queryset.order_by('article_ID')
        return queryset

class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('ID', 'aritcle_ID', 'format', 'content')    #, 'url_content')

    def get_queryset(self, request):
        queryset = super(MultimediaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('ID')
        return queryset


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_ID', 'subscriber_ID', 'article_ID', 'comment_date', 'comment_content')

    def get_queryset(self, request):
        queryset = super(CommentAdmin, self).get_queryset(request)
        queryset = queryset.order_by('comment_ID')
        return queryset


class RateAdmin(admin.ModelAdmin):
    list_display = ('rate_ID', 'subscriber_ID', 'article_ID', 'subscriber_rating')

    def get_queryset(self, request):
        queryset = super(RateAdmin, self).get_queryset(request)
        queryset = queryset.order_by('rate_ID')
        return queryset


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_ID', 'article_ID', 'purchase_date', 'download_code')

    def get_queryset(self, request):
        queryset = super(PurchaseAdmin, self).get_queryset(request)
        queryset = queryset.order_by('purchase_ID')
        return queryset


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_ID', 'EIC_ID', 'writer_ID', 'article_ID', 'EIC_comment', 'final_decision')

    def get_queryset(self, request):
        queryset = super(FeedbackAdmin, self).get_queryset(request)
        queryset = queryset.order_by('feedback_ID')
        return queryset


class Article_RevisionAdmin(admin.ModelAdmin):
    list_display = ('article_revision_ID', 'AE_ID', 'article_ID', 'EIC_ID', 'reviewer_ID', 'assign_date', 'AE_comment', 'invite_date', 'R_comment', 'AE_recommendation', )  #'AE_decision', 'R_decision')

    def get_queryset(self, request):
        queryset = super(Article_RevisionAdmin, self).get_queryset(request)
        queryset = queryset.order_by('article_revision_ID')
        return queryset


class SettingAdmin(admin.ModelAdmin):
    list_display = ('article_price','online_duration','editorial_duration')

        
admin.site.register(User, UserAdmin)
admin.site.register(EBM, EBMAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
admin.site.register(Associate_Editor, Associate_EditorAdmin)
admin.site.register(Editor_in_Chief, Editor_in_ChiefAdmin)
# admin.site.register(Guest, GuestAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Writer, WriterAdmin)
# admin.site.register(Credit_Card, Credit_CardAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Multimedia, MultimediaAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Article_Revision, Article_RevisionAdmin)
admin.site.register(Setting, SettingAdmin)