import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:post_app/list_user_page.dart';

class MockClient extends Mock implements http.Client {}

void main() {
  group('ListUsersPage Tests', () {
    // Test case for display list of users ok
    testWidgets('Displays list of users', (WidgetTester tester) async {
      final client = MockClient();

      // Mock the HTTP response
      when(client.get(Uri.parse('http://localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response(
              jsonEncode([
                {'id': 1, 'username': 'John Doe', 'email': 'john@mail.com'},
                {'id': 2, 'username': 'Jane Doe', 'email': 'jane@mail.com'}
              ]),
              200));

      // Build our app and trigger a frame.
      await tester.pumpWidget(MaterialApp(
        home: ListUserPage(),
      ));

      // Verify that the list of users is displayed.
      expect(find.text('John Doe'), findsOneWidget);
      expect(find.text('Jane Doe'), findsOneWidget);
    });

    testWidgets('Displays error message on failed request', (WidgetTester tester) async {
      final client = MockClient();

      // Mock the HTTP response
      when(client.get(Uri.parse('http://localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response('Not Found', 404));

      // Build our app and trigger a frame.
      await tester.pumpWidget(MaterialApp(
        home: ListUserPage(),
      ));

      // Verify that the error message is displayed.
      expect(find.text('Failed to load users'), findsOneWidget);
    });

    testWidgets('Displays loading indicator while fetching users', (WidgetTester tester) async {
      final client = MockClient();

      // Mock the HTTP response with a delayed future
      when(client.get(Uri.parse('http://localhost:5000/api/users')))
          .thenAnswer((_) async => Future.delayed(
              Duration(seconds: 2), () => http.Response('[]', 200)));

      // Build our app and trigger a frame.
      await tester.pumpWidget(MaterialApp(
        home: ListUserPage(),
      ));

      // Verify that the loading indicator is displayed.
      expect(find.byType(CircularProgressIndicator), findsOneWidget);

      // Wait for the future to complete.
      await tester.pumpAndSettle();

      // Verify that the loading indicator is gone.
      expect(find.byType(CircularProgressIndicator), findsNothing);
    });

    testWidgets('Displays empty state when no users are found', (WidgetTester tester) async {
      final client = MockClient();

      // Mock the HTTP response with an empty list
      when(client.get(Uri.parse('http://localhost:5000/api/users')))
          .thenAnswer((_) async => http.Response('[]', 200));

      // Build our app and trigger a frame.
      await tester.pumpWidget(MaterialApp(
        home: ListUserPage(),
      ));

      // Verify that the empty state message is displayed.
      expect(find.text('No users found'), findsOneWidget);
    });
  });
}