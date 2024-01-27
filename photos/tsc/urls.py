from django.urls import path
from . import views

urlpatterns =[
    path("store_display",views.display,name="display"),
    path("s_entry",views.store_entry,name="store entry"),
    path("s_del/<int:id>",views.del_store,name="store_delete"),
    path("s_edit/<int:id>",views.store_edit,name="storeEdit"),
    path("<int:id>",views.save_store_edit,name="savestoreeditdata"),
    path("upload",views.photos_upload,name="uploadPhotos"),
    path("p_display",views.photos_display,name="photos_display"),
    path("b_n_entry",views.brand_name_entry,name="brandsDisplay"),
    path("filter",views.filter_data,name="filterdate"),
    path("",views.main_page,name="mainPage"),

]
