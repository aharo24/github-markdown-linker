package io.twitter.backend.models;

import java.sql.Date;
import java.util.HashSet;
import java.util.Set;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Table(name = "users")
@Entity
public class ApplicationUser {
  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  @Column(name = "user_id")
  private Long id;

  @Column(name = "first_name")
  private String firstName;

  @Column(name = "last_name")
  private String lastName;

  @Column(unique = true)
  private String email;

  private String phone;

  @Column(name = "dob")
  private Date dateOfBirth;

  @Column(unique = true)
  private String username;

  @JsonIgnore
  private String password;

  @ManyToMany(fetch = FetchType.EAGER)
  @JoinTable(name = "user_role_junction", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "role_id"))
  private Set<Role> authorities;

  private Boolean enabled;

  @Column(nullable = true)
  @JsonIgnore
  private Long verification;

  public ApplicationUser() {
    this.authorities = new HashSet<>();
  }

  @Override
  public String toString() {
    return "ApplicationUser [id=" + id + ", firstName=" + firstName + ", lastName=" + lastName + ", email=" + email
        + ", phone=" + phone + ", dateOfBirth=" + dateOfBirth + ", username=" + username + ", password=" + password
        + ", authorities=" + authorities + ", enabled=" + enabled + ", verification=" + verification + "]";
  }

}
