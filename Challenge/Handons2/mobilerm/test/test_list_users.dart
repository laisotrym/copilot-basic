import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http_mock_adapter/http_mock_adapter.dart';
import 'dart:convert';
import 'package:my_app/list_user.dart'; // Adjust the import according to your project structure

void main() {
  group('ListUserPage', () {
    late DioAdapter dioAdapter;
    late http.Client client;

    setUp(() {
      client = http.Client();
      dioAdapter = DioAdapter(dio: client);
    });

    testWidgets('displays loading icon while fetching data', (WidgetTester tester) async {
      dioAdapter.onGet(
        'https://jsonplaceholder.typicode.com/users',
        (server) => server.reply(200, []),
      );

      await tester.pumpWidget(MaterialApp(home: ListUserPage()));

      // Verify that the CircularProgressIndicator is displayed
      expect(find.byType(CircularProgressIndicator), findsOneWidget);

      await tester.pumpAndSettle();
    });

    testWidgets('displays users fetched from API', (WidgetTester tester) async {
      final mockResponse = [
        {"name": "User1", "email": "user1@example.com"},
        {"name": "User2", "email": "user2@example.com"},
      ];

      dioAdapter.onGet(
        'https://jsonplaceholder.typicode.com/users',
        (server) => server.reply(200, mockResponse),
      );

      await tester.pumpWidget(MaterialApp(home: ListUserPage()));

      await tester.pumpAndSettle();

      expect(find.text('User1'), findsOneWidget);
      expect(find.text('user1@example.com'), findsOneWidget);
      expect(find.text('User2'), findsOneWidget);
      expect(find.text('user2@example.com'), findsOneWidget);
    });

    testWidgets('displays error message on API failure', (WidgetTester tester) async {
      dioAdapter.onGet(
        'https://jsonplaceholder.typicode.com/users',
        (server) => server.reply(500, {}),
      );

      await tester.pumpWidget(MaterialApp(home: ListUserPage()));

      await tester.pumpAndSettle();

      expect(find.text('Failed to load users'), findsOneWidget);
    });

    testWidgets('displays message when no users are available', (WidgetTester tester) async {
      dioAdapter.onGet(
        'https://jsonplaceholder.typicode.com/users',
        (server) => server.reply(200, []),
      );

      await tester.pumpWidget(MaterialApp(home: ListUserPage()));

      await tester.pumpAndSettle();

      expect(find.text('No users available'), findsOneWidget);
    });
  });
}