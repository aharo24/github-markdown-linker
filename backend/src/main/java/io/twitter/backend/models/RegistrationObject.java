package io.twitter.backend.models;

import java.sql.Date;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class RegistrationObject {
  private String firstName;
  private String lastName;
  private String email;
  private Date dob;

}
