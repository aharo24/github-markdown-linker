package io.twitter.backend.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.twitter.backend.models.ApplicationUser;

@Repository
public interface UserRepository extends JpaRepository<ApplicationUser, Long> {
  // allow us to not pass null around and instead use Optional
  Optional<ApplicationUser> findByUsername(String username);

}
