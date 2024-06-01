package io.twitter.backend.services;

import com.google.api.client.googleapis.json.GoogleJsonResponseException;
import com.google.api.services.gmail.Gmail;
import com.google.api.services.gmail.model.Message;

import io.twitter.backend.exeptions.EmailFailedToSendException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jakarta.mail.Session;
import jakarta.mail.internet.InternetAddress;
import jakarta.mail.internet.MimeMessage;
import java.io.ByteArrayOutputStream;
import java.util.Base64;
import java.util.Properties;

@Service
public class MailService {

  private final Gmail gmail;

  @Autowired
  public MailService(Gmail gmail) {
    this.gmail = gmail;
  }

  public void sendEmail(String toAddress, String subject, String content) throws Exception {
    Properties props = new Properties();
    Session session = Session.getInstance(props, null);
    MimeMessage email = new MimeMessage(session);

    try {
      email.setFrom(new InternetAddress("haro.j.angel@gmail.com"));
      email.addRecipient(jakarta.mail.Message.RecipientType.TO, new InternetAddress(toAddress));
      email.setSubject(subject);
      email.setText(content);

      ByteArrayOutputStream buffer = new ByteArrayOutputStream();
      email.writeTo(buffer);
      byte[] rawMessageBytes = buffer.toByteArray();
      String encodedEmail = Base64.getUrlEncoder().encodeToString(rawMessageBytes);

      Message message = new Message();
      message.setRaw(encodedEmail);

      message = gmail.users().messages().send("me", message).execute();
    } catch (GoogleJsonResponseException e) {
      throw new EmailFailedToSendException();
    }
  }
}
