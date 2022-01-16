# from SKOBADIUM.authz.authz import model
from authz import ma
from authz.model import User



class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        
    id = ma.auto_field(dump_only = True)            # faqat khandani hast user nemitone behesh dast bezane faqat mitone bebibe dump_only in karo mikone 
                                                    # auto_field mire model ro baz mikone User ro mikhone mire soraqe field id va moshakhasatesho mibine va load mikone.
                                                    
    username = ma.auto_field()                      # user ham mitone bekhone ham mitone benevise pas () khali mimone
    password = ma.auto_field(load_only = True)      #user faqat bara avalin bar mizane va hash mishe mire to db va dh be user namayesh dade nemishe
    role = ma.auto_field()
    register_at = ma.auto_field(dump_only = True)
    last_active_at = ma.auto_field(dump_only = True)
    last_failed_at = ma.auto_field(dump_only = True)
    status = ma.auto_field()
    
    