from django.urls import path
from .views import Home, Signin, Signup, Homepage, Cart, SellerHome, AddCatalog, EditCatalog, SellerCatalogs, EditProfile, SellerEditProfile,OrderStatusChange,Ratings, SellerPendingOrders, SellerCompleteOrders, BuyerPendingOrders, BuyerCompleteOrders, AdminPanel, EditProfileAdmin, ConflictOnOrder, PostConflict, ConflictStatusChange, AdminbPendingConflicts, AdminbCompleteConflicts, PaymentPageView, Charge
from .views.checkout import Checkout
from .views.order import OrderView
from store import views
urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('signin', Signin.as_view(), name='signin'),
    path('home' , Homepage.as_view()),
    path('cart', Cart.as_view(), name='cart'),
    path('logout' , views.logout, name='logout'),
    path('sellerlogout' , views.sellerlogout, name='seller_logout'),
    path('addcatalog' , AddCatalog.as_view(), name='addcatalog'),
    path('sellerhome' , SellerHome.as_view(), name='seller_home'),
    path('editcatalog<str:catalogid>' , EditCatalog.as_view(), name='editcatalog'),
    path('deletecatalog<str:catalogid>' , views.deleteCatalog, name='deletecatalog'),
    path('sellercatalogs' , SellerCatalogs.as_view(), name='sellercatalogs'),
    path('checkout' , Checkout.as_view(), name='checkout'),
    path('orders' , OrderView.as_view(), name='orders'),
    path('editprofile', EditProfile.as_view(), name='editprofile'),
    path('sellereditprofile', SellerEditProfile.as_view(), name='sellereditprofile'),
    path('orderstatuschange<str:order>' , OrderStatusChange.as_view(), name='orderstatuschange'),
    path('rating<int:order>/<int:rate>' , Ratings.as_view(), name='rating'),
    path('sellerpendingorders', SellerPendingOrders.as_view(), name='sellerpendingorders'),
    path('sellercompleteorders', SellerCompleteOrders.as_view(), name='sellercompleteorders'),
    path('buyerpendingorders', BuyerPendingOrders.as_view(), name='buyerpendingorders'),
    path('buyercompleteorders', BuyerCompleteOrders.as_view(), name='buyercompleteorders'),
    path('adminpanel', AdminPanel.as_view(), name='adminpanel'),
    path('editprofileadmin', EditProfileAdmin.as_view(), name='editprofileadmin'),
    path('postconflict', PostConflict.as_view(), name='postconflict'),
    path('adminbpendingc', AdminbPendingConflicts.as_view(), name='adminbpendingc'),
    path('adminbcompletec', AdminbCompleteConflicts.as_view(), name='adminbcompletec'),
    path('conflictstatuschange<str:conflict>' , ConflictStatusChange.as_view(), name='conflictstatuschange'),
    path('conflictonorder<str:order>' , ConflictOnOrder.as_view(), name='conflictonorder'),
    path('payment/',PaymentPageView.as_view(), name = 'payment'),
    path('charge/',Charge.as_view(), name = 'charge'),
] 