package io.twitter.backend;

import java.util.HashSet;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import io.twitter.backend.models.ApplicationUser;
import io.twitter.backend.models.Role;
import io.twitter.backend.repositories.RoleRepository;
import io.twitter.backend.repositories.UserRepository;
import io.twitter.backend.services.UserService;

@SpringBootApplication
public class BackendApplication {

  public static void main(String[] args) {
    SpringApplication.run(BackendApplication.class, args);
  }

  @Bean
  CommandLineRunner run(RoleRepository roleRepo, UserService userService) {
    return args -> {
      roleRepo.save(new Role(1L, "USER"));
      ApplicationUser u = new ApplicationUser();
      u.setFirstName("aharo");
      u.setLastName("J");
      // userService.registerUser(u);
      /*
       * ApplicationUser u = new ApplicationUser();
       * u.setFirtName("Angel");
       * u.setLastName("Haro");
       * HashSet<Role> roles = new HashSet<>();
       * roles.add(roleRepo.findRoleByAuthority("USER").get());
       * u.setAuthorities(roles);
       * userRepo.save(u);
       */
    };
  }
}
