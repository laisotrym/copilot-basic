package com.cmcg.investor.users;

import com.cmcg.investor.users.controllers.UserController;
import com.cmcg.investor.users.models.User;
import com.cmcg.investor.users.services.UserService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

public class UserControllerTest {

    @Mock
    private UserService userService;

    @InjectMocks
    private UserController userController;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void createUserSuccessfully() {
        User user = new User();
        User createdUser = new User();
        when(userService.createUser(user)).thenReturn(createdUser);

        ResponseEntity<User> response = userController.createUser(user);

        assertEquals(ResponseEntity.ok(createdUser), response);
        verify(userService, times(1)).createUser(user);
    }

    @Test
    void getUserByIdSuccessfully() {
        Long userId = 1L;
        User user = new User();
        when(userService.getUserById(userId)).thenReturn(user);

        ResponseEntity<User> response = userController.getUserById(userId);

        assertEquals(ResponseEntity.ok(user), response);
        verify(userService, times(1)).getUserById(userId);
    }

    @Test
    void updateUserSuccessfully() {
        Long userId = 1L;
        User user = new User();
        User updatedUser = new User();
        when(userService.updateUser(userId, user)).thenReturn(updatedUser);

        ResponseEntity<User> response = userController.updateUser(userId, user);

        assertEquals(ResponseEntity.ok(updatedUser), response);
        verify(userService, times(1)).updateUser(userId, user);
    }

    @Test
    void deleteUserSuccessfully() {
        Long userId = 1L;
        doNothing().when(userService).deleteUser(userId);

        ResponseEntity<Void> response = userController.deleteUser(userId);

        assertEquals(ResponseEntity.noContent().build(), response);
        verify(userService, times(1)).deleteUser(userId);
    }

    @Test
    void getAllUsersSuccessfully() {
        List<User> users = Arrays.asList(new User(), new User());
        when(userService.getAllUsers()).thenReturn(users);

        ResponseEntity<List<User>> response = userController.getAllUsers();

        assertEquals(ResponseEntity.ok(users), response);
        verify(userService, times(1)).getAllUsers();
    }
}