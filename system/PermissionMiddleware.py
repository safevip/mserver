from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response
from system.models import Permission


class UrlPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理前
        if perm_check(request) or request.path.startswith("/admin"):
            response = self.get_response(request)
            # 处理后
            return response
        else:
            return render_to_response("403.html")


def perm_check(request, *args, **kwargs):
    get_perm = Permission.objects.filter(url=request.path)
    if get_perm:
        for i in get_perm:
            codename = i.codename
            content_type = ContentType.objects.get_for_id(i.content_type_id)
            if content_type:
                perm_str = '%s.%s' % (content_type.model, codename)
                if request.user.has_perm(perm_str):
                    print('====》权限已匹配')
                    return True
        else:
            print('---->权限没有匹配')
            return False
    else:
        return False
