package io.twitter.backend.exeptions;

/**
 * email must be unique
 */
public class EmailAlreadyTakenExeption extends RuntimeException {
  private static final long serialVersionUID = 1L;

  public EmailAlreadyTakenExeption() {
    super("The email provided already taken.");
  }

}
