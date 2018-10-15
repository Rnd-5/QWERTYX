function showRecoverForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.recoverBox').fadeIn('fast');
        $('.login-footer').fadeOut();
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
       
}

/*function showLoginForm0(){
    $('#loginModal .recoverBox').fadeOut('fast',function(){
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');
        });
    }
}*/
function showLoginForm(){
    $('#loginModal .registerBox').fadeOut('fast',function(){
        $('.registroSoliciante').fadeOut('fast'); //Oculta el from. del solicitante
        $('.registroEmpleador').fadeOut('fast'); //Oculta el from. del empleador
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');    
        });
        
        $('.modal-title').html('Login with');
    });       
     $('.error').removeClass('alert alert-danger').html('');
}
//===MUESTRA LOS FORMULARIOS DEL SOLICITANTE Y DEL EMPLEADOR===============//
function showRegisterForm_Solicitante(){
     $('.registerBox').fadeOut('fast',function(){
        $('.registroSoliciante').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
}
function showRegisterForm_Empleador(){
     $('.registerBox').fadeOut('fast',function(){
        $('.registroEmpleador').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
}
//========================================================================//

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230); 
}
function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230);
}
function loginAjax(){
    /*   Remove this comments when moving to server
    $.post( "/login", function( data ) {
            if(data == 1){
                window.location.replace("/home");            
            } else {
                 shakeModal(); 
            }
        });
    */
/*   Simulate error message from the server   */
     shakeModal();
}
function shakeModal(){
    $('#loginModal .modal-dialog').addClass('shake');
             $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
             $('input[type="password"]').val('');
             setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 ); 
}

   