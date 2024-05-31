package io.twitter.backend.controllers;

import java.util.LinkedHashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import io.twitter.backend.exeptions.EmailAlreadyTakenExeption;
import io.twitter.backend.exeptions.UserDoesNotExistException;
import io.twitter.backend.models.ApplicationUser;
import io.twitter.backend.models.RegistrationObject;
import io.twitter.backend.services.UserService;

/**
 * AuthenticationController
 */
@RequestMapping("/auth")
@RestController
public class AuthenticationController {
  private final UserService userService;

  @Autowired
  public AuthenticationController(UserService userService) {
    this.userService = userService;
  }

  @ExceptionHandler({ EmailAlreadyTakenExeption.class })
  public ResponseEntity<String> handleEmailTaken() {

    return new ResponseEntity<>("The email provided is already in use", HttpStatus.CONFLICT);
  }

  // https://localhost:8080/auth/register
  @PostMapping("/register")
  public ApplicationUser registerUser(@RequestBody RegistrationObject ro) {
    return userService.registerUser(ro);
  }

  @ExceptionHandler({ UserDoesNotExistException.class })
  public ResponseEntity<String> handleUserDoesNotExist() {
    return new ResponseEntity<>("The user you are looking for does not exist", HttpStatus.NOT_FOUND);
  }

  @PutMapping("/update/phone")
  public ApplicationUser updatePhoneNumber(@RequestBody LinkedHashMap<String, String> body) {
    String username = body.get("username");
    String phone = body.get("phone");

    ApplicationUser user = userService.getUserByUsername(username);
    user.setPhone(phone);

    return userService.updateUser(user);

  }

  @PostMapping("/email/code")
  public ResponseEntity<String> createEmailVerification(@RequestBody LinkedHashMap<String, String> body){
    userService.generateEmailVerification(body.get("username"));
    return new ResponseEntity<String>("Verification code generated, email sent", HttpStatus.OK);

  }

}
