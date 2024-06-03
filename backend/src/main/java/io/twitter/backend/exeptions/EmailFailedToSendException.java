package io.twitter.backend.exeptions;

/**
 * EmailFailedToSendException
 */
public class EmailFailedToSendException extends RuntimeException{
  public EmailFailedToSendException(){
    super("The email failed to send");
  }

  
}
